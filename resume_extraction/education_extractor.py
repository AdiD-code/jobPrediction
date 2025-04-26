"""
import re

def extract_education_details(text):
    education_details = {
        'degree': '',
        'course': '',
        'college': '',
        'cgpa': '',
        'hsc': '',
        'ssc': ''
    }

    # Lists of possible degree names and courses
    degree_names = [
        "Bachelor of Technology", "B.Tech", "Master of Technology", "M.Tech", 
        "Doctor of Philosophy", "Ph.D.", "Bachelor of Science", "B.Sc", "Master of Science", "M.Sc",
        "Bachelor of Engineering", "BE", "Bachelor of Arts", "BA", "Master of Arts", "MA"
        # Add more variations as needed
    ]

    course_names = [
        "Computer Science and Engineering", "CSE", "Electronics", 
        "Mechanical Engineering", "Civil Engineering", "Information Technology", "IT"
        # Add more variations as needed
    ]

    # Lists of possible variations for HSC and SSC
    hsc_variations = [
        "HSC", "12th Standard", "Intermediate", "Higher Secondary School Certificate",
        "Senior Secondary Certificate", "Pre-University Certificate", "Class 12", "12th"
        # Add more variations as needed
    ]
    ssc_variations = [
        "SSC", "Class 10", "Matriculation", "10th Standard", "Class X", 
        "All India Secondary School Examination", "Secondary School Leaving Certificate", "10th"
        # Add more variations as needed
    ]

    # Dictionary for acronyms and abbreviations
    acronyms = {
        "CSE": "Computer Science and Engineering",
        "IT": "Information Technology",
        # Add more mappings as needed
    }

    # Degree extraction
    for degree in degree_names:
        degree_pattern = re.compile(rf'\b{degree}\b', re.IGNORECASE)
        degree_match = degree_pattern.search(text)
        if degree_match:
            education_details['degree'] = degree_match.group().strip()
            break

    # Course extraction
    for course in course_names:
        course_pattern = re.compile(rf'\b{course}\b', re.IGNORECASE)
        course_match = course_pattern.search(text)
        if course_match:
            education_details['course'] = course_match.group().strip()
            break

    # College extraction (unchanged)
    college_pattern = re.compile(r'(?:[A-Za-z\s]+(?:College|University|Institute))[^\n]*', re.IGNORECASE)
    college_match = college_pattern.search(text)
    if college_match:
        education_details['college'] = college_match.group().strip()

    # CGPA extraction (unchanged)
    cgpa_floating_pattern = re.compile(r'\b([0-9]{1}\.[0-9]+|[0-9]\.[0-9]{1,2})\b', re.IGNORECASE)
    cgpa_floating_matches = cgpa_floating_pattern.findall(text)
    for match in cgpa_floating_matches:
        value = float(match)
        if 5.0 < value < 10.0:
            education_details['cgpa'] = match
            break
    
    # HSC extraction
    for variation in hsc_variations:
        pattern = re.compile(rf'{variation}[:\-]?\s*([\d\.]+)%?', re.IGNORECASE)
        hsc_match = pattern.search(text)
        if hsc_match:
            value = float(hsc_match.group(1))
            if 35 <= value <= 100:
                education_details['hsc'] = hsc_match.group(1).strip()
                break

    # SSC extraction
    for variation in ssc_variations:
        pattern = re.compile(rf'{variation}[:\-]?\s*([\d\.]+)%?', re.IGNORECASE)
        ssc_match = pattern.search(text)
        if ssc_match:
            value = float(ssc_match.group(1))
            if 35 <= value <= 100:
                education_details['ssc'] = ssc_match.group(1).strip()
                break

    return education_details

    """

import re

