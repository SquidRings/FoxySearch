import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent

class MyScraper:
    def __init__(self, start_urls_file, proxies=None):
        self.start_urls = self.load_start_urls(start_urls_file)
        self.proxies = proxies
        self.user_agent = UserAgent()

    def load_start_urls(self, start_urls_file):
        with open(start_urls_file) as f:
            urls = json.load(f)
        return urls

    def scrape(self):
        for url in self.start_urls:
            try:
                headers = {'User-Agent': self.user_agent.random}
                response = requests.get(url, headers=headers, proxies=self.proxies)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    title = soup.find('title').get_text()
                    print("Page title:", title)

                    # Extract links
                    links = [a['href'] for a in soup.find_all('a', href=True)]
                    print("Links:", links)

                    # Save data to a JSON file
                    data = {
                        'url': url,
                        'title': title,
                        'links': links
                    }
                    with open('output.json', 'a') as f:
                        json.dump(data, f, indent=4)
                        f.write('\n')
                else:
                    print(f"Failed to scrape {url}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Failed to scrape {url}. Error: {str(e)}")

if __name__ == "__main__":
    start_urls_file = 'urls.json'
    proxies = {
        'http': 'http://orzzxxio-rotate:98jci0yjnkb0@p.webshare.io:80/',
        'https': 'http://orzzxxio-rotate:98jci0yjnkb0@p.webshare.io:80/'
    }
    scraper = MyScraper(start_urls_file, proxies)
    scraper.scrape()
