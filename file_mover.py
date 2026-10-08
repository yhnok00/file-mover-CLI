"""
takes files matching a specific pattern from a source directory 
and moves them directly into a destination directory(creates if doesnt already exist).
"""


# module imports 
import argparse
import shutil
from pathlib import Path


# function 
def move_files(source_path, dest_path, pattern="*.py"):

    
    
    source_folder = Path(source_path)
    dest_folder = Path(dest_path)
    
    # check if souce floder exists or not
    if not source_folder.exists() or not source_folder.is_dir():
        print(f"Error: Source path '{source_folder.resolve()}' is not a valid directory.")
        return

    # make a destination folder if doesnt exist
    dest_folder.mkdir(parents=True, exist_ok=True)
    
    
    print(f"\nMoving files from '{source_folder.name}' to '{dest_folder.name}' matching '{pattern}'...")

    
    moved_count = 0

    # searching the targeted files and moving them
    for file_path in source_folder.glob(pattern):
        
        
        if file_path.is_file():
            
            
            #  checking to  prevent the script from accidentally moving itself if it exists in source folder
            try:
                if file_path.resolve() == Path(__file__).resolve():
                    continue 
            except NameError:
                pass
            
           
            destination_file_path = dest_folder / file_path.name
            
            shutil.move(str(file_path), str(destination_file_path))
            
            
            print(f"  [Moved] {file_path.name}")
            
            moved_count += 1


    print(f"\nSuccess! Moved {moved_count} file(s).\n")



# COMMAND-LINE INTERFACE (CLI) setup

if __name__ == "__main__":
    
    #  helpful description
    parser = argparse.ArgumentParser(description="Move specific files from one folder to another via the terminal.")
    
    # defining source folder 
    parser.add_argument("source", help="Path to the source folder containing the files")
    
    # defining destination folder 
    parser.add_argument("destination", help="Path to the destination folder where files will go")
    
    #defining pattern of files to be moved
    parser.add_argument("pattern", nargs="?", default="*.py", help="File pattern, e.g. '*.py', '*.txt', or '*' (default: '*.py')")

    # parse all the arguments entered by the user in the terminal
    args = parser.parse_args()
    
    # calling the function
    move_files(args.source, args.destination, args.pattern)
