import os
import argparse

def check_jsp_files(jsp_list_file, code_folder, output_file):
    # Read the JSP filenames from the list file
    with open(jsp_list_file, 'r') as file:
        jsp_filenames = [line.strip() for line in file.readlines()]

    # Initialize a list to store JSP filenames that contain 'request.getParameter'
    found_files = []

    # Loop through the JSP filenames and check for 'request.getParameter'
    for jsp_filename in jsp_filenames:
        jsp_path = os.path.join(code_folder, jsp_filename)

        # Check if the file exists in the specified folder
        if os.path.isfile(jsp_path):
            with open(jsp_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                if 'request.getParameter' in content:
                    found_files.append(jsp_filename)

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
