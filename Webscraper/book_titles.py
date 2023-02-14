import requests
from bs4 import BeautifulSoup

# webscraper that scrapes all of the book titles from http://books.toscrape.com/
def book_titles():
    url = "http://books.toscrape.com/"
    # get the html from the website
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    books = soup.find_all("h3")
    for book in books:
        print(book.text)


book_titles()