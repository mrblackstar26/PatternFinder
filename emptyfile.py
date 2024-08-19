import os
import argparse

def check_empty_jsp_files(jsp_list_file, main_code_dir, empty_files_output):
    # Read the list of JSP file names from the .txt file
    with open(jsp_list_file, 'r') as file:
        jsp_files_to_check = [line.strip() for line in file]

    # List to store the names of empty JSP files
    empty_jsp_files = []

    # Iterate over the list of JSP files and check if they are empty
    for jsp_file in jsp_files_to_check:
        jsp_file_path = os.path.join(main_code_dir, jsp_file)
        
        # Check if the file exists and is empty
        if os.path.exists(jsp_file_path) and os.path.getsize(jsp_file_path) == 0:
            empty_jsp_files.append(jsp_file)

    # Write the names of the empty JSP files to the output .txt file
    with open(empty_files_output, 'w') as output_file:
        for empty_jsp_file in empty_jsp_files:
            output_file.write(f"{empty_jsp_file}\n")

    print(f"Empty JSP files have been written to {empty_files_output}.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Check for empty JSP files.")
    parser.add_argument("jsp_list_file", help="Path to the .txt file containing the JSP filenames.")
    parser.add_argument("main_code_dir", help="Path to the directory containing the main code JSP files.")
    parser.add_argument("empty_files_output", help="Path to the output .txt file for empty JSP files.")
    
    args = parser.parse_args()

    # Run the check with the provided arguments
    check_empty_jsp_files(args.jsp_list_file, args.main_code_dir, args.empty_files_output)
