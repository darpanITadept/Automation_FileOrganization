import os
import shutil


# List File Names
def list_directory_contents(path):
    """
    Lists the names of files in the specified directory.
    """
    file_names = os.listdir(path)
    print(file_names)
    return file_names
    
# List File Extensions
def list_file_extensions(file_names):
    """
    Extracts and lists the file extensions from a list of file names.
    """
    file_extensions = set()
    
    for file_name in file_names:
        file_extensions.add(os.path.splitext(file_name)[1])
        
    unique_file_extensions = list(file_extensions)
    
    print(unique_file_extensions)
    
    return unique_file_extensions

def organize_files_by_extension(path, file_extensions, file_names):
    for extension in file_extensions:
        # Creating a path for the new directory
        extension_dir = os.path.join(path, extension)
        
        os.makedirs(extension_dir, exist_ok=True)
        
        # Move files with the corresponding extension to the directory
        for file_name in file_names:
            if file_name.lower() == ".ds_store":
                continue  # Skip the .DS_Store file
            
            _, file_extension = os.path.splitext(file_name)
            
            if file_extension.lower() == extension.lower():
                source_path = os.path.join(path, file_name)
                destination_path = os.path.join(extension_dir, file_name)  
                
                # Move the file with error handling
                try:
                    shutil.move(source_path, destination_path)
                except shutil.Error as e:
                    print(f"Error moving file '{file_name}': {e}")
