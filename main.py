import file_handler

# File Path
default_path = '/Users/darpanchoudhary128/Documents/Test'

def main(path):
    
    # Asking user if they want to enter path of their choice or use the default path
    while True:
        yesNo = input("Do you want to choose path of your choice? (Y|N): ")
        
        if yesNo.upper() == 'Y':
            userPath = input("Please enter your path: ")
            path = userPath
            break
        elif yesNo.upper() == 'N':
            print(f"Default Path Used! {path}")
            break
        else:
            print("Try Again! Enter a Valid Input")
        
            
    try:
        # Extracting file names in the directory
        print("File Names:")
        file_names = file_handler.list_directory_contents(path)
        
        if not file_names:
            print("No files found in the specified directory.")
            return  # Stop further execution if no files are found
        
        # Extracting extensions of files in the directory
        print("File Extensions:")
        file_extensions = file_handler.list_file_extensions(file_names)
        
        # Organizing files into respective Directories based on their extensions
        file_handler.organize_files_by_extension(path, file_extensions, file_names)
        print("Files Organized!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
        

if __name__ == '__main__':
    main(default_path)
