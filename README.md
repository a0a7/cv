# LaTeX résumé/cover letter [![Build LaTeX document](https://github.com/a0a7/cv/actions/workflows/build.yml/badge.svg)](https://github.com/a0a7/cv/actions/workflows/build.yml) [![Static Badge](https://img.shields.io/badge/cv%20link-%23121?logo=github&link=https%3A%2F%2Fa0a7.github.io%2Fcv%2Fcv.pdf)](https://a0a7.github.io/cv/cv.pdf) [![Static Badge](https://img.shields.io/badge/cover%20letter%20link-%23121?logo=github&link=https%3A%2F%2Fa0a7.github.io%2Fcv%2Fcv.pdf)](https://a0a7.github.io/cv/cover-letter.pdf)

This repo contains the source for my CV and cover letter. It builds and hosts the pdfs automatically using Github actions on push (links above).

<img src="https://github.com/user-attachments/assets/87851762-c551-457f-a739-e0a60051c854" width="49%"/> <img src="https://github.com/user-attachments/assets/aa4ce13e-ebf7-45c3-8318-5424fd9b3771" width="49.1%"/>

## Usage

### Local Development

1. **Edit Content**: Update `data.yaml` with your information
2. **Generate LaTeX Commands**:
   ```bash
   # For CV
   cd src/cv
   python yaml_to_latex.py ../../data.yaml cv > cvdata.tex
   
   # For Cover Letter
   cd src/cover-letter
   python yaml_to_latex.py ../../data.yaml cover-letter > coverletterdata.tex
   ```
3. **Compile PDFs**:
   ```bash
   xelatex main.tex
   ```

## Requirements

- **Local**: Python 3.x with PyYAML, XeLaTeX or LuaLaTeX

