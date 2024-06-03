import tempfile
import uuid
from os.path import join
from pathlib import Path
from pdf_token_type_labels.TokenType import TokenType
from configuration import service_logger


def get_file_path(file_name, extension):
    return join(tempfile.gettempdir(), file_name + "." + extension)


def pdf_content_to_pdf_path(file_content):
    file_id = str(uuid.uuid1())

    pdf_path = Path(get_file_path(file_id, "pdf"))
    pdf_path.write_bytes(file_content)

    return pdf_path


def extract_analysis(segment_boxes: list[dict], types: str):
    if types == "all":
        token_types: list[TokenType] = [t for t in TokenType]
    else:
        token_types: list[TokenType] = [TokenType.from_text(t) for t in types.split()]
    return [segment_box for segment_box in segment_boxes if TokenType.from_text(segment_box["type"]) in token_types]


def extract_text(segment_boxes: list[dict], types: str):
    if types == "all":
        token_types: list[TokenType] = [t for t in TokenType]
    else:
        token_types: list[TokenType] = [TokenType.from_text(t) for t in types.split()]
    service_logger.info(f"Extracted types: {[t.name for t in token_types]}")
    text = " ".join([segment_box["text"] for segment_box in segment_boxes if
                     TokenType.from_text(segment_box["type"]) in token_types])
    return text
