import difflib
import sys

def compare_files(file1, file2):
    """Compare two Python files and highlight differences."""
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        diff = difflib.unified_diff(lines1, lines2, fromfile=file1, tofile=file2, lineterm='')
        
        print("\nDifferences between files:")
        for line in diff:
            if line.startswith("-") and not line.startswith("---"):
                print(f"\033[91m{line}\033[0m")  # Red for removed lines
            elif line.startswith("+") and not line.startswith("+++"):
                print(f"\033[92m{line}\033[0m")  # Green for added lines
            else:
                print(line)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    file1 = 'Eliminating_SystemDesk\\trash\\harshit\\arlements_def\\arElements_def_V4_1_3\\arElements_def_V4_1_3.py'
    file2 = 'Eliminating_SystemDesk\\trash\\harshit\\arlements_def\\arlements_def_V4_0_2\\arlements_def_V4_0_2.py'
    compare_files(file1, file2)
