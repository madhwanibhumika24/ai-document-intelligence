from pathlib import Path

import pdfplumber
from pypdf import PdfReader

from app.schemas.extraction import ExtractionResponse
from app.utils.text_cleaner import TextCleaner


class PDFService:

    def extract_text(
        self,
        document_id: str,
        file_path: Path,
        strategy: str = "auto",
    ) -> ExtractionResponse:

        if strategy == "pypdf":
            return self._extract_with_pypdf(document_id, file_path)

        if strategy == "pdfplumber":
            return self._extract_with_pdfplumber(document_id, file_path)

        # Auto Strategy
        response = self._extract_with_pypdf(document_id, file_path)

        if response.character_count > 50:
            return response

        return self._extract_with_pdfplumber(document_id, file_path)

    def _extract_with_pypdf(
        self,
        document_id: str,
        file_path: Path,
    ) -> ExtractionResponse:

        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:
            pages.append(page.extract_text() or "")

        text = "\n".join(pages)

        # Clean extracted text
        text = TextCleaner.clean(text)

        return ExtractionResponse(
            document_id=document_id,
            page_count=len(reader.pages),
            character_count=len(text),
            text=text,
            extraction_engine="pypdf",
            message="Text extracted successfully.",
        )

    def _extract_with_pdfplumber(
        self,
        document_id: str,
        file_path: Path,
    ) -> ExtractionResponse:

        pages = []

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:
                pages.append(page.extract_text() or "")

        text = "\n".join(pages)

        # Clean extracted text
        text = TextCleaner.clean(text)

        return ExtractionResponse(
            document_id=document_id,
            page_count=len(pdf.pages),
            character_count=len(text),
            text=text,
            extraction_engine="pdfplumber",
            message="Text extracted successfully.",
        )