import os
import ast

def parse_files(repo_path):
    code_structure = []
    for root, _,files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=file_path)
                        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                        imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
                        code_structure.append({
                            "file": file_path.replace(repo_path, ""),
                            "function" : functions,
                            "classes": classes, 
                            "imports": imports,
                        })
                    except Exception as e:
                        print("parsing error: {e}")
    return code_structure


