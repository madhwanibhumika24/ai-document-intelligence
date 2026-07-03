from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkingService:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],
        )

    def create_chunks(self, text: str) -> list[str]:

        if not text.strip():
            return []

        return self.text_splitter.split_text(text)