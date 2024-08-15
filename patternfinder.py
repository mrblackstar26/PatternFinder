import os
import argparse

def check_jsp_files(jsp_list_file, code_folder, output_file):
    # Read the JSP filenames from the list file
    with open(jsp_list_file, 'r') as file:
        jsp_filenames = [line.strip() for line in file.readlines()]

    # Initialize a list to store JSP filenames that contain 'request.getParameter'
    found_files = []

    # Loop through each JSP file in the code folder
    for root, dirs, files in os.walk(code_folder):
        for file in files:
            if file in jsp_filenames and file.endswith('.jsp'):
                jsp_path = os.path.join(root, file)

                # Check if the file exists and read its content
                with open(jsp_path, 'r', encoding='utf-8', errors='ignore') as jsp_file:
                    content = jsp_file.read()
                    if 'request.getParameter' in content:
                        found_files.append(file)

    # Save the results to the output file
    with open(output_file, 'w') as file:
        for filename in found_files:
            file.write(filename + '\n')

    print(f"Found {len(found_files)} JSP files containing 'request.getParameter'.")
    print(f"Results have been saved to {output_file}.")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Check JSP files for 'request.getParameter'")
    parser.add_argument('jsp_list_file', help="Path to the text file containing the list of JSP filenames")
    parser.add_argument('code_folder', help="Path to the code folder containing the JSP files")
    parser.add_argument('output_file', help="Path to the output text file where the results will be saved")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    check_jsp_files(args.jsp_list_file, args.code_folder, args.output_file)
