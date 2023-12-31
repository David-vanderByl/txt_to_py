# Use case:
Use with gpt-engineer: https://github.com/AntonOsika/gpt-engineer

Note:
-  The format of the example `all_output.txt` may result in extra .py outputs
-  This code has not been tested on many .txt cases/variations.
-  The code in the example txt files may not be correct as this was autogenerated and not tested.


# Python File Generator from TXT
This script is used to generate Python `.py` files from a text (`.txt`) file. It is designed to work with text files formatted in a specific way: Python code must be enclosed in triple backticks (```) with `python` right after the opening backticks. File names are extracted from lines containing `.py` references.

## Files
1. `file_parser.py`: Contains the `FileParser` class used for parsing the input text file and extracting the Python code blocks.
2. `file_writer.py`: Contains the `FileWriter` class used for writing the Python code blocks into separate `.py` files.
3. `main.py`: Contains the `main` function, which orchestrates the parsing of the text file and the writing of the Python files.

## Usage
Call the `main` function in `main.py` with the path to the input `.txt` file and the output directory as arguments. For example:

```python
