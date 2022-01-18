
import webbrowser as web
import requests


def playonprime(topic: str, open_video: bool = True):

    url = f"https://music.amazon.in/search/{topic}"
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/search":
        raise Exception("No Video Found for this Topic!")

    if True:
        web.open(f"https://music.amazon.in/search/{topic}")
    return f"https://music.amazon.in/search/{topic}"


def playonyt(topic: str,  open_video: bool = True):
    url = f"https://www.youtube.com/results?q={topic}"
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/results":
        raise Exception("No Video Found for this Topic!")
    if open_video:
        web.open(f"https://www.youtube.com{lst[count - 5]}")
    return f"https://www.youtube.com{lst[count - 5]}"
