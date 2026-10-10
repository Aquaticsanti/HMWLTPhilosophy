import rich
from rich.console import Console
from bs4 import BeautifulSoup
import requests

c = Console()

c.rule("[bold]H[/bold]ow [bold]M[/bold]any [bold]W[/bold]iki [bold]L[/bold]inks [bold]T[/bold]o [bold]P[/bold]hilosophy?")
c.print("[bold]Welcome to HMWLTPhilosophy![/bold]")
c.print("[bold]Enter an English Wikipedia Link below, and know how many pages separate it from [link=https://en.wikipedia.org/wiki/Philosophy]Philosophy[/link]![/bold]")
c.print("[italic]For more information on this phenomenon, see [link=https://en.wikipedia.org/wiki/Wikipedia_philosophy_phenomenon]Wikipedia philosophy phenomenon[/link][/italic]")

start = c.input("What will be the starting page? (Full link) ")
while True:
    if "en.wikipedia.org/wiki/" not in start:
        start = c.input("That's doesn't seem to be in english or a full link: ")
    else:
        break

html = requests.get(start, headers={"User-Agent": "HMWLTPhilosophy/1.0 (aquaticsanti@gmail.com)"})
soup = BeautifulSoup(html.text, 'html.parser')

soup = soup.select_one('[data-mw-section-id="0"]')
soup = soup.select_one("p:not(.mw-empty-elt)")
for tag in soup.find_all(["b", "i", "span", "p", "abbr"]):
    tag.unwrap()
soup = str(soup)
tempIndex = ""
for index, char in enumerate(soup):
    if char != "(" and char != ")":
        continue
    elif char == "(":
        if tempIndex == "":
            tempIndex = index
    elif char == ")":
        soup = soup.replace(soup[tempIndex:index+1], "")
        break
soup = BeautifulSoup(soup, 'html.parser')
soup = soup.select_one("a")
link = soup["href"]
print(link)