import os

class ReadmeWriter:
    def __init__(self, output_dir_path: str):
        """
        Initialize the ReadmeWriter object.

        Args:
            output_dir_path: Path to the output directory.
        """
        self.output_dir_path = output_dir_path

    def write_readme(self, file_name: str, file_contents: str):
        """
        Write the file contents to the README file.

        Args:
            file_name: Name of the file.
            file_contents: Contents of the file.
        """
        file_path = os.path.join(self.output_dir_path, 'README.md')

        with open(file_path, 'a') as f:   # Notice 'a' for appending
            f.write(f'## {file_name}\n\n')  # Markdown header for the file name
            f.write('```python\n')
            f.write(file_contents + '\n')
            f.write('```\n\n')  # Code block end
