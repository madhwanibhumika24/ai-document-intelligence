from app.rag.chunking import ChunkingService


text = """
Artificial Intelligence is transforming industries worldwide.
Machine Learning is a subset of AI.

Deep Learning is a subset of Machine Learning.

Large Language Models are trained on massive datasets.
"""

chunker = ChunkingService(
    chunk_size=50,
    chunk_overlap=10,
)

chunks = chunker.create_chunks(text)

print(f"Total Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}")
    print("-" * 40)
    print(chunk)
    print()