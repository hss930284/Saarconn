import pandas as pd

# Load the Excel file
dataframe1 = pd.read_excel('package_data.xlsx', header=None)  # Ensure the file path is correct

# Display the DataFrame to understand its structure (optional)
print(dataframe1)

# Extract the project name value from the appropriate row
project_name_value = dataframe1.iloc[3, 2]  # This will give you 'xyz'

# Output the project name variable
print(f"Project Name: {project_name_value}")

# Use project_name_value in another variable
new_variable = f"The project name is: {project_name_value}"

# Output the new variable
print(new_variable)