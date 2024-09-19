from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
import pymupdf
import pytesseract
import re
import os


def pdf_text_extractor(filepath):
    text = extract_text(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    folder_name = re.sub(
        r"_(en|pt)$", "", os.path.splitext(os.path.basename(filepath))[0]
    )
    new_filepath = f"data/documents/extracted/{folder_name}"
    if not os.path.exists(new_filepath):
      os.mkdir(new_filepath)

    if bool(text.strip()):
        with pymupdf.open(filepath) as pdf:
            with open(f"{new_filepath}/{filename}.txt", "w") as text_file:
              text_file.truncate()
              for page in pdf:
                pdf_text = page.get_text("text")
                if len(re.sub(r"\s+", "", pdf_text)) == 0:
                  continue
                text_file.write("".join(pdf_text) + "\n")
    else:
      images = convert_from_path(filepath)
      with open(f"{new_filepath}/{filename}.txt", "w") as text_file:
        text_file.truncate()
        for image in images:
          pdf_text = pytesseract.image_to_string(image)
          if pdf_text.strip():
            text_file.write("".join(pdf_text) + "\n")
          else:
            continue
          
