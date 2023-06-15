from file_parser import FileParser
from file_writer import FileWriter
from readme_writer import ReadmeWriter

def main(input_file_path: str, output_dir_path: str):
    """
    Main function to parse the input file, write Python files, and generate a README.

    Args:
        input_file_path: Path to the input file.
        output_dir_path: Path to the output directory.

    """
    # Create instances of FileParser, FileWriter, and ReadmeWriter
    file_parser = FileParser(input_file_path)
    file_writer = FileWriter(output_dir_path)
    readme_writer = ReadmeWriter(output_dir_path)

    # Parse the input file to obtain file contents
    file_contents = file_parser.parse()

    # Iterate over file contents and write Python files
    for file_name, contents in file_contents:
        file_writer.write_file(file_name, contents)
        readme_writer.write_readme(file_name, contents)


# Input and output directory paths
input_txt = './example_2/workspace/all_output.txt'
output_dir = './example_2/workspace'

# Call the main function with the input and output paths
main(input_txt, output_dir)
