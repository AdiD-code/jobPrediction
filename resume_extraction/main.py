import os
from pdf_parser import extract_text_from_pdf
from skills_extractor import extract_skills
from experience_categorizer import categorize_experience, extract_experience_details
from positions_responsibility_extractor import extract_positions, extract_responsibilities
from education_extractor import extract_education_details
from text_extractor import extract_key_values
from data_formatter import format_data_to_csv, format_data_to_json
from additional_features import extract_languages, extract_certifications

def process_resume(pdf_path):
    #Adding Name
    filename = os.path.basename(pdf_path)

    # Splitting the filename to remove .pdf
    filename_without_extension = filename.split(".pdf")[0]

    # Splitting and selecting the parts you want
    parts = filename_without_extension.split()
    length = len(parts)
    edited_name = ""
    if length == 4:
        edited_name = parts[1] + " " + parts[3]
    elif length == 3:
        edited_name = parts[1] + " " + parts[2]
    else:
        for i in range(1, length, 1):
            edited_name += parts[i] + " "
        edited_name = edited_name.strip()

    # Capitalize the first letter of each word
    edited_name = edited_name.title()

    # Extract text from the resume
    text = extract_text_from_pdf(pdf_path)

    # Extract skills
    skills = extract_skills(text)

    # Categorize and extract experience details
    experience = categorize_experience(text)
    technical_experience = extract_experience_details(experience['technical'])
    non_technical_experience = extract_experience_details(experience['non_technical'])

    # Extract positions of responsibility
    positions = extract_positions(text)
    responsibilities = [extract_responsibilities(pos) for pos in positions]

    # Extract educational details
    education = extract_education_details(text)

    # Extract additional information
    key_values = extract_key_values(text)
    languages = extract_languages(text)
    certifications = extract_certifications(text)

    # Compile all extracted data into a structured format
    data = {
        'Name': edited_name,
        'Technical Skills': skills['Technical Skills'],
        '# of Tech Skills': len(skills['Technical Skills']),
        'Non Technical Skills': skills['Non-Technical Skills'],
        '# of Non Technical Skills': len(skills['Non-Technical Skills']),
        #'Tech_Role': technical_experience['Role'],
        #'Tech_Org': technical_experience['Organization'],
        #'Tech_Dur': technical_experience['Duration'],
        #'Non_Tech_Role': non_technical_experience['Role'],
        #'Non_Tech_Org': non_technical_experience['Organization'],
        #'Non_Tech_Dur': non_technical_experience['Duration'],
        #'Positions': positions,
        '# of Positions': (len(positions) if len(positions) <= 10 else len(positions) // 4),
        #'Responsibilities': responsibilities,
        'Degree': education['degree'],
        'Course': education['course'],
        'College': education['college'],
        'CGPA': education['cgpa'],
        'HSC': education['hsc'],
        'SSC': education['ssc'],
        'Additional Info': {
            'Key Values': key_values,
            'Languages': languages,
            'Certifications': certifications
        }
    }

    return data


def process_all_resumes(directory_path, output_csv_path, output_json_path):
    all_data = []
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory_path, filename)
            print(f"Processing: {pdf_path}")
            resume_data = process_resume(pdf_path)
            all_data.append(resume_data)
    
    # Save the data in both CSV and JSON formats
    format_data_to_csv(all_data, output_csv_path)
    format_data_to_json(all_data, output_json_path)

if __name__ == "__main__":
    # Specify the directory path containing resumes
    directory_path = "C:/Users/Aditya/Desktop/Basuri/MajorProj/Good_resumes"
    # Specify the output file paths
    output_csv_path = "C:/Users/Aditya/Desktop/Basuri/MajorProj/resume_data.csv"
    output_json_path = "C:/Users/Aditya/Desktop/Basuri/MajorProj/resume_data.json"
    process_all_resumes(directory_path, output_csv_path, output_json_path)
