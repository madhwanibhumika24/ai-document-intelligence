import re


class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Join hyphenated words split across lines
        # Example:
        # develop-
        # ment
        # becomes development
        text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

        # Remove spaces and tabs before newlines
        text = re.sub(r"[ \t]+\n", "\n", text)

        # Collapse multiple spaces/tabs into one space
        text = re.sub(r"[ \t]+", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove spaces at the beginning/end of lines
        text = "\n".join(line.strip() for line in text.splitlines())

        return text.strip()