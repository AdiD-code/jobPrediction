import re

# Predefined lists of technical and non-technical skills
technical_skills = set([
    'Machine Learning', 'Python', 'Java', 'SQL', 'C++', 'TensorFlow', 'React', 'JavaScript', 'C#', 'Ruby',
    'Swift', 'Kotlin', 'PHP', 'HTML', 'CSS', 'MATLAB', 'R', 'SAS', 'Hadoop', 'Spark', 'AWS', 'Azure',
    'Google Cloud Platform', 'Docker', 'Kubernetes', 'Git', 'Version Control', 'RESTful APIs', 'GraphQL',
    'NoSQL', 'MongoDB', 'PostgreSQL', 'MySQL', 'SQLite', 'Elasticsearch', 'Redis', 'Nginx', 'Apache',
    'Jenkins', 'CI/CD', 'Agile', 'Scrum', 'DevOps', 'Linux', 'Unix', 'Bash', 'PowerShell', 'Microservices',
    'Distributed Systems', 'Big Data', 'Data Visualization', 'Tableau', 'Power BI', 'Jupyter Notebooks',
    'Computer Vision', 'NLP', 'Natural Language Processing', 'Deep Learning', 'Neural Networks', 'AI',
    'Data Mining', 'Cloud Computing', 'Serverless Computing', 'Web Development', 'Mobile Development',
    'iOS Development', 'Android Development', 'Game Development', 'Virtual Reality', 'Augmented Reality',
    'Blockchain', 'Cryptocurrency', 'Robotic Process Automation', 'Embedded Systems', 'Internet of Things (IoT)',
    'GIS', 'Bioinformatics', 'Graph Theory', 'Algorithm Design', 'Data Structures', 'Software Development',
    'Systems Programming'
])

non_technical_skills = set([
    'Project Management', 'Team Leadership', 'Communication', 'Public Speaking', 'Negotiation', 'Conflict Resolution',
    'Strategic Planning', 'Time Management', 'Risk Management', 'Client Relations', 'Customer Service', 'Sales',
    'Marketing', 'Budgeting', 'Financial Analysis', 'Human Resources', 'Recruitment', 'Employee Training',
    'Organizational Development', 'Change Management', 'Process Improvement', 'Vendor Management', 'Event Planning',
    'Networking', 'Presentation Skills', 'Persuasion', 'Analytical Thinking', 'Creative Problem Solving',
    'Critical Thinking', 'Decision Making', 'Interpersonal Skills', 'Leadership Development', 'Crisis Management',
    'Compliance Management', 'Policy Development', 'Cultural Competency', 'Ethical Leadership', 'Business Analysis',
    'Administrative Support', 'Office Management', 'Workflow Optimization', 'Product Development', 'Innovation',
    'Data Analysis', 'Report Writing', 'Documentation', 'Team Building', 'Mentoring', 'Coaching', 'Sales Strategy',
    'Market Research', 'Product Management', 'Strategic Communication', 'Training and Development', 'Organizational Skills',
    'Change Facilitation', 'Customer Relationship Management', 'Negotiation Skills', 'Organizational Behavior',
    'Public Relations', 'Brand Management', 'Fundraising', 'Outreach'
])

def standardize_skill(skill):
    # Map common abbreviations to standard forms
    skill_mapping = {
        'ML': 'Machine Learning', 'AI': 'Artificial Intelligence', 'DL': 'Deep Learning', 'NLP': 'Natural Language Processing',
        'SQL': 'Structured Query Language', 'HTML': 'Hypertext Markup Language', 'CSS': 'Cascading Style Sheets',
        'JS': 'JavaScript', 'AWS': 'Amazon Web Services', 'GCP': 'Google Cloud Platform', 'Azure': 'Microsoft Azure',
        'Git': 'Git Version Control', 'CI/CD': 'Continuous Integration/Continuous Deployment', 'PHP': 'PHP', 'Go': 'Go',
        'R': 'R', 'MATLAB': 'MATLAB', 'API': 'Application Programming Interface', 'JVM': 'Java Virtual Machine',
        'SDK': 'Software Development Kit', 'OOP': 'Object-Oriented Programming', 'MVC': 'Model-View-Controller',
        'Django': 'Django', 'Flask': 'Flask', 'JIRA': 'JIRA', 'SCRUM': 'Scrum', 'Agile': 'Agile', 'DevOps': 'DevOps',
        'UX/UI': 'User Experience/User Interface', 'SEO': 'Search Engine Optimization', 'SEM': 'Search Engine Marketing',
        'HDFS': 'Hadoop Distributed File System', 'RDBMS': 'Relational Database Management System', 'NoSQL': 'Not Only SQL',
        'JPA': 'Java Persistence API', 'ORM': 'Object-Relational Mapping', 'ETL': 'Extract, Transform, Load',
        'OLAP': 'Online Analytical Processing', 'OLTP': 'Online Transaction Processing', 'REST': 'Representational State Transfer',
        'SOAP': 'Simple Object Access Protocol', 'SaaS': 'Software as a Service', 'PaaS': 'Platform as a Service',
        'IaaS': 'Infrastructure as a Service', 'IoT': 'Internet of Things', 'BPM': 'Business Process Management',
        'ERP': 'Enterprise Resource Planning', 'CRM': 'Customer Relationship Management', 'JSON': 'JavaScript Object Notation',
        'XML': 'eXtensible Markup Language', 'XSD': 'XML Schema Definition', 'XSLT': 'eXtensible Stylesheet Language Transformations',
        'YAML': 'YAML Ain\'t Markup Language', 'XMPP': 'Extensible Messaging and Presence Protocol', 'LDAP': 'Lightweight Directory Access Protocol',
        'OAuth': 'Open Authorization', 'JWT': 'JSON Web Token'
    }
    return skill_mapping.get(skill, skill)

def extract_skills(text):
    technical_found = set()
    non_technical_found = set()

    # Extract skills from predefined lists
    for skill in technical_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            technical_found.add(skill)

    for skill in non_technical_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            non_technical_found.add(skill)

    # Detect new or unique skills
    words = set(re.findall(r'\b\w+\b', text))
    for word in words:
        standardized = standardize_skill(word)
        if standardized not in technical_skills and standardized not in non_technical_skills:
            if word in technical_skills:
                technical_found.add(standardized)
            elif word in non_technical_skills:
                non_technical_found.add(standardized)

    return {
        'Technical Skills': list(technical_found),
        'Non-Technical Skills': list(non_technical_found)
    }

# Example usage
text_example = """
Collaborated with a team to enhance the Quiz section using ReactJs, Python, and Machine Learning.
Experienced in project management and public speaking. Proficient in JavaScript, SQL, and Data Visualization.
"""
print(extract_skills(text_example))
