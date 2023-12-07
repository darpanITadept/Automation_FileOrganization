import listFiles

# File Path
path = '/Users/darpanchoudhary128/Documents/Datasets'

def main():
    print("File Names:")
    file_names = listFiles.list_directory_contents(path)
    
    print("File Extensions:")
    file_extensions = listFiles.list_file_extensions(file_names)
    
    

    
if __name__ == '__main__':
    main()
