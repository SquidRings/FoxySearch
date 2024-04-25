import json

class Indexer:
    def __init__(self, output_file):
        self.output_file = output_file
        self.index = {}

    def load_data(self):
        with open(self.output_file, 'r') as f:
            data = json.load(f)
            for item in data:
                url = item['url']
                title = item['title']
                content = ' '.join(item['links'])
                self.index[url] = {'title': title, 'content': content}

    def search(self, query):
        results = []
        for url, info in self.index.items():
            if query.lower() in info['content'].lower():
                results.append({'url': url, 'title': info['title']})
        return results

if __name__ == "__main__":
    output_file = 'output.json'
    indexer = Indexer(output_file)
    indexer.load_data()
    query = input("Enter your search query: ")
    results = indexer.search(query)
    if results:
        print("Search results:")
        for result in results:
            print(f"Title: {result['title']}, URL: {result['url']}")
    else:
        print("No results found for the query.")
