import re

def extract_positions(text):
    positions = []

    positions_keywords = [
        'President', 'Secretary', 'Treasurer', 'Coordinator', 'Chairperson', 'VP', 'Vice President',
        'Director', 'Manager', 'Chair', 'Head', 'Chief', 'Administrator', 'Organizer', 'Convener',
        'Member', 'Rep', 'Representative', 'Delegate', 'Lead', 'Captain', 'Chief Executive Officer',
        'CEO', 'Chief Operating Officer', 'COO', 'Chief Financial Officer', 'CFO', 'Chief Technology Officer',
        'CTO', 'Chief Marketing Officer', 'CMO', 'Program Manager', 'Project Manager', 'Team Leader',
        'Project Coordinator', 'Event Coordinator', 'Club President', 'Club Secretary', 'Club Treasurer',
        'Student Council President', 'Student Council Secretary', 'Student Council Treasurer', 'Head of Department',
        'Faculty Advisor', 'Committee Chair', 'Committee Member', 'Committee Coordinator', 'Board Member',
        'Board Chair', 'Board Secretary', 'Board Treasurer', 'Operations Manager', 'Sales Manager',
        'Marketing Manager', 'HR Manager', 'Recruitment Manager', 'Training Manager', 'Development Lead',
        'Product Manager', 'Technical Lead', 'Innovation Lead', 'Quality Assurance Lead', 'Content Lead',
        'Editorial Lead', 'Community Manager', 'Public Relations Manager', 'Media Coordinator', 'Social Media Manager',
        'Networking Coordinator', 'Outreach Coordinator', 'Fundraising Coordinator', 'Event Manager',
        'Events Chair', 'Event Organizer', 'Conference Chair', 'Symposium Chair', 'Workshop Coordinator',
        'Seminar Coordinator', 'Guest Speaker', 'Advisor', 'Mentor', 'Consultant', 'Ambassador', 'Spokesperson',
        'Facilitator', 'Moderator', 'Strategist', 'Analyst'
    ]

    lines = text.split('\n')
    for line in lines:
        for keyword in positions_keywords:
            if keyword.lower() in line.lower():
                positions.append(line)
                break

    return positions

def extract_responsibilities(position_text):
    responsibilities = re.findall(r'- (.+)', position_text)
    return responsibilities
