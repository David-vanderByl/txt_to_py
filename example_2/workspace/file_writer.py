# This code was automatically generated from a text file.

import os


class FileWriter:
    def __init__(self, output_dir_path: str):
        self.output_dir_path = output_dir_path

    def write_file(self, file_name: str, file_contents: str):
        file_path = os.path.join(self.output_dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write(file_contents)
