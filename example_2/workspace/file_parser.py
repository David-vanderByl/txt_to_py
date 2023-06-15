# This code was automatically generated from a text file.

from typing import List, Tuple


class FileParser:
    def __init__(self, input_file_path: str):
        self.input_file_path = input_file_path

    def parse(self) -> List[Tuple[str, str]]:
        with open(self.input_file_path, 'r') as f:
            lines = f.readlines()

        file_contents = []
        current_file_contents = []
        current_file_name = None

        for line in lines:
            if line.startswith('#'):
                if current_file_name is not None:
                    file_contents.append((current_file_name, ''.join(current_file_contents)))
                    current_file_contents = []
                current_file_name = line.strip()[1:].strip() + '.py'
            else:
                current_file_contents.append(line)

        if current_file_name is not None:
            file_contents.append((current_file_name, ''.join(current_file_contents)))

        return file_contents
