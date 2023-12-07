import file_handler

# Default file path
default_path = '/Users/darpanchoudhary128/Documents/Test'

def main(path):
    # Ask the user if they want to enter a custom path or use the default path
    while True:
        user_choice = input("Do you want to choose a custom path? (Y|N): ")
        
        if user_choice.upper() == 'Y':
            user_path = input("Please enter your path: ")
            path = user_path
            break
        elif user_choice.upper() == 'N':
            print(f"Default Path Used: {path}")
            break
        else:
            print("Try Again! Enter a Valid Input")
            
    try:
        # Extract file names in the directory
        print("File Names:")
        file_names = file_handler.list_directory_contents(path)
        
        if not file_names:
            print("No files found in the specified directory.")
            return  # Stop further execution if no files are found
        
        # Extract file extensions in the directory
        print("File Extensions:")
        file_extensions = file_handler.list_file_extensions(file_names)
        
        # Organize files into respective directories based on their extensions
        file_handler.organize_files_by_extension(path, file_extensions, file_names)
        print("Files Organized!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Start the main function with the default path
    main(default_path)
