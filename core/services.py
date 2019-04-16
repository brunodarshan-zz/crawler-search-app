from bs4 import BeautifulSoup
import requests
import os

TAGS = "a h1 h2 h3 h4 h5 h6 p"

class SearchService:
    def __init__(self, source, deep = 0):
        self.store = []
        self.deep = deep
        self.source = source

    def search(self, query):
        self.query = query
        response = requests.get(self.source)
        html = BeautifulSoup(response.text, 'lxml')
        self.search_in_deep(html)
    
    def search_in_deep(self, html):
        while len(self.store) < 1 and self.deep >= 0:
            self.search_on_tags(html)
            self.deep -= 1
    
    def search_on_tags(self, html):
        for tag in TAGS.split():
           result_for_tag = html.find_all(tag)
           for result in result_for_tag:
               if self.query in result.get_text():
                   self.store.append({
                       "content": result.get_text,
                       "href": result.get('href')
                   })

    def status(self):
        return str(len(self.store)) +  " resultados para " + self.query
    

    
    
