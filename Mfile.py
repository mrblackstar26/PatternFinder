import os
import argparse

def find_missing_jsp_files(jsp_list_file, code_folder, output_file):
    # Read the JSP filenames from the list file
    with open(jsp_list_file, 'r') as file:
        jsp_filenames = [line.strip() for line in file.readlines()]

    # Initialize a list to store JSP filenames that are missing in the code folder
    missing_files = []

    # Loop through the JSP filenames
    for jsp_filename in jsp_filenames:
        file_found = False

        # Walk through all directories and subdirectories to search for the file
        for root, dirs, files in os.walk(code_folder):
            if jsp_filename in files:
                file_found = True
                break

        # If the file is not found, add it to the missing files list
        if not file_found:
            missing_files.append(jsp_filename)

    # Save the missing filenames to the output file
    with open(output_file, 'w') as file:
        for filename in missing_files:
            file.write(filename + '\n')

    print(f"Found {len(missing_files)} missing JSP files.")
    print(f"Missing files have been saved to {output_file}.")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Find missing JSP files in the code folder and subfolders")
    parser.add_argument('jsp_list_file', help="Path to the text file containing the list of JSP filenames")
    parser.add_argument('code_folder', help="Path to the code folder containing the JSP files")
    parser.add_argument('output_file', help="Path to the output text file where the results will be saved")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    find_missing_jsp_files(args.jsp_list_file, args.code_folder, args.output_file)
