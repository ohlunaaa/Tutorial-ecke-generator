from playwright.sync_api import Playwright, sync_playwright, expect
import time
import requests
import random
import string
import colorama
from colorama import Fore, Style
from threading import RLock, Thread
from concurrent.futures import ThreadPoolExecutor
from os import system

genned = 0
failed = 0


class data:
    def name():
        r=requests.get('https://story-shack-cdn-v2.glitch.me/generators/username-generator?')
        return r.json()["data"]["name"]
def passwords():
    chars = "abcdefghijklmnopqrstuvwxytABDOWEITJ"
    number = 6 
    length = 8
    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)
    return passwords
def emails():
    chars_after_at = 7
    letters_list = [string.ascii_lowercase, string.ascii_uppercase]
    letters_list_to_str = "".join(letters_list)
    email_format = "@gmail.com"
    email = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + email_format
    return email

def gen():
    global genned
    global failed
    username = data.name()
    password = passwords()
    email = emails()
    try:
        system(f"title Account Generator V1  Genned: {genned}  Failed: {failed} ")
        proxy = random.choice(open("proxies.txt","r").read().splitlines())
        with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=False,proxy={"server": f'http://{proxy}'})
                context = browser.new_context()
                page = context.new_page()
                page.goto("https://dash.tutorialecke.org/register")
                page.locator("[placeholder=\"Username\"]").fill(username)
                page.locator("[placeholder=\"Email\"]").click()
                page.locator("[placeholder=\"Email\"]").fill(email)
                page.locator("[placeholder=\"Password\"]").click()
                page.locator("[placeholder=\"Password\"]").fill(password)
                page.locator("[placeholder=\"Retype password\"]").click()
                page.locator("[placeholder=\"Retype password\"]").fill(password)
                page.locator("button:has-text(\"Register\")").click()
                time.sleep(3)
                page.locator("a[role=\"button\"]:has-text(\"10.00\")").click()
                page.locator("text=Redeem code").click()
                page.locator("[placeholder=\"SUMMER\"]").click()
                page.locator("[placeholder=\"SUMMER\"]").fill("rexderking")
                time.sleep(2)
                page.locator("button:has-text(\"Redeem\")").click()
                page.reload()
                page.locator("a[role=\"button\"]:has-text(\"110.00\")").click()
                page.locator("text=Redeem code").click()
                page.locator("[placeholder=\"SUMMER\"]").click()
                page.locator("[placeholder=\"SUMMER\"]").fill("aOHeGTZZpO5yuj")
                time.sleep(2)
                page.locator("button:has-text(\"Redeem\")").click()
                time.sleep(5)
                file = open("accounts.txt","a")
                file.write(f"{username}:{email}:{password}\n")
                genned += 1
                print(f"{Fore.GREEN}[Genned] {Fore.RESET}{username}:{email}:{password}")
                page.close()
    except:
        failed += 1
        print(f"{Fore.RED}[Failed]{Fore.RESET}")

if __name__ == "__main__":
    system("cls")
    print(f""" {Fore.BLUE}
     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{Style.RESET_ALL}
    """)
    threadAmount = input(f"{Fore.BLUE}{Style.BRIGHT}[?] Number of threads -> {Style.RESET_ALL}")
    threadAmount = 1 if threadAmount == "" else int(threadAmount)
    system("cls")
    threads = []
    while True:
        with ThreadPoolExecutor(max_workers=threadAmount) as ex : 
            
            for x in range(threadAmount):
                
                ex.submit(gen)