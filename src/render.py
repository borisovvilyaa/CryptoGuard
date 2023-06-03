import pathlib

def print_directory_files(directory) -> None:
        currentDirectory = pathlib.Path(directory)
        print("\n!!!Folder /%s\n" % currentDirectory)
        for currentFile in currentDirectory.iterdir():  
            print(currentFile)