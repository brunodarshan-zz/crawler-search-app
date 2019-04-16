from bs4 import BeautifulSoup
import requests
import os

TAGS = "a h1 h2 h3 h4 h5 h6 p"

class SerchService:
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
        for tag in self.TAGS.split():
           result_for_tag = html.find_all(tag)
           for result in result_for_tag:
               if self.query in result.get_text():
                   self.store.append({
                       "content": result.get_text,
                       "href": result.get('href')
                   })

    def status(self):
        return str(len(self.store)) +  " resultados para " + self.query
    
    def create_view(self):
        fl = open('index.html', '+w')
        fl.write('<body style="width: 100%; height: 100%";>\n')
        fl.write('<pre style="background:#ddd; margin: 5%; padding: 2em;">\n')
        for data in self.store:
            fl.write(str(data['content']) + "\n\r")
        fl.write('</pre>\n')
        fl.write('</body>')

    
    
