# Script for docx and PDF text extract

Here's small project to automatize text extraction from pdf and docx files and break into text chunks to feed Google AI Translator. That's why, at [directory tree and organization example](#directory-tree-and-organization-example), there's documents containg the same name except for _en and _pt at the end. You can fork this project and make changes to use for your own needs. 

## Table of Contents

  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Directory tree and organization example](#directory-tree-and-organization-example)
  - [Contributing](#contributing)

## Dependencies

## Installation

## Usage

## Directory tree and organization example
This is the directory tree and how your files should be organized so the script works

├── README
├── data
│   ├── documents
│   │   ├── original
│   │   │   └── document_name
│   │   │       ├── document_name_en.docx/pdf
│   │   │       └── document_name_pt.docx/pdf
│   │   └── extracted
│   │       └── document_name
│   │           ├── document_name_en.txt
│   │           └── document_name_pt.txt
│   └── text_chunks
│       └── document_name
│           ├── document_name_en.csv
│           └── document_name_pt.csv
└── src
    ├── app.py
    ├── docx_extractor.py
    └── pdf_extractor.py

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.
and thanks for contributing :)

