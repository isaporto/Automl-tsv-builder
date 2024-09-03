import os
from pdf_extractor import pdf_text_extractor
from docx_extractor import docx_text_extractor

def main():
  original_documents_path = "data/documents/original"

  for filename in os.listdir(original_documents_path):
    current_folder_path = os.path.join(original_documents_path, filename)
    for file in os.listdir(current_folder_path):
      full_current_file_path = f"{current_folder_path}/{file}"
      if file.endswith('.pdf'):
        pdf_text_extractor(full_current_file_path)
      elif file.endswith('.docx'):
        docx_text_extractor(full_current_file_path)
      else:
        print(f'File ${file} type not supported')

main()