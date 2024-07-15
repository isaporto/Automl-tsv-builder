import os

def main():
  original_documents_path = "data/documents/original"

  for filename in os.listdir(original_documents_path):
    current_folder_path = os.path.join(original_documents_path, filename)
    for file in os.listdir(current_folder_path):
      if file.endswith('.pdf'):
        print('pdf')
      elif file.endswith('.docx'):
        print('docx')
      else:
        print('neither')

main()