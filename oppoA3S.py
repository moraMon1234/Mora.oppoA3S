import requests
import bs4
url = "https://www.olx.com.eg/en/mobile-phones-tablets-accessories-numbers/mobile-phones/q-oppo-a3s/"
page = requests.get(url)
# print(page)
soup = bs4.BeautifulSoup(page.content, 'html.parser')
oppoA3S = soup.find_all("ul", {"class": "ba608fb8 de8df3a3"})
for x in oppoA3S:
    print(x.get_text())
