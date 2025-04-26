import re

def extract_key_values(text):
    key_values = {}

    # Patterns for specific sections
    patterns = {
        'cgpa': r'CGPA\s*:\s*(?P<cgpa>[0-9.]+)',
        'percentage': r'Percentage\s*:\s*(?P<percentage>[0-9.]+)',
        'skills': r'Skills\s*:\s*(?P<skills>.+)',
        'college': r'College\s*:\s*(?P<college>.+)',
    }

    for label, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            key_values[label] = match.group(label).strip()

    return key_values
