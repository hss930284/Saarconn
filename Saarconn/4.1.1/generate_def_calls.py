import ast

# Input Python file (update this to your source file name)
input_file = "ArElements_Def_v4.1.1.py"

# Output Python file
output_file = "CallFunctions.py"

# Parse the input file and extract function names
with open(input_file, "r") as file:
    tree = ast.parse(file.read())

# Extract function names
function_names = [
    node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
]

# Write the function calls to the output file
with open(output_file, "w") as file:
    file.write("# Auto-generated script to call all functions\n\n")
    for function_name in function_names:
        file.write(f"{function_name}()\n")

print(f"Function calls have been written to {output_file}")
