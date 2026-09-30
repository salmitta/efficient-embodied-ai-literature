// Compute document embeddings for semantic search (same model the site uses for queries).
// Usage: cd _work && npm install && node embed.mjs   ->  docs/embeddings.bin (int8, row-major, L2-normalised x127)
import { pipeline } from "@huggingface/transformers";
import fs from "node:fs";
export const MODEL = "Xenova/bge-small-en-v1.5";
const root = new URL("..", import.meta.url).pathname;
const rows = fs.readFileSync(root + "literature_db.jsonl", "utf8").trim().split("\n").map(JSON.parse);
const text = r => [r.title, r.tldr, (r.techniques || []).join(", "), (r.keywords || []).join(", ")].filter(Boolean).join(". ");
const embed = await pipeline("feature-extraction", MODEL, { dtype: "q8" });
const dim = 384, out = new Int8Array(rows.length * dim);
for (let i = 0; i < rows.length; i += 32) {
  const batch = rows.slice(i, i + 32).map(text);
  const t = await embed(batch, { pooling: "cls", normalize: true });
  const d = t.data;
  for (let j = 0; j < batch.length; j++)
    for (let k = 0; k < dim; k++) out[(i + j) * dim + k] = Math.max(-127, Math.min(127, Math.round(d[j * dim + k] * 127)));
  if (i % 320 === 0) console.log(`${i}/${rows.length}`);
}
fs.mkdirSync(root + "docs", { recursive: true });
fs.writeFileSync(root + "docs/embeddings.bin", Buffer.from(out.buffer));
fs.writeFileSync(root + "docs/embeddings.json", JSON.stringify({ model: MODEL, dtype: "q8", pooling: "cls", dim, n: rows.length,
  first: rows[0].id, last: rows[rows.length - 1].id }));
console.log(`wrote ${rows.length} x ${dim}`);
