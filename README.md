# SNAS
### Swap Newline and Spaces



Losslessly Swap Newline and Space (Linux/Ubuntu CLI Command)

This is a Python script that allows you to swap spaces and newlines in any given text file, or restore them back to their original state.

## Requirements
- Python 3.x

## Installation
1. Clone or download the script to your local machine.
2. Open a terminal and navigate to the directory where the script is located.

## Usage
1. In the terminal, run the script by typing `python snas.py`.
2. Enter the path to the file you want to process when prompted.
3. Choose the operation you want to perform (swap or restore).
4. The processed file will be saved with the suffix "_processed_swap.txt" or "_processed_restore.txt" in the same directory as the original file.

## Functions

### `swap_spaces_newlines(text: str) -> str`
Replaces spaces with null characters and newlines with spaces in a given string.

### `restore_spaces_newlines(text: str) -> str`
Replaces null characters with newlines and spaces with null characters in a given string.

### `process_file(file_path: str, operation: str)`
Processes a file located at `file_path` based on the specified `operation` (swap or restore). The processed file will be saved in the same directory as the original file with the suffix "_processed_swap.txt" or "_processed_restore.txt".
