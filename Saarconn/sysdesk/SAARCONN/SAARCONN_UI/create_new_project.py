import os
import sys

def process_file(file_path):
    # Print the path of the received file
    print(f"Processing Excel file: {file_path}")
    
    # Simulate some processing (you can replace this with actual logic)
    # For example: processing the Excel file
    
    # Delete the file after processing
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    else:
        print(f"File {file_path} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script1.py <file_path>")
    else:
        file_path = sys.argv[1]
        process_file(file_path)
