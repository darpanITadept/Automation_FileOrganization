import os


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
    file_extensions = []
    
    for file_name in file_names:
        file_extensions.append(os.path.splitext(file_name)[1])
        
    print(file_extensions)
    
    return file_extensions

    