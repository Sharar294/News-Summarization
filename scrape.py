# Handles web scraping to extract content from URLs

import requests
from bs4 import BeautifulSoup

def fetchArticle(url):
    try:
        # Add headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        # Fetch the webpage with a timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()


        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # # Find the main content section
        # content = soup.find('div', class_='story')
        # if not content:
        #     return "Content not found on the page."

        # # Extract title
        # title_tag = soup.find('h1', class_='detailHeadline')
        # title = title_tag.text.strip() if title_tag else "Title not found."



         # Find the title
        title_tag = soup.find('h1')
        title = title_tag.text.strip() if title_tag else "Title not found."

        # Find the main content section (adjust selector for flexibility)
        content = soup.find('div', class_='story') or soup.find('article') or soup.find('div', class_='content')
        if not content:
            return "Content not found on the page."



        # Extract body paragraphs

        paragraph_text = []
        if content:
            for p in content.find_all('p'):
                text = p.text.strip()
                paragraph_text.append(text)

        # Combine the extracted information
        combined = (
            f"Title: {title}\n"
            f"Content: {' '.join(paragraph_text)}"
        )
        return combined

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the URL: {e}"

# Example usage
# url = 'https://www.cbc.ca/news/canada/saskatchewan/victor-santos-cardoza-breaks-record-youngest-councillor-moosomin-sask-1.7391935'
# url = 'https://www.bbc.com/news/articles/c2kx7qj8z4wo'

# content = fetchArticle(url)
# print(content)
