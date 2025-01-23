import ast

def find_duplicate_variables(code):
    tree = ast.parse(code)
    variables = set()
    duplicates = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if node.id in variables:
                if node.id in duplicates:
                    duplicates[node.id].append(node.lineno)
                else:
                    duplicates[node.id] = [node.lineno]
            variables.add(node.id)

    return duplicates

with open('Combined_main.py', 'r') as f:
    code = f.read()

duplicates = find_duplicate_variables(code)

with open('duplicates.txt', 'w') as f:
    for variable, line_numbers in duplicates.items():
        f.write(f"{variable}: {line_numbers}\n")