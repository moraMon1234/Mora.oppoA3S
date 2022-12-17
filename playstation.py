import requests
import bs4
url = "https://www.noon.com/egypt-ar/playstation-consoles/"
page = requests.get(url)
print(page.status_code)
print('sd')
'''
soup = bs4.BeautifulSoup(page.content, 'html.parser')
playstation = soup.find_all("span", {"class": "sc-5e739f1b-0 gEERDr wrapper productContainer"})
for x in playstation:
    print(x.get_text())
'''