# PAC 2026 Report Parser
Parses the PDF report from PDF Accessibility Checker 2026

Given the `pdftext` output of the PAC 2026 "PDF report", extract key metrics (e.g. pass/warn/fail for PDF Syntax, Fonts, Content, etc.) for easier use in subsequent machine processing.

## Requirements
```
pip install pdftext
```

### Usage

#### Output JSON
```
pdftext [filename] | python parse_pdf_report.py
```

#### Output CSV
```
pdftext [filename] | python parse_pdf_report.py | python reformat_parsed_report.py
```

Copyright 2025, University of Pittsburgh, University Library System
Released under an MIT license.