def standardize_degree(degree):
    # Map common degree abbreviations to standard forms
    degree_mapping = {
        'B.Tech': 'Bachelor of Technology', 'B.TECH': 'Bachelor of Technology', 'B.TECH.': 'Bachelor of Technology',
        'B.Tech.': 'Bachelor of Technology', 'Bachelor of Engineering': 'Bachelor of Engineering',
        'BE': 'Bachelor of Engineering', 'B.E.': 'Bachelor of Engineering', 'B.Sc. Engineering': 'Bachelor of Science in Engineering',
        'B.Sc Engineering': 'Bachelor of Science in Engineering', 'M.Tech': 'Master of Technology',
        'M.TECH': 'Master of Technology', 'M.TECH.': 'Master of Technology', 'M.Tech.': 'Master of Technology',
        'M.E.': 'Master of Engineering', 'M.E': 'Master of Engineering', 'M.Sc. Engineering': 'Master of Science in Engineering',
        'M.Sc Engineering': 'Master of Science in Engineering', 'Ph.D.': 'Doctor of Philosophy',
        'PhD': 'Doctor of Philosophy', 'D.Sc': 'Doctor of Science', 'D.Tech': 'Doctor of Technology',
        'MSc': 'Master of Science', 'MASc': 'Master of Applied Science', 'MEng': 'Master of Engineering',
        'B.Sc': 'Bachelor of Science', 'BA': 'Bachelor of Arts', 'MA': 'Master of Arts',
        'MBA': 'Master of Business Administration', 'BBA': 'Bachelor of Business Administration'
    }
    return degree_mapping.get(degree, degree)

def standardize_course(course):
    # Map common course abbreviations to standard forms
    course_mapping = {
        'CSE': 'Computer Science and Engineering', 'Computer Science': 'Computer Science and Engineering',
        'IT': 'Information Technology', 'Information Technology': 'Information Technology',
        'ECE': 'Electronics and Communication Engineering', 'Electronics': 'Electronics and Communication Engineering',
        'EEE': 'Electrical and Electronics Engineering', 'Electrical': 'Electrical and Electronics Engineering',
        'ME': 'Mechanical Engineering', 'Mechanical': 'Mechanical Engineering',
        'CE': 'Civil Engineering', 'Civil Engineering': 'Civil Engineering',
        'ChE': 'Chemical Engineering', 'Chemical Engineering': 'Chemical Engineering',
        'AE': 'Aerospace Engineering', 'Aerospace Engineering': 'Aerospace Engineering',
        'BioE': 'Bioengineering', 'Biomedical Engineering': 'Biomedical Engineering',
        'EnvE': 'Environmental Engineering', 'Environmental Engineering': 'Environmental Engineering',
        'IE': 'Industrial Engineering', 'Industrial Engineering': 'Industrial Engineering',
        'SE': 'Software Engineering', 'Software Engineering': 'Software Engineering',
        'CS': 'Computer Science', 'Data Science': 'Data Science', 'DS': 'Data Science',
        'Cybersec': 'Cybersecurity', 'Cybersecurity': 'Cybersecurity',
        'NLP': 'Natural Language Processing', 'AI': 'Artificial Intelligence',
        'ML': 'Machine Learning', 'DBS': 'Database Systems', 'CC': 'Cloud Computing',
        'WD': 'Web Development', 'MC': 'Mobile Computing', 'ES': 'Embedded Systems',
        'VLSI': 'Very-Large-Scale Integration', 'SP': 'Signal Processing',
        'PS': 'Power Systems', 'CS': 'Control Systems', 'Robotics': 'Robotics Engineering'
    }
    return course_mapping.get(course, course)


