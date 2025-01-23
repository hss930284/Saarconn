import ast

def find_duplicate_variable_definitions(code):
    tree = ast.parse(code)
    variable_definitions = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variable_name = target.id
                    if variable_name in variable_definitions:
                        variable_definitions[variable_name].append(node.lineno)
                    else:
                        variable_definitions[variable_name] = [node.lineno]

    duplicates = {}
    for variable_name, line_numbers in variable_definitions.items():
        if len(line_numbers) > 1:
            duplicates[variable_name] = line_numbers

    return duplicates

with open('Combined_main.py', 'r') as f:
    code = f.read()

duplicates = find_duplicate_variable_definitions(code)

with open('duplicates.txt', 'w') as f:
    for variable, line_numbers in duplicates.items():
        f.write(f"{variable}: {line_numbers}\n")