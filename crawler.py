import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent

class MyScraper:
    def __init__(self, start_urls_file, output_file, proxies=None):
        self.start_urls = self.load_start_urls(start_urls_file)
        self.output_file = output_file
        self.proxies = proxies
        self.user_agent = UserAgent()

    def load_start_urls(self, start_urls_file):
        with open(start_urls_file) as f:
            urls = json.load(f)
        return urls

    def scrape(self):
        with open(self.output_file, 'a') as f:
            f.write("[")  # Add opening bracket
            for i, url in enumerate(self.start_urls):
                try:
                    headers = {'User-Agent': self.user_agent.random}
                    response = requests.get(url, headers=headers, proxies=self.proxies)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        title = soup.find('title').get_text()
                        print("Page title:", title)

                        # Extract main text content
                        text_content = soup.get_text()

                        # Extract metadata
                        meta_tags = soup.find_all('meta')
                        metadata = {tag.get('name', tag.get('property')): tag.get('content') for tag in meta_tags}

                        # Extract links
                        links = [a['href'] for a in soup.find_all('a', href=True)]

                        # Save data to the output file
                        data = {
                            'url': url,
                            'title': title,
                            'text_content': text_content,
                            'metadata': metadata,
                            'links': links
                        }
                        json.dump(data, f)
                        if i < len(self.start_urls) - 1:  # Add comma if not the last item
                            f.write(",")
                        f.write('\n')
                    else:
                        print(f"Failed to scrape {url}. Status code: {response.status_code}")
                except Exception as e:
                    print(f"Failed to scrape {url}. Error: {str(e)}")
            f.write("]")  # Add closing bracket

if __name__ == "__main__":
    start_urls_file = 'urls.json'
    output_file = 'output.json'
    proxies = {
        'http': 'http://orzzxxio-rotate:98jci0yjnkb0@p.webshare.io:80/',
        'https': 'http://orzzxxio-rotate:98jci0yjnkb0@p.webshare.io:80/'
    }
    scraper = MyScraper(start_urls_file, output_file, proxies)
    scraper.scrape()
    