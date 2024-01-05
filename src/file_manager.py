import os
import csv
from datetime import datetime

def find_files(base_path, file_name):
    """
    Recursively search for files with a specific name in a directory tree.
    """
    files_found = []
    for root, dirs, files in os.walk(base_path):
        if file_name in files:
            files_found.append(os.path.join(root, file_name))
    return files_found

def extract_date_from_path(path):
    """
    Extracts the date from the folder structure.
    Assumes folder structure includes: .../yyyy/mm/dd/...
    """
    parts = path.strip(os.sep).split(os.sep)
    try:
        # Find the year part (four digits) and assume the next two parts are month and day
        for i, part in enumerate(parts):
            if part.isdigit() and len(part) == 4:
                year, month, day = parts[i], parts[i + 1], parts[i + 2]
                print('year, month, day ->', year, month, day)
                return datetime(int(year), int(month), int(day)).strftime('%Y-%m-%d')
        # If year is not found or date is invalid, return None
    except (ValueError, IndexError):
        print('error: extract_date_from_path error for path:', path)
        return None
    
def read_file(file_path):
    """
    Reads the content of a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def process_files(base_path):
    """
    Process the files and save the data as a CSV file.
    """
    original_titles = find_files(base_path, "titles-original")
    afterGPT_titles = find_files(base_path, "titles-afterGPT")

    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Original Title', 'Uploaded Title'])

        for original, afterGPT in zip(original_titles, afterGPT_titles):
            date = extract_date_from_path(original)
            if date:
                original_title = read_file(original)
                afterGPT_title = read_file(afterGPT)
                writer.writerow([date, original_title, afterGPT_title])

if __name__ == "__main__":
    base_path = input("Enter the base directory path: ")
    process_files(base_path)
