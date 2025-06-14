#!/usr/bin/env python3
"""
Convert YAML CV data to LaTeX commands
Usage: python yaml_to_latex.py data.yaml [cv|cover-letter]
"""

import yaml
import sys
import re

def escape_latex(text):
    """Escape special LaTeX characters in text"""
    # Don't escape text that already contains LaTeX commands
    if '\\' in text and any(cmd in text for cmd in ['href', 'textbf', 'Delta', '@']):
        return text
    
    # Basic escaping for plain text
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('^', '\\^{}')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\~{}')
    return text

def load_yaml(filename):
    """Load YAML data from file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_latex_commands(data):
    """Generate LaTeX commands from YAML data"""
    commands = []
    
    # Personal information
    commands.append("% CV Data - LaTeX commands generated from YAML")
    commands.append(f"\\newcommand{{\\cvname}}{{{escape_latex(data['personal']['name'])}}}")
    commands.append(f"\\newcommand{{\\cvtitle}}{{{escape_latex(data['personal']['title'])}}}")
    commands.append("")
    
    # Contact information
    commands.append("% Contact information")
    for i, contact in enumerate(data['personal']['contacts']):
        suffix = ['email', 'web', 'github', 'linkedin', 'orcid'][i]
        commands.append(f"\\newcommand{{\\contact{suffix}}}{{{escape_latex(contact['text'])}}}")
        if 'url' in contact:
            commands.append(f"\\newcommand{{\\contact{suffix}url}}{{{contact['url']}}}")
        commands.append(f"\\newcommand{{\\contact{suffix}icon}}{{{contact['icon']}}}")
        commands.append(f"\\newcommand{{\\contact{suffix}raise}}{{{contact['raise']}}}")
        commands.append("")
    
    # Experience entries
    commands.append("% Experience entries")
    commands.append(f"\\newcommand{{\\experiencecount}}{{{len(data['experience'])}}}")
    commands.append("")
    
    for i, exp in enumerate(data['experience'], 1):
        num = ['one', 'two', 'three', 'four', 'five'][i-1]
        commands.append(f"\\newcommand{{\\experience{num}ta}}{{{escape_latex(exp['title'])}}}")
        commands.append(f"\\newcommand{{\\experience{num}org}}{{{escape_latex(exp['organization'])}}}")
        commands.append(f"\\newcommand{{\\experience{num}orgurl}}{{{exp['organization_url']}}}")
        commands.append(f"\\newcommand{{\\experience{num}loc}}{{{escape_latex(exp['location'])}}}")
        commands.append(f"\\newcommand{{\\experience{num}date}}{{{escape_latex(exp['duration'])}}}")
        commands.append(f"\\newcommand{{\\experience{num}itemcount}}{{{len(exp['items'])}}}")
        
        for j, item in enumerate(exp['items'], 1):
            item_num = ['one', 'two', 'three', 'four', 'five'][j-1]
            commands.append(f"\\newcommand{{\\experience{num}item{item_num}}}{{{item}}}")
        commands.append("")
    
    # Education entries
    commands.append("% Education entries")
    commands.append(f"\\newcommand{{\\educationcount}}{{{len(data['education'])}}}")
    commands.append("")
    
    for i, edu in enumerate(data['education'], 1):
        num = ['one', 'two', 'three', 'four', 'five'][i-1]
        commands.append(f"\\newcommand{{\\education{num}inst}}{{{escape_latex(edu['institution'])}}}")
        commands.append(f"\\newcommand{{\\education{num}insturl}}{{{edu['institution_url']}}}")
        commands.append(f"\\newcommand{{\\education{num}degree}}{{{escape_latex(edu['degree'])}}}")
        commands.append(f"\\newcommand{{\\education{num}loc}}{{{escape_latex(edu['location'])}}}")
        commands.append(f"\\newcommand{{\\education{num}date}}{{{escape_latex(edu['duration'])}}}")
        commands.append(f"\\newcommand{{\\education{num}itemcount}}{{{len(edu['items'])}}}")
        
        for j, item in enumerate(edu['items'], 1):
            item_num = ['one', 'two', 'three', 'four', 'five'][j-1]
            commands.append(f"\\newcommand{{\\education{num}item{item_num}}}{{{item}}}")
        commands.append("")
    
    # Volunteering entries
    commands.append("% Volunteering entries")
    commands.append(f"\\newcommand{{\\volunteeringcount}}{{{len(data['volunteering'])}}}")
    commands.append("")
    
    for i, vol in enumerate(data['volunteering'], 1):
        num = ['one', 'two', 'three', 'four', 'five'][i-1]
        commands.append(f"\\newcommand{{\\volunteering{num}ta}}{{{escape_latex(vol['title'])}}}")
        commands.append(f"\\newcommand{{\\volunteering{num}org}}{{{escape_latex(vol['organization'])}}}")
        commands.append(f"\\newcommand{{\\volunteering{num}orgurl}}{{{vol['organization_url']}}}")
        commands.append(f"\\newcommand{{\\volunteering{num}loc}}{{{escape_latex(vol['location'])}}}")
        commands.append(f"\\newcommand{{\\volunteering{num}date}}{{{escape_latex(vol['duration'])}}}")
        commands.append(f"\\newcommand{{\\volunteering{num}itemcount}}{{{len(vol['items'])}}}")
        
        for j, item in enumerate(vol['items'], 1):
            item_num = ['one', 'two', 'three', 'four', 'five'][j-1]
            commands.append(f"\\newcommand{{\\volunteering{num}item{item_num}}}{{{item}}}")
        commands.append("")
    
    # Honors/Awards
    commands.append("% Honors/Awards")
    commands.append(f"\\newcommand{{\\honorscount}}{{{len(data['honors'])}}}")
    commands.append("")
    
    for i, honor in enumerate(data['honors'], 1):
        num = ['one', 'two', 'three', 'four', 'five', 'six'][i-1]
        commands.append(f"\\newcommand{{\\honors{num}title}}{{{escape_latex(honor['title'])}}}")
        commands.append(f"\\newcommand{{\\honors{num}org}}{{{escape_latex(honor['organization'])}}}")
        commands.append(f"\\newcommand{{\\honors{num}date}}{{{escape_latex(honor['date'])}}}")
        commands.append("")
    
    # Skills
    commands.append("% Skills")
    commands.append(f"\\newcommand{{\\skillscount}}{{{len(data['skills'])}}}")
    commands.append("")
    
    for i, skill in enumerate(data['skills'], 1):
        num = ['one', 'two', 'three', 'four', 'five'][i-1]
        commands.append(f"\\newcommand{{\\skills{num}category}}{{{escape_latex(skill['category'])}}}")
        commands.append(f"\\newcommand{{\\skills{num}items}}{{{skill['items']}}}")
        commands.append("")
    
    # Languages
    commands.append("% Languages")
    commands.append(f"\\newcommand{{\\languagescount}}{{{len(data['languages'])}}}")
    commands.append("")
    
    for i, lang in enumerate(data['languages'], 1):
        num = ['one', 'two', 'three', 'four', 'five'][i-1]
        commands.append(f"\\newcommand{{\\language{num}lang}}{{{escape_latex(lang['language'])}}}")
        commands.append(f"\\newcommand{{\\language{num}prof}}{{{escape_latex(lang['proficiency'])}}}")
        if i < len(data['languages']):
            commands.append("")
    
    return '\\n'.join(commands)

def generate_cover_letter_commands(data):
    """Generate LaTeX commands for cover letter from YAML data"""
    commands = []
    
    # Personal information (shared with CV)
    commands.append("% Cover Letter Data - LaTeX commands generated from YAML")
    commands.append(f"\\newcommand{{\\cvname}}{{{escape_latex(data['personal']['name'])}}}")
    commands.append(f"\\newcommand{{\\cvtitle}}{{{escape_latex(data['personal']['title'])}}}")
    commands.append("")
    
    # Contact information (shared with CV)
    commands.append("% Contact information")
    for i, contact in enumerate(data['personal']['contacts']):
        suffix = ['email', 'web', 'github', 'linkedin', 'orcid'][i]
        commands.append(f"\\newcommand{{\\contact{suffix}}}{{{escape_latex(contact['text'])}}}")
        if 'url' in contact:
            commands.append(f"\\newcommand{{\\contact{suffix}url}}{{{contact['url']}}}")
        commands.append(f"\\newcommand{{\\contact{suffix}icon}}{{{contact['icon']}}}")
        commands.append(f"\\newcommand{{\\contact{suffix}raise}}{{{contact['raise']}}}")
        commands.append("")
    
    # Cover letter specific content
    if 'cover_letter' in data:
        cl = data['cover_letter']
        commands.append("% Cover letter specific content")
        
        # Recipient
        commands.append(f"\\newcommand{{\\recipientname}}{{{escape_latex(cl['recipient']['name'])}}}")
        commands.append(f"\\newcommand{{\\recipienttitle}}{{{escape_latex(cl['recipient']['title'])}}}")
        commands.append(f"\\newcommand{{\\recipientorg}}{{{escape_latex(cl['recipient']['organization'])}}}")
        commands.append(f"\\newcommand{{\\recipientaddress}}{{{escape_latex(cl['recipient']['address'])}}}")
        commands.append("")
        
        # Letter content
        commands.append(f"\\newcommand{{\\coverlettersubject}}{{{escape_latex(cl['subject'])}}}")
        commands.append(f"\\newcommand{{\\coverlettergreeting}}{{{escape_latex(cl['greeting'])}}}")
        commands.append("")
        
        # Content paragraphs
        commands.append(f"\\newcommand{{\\coverletteropening}}{{{escape_latex(cl['content']['opening'])}}}")
        commands.append(f"\\newcommand{{\\coverletterbody}}{{{escape_latex(cl['content']['body'])}}}")
        commands.append(f"\\newcommand{{\\coverletterclosing}}{{{escape_latex(cl['content']['closing'])}}}")
        commands.append("")
        
        # Signature
        commands.append(f"\\newcommand{{\\coverlettersignature}}{{{escape_latex(cl['signature'])}}}")
    
    return '\\n'.join(commands)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python yaml_to_latex.py data.yaml [cv|cover-letter]")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    doc_type = sys.argv[2] if len(sys.argv) == 3 else 'cv'
    
    if doc_type not in ['cv', 'cover-letter']:
        print("Document type must be 'cv' or 'cover-letter'")
        sys.exit(1)
    
    try:
        data = load_yaml(yaml_file)
        if doc_type == 'cv':
            latex_commands = generate_latex_commands(data)
        else:  # cover-letter
            latex_commands = generate_cover_letter_commands(data)
        print(latex_commands)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
