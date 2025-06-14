# CV and Cover Letter - Dynamic LaTeX from YAML

This repository contains a CV and cover letter system that generates LaTeX documents from structured YAML data, ensuring consistency across documents and easy maintenance.

## Repository Structure

```
├── data.yaml                      # Single source of truth for all content
├── .github/workflows/build.yml    # Automated PDF generation
├── src/
│   ├── cv/
│   │   ├── main.tex              # CV LaTeX template
│   │   ├── cvdata.tex            # Generated LaTeX commands (from YAML)
│   │   ├── yaml_to_latex.py      # YAML to LaTeX converter
│   │   └── README.md             # CV-specific documentation
│   └── cover-letter/
│       ├── main.tex              # Cover letter LaTeX template
│       ├── coverletterdata.tex   # Generated LaTeX commands (from YAML)
│       └── yaml_to_latex.py      # YAML to LaTeX converter (copy)
└── static/
    ├── font/                     # Custom fonts (MontserratExtrabold, etc.)
    └── icon/                     # Icons for contact information
```

## Key Features

- **Single Source of Truth**: All content stored in `data.yaml` at repository root
- **Dynamic Generation**: Both CV and cover letter generated from the same data source
- **Automated CI/CD**: GitHub Actions automatically builds PDFs on push
- **Custom Fonts**: Uses MontserratExtrabold for titles with XeLaTeX compilation
- **Consistent Styling**: Same contact information and formatting across documents

## YAML Data Structure

The `data.yaml` file contains:

### Personal Information (Shared)
- `personal.name`: Full name
- `personal.title`: Professional title/description
- `personal.contacts`: Contact information with icons and formatting

### CV Sections
- `experience`: Work experience entries
- `education`: Educational background
- `volunteering`: Volunteer work
- `honors`: Awards and honors
- `skills`: Technical and soft skills categorized
- `languages`: Language proficiencies

### Cover Letter Section
- `cover_letter.recipient`: Recipient information
- `cover_letter.subject`: Letter subject line
- `cover_letter.greeting`: Personalized greeting
- `cover_letter.content`: Letter body (opening, body, closing paragraphs)
- `cover_letter.signature`: Signature name

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
   xelatex main.tex  # or lualatex main.tex
   ```

### Automated Builds

The GitHub Actions workflow automatically:
1. Sets up Python and installs PyYAML
2. Generates LaTeX command files from YAML data
3. Compiles both CV and cover letter with XeLaTeX
4. Uploads PDFs as artifacts

## Requirements

- **Local**: Python 3.x with PyYAML, XeLaTeX or LuaLaTeX
- **CI/CD**: Handled automatically by GitHub Actions

## Benefits

- **Maintainability**: Update content once in YAML, reflects in both documents
- **Consistency**: Same contact info and personal details across all documents
- **Version Control**: Structured data makes changes easy to track
- **Automation**: Push to GitHub automatically generates updated PDFs
- **Flexibility**: Easy to customize templates while maintaining data separation

## Customization

- **Fonts**: Update font paths in LaTeX templates
- **Styling**: Modify LaTeX templates in `main.tex` files
- **Content**: Edit structured data in `data.yaml`
- **Fields**: Extend Python scripts to support additional YAML fields and cover letter
compile with lualatex or xelatex. lot of dependencies

Visual Appearance:

<img src="https://github.com/user-attachments/assets/87851762-c551-457f-a739-e0a60051c854" width="49%"/> <img src="https://github.com/user-attachments/assets/aa4ce13e-ebf7-45c3-8318-5424fd9b3771" width="49.1%"/>
