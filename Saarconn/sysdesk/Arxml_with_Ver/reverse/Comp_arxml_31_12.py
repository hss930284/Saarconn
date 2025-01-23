import os
import xml.etree.ElementTree as ET
import pandas as pd
from difflib import unified_diff
import re

def remove_namespace(xml_string):
    """
    Remove namespaces from the XML string to simplify comparison.
    """
    return re.sub(r'xmlns(:\w+)?="[^"]+"|<(\w+):|</(\w+):|(\w+):', r'<\1', xml_string)

def compare_xml_files(file1, file2):
    """
    Compare two ARXML files (after removing namespaces) and return a list of differences grouped into blocks.
    Each block is assigned a serial number starting from 1.
    """
    # Parse the XML files
    try:
        tree1 = ET.parse(file1)
        tree2 = ET.parse(file2)
    except ET.ParseError as e:
        return [f"Error parsing files: {file1}, {file2}, {e}"]

    # Convert XML to string for comparison, and remove namespaces
    xml1 = ET.tostring(tree1.getroot(), encoding='utf-8').decode('utf-8')
    xml2 = ET.tostring(tree2.getroot(), encoding='utf-8').decode('utf-8')

    # Remove namespaces from both XML strings
    xml1_no_ns = remove_namespace(xml1)
    xml2_no_ns = remove_namespace(xml2)

    # Use unified_diff for a line-by-line diff
    diff = list(unified_diff(xml1_no_ns.splitlines(), xml2_no_ns.splitlines(), fromfile=file1, tofile=file2))

    if not diff:
        return ["No differences found."]

    # Group differences into blocks and assign serial numbers
    diff_blocks = []
    current_block = []
    for line in diff:
        if line.startswith("@@"):  # Start of a new block
            if current_block:  # Save the previous block
                diff_blocks.append(current_block)
            current_block = [line]  # Start a new block with the metadata line
        else:
            current_block.append(line)
    if current_block:  # Save the last block
        diff_blocks.append(current_block)

    # Add serial numbers to each block
    diff_with_serial = []
    for i, block in enumerate(diff_blocks, start=1):
        diff_with_serial.append(f"Difference {i}:")
        diff_with_serial.extend(block)

    return diff_with_serial

def generate_comparison_report(folder_path):
    """
    Compare all ARXML files in the provided folder (ignoring namespaces) and generate a comparison report in Excel and text file.
    """
    # Get all ARXML files in the folder
    arxml_files = [f for f in os.listdir(folder_path) if f.endswith('.arxml')]
    
    if len(arxml_files) < 2:
        print("At least two ARXML files are needed for comparison.")
        return

    # Prepare data for Excel and text file
    all_comparison_data = []
    comparisons = []
    header = ['Compared File']  # Start the header with "Compared File"

    # Generate all unique comparison pairs
    for i in range(len(arxml_files)):
        for j in range(i + 1, len(arxml_files)):
            comparisons.append(f"{arxml_files[i]} vs {arxml_files[j]}")

    # Extend the header with all unique comparison pairs
    header.extend(comparisons)

    # Generate comparison results for each file
    for i in range(len(arxml_files)):
        file1 = arxml_files[i]
        file1_path = os.path.join(folder_path, file1)
        
        comparison_results = [file1]  # Add the "Compared File" column
        
        # Compare the file with each of the other files
        for j in range(len(arxml_files)):
            if i != j:
                file2 = arxml_files[j]
                file2_path = os.path.join(folder_path, file2)
                differences = compare_xml_files(file1_path, file2_path)
                comparison_results.append("\n".join(differences))  # Store differences as a string
        
        # Ensure the row has the same number of columns as the header
        if len(comparison_results) < len(header):
            comparison_results.extend([""] * (len(header) - len(comparison_results)))
        
        all_comparison_data.append(comparison_results)

    # Create a separate sheet for each comparison in the Excel report
    report_filename_excel = os.path.join(folder_path, "comparison_report.xlsx")
    with pd.ExcelWriter(report_filename_excel, engine='openpyxl') as writer:
        for i in range(len(arxml_files)):
            file1 = arxml_files[i]
            file1_path = os.path.join(folder_path, file1)
            for j in range(i+ 1, len(arxml_files)):
                file2 = arxml_files[j]
                file2_path = os.path.join(folder_path, file2)
                differences = compare_xml_files(file1_path, file2_path)

                # Create a DataFrame for the current comparison
                comparison_df = pd.DataFrame(differences, columns=["Differences"])
                sheet_name = f"{file1} vs {file2}"[:30]  # Limit sheet name length to 30 characters
                comparison_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Excel comparison report generated with separate sheets: {report_filename_excel}")

    # Save the report to a text file
    report_filename_txt = os.path.join(folder_path, "comparison_report.txt")
    with open(report_filename_txt, "w") as txt_file:
        # Write the header
        txt_file.write("\t".join(header) + "\n")  # Write the header to the text file
        for i in range(len(arxml_files)):
            file1 = arxml_files[i]
            file1_path = os.path.join(folder_path, file1)
            for j in range(i + 1, len(arxml_files)):
                file2 = arxml_files[j]
                file2_path = os.path.join(folder_path, file2)
                differences = compare_xml_files(file1_path, file2_path)
                txt_file.write(f"{file1} vs {file2}\n")  # Write the comparison header
                for line in differences:
                    if line.startswith("Difference"):
                        txt_file.write(line + "\n")  # Write the difference header
                    else:
                        txt_file.write(line + "\n")  # Write the difference line
                txt_file.write("***********************************************************************************\n")  # Add separator line
        
    print(f"Text comparison report generated: {report_filename_txt}")

# Main function to get user input and generate the report
def main():
    folder_path = input("Enter the folder path containing the ARXML files: ").strip()

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("Invalid folder path. Please provide a valid directory.")
        return

    generate_comparison_report(folder_path)

if __name__ == "__main__":
    main()