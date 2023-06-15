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
