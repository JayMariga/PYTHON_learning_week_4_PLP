def read_modify_write(file_name, output_file_name):
    try:
        with open(file_name, 'r') as file:  # Try to read the file
            content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        return

    # Modify the content
    modified_content = [line + " - Modified" for line in content]

    try:
        with open(output_file_name, 'w') as output_file:  # Write to a new file
            output_file.writelines(modified_content)
    except Exception as e:
        print(f"Error: An error occurred while writing to '{output_file_name}': {str(e)}")

    print(f"File '{output_file_name}' has been written successfully.")


def main():
    filename = input("Enter the name of the file you want to modify: ")
    modified_output_filename = input("Enter the name for the modified output file: ")

    read_modify_write(filename, modified_output_filename)


if __name__ == "__main__":
    main()