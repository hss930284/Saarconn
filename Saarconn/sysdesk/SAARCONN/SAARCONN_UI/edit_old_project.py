import os
import sys

def process_files(excel_file_path, sdp_file_path):
    # Print the paths of the received files
    print(f"Processing Excel file: {excel_file_path}")
    print(f"Processing SDP file: {sdp_file_path}")
    
    # Simulate some processing (you can replace this with actual logic)
    # For example: processing the Excel and SDP files
    
    # Delete the files after processing
    if os.path.exists(excel_file_path):
        os.remove(excel_file_path)
        print(f"Excel file {excel_file_path} deleted successfully.")
    else:
        print(f"Excel file {excel_file_path} not found.")
    
    if os.path.exists(sdp_file_path):
        os.remove(sdp_file_path)
        print(f"SDP file {sdp_file_path} deleted successfully.")
    else:
        print(f"SDP file {sdp_file_path} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script2.py <excel_file_path> <sdp_file_path>")
    else:
        excel_file_path = sys.argv[1]
        sdp_file_path = sys.argv[2]
        process_files(excel_file_path, sdp_file_path)
