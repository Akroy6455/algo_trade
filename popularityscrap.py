import requests
from bs4 import BeautifulSoup
import time

def google_search(query, num_pages):
    total_results = 0
    for i in range(num_pages):
        url = f"https://www.google.com/search?q={query}&start={i*10}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = len(soup.find_all('div', class_='g'))
        total_results += results
        if results == 0:
            break
        time.sleep(1)  # Delay to avoid being blocked
    return total_results

def twitter_search(query, num_pages):
    total_tweets = 0
    for i in range(num_pages):
        url = f"https://twitter.com/search?q={query}&src=typed_query&f=live&p={i+1}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        tweets = len(soup.find_all('div', {'data-testid': 'tweet'}))
        total_tweets += tweets
        if tweets == 0:
            break
        time.sleep(1)  # Delay to avoid being blocked
    return total_tweets

def news_search(query, num_pages):
    total_articles = 0
    for i in range(num_pages):
        url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en&p={i+1}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = len(soup.find_all('article'))
        total_articles += articles
        if articles == 0:
            break
        time.sleep(1)  # Delay to avoid being blocked
    return total_articles

def main():
    stock = input("Enter the stock symbol you want to search for: ")
    num_pages = int(input("Enter the number of pages to search on each platform: "))

    print(f"Searching {num_pages} pages on each platform... (This may take several minutes)")

    # Google search
    google_results = google_search(stock, num_pages)
    print(f"Google search results: {google_results}")

    # Twitter search
    twitter_results = twitter_search(stock, num_pages)
    print(f"Twitter mentions: {twitter_results}")

    # News search
    news_results = news_search(stock, num_pages)
    print(f"News articles: {news_results}")

    # Calculate popularity score (simple sum of all results)
    popularity_score = google_results + twitter_results + news_results
    print(f"Overall popularity score for {stock}: {popularity_score}")

if __name__ == "__main__":
    main()
