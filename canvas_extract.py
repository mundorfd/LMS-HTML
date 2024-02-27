import os
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def convert_html_to_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        # Remove all image tags
        for img_tag in soup.find_all('img'):
            img_tag.decompose()
        html_content = soup.prettify()
        return md(html_content)

def search_and_convert(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                markdown = convert_html_to_markdown(file_path)
                markdown_file_name = os.path.splitext(file)[0] + '.md'
                markdown_file_path = os.path.join(destination_directory, markdown_file_name)
                with open(markdown_file_path, 'w', encoding='utf-8') as markdown_file:
                    markdown_file.write(markdown)

# Prompt for source and destination directories
source_directory = input("Enter the source directory path containing HTML files: ")
destination_directory = input("Enter the destination directory path for Markdown files: ")
search_and_convert(source_directory, destination_directory)
