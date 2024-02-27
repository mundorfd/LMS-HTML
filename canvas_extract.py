import os
from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        return soup.get_text()

def search_and_convert(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                text = extract_text_from_html(file_path)
                text_file_name = os.path.splitext(file)[0] + '.txt'
                text_file_path = os.path.join(destination_directory, text_file_name)
                with open(text_file_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(text)

# Prompt for source and destination directories
source_directory = input("Enter the source directory path containing HTML files: ")
destination_directory = input("Enter the destination directory path for text files: ")

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

search_and_convert(source_directory, destination_directory)
