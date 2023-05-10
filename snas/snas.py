import os


def swap_spaces_newlines(text: str) -> str:
    swapped_text = text.replace(" ", "\0")
    swapped_text = swapped_text.replace("\n", " ")
    swapped_text = swapped_text.replace("\0", "\n")
    return swapped_text


def restore_spaces_newlines(text: str) -> str:
    restored_text = text.replace("\n", "\0")
    restored_text = restored_text.replace(" ", "\n")
    restored_text = restored_text.replace("\0", " ")
    return restored_text


def process_file(file_path: str, operation: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()

    if operation == "swap":
        processed_text = swap_spaces_newlines(original_text)
    elif operation == "restore":
        processed_text = restore_spaces_newlines(original_text)
    else:
        print("Invalid operation. Please choose 'swap' or 'restore'.")
        return

    output_file_path = os.path.splitext(file_path)[0] + f"_processed_{operation}.txt"
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(processed_text)

    print(f"Processed file saved as {output_file_path}")


# Example usage
file_path = input("Enter the path to the file you want to process: ")
operation = input("Enter the operation you want to perform (swap or restore): ")
process_file(file_path, operation)
