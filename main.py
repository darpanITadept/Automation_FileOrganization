import file_handler

# File Path
path = '/Users/darpanchoudhary128/Documents/Test'

def main():
    try:
        print("File Names:")
        file_names = file_handler.list_directory_contents(path)
        
        if not file_names:
            print("No files found in the specified directory.")
            return  # Stop further execution if no files are found
        
        print("File Extensions:")
        file_extensions = file_handler.list_file_extensions(file_names)
        
        file_handler.organize_files_by_extension(path, file_extensions, file_names)
        print("Files Organized!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
