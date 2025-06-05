# Title Insurance Document Parser

This project provides a simple Flask web application that allows users to upload legal documents related to title insurance. The application extracts key sections such as **Exceptions**, **Requirements**, and the **Mortgage Schedule**.

## Installation

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Running

```bash
python app.py
```

Then open your browser at <http://localhost:5000> to upload a document.

The parser supports PDF or plain text files. PDF support requires the `PyPDF2` package.

## Command Line Usage

You can also parse a file directly using the parser module:

```bash
python parser.py path/to/document.pdf
```
