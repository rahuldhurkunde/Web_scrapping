import numpy as np
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

class ProductExtractor(object):
    BASE_URL = 'http://books.toscrape.com'

    def make_request(self, url):
        return requests.get(url)

    def extract_urls(self, start_url):
                response = self.make_request(start_url)
                parser = BeautifulSoup(response.text, 'html.parser')
                product_links = parser.select('article.product_pod > h3 > a')
                for link in product_links:
                    relative_url = link.attrs.get('href')
                    absolute_url = urljoin(self.BASE_URL, relative_url.replace('../../..', 'catalogue'))
                    yield absolute_url


extractor = ProductExtractor()
product_urls = extractor.extract_urls('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
print(product_urls)
extracted_data = []      

extractor.export_json(extracted_data, 'data.json')
def export_json(self, data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f)
