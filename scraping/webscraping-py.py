from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.seloger.com/list.htm?projects=2,5&types=1&natures=1,2,4&places=[{%22divisions%22:[2238]}]&price=NaN/500000&mandatorycommodities=0&view=1&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results').text
print(html_text)
