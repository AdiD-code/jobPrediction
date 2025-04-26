import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/resume_data.csv')

# Convert the 'Technical Skills' and 'Non Technical Skills' columns from strings to lists
df['Technical Skills'] = df['Technical Skills'].apply(eval)
df['Non Technical Skills'] = df['Non Technical Skills'].apply(eval)

# Create new columns for the count of skills
df['# of tech skills'] = df['Technical Skills'].apply(len)
df['# of non tech skills'] = df['Non Technical Skills'].apply(len)

# Save the updated DataFrame to a new CSV file
df.to_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/resume_data.csv', index=False)

print("Count columns added and saved to skills_count_updated.csv")