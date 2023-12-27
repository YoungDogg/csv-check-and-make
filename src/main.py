import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.gui import select_file
from src.file_manager import process_files
from src.utilities import some_utility_function  # Replace with actual utility functions

def main():
    # Launch the GUI and get the selected file path
    file_path = select_file()

    if file_path:
        # Process the selected file
        process_files(file_path)
        print(f"Processed file: {file_path}")
    else:
        print("No file was selected.")

if __name__ == "__main__":
    main()
