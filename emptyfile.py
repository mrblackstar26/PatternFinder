import os
import sys

def check_empty_jsp_files(directory, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file has a .jsp extension
                if file.endswith('.jsp'):
                    file_path = os.path.join(root, file)
                    # Check if the file is empty
                    if os.path.getsize(file_path) == 0:
                        outfile.write(f"{file_path}\n")
                        print(f"Empty file found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <directory_path> <output_file_path>")
    else:
        directory_path = sys.argv[1]
        output_file_path = sys.argv[2]
        
        check_empty_jsp_files(directory_path, output_file_path)
