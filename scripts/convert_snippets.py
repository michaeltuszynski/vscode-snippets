import os
import json

def read_snippet_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def convert_to_snippet(file_path, snippet_text, description):
    lines = snippet_text.split('\n')
    body = [line for line in lines]
    return {
        "prefix": os.path.splitext(os.path.basename(file_path))[0],
        "scope": "terraform",
        "body": body,
        "description": description
    }

def main():
    # Update the snippets_dir path to point to the terraform-snippets folder
    snippets_dir = os.path.join(os.path.dirname(__file__), '../terraform-snippets')
    snippets = {}

    for root, _, files in os.walk(snippets_dir):
        for file_name in files:
            if file_name.endswith('.tf'):
                file_path = os.path.join(root, file_name)
                snippet_text = read_snippet_file(file_path)
                description = f"Snippet for {file_name}"
                snippet_key = os.path.splitext(file_name)[0]
                snippets[snippet_key] = convert_to_snippet(file_path, snippet_text, description)

    # Output the snippets file to the VS Code snippets directory
    output_path = os.path.expanduser('~/Library/Application Support/Code/User/snippets/terraform-snippets.code-snippets')
    with open(output_path, 'w') as snippets_file:
        json.dump(snippets, snippets_file, indent=2)

if __name__ == "__main__":
    main()
