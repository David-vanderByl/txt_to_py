import re
from typing import List, Tuple

class FileParser:
    def __init__(self, input_file_path: str):
        # Store the path of the input file
        self.input_file_path = input_file_path

    def parse(self) -> List[Tuple[str, str]]:
        """
        Parse the input file and extract Python code blocks with associated file names.

        Returns:
            List of tuples, where each tuple contains a file name and its associated code block.
        """
        # Open the input file and read its content
        with open(self.input_file_path, 'r') as f:
            content = f.read()

        # Parse the content to extract code blocks and file names
        file_pairs = self.parse_python_content(content)
        return file_pairs

    def parse_python_content(self, content):
        """
        Parse the content to extract Python code blocks and associated file names.

        Args:
            content: The content of the input file.

        Returns:
            List of tuples, where each tuple contains a file name and its associated code block.
        """
        # Use regex to find the python code blocks and associated file names
        code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)
        file_names = re.findall(r'(\w+)\.py', content)

        # Add comments to the top of each python file
        comments = '# This code was automatically generated from a text file.'
        code_blocks = [comments + '\n' + block for block in code_blocks]

        file_pairs = list(zip(file_names, code_blocks))
        return file_pairs
