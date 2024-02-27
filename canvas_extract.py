import os
from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        return soup.get_text()

def search_and_convert(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                text = extract_text_from_html(file_path)
                text_file_path = os.path.splitext(file_path)[0] + '.txt'
                with open(text_file_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(text)

# Replace 'your_directory_path' with the path to the directory containing HTML files
search_and_convert('/Users/mundorfd/Dropbox/Projects/qmreviewgeog/qm-review-geog-380-export')
