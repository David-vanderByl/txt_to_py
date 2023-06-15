## file_parser

```python
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

```

## file_writer

```python
# This code was automatically generated from a text file.

import os


class FileWriter:
    def __init__(self, output_dir_path: str):
        self.output_dir_path = output_dir_path

    def write_file(self, file_name: str, file_contents: str):
        file_path = os.path.join(self.output_dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write(file_contents)

```

## main

```python
# This code was automatically generated from a text file.

from typing import List, Tuple
from file_parser import FileParser
from file_writer import FileWriter


def main(input_file_path: str, output_dir_path: str):
    file_parser = FileParser(input_file_path)
    file_writer = FileWriter(output_dir_path)

    file_contents = file_parser.parse()

    for file_name, contents in file_contents:
        file_writer.write_file(file_name, contents)

```

