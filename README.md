# legal-document-analyzer
Legal Document Analyzer is a Python-based tool designed to scan and analyze legal documents for potential security vulnerabilities, such as the inclusion of sensitive information or metadata that could be exploited. The tool leverages natural language processing (NLP) and pattern recognition techniques to identify and flag potential risks.

Features:
- Scans documents for sensitive information (e.g., PII, financial data)
- Identifies hidden metadata in legal documents
- Evaluates document security based on file type and content
- Provides a security score and recommendations for document sanitization

## Installation
```bash
pip install -r requirements.txt

## Usage
python legaldocanalyzer.py document.pdf
