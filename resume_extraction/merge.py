import pandas as pd

# Load the first CSV file into a DataFrame
df1 = pd.read_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/resume_data.csv')

# Load the second CSV file into a DataFrame
df2 = pd.read_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/Job Roles  - Sheet1.csv')

# Ensure the 'Name' column exists in both DataFrames
if 'Name' not in df1.columns or 'Name' not in df2.columns:
    print("The 'Name' column is missing from one of the files.")
else:
    # Strip whitespace from the 'Name' column in both DataFrames
    df1['Name'] = df1['Name'].str.strip()
    df2['Name'] = df2['Name'].str.strip()

    # Merge the two DataFrames on the common column 'Name'
    merged_df = pd.merge(df1, df2, on='Name')

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/merged_file.csv', index=False)

    # Find the indices of the rows that were merged in the original DataFrames
    df1_merged_indices = df1[df1['Name'].isin(merged_df['Name'])].index
    df2_merged_indices = df2[df2['Name'].isin(merged_df['Name'])].index

    # Drop the merged rows from the original DataFrames
    df1_dropped = df1.drop(df1_merged_indices)
    df2_dropped = df2.drop(df2_merged_indices)

    # Save the updated DataFrames back to CSV files
    df1_dropped.to_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/resume_data.csv', index=False)
    df2_dropped.to_csv('C:/Users/Aditya/Desktop/Basuri/MajorProj/already_made/Job Roles  - Sheet1.csv', index=False)

    print("Files merged and updated successfully!")
