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
        if start == "https://en.wikipedia.org/wiki/Philosophy" or start == "http://en.wikipedia.org/wiki/Philosophy":
            start = c.input("You think you're funny, huh? Provide an article that [italic]isn't[/italic] the one on Philosophy: ")
        else:
            break

html = requests.get(start, headers={"User-Agent": "HMWLTPhilosophy/1.0 (aquaticsanti@gmail.com)"})
visitedPages = [start]
c.print(f"[bold][link={start}]{start.replace("https://en.wikipedia.org/wiki/", "").replace("http://en.wikipedia.org/wiki/", "").replace("_", " ")}[/link][/bold]", end=" → ")
while True:
    soup = BeautifulSoup(html.text, 'html.parser')
    soup = soup.select_one('[data-mw-section-id="0"]')
    soup = soup.select_one("p:not(.mw-empty-elt):not(.sidebar p):not(table p)") # ChatGPT helped with this, as the article on religion was causing wayy too much trouble
    for tag in soup.find_all(["b", "i", "span", "p", "abbr"]):
        tag.unwrap()
    soup = str(soup)
    if "(" in soup:
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
    soupTemp = soup.select_one("a")
    link = soupTemp["href"]
    if "#cite_note" in link:
        link = soup.select_one("a:nth-of-type(2)")["href"]
    if link in visitedPages:
        c.print(f"[bold][link={link}]{link.replace("https://en.wikipedia.org/wiki/", "").replace("http://en.wikipedia.org/wiki/", "").replace("_", " ")}[/link][/bold]", end=" 🔁 \n")
        c.print(f"Whoops, this loops at [bold]{len(visitedPages)+1}[/bold] pages...")
        break
    visitedPages.append(link)
    if link == "https://en.wikipedia.org/wiki/Philosophy" or link == "http://en.wikipedia.org/wiki/Philosophy":
        c.print(f"[bold][link={link}]{link.replace("https://en.wikipedia.org/wiki/", "").replace("http://en.wikipedia.org/wiki/", "").replace("_", " ")}[/link][/bold]", end=" 🏁 \n")
        c.print(f"[bold]{len(visitedPages)}[/bold] pages to [link=https://en.wikipedia.org/wiki/Philosophy]Philosophy[/link]!")
        break
    c.print(f"[bold][link={link}]{link.replace("https://en.wikipedia.org/wiki/", "").replace("http://en.wikipedia.org/wiki/", "").replace("_", " ")}[/link][/bold]", end=" → ")
    html = requests.get(link, headers={"User-Agent": "HMWLTPhilosophy/1.0 (aquaticsanti@gmail.com)"})

