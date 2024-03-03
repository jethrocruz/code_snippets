import re

with open(r'/home/jet/VSCODE_SYNC/code_snippets/Regular-Expressions/data.txt') as f:
    data = f.read()

result = re.compile(r'\b\d{3}\b')

result_matches = result.finditer(data)

for matched in result_matches:
    print(matched)
