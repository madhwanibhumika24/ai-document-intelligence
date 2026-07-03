import json
from pathlib import Path

from app.schemas.registry import DocumentMetadata


class RegistryService:

    def __init__(self):
        self.registry_file = Path("app/storage/documents.json")

        if not self.registry_file.exists():
            self.registry_file.parent.mkdir(parents=True, exist_ok=True)
            self.registry_file.write_text("[]")

    def _read(self):
        with open(self.registry_file, "r") as file:
            return json.load(file)

    def _write(self, data):
        with open(self.registry_file, "w") as file:
            json.dump(data, file, indent=4)

    def add_document(self, document: DocumentMetadata):
        data = self._read()
        data.append(document.model_dump())
        self._write(data)

    def get_document(self, document_id: str):

        data = self._read()

        for document in data:
            if document["document_id"] == document_id:
                return document

        return None

    def list_documents(self):
        return self._read()