import os
import ast
import builtins

class FileWriter:
    def __init__(self, output_dir_path: str):
        # Store the path of the output directory
        self.output_dir_path = output_dir_path

    def write_file(self, file_name: str, file_contents: str):
        """
        Write the file contents to a .py file in the output directory.

        Args:
            file_name: The name of the file (without the .py extension).
            file_contents: The contents of the file as a string.
        """
        file_path = os.path.join(self.output_dir_path, file_name + '.py')
        with open(file_path, 'w') as f:
            f.write(file_contents)
        
        # After writing the Python file, check its content for import statements
        self.check_dependencies(file_contents)

    def check_dependencies(self, file_contents: str):
        """
        Check the file contents for import statements and write them to a requirements.txt file.

        Args:
            file_contents: The contents of the file as a string.
        """
        imports = set()  # to avoid duplicates
        tree = ast.parse(file_contents)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module.split('.')[0])

        # Get the list of built-in modules
        built_in_modules = dir(builtins)

        requirements = [lib for lib in imports if lib not in built_in_modules]
        if requirements:
            self.write_requirements_file(requirements)

    def write_requirements_file(self, requirements: list):
        """
        Write the list of requirements to a requirements.txt file.

        Args:
            requirements: List of required libraries or modules.
        """
        file_path = os.path.join(self.output_dir_path, 'requirements.txt')
        with open(file_path, 'a') as f:
            for requirement in requirements:
                f.write(requirement + '\n')


