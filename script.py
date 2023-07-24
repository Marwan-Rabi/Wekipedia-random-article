from selenium import webdriver
import keyboard
class Soup_on:
    def __init__(self):
        pass
        # self.Url = Url

    def collectdata(self):
    
        print("""
Hello in wekipedia articles app!
Here you can read many random articles in wekipedia by just 1 click
HOPE YOU A ENJOYABLE JOURNEY!!""")
    def randomArticle(self):
        self.restart = 'a'
        while self.restart == 'a':
            self.artLang = input("what's your language(ar,en)\n")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            self.chrome= webdriver.Chrome(options=options)
            self.chrome.maximize_window()
            self.Url = "https://www.wikipedia.org/"
            self.chrome.get(self.Url)
            if self.artLang == "ar":
                self.chrome.get("https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A9_%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D8%A9")
                keyboard.press_and_release('alt+x')
            elif self.artLang == "en":
                self.chrome.get("https://en.wikipedia.org/wiki/Main_Page")
                keyboard.press_and_release("alt+x")
            else:
                print("this language is not supported")
            self.restart = input("if you want to read another article click a ")
            if self.restart != 'a':
                print("Thank you!, see you again")
                input("")
        
soup = Soup_on()
soup.collectdata()
soup.randomArticle()