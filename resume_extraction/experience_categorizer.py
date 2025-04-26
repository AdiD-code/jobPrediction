import re

def categorize_experience(text):
    experience = {'technical': [], 'non_technical': []}

    # Define patterns for technical and non-technical roles
    technical_keywords = [
        'Developer', 'Engineer', 'Data Scientist', 'Programmer', 'Architect', 'Analyst',
        'Software Engineer', 'Systems Engineer', 'Backend Developer', 'Frontend Developer',
        'Full Stack Developer', 'Machine Learning Engineer', 'AI Engineer', 'Data Engineer',
        'Database Administrator', 'DevOps Engineer', 'Cloud Engineer', 'Embedded Systems Engineer',
        'Security Engineer', 'Network Engineer', 'QA Engineer', 'Test Engineer', 'Application Developer',
        'Mobile Developer', 'Web Developer', 'Game Developer', 'UI/UX Designer', 'Solutions Architect',
        'Technical Lead', 'Research Scientist', 'Data Analyst', 'Business Intelligence Analyst', 
        'Big Data Engineer', 'IoT Engineer', 'Blockchain Developer', 'AR/VR Developer', 'Automation Engineer',
        'Performance Engineer', 'Site Reliability Engineer', 'Technical Consultant', 'Systems Administrator',
        'Data Architect', 'Product Engineer', 'Technology Consultant', 'Technical Writer', 'Software Architect',
        'Integration Engineer', 'Release Manager', 'Cloud Solutions Architect', 'Systems Analyst', 'Database Engineer',
        'Algorithm Engineer', 'Bioinformatics Specialist', 'Robotics Engineer', 'Graphics Programmer'
    ]

    non_technical_keywords = [
        'Manager', 'Coordinator', 'Consultant', 'Administrator', 'Executive', 'Director', 'Supervisor', 'Leader',
        'Officer', 'Specialist', 'Advisor', 'Project Manager', 'Program Manager', 'Business Manager',
        'Operations Manager', 'HR Manager', 'Training Manager', 'Account Manager', 'Sales Manager',
        'Marketing Manager', 'Customer Service Manager', 'Public Relations Manager', 'Event Manager', 
        'Finance Manager', 'Product Manager', 'Compliance Officer', 'Risk Manager', 'Strategist', 'Planner',
        'Analyst', 'Recruiter', 'Director of Operations', 'Chief Officer', 'Executive Director', 'Vice President',
        'President', 'Chief Executive Officer', 'Chief Operating Officer', 'Chief Financial Officer',
        'Chief Marketing Officer', 'Chief Human Resources Officer', 'Chief Administrative Officer',
        'Team Leader', 'Client Relationship Manager', 'Fundraising Manager', 'Outreach Coordinator',
        'Business Development Manager', 'Training Coordinator', 'Program Coordinator', 'Consulting Manager',
        'Customer Experience Manager', 'Policy Advisor', 'Administrative Assistant', 'Office Manager',
        'Regional Manager', 'Branch Manager', 'Site Manager', 'Inventory Manager', 'Quality Assurance Manager',
        'Logistics Manager', 'Procurement Manager', 'Facility Manager', 'Strategic Planner', 'Communication Specialist',
        'Project Coordinator', 'Executive Assistant', 'Operations Director'
    ]

    lines = text.split('\n')
    for line in lines:
        line_lower = line.lower()

        if any(keyword.lower() in line_lower for keyword in technical_keywords):
            experience['technical'].append(line)
        
        elif any(keyword.lower() in line_lower for keyword in non_technical_keywords):
            experience['non_technical'].append(line)

    return experience

def extract_experience_details(experience):
    details = {
        'Role': [],
        'Organization': [],
        'Duration': []
    }

    for role in experience:
        match = re.search(r'(?P<role>[\w\s]+?)\s+at\s+(?P<organization>[\w\s]+?),\s+(?P<duration>[\w\s]+)', role)
        if match:
            details['Role'].append(match.group('role').strip())
            details['Organization'].append(match.group('organization').strip())
            details['Duration'].append(match.group('duration').strip())
        else:
            print(f"Could not parse the following line: {role}")

    # If you want to return single strings instead of lists, join them
    # details['Role'] = ', '.join(details['Role'])
    # details['Organization'] = ', '.join(details['Organization'])
    # details['Duration'] = ', '.join(details['Duration'])

    return details

