import sys

def find_matching_files(file1_path, file2_path, output_file_path):
    # Read the contents of the first and second text files
    with open(file1_path, 'r') as file1:
        file1_lines = file1.read().splitlines()

    with open(file2_path, 'r') as file2:
        file2_lines = file2.read().splitlines()

    # List to hold the matched filenames
    matched_files = []

    # Check for each filename in the first file if it exists in the second file
    for filename in file1_lines:
        if filename in file2_lines:
            matched_files.append(filename)

    # Write the matched filenames to a new text file
    with open(output_file_path, 'w') as output_file:
        for matched_file in matched_files:
            output_file.write(matched_file + '\n')

    print(f"Matching filenames have been written to '{output_file_path}'.")

if __name__ == "__main__":
    # Check if the correct number of arguments have been passed
    if len(sys.argv) != 4:
        print("Usage: python script.py <file1.txt> <file2.txt> <output_file.txt>")
        sys.exit(1)

    # Assign command-line arguments to variables
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    output_file_path = sys.argv[3]

    # Call the function to find matching files
    find_matching_files(file1_path, file2_path, output_file_path)
