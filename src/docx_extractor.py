from zipfile import ZipFile
from lxml import etree
import re
import os

def docx_text_extractor(filepath):
    with ZipFile(filepath) as docx_zip:
      with docx_zip.open('word/document.xml') as docx_xml:
        docx_xml_content = docx_xml.read()
        docx_xml_root = etree.XML(docx_xml_content)
        NSMAP=docx_xml_root.nsmap
        docx_paragraphs = docx_xml_root.xpath("w:body//w:p", namespaces=NSMAP)

        filename = os.path.splitext(os.path.basename(filepath))[0]
        folder_name = re.sub(r"_(en|pt)$", "", os.path.splitext(os.path.basename(filepath))[0])
        new_filepath = f'data/documents/extracted/{folder_name}'
        if not os.path.exists(new_filepath):
          os.mkdir(new_filepath)

        with open(f"{new_filepath}/{filename}.txt", "w") as text_file:
          for paragraph in docx_paragraphs:
            inner_texts = paragraph.xpath(".//text()")
            if len(inner_texts) == 0:
              continue

            text_file.write("".join(inner_texts) + "\n")




           