def extract_education_details(text):
    education_details = {
        'degree': '',
        'course': '',
        'college': '',
        'cgpa': '',
        'hsc': '',
        'ssc': ''
    }

    # List of possible degree names
    degree_names = [
        # Bachelor's Degrees
        "Bachelor of Technology", "B.Tech", "Bachelor of Science in Engineering", "B.Sc. Eng.", 
        "Bachelor of Engineering", "BE", "Bachelor of Applied Science", "BASc", "Bachelor of Science", "B.Sc",
        "Bachelor of Computer Science", "BCompSc", "Bachelor of Electrical Engineering", "BEEE",
        "Bachelor of Mechanical Engineering", "BME", "Bachelor of Civil Engineering", "BCE",
        "Bachelor of Chemical Engineering", "BChE", "Bachelor of Aerospace Engineering", "BAeroE",
        "Bachelor of Industrial Engineering", "BIE", "Bachelor of Environmental Engineering", "BEnvE",
        "Bachelor of Bioengineering", "BioE", "Bachelor of Software Engineering", "BSE",
        "Bachelor of Information Technology", "BIT", "Bachelor of Construction Engineering", "BConE",
        "Bachelor of Structural Engineering", "BSE", "Bachelor of Systems Engineering", "BSEng",
        "Bachelor of Telecommunications Engineering", "BTE", "Bachelor of Petroleum Engineering", "BPE",
        "Bachelor of Manufacturing Engineering", "BManE", "Bachelor of Robotics Engineering", "BRE",
        "Bachelor of Mechatronics Engineering", "BME", "Bachelor of Optoelectronics Engineering", "BOE",
        "Bachelor of Marine Engineering", "BMarE",

        # Master's Degrees
        "Master of Technology", "M.Tech", "Master of Science in Engineering", "M.Sc. Eng.",
        "Master of Engineering", "ME", "Master of Applied Science", "MASc", "Master of Computer Science", "MCompSc",
        "Master of Electrical Engineering", "MEEE", "Master of Mechanical Engineering", "MME",
        "Master of Civil Engineering", "MCE", "Master of Chemical Engineering", "MChE",
        "Master of Aerospace Engineering", "MAeroE", "Master of Industrial Engineering", "MIE",
        "Master of Environmental Engineering", "MEnvE", "Master of Bioengineering", "BioE",
        "Master of Software Engineering", "MSE", "Master of Information Technology", "MIT",
        "Master of Construction Engineering", "MConE", "Master of Structural Engineering", "MSE",
        "Master of Systems Engineering", "MSEng", "Master of Telecommunications Engineering", "MTE",
        "Master of Petroleum Engineering", "MPE", "Master of Manufacturing Engineering", "MManE",
        "Master of Robotics Engineering", "MRE", "Master of Mechatronics Engineering", "MME",
        "Master of Optoelectronics Engineering", "MOE", "Master of Marine Engineering", "MMarE",

        # Doctoral Degrees
        "Doctor of Philosophy", "Ph.D.", "Doctor of Engineering", "DEng", "Doctor of Applied Science", "DASc",
        "Doctor of Computer Science", "DCompSc", "Doctor of Electrical Engineering", "DEEE",
        "Doctor of Mechanical Engineering", "DME", "Doctor of Civil Engineering", "DCE",
        "Doctor of Chemical Engineering", "DChE", "Doctor of Aerospace Engineering", "DAeroE",
        "Doctor of Industrial Engineering", "DIE", "Doctor of Environmental Engineering", "DEnvE",
        "Doctor of Bioengineering", "DBioE", "Doctor of Software Engineering", "DSE",
        "Doctor of Information Technology", "DIT", "Doctor of Construction Engineering", "DConE",
        "Doctor of Structural Engineering", "DSE", "Doctor of Systems Engineering", "DSEng",
        "Doctor of Telecommunications Engineering", "DTE", "Doctor of Petroleum Engineering", "DPE",
        "Doctor of Manufacturing Engineering", "DManE", "Doctor of Robotics Engineering", "DRE",
        "Doctor of Mechatronics Engineering", "DME", "Doctor of Optoelectronics Engineering", "DOE",
        "Doctor of Marine Engineering", "DMarE",

        # Additional Degrees
        "Bachelor of Design", "B.Des", "Master of Design", "M.Des", "Bachelor of Fine Arts", "BFA",
        "Master of Fine Arts", "MFA", "Bachelor of Architecture", "B.Arch", "Master of Architecture", "M.Arch",
        "Bachelor of Planning", "B.Planning", "Master of Planning", "M.Planning", "Bachelor of Business Administration", "BBA",
        "Master of Business Administration", "MBA", "Bachelor of Management Studies", "BMS", "Master of Management Studies", "MMS",
        "Bachelor of Laws", "LL.B", "Master of Laws", "LL.M", "Bachelor of Commerce", "B.Com", "Master of Commerce", "M.Com",
        "Bachelor of Education", "B.Ed", "Master of Education", "M.Ed", "Bachelor of Hotel Management", "BHM",
        "Master of Hotel Management", "MHM", "Bachelor of Public Administration", "BPA", "Master of Public Administration", "MPA",
    ]

    # List of possible course names
    course_names = [
        # Computer Science and Engineering
        "Computer Science and Engineering", "CSE", "Computer Engineering", "CompE",
        "Software Engineering", "SE", "Information Technology", "IT", "Information Systems", "IS",
        "Cybersecurity", "Cybersec", "Artificial Intelligence", "AI", "Data Science", "DS",
        "Machine Learning", "ML", "Computer Graphics", "CG", "Human-Computer Interaction", "HCI",
        "Computer Networks", "CN", "Database Systems", "DBS", "Cloud Computing", "CC",
        "Web Development", "WD", "Mobile Computing", "MC", "Embedded Systems", "ES",
        "Computer Vision", "CV", "Natural Language Processing", "NLP", "Big Data", "BD",

        # Electrical and Electronics Engineering
        "Electrical Engineering", "EE", "Electronics Engineering", "ECE", "Electronics and Communication Engineering", "ECE",
        "Power Systems", "PS", "Control Systems", "CS", "Signal Processing", "SP",
        "Microelectronics", "ME", "VLSI Design", "VLSI", "Embedded Systems", "ES",
        "Communication Systems", "ComSys", "Instrumentation Engineering", "IE",
        "Electrical and Electronics Engineering", "EEE", "Energy Systems", "ES",

        # Mechanical Engineering
        "Mechanical Engineering", "ME", "Thermal Engineering", "TE", "Design Engineering", "DE",
        "Manufacturing Engineering", "ManE", "Automobile Engineering", "AE",
        "Aerospace Engineering", "AE", "Robotics", "RO", "Mechatronics", "MT",
        "Structural Mechanics", "SM", "Fluid Mechanics", "FM",

        # Civil Engineering
        "Civil Engineering", "CE", "Structural Engineering", "SE", "Geotechnical Engineering", "GE",
        "Transportation Engineering", "TE", "Environmental Engineering", "EnvE",
        "Water Resources Engineering", "WRE", "Construction Engineering", "ConE",
        "Urban Planning", "UP", "Building Technology", "BT",

        # Chemical Engineering
        "Chemical Engineering", "ChE", "Process Engineering", "PE", "Biochemical Engineering", "BE",
        "Petroleum Engineering", "PE", "Materials Science", "MS", "Environmental Chemical Engineering", "ECE",

        # Aerospace Engineering
        "Aerospace Engineering", "AE", "Aeronautical Engineering", "AE", "Astronautical Engineering", "AE",
        "Space Systems Engineering", "SSE", "Propulsion Systems", "PS",

        # Industrial Engineering
        "Industrial Engineering", "IE", "Operations Research", "OR", "Manufacturing Systems", "MS",
        "Supply Chain Management", "SCM", "Quality Engineering", "QE",
        "Human Factors Engineering", "HFE", "Systems Engineering", "SE",

        # Bioengineering and Biomedical Engineering
        "Bioengineering", "BioE", "Biomedical Engineering", "BME", "Biotechnology", "BT",
        "Genetic Engineering", "GE", "Biomechanics", "BM", "Medical Devices", "MD",

        # Environmental Engineering
        "Environmental Engineering", "EnvE", "Sustainable Engineering", "SE", "Water Resources Engineering", "WRE",
        "Waste Management", "WM", "Air Quality Engineering", "AQE", "Environmental Science", "ES",

        # Information Engineering
        "Information Engineering", "IE", "Data Engineering", "DE", "Information Systems", "IS",
        "Information Security", "ISec", "Software Development", "SD", "Database Management", "DBM",

        # Architecture and Planning
        "Architecture", "Arch", "Urban Planning", "UP", "Landscape Architecture", "LA",
        "Construction Management", "CM", "Building Design", "BD", "Sustainable Architecture", "SA",

        # Design and Arts
        "Industrial Design", "ID", "Product Design", "PD", "Graphic Design", "GD",
        "Interior Design", "ID", "Fashion Design", "FD", "Animation", "AN", "Multimedia Design", "MD",

        # Management and Business
        "Business Administration", "BA", "Management Studies", "MS", "Finance", "Fin",
        "Marketing", "MKT", "Human Resources", "HR", "Operations Management", "OM",
        "Entrepreneurship", "ENT", "Strategic Management", "SM",

        # Miscellaneous Engineering Fields
        "Marine Engineering", "MarE", "Nuclear Engineering", "NE", "Petroleum Engineering", "PE",
        "Metallurgical Engineering", "MetE", "Textile Engineering", "TE", "Automotive Engineering", "AE",
        "Agricultural Engineering", "AgE", "Renewable Energy Engineering", "REE"
    ]

    # List of possible variations for HSC
    hsc_variations = [
    # General Terms
        "HSC", "Higher Secondary Certificate", "Higher Secondary School Certificate",
        "12th Standard", "12th Grade", "12th", "Senior Secondary School Certificate",
        "Senior Secondary Certificate", "Intermediate", "Inter", "Class 12", "Grade 12",
        "Higher Secondary", "Higher Sec", "Higher Secondary Education",

        # Alternative Terms and Abbreviations
        "Higher Secondary Exam", "HSE", "Higher Secondary School Exam", "HSSCE",
        "Pre-University", "PUC", "Pre-University Course", "PUC",
        "Plus Two", "10+2", "Senior Secondary Examination", "SSE",
        "Secondary School Certificate", "SSC", "Secondary School Leaving Certificate", "SSLC",
        "A-Level", "Advanced Level", "AS-Level", "Advanced Subsidiary Level",

        # International Terms
        "Secondary Education", "Secondary School", "Senior Year", "Upper Secondary Education",
        "Senior High School", "SHS", "High School Diploma", "HSD", "High School Certificate",

        # Other Regional Variations
        "AISSCE", "All India Senior School Certificate Examination", "CBSE 12th", "ICSE 12th",
        "ISC 12th", "Intermediate Certificate", "Inter Certificate",
        "Senior School Certificate Examination", "SSCE", "Pre-College", "Pre-College Certificate",
    ]


    # List of possible variations for SSC
    ssc_variations = [
    # General Terms
        "SSC", "Secondary School Certificate", "Class 10", "10th Standard", "10th Grade",
        "Matriculation", "Matric", "Secondary School Leaving Certificate", "SSLC",
        "Secondary School Examination", "SSE", "Secondary Certificate", "SC",
        "Senior Secondary School Certificate", "Senior Secondary Certificate",
        
        # Alternative Terms and Abbreviations
        "10+1", "Pre-Matriculation", "Pre-Matric", "Junior Secondary", "JS",
        "Lower Secondary", "LS", "Secondary Education", "SE",
        "High School Diploma", "HSD", "High School Certificate", "HSC",
        
        # International Terms
        "IGCSE", "International General Certificate of Secondary Education",
        "O-Level", "Ordinary Level", "GCSE", "General Certificate of Secondary Education",
        
        # Other Regional Variations
        "ICSE 10th", "CBSE 10th", "ISC 10th", "AISSCE 10th",
        "10th Year", "Tenth Year", "Pre-High School", "Pre-High School Certificate",
        "Basic Education Certificate", "BEC", "Junior High School Diploma",
    ]


    # Dictionary for acronyms and abbreviations
    acronyms = {
        # Engineering and Technology
        "CSE": "Computer Science and Engineering",
        "IT": "Information Technology",
        "SE": "Software Engineering",
        "AI": "Artificial Intelligence",
        "ML": "Machine Learning",
        "DS": "Data Science",
        "CV": "Computer Vision",
        "NLP": "Natural Language Processing",
        "DBS": "Database Systems",
        "CC": "Cloud Computing",
        "WD": "Web Development",
        "MC": "Mobile Computing",
        "ES": "Embedded Systems",
        "PS": "Power Systems",
        "CS": "Control Systems",
        "SP": "Signal Processing",
        "VLSI": "Very-Large-Scale Integration",
        "IE": "Industrial Engineering",
        "BioE": "Bioengineering",
        "BME": "Biomedical Engineering",
        "EnvE": "Environmental Engineering",
        "SSE": "Space Systems Engineering",
        "ME": "Mechanical Engineering",
        "CE": "Civil Engineering",
        "ChE": "Chemical Engineering",
        "AE": "Aerospace Engineering",
        "TE": "Transportation Engineering",
        "WRE": "Water Resources Engineering",
        "ManE": "Manufacturing Engineering",
        "RE": "Renewable Energy Engineering",
        "NE": "Nuclear Engineering",
        "MarE": "Marine Engineering",
        "Robotics": "Robotics Engineering",
        "MT": "Mechatronics Engineering",
        
        # Education and Qualifications
        "HSC": "Higher Secondary Certificate",
        "12th": "12th Standard",
        "SSC": "Secondary School Certificate",
        "10th": "10th Standard",
        "A-Level": "Advanced Level",
        "GCSE": "General Certificate of Secondary Education",
        "IGCSE": "International General Certificate of Secondary Education",
        "PUC": "Pre-University Course",
        "MASc": "Master of Applied Science",
        "ME": "Master of Engineering",
        "MSc": "Master of Science",
        "MTech": "Master of Technology",
        "PhD": "Doctor of Philosophy",
        "DEng": "Doctor of Engineering",
        "DASc": "Doctor of Applied Science",
        
        # Business and Management
        "MBA": "Master of Business Administration",
        "BBA": "Bachelor of Business Administration",
        "HR": "Human Resources",
        "OM": "Operations Management",
        "SCM": "Supply Chain Management",
        "ENT": "Entrepreneurship",
        "MKT": "Marketing",
        "SM": "Strategic Management",
        
        # Design and Arts
        "ID": "Industrial Design",
        "PD": "Product Design",
        "GD": "Graphic Design",
        "FD": "Fashion Design",
        "AN": "Animation",
        "MD": "Multimedia Design",
        
        # Miscellaneous
        "HSD": "High School Diploma",
        "JS": "Junior Secondary",
        "LS": "Lower Secondary",
        "BEC": "Basic Education Certificate",
        "T": "Technical",
        "PE": "Petroleum Engineering",
        "BE": "Bachelor of Engineering",
        "BTech": "Bachelor of Technology",
        "MTech": "Master of Technology",
        "MSc": "Master of Science",
    }

    # Enhanced pattern to ensure "BE" and "ME" are matched only as standalone degrees
    for degree in degree_names:
        degree_pattern = re.compile(r'\b' + re.escape(degree) + r'\b(?!\w)', re.IGNORECASE)
        degree_match = degree_pattern.search(text)
        if degree_match:
            standardized_degree = standardize_degree(degree_match.group().strip())
            education_details['degree'] = standardized_degree
            break

    # Standardize degrees
    for degree in degree_names:
        degree_pattern = re.compile(rf'\b{degree}\b', re.IGNORECASE)
        degree_match = degree_pattern.search(text)
        if degree_match:
            standardized_degree = standardize_degree(degree_match.group().strip())
            education_details['degree'] = standardized_degree
            break

    # Standardize courses
    for course in course_names:
        course_pattern = re.compile(rf'\b{course}\b', re.IGNORECASE)
        course_match = course_pattern.search(text)
        if course_match:
            standardized_course = standardize_course(course_match.group().strip())
            education_details['course'] = standardized_course
            break

    # College extraction
    college_pattern = re.compile(r'(?:[A-Za-z\s]+(?:College|University|Institute))[^\n]*', re.IGNORECASE)
    college_match = college_pattern.search(text)
    if college_match:
        education_details['college'] = college_match.group().strip()

    # CGPA extraction
    cgpa_floating_pattern = re.compile(r'\b([0-9]{1}\.[0-9]+|[0-9]\.[0-9]{1,2})\b', re.IGNORECASE)
    cgpa_floating_matches = cgpa_floating_pattern.findall(text)
    for match in cgpa_floating_matches:
        value = float(match)
        if 5.0 < value < 10.0:
            education_details['cgpa'] = match
            break
    
    # HSC extraction
    for variation in hsc_variations:
        pattern = re.compile(rf'{variation}[:\-]?\s*([\d\.]+)%?', re.IGNORECASE)
        hsc_match = pattern.search(text)
        if hsc_match:
            hsc_value = hsc_match.group(1).strip()
            try:
                value = float(hsc_value)
                if 35 <= value <= 100:
                    education_details['hsc'] = hsc_value
                    break
            except ValueError:
                continue

    # SSC extraction
    for variation in ssc_variations:
        pattern = re.compile(rf'{variation}[:\-]?\s*([\d\.]+)%?', re.IGNORECASE)
        ssc_match = pattern.search(text)
        if ssc_match:
            ssc_value = ssc_match.group(1).strip()
            try:
                value = float(ssc_value)
                if 35 <= value <= 100:
                    education_details['ssc'] = ssc_value
                    break
            except ValueError:
                continue

    return education_details