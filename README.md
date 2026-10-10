# HMWLTPhilosophy
**H**ow **M**any **W**iki **L**inks **T**o **Philosophy**

How many Wikipedia Links does it take to get to the Philosophy Article?

Input an article of your choice, and find out!

_See more on why this occurs [here](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy)_

---
# Demo video
![Demo video](demo-video.mp4)

---
# Usage
There are 2 ways to use this program:

## The normal way
Just launch the .exe, answer the prompts and watch the magic happen!

## The hacker way
This app takes command-line arguments!

- `-s` or `--start` to provide the wiki link
- `-e` or `--end` to provide a custom end link! (Must not be the same as start)

# Downloads
Got your interest? Head to the releases section and grab the [latest one](https://github.com/Aquaticsanti/HMWLTPhilosophy/releases/latest)!

> [!IMPORTANT]
> This program is only available for Windows 10/11, as I don't have the resources to build for other platforms.

# Building
## Requirements for building
- [rich](https://rich.readthedocs.io/en/latest/index.html)
- [bs4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
To build the .exe, use PyInstaller!
```
git clone https://github.com/Aquaticsanti/HMWLTPhilosophy.git
```
```
cd HMWLTPhilosophy
```
```
pyinstaller HMWLTPhilosophy.spec
```



