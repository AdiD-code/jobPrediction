import re

def extract_languages(text):
    languages_pattern = r'Languages\s*:\s*(?P<languages>.+)'
    match = re.search(languages_pattern, text, re.IGNORECASE)
    if match:
        return match.group('languages').split(', ')
    return []

def extract_certifications(text):
    certifications_pattern = r'Certifications\s*:\s*(?P<certifications>.+)'
    match = re.search(certifications_pattern, text, re.IGNORECASE)
    if match:
        return match.group('certifications').split(', ')
    return []
