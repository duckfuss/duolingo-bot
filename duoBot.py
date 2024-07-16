from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, random

class duoBot():
    def __init__(self) -> None:
        service = Service(executable_path="/Users/danielfussey/Documents/firefoxprofile/geckodriver")
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=2560")
        options.add_argument("--height=1440")
        self.browser = webdriver.Firefox(service=service, options=options)
        self.cE = {
            "CONTINUER": "/html/body/div[1]/div[1]/div/div/div[3]/div/div/div/button",
            "q1:1": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[5]/div/ul/li[1]/button",
            "q1:2": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[5]/div/ul/li[2]/button",
            "q1:3": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[5]/div/ul/li[3]/button",
            "q2:1": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[10]/div/ul/li[1]/button",
            "q2:2": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[10]/div/ul/li[2]/button",
            "runs": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[14]/div/div[2]/div/span[3]/span/button",
            "hand": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[22]/div/div[2]/div/span[11]/span/button",
            "q3:1": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[25]/div/ul/li[1]/button",
            "q3:2": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[25]/div/ul/li[2]/button",
            "q3:3": "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[25]/div/ul/li[3]/button"
        } # Common Elements dict
        self.matchDictL = [
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[1]/li[1]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[1]/li[2]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[1]/li[3]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[1]/li[4]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[1]/li[5]/span/button",
        ]
        self.matchDictR = [
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[2]/li[1]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[2]/li[2]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[2]/li[3]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[2]/li[4]/span/button",
            "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[26]/div/div[2]/div/ul[2]/li[5]/span/button",
        ]
    def xpathClick(self, path, click=True):
        btn = None
        c = 0
        while not btn:
            c+=1
            try:
                btn = self.browser.find_element(By.XPATH, path)
            except NoSuchElementException:
                time.sleep(0.1)
                if c > 100:
                    return btn
        if click:
            self.browser.execute_script("arguments[0].click();", btn)
        return btn
    def repContinuers(self, n, t=4):
        for i in range(n):
            time.sleep(t)
            self.xpathClick(self.cE["CONTINUER"])
            print("clicked", i)
    def match(self):
        for i in self.matchDictL:
            for j in self.matchDictR:
                self.xpathClick(i)
                self.xpathClick(j)

    def login(self):
        username = input('what is your username? ')
        password = input('what is your password? ')
        self.browser.get("https://www.duolingo.com/course/en/fr/Learn-English")
        time.sleep(5)
        self.xpathClick("/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/button")
        usrnme = self.xpathClick('//*[@id="web-ui1"]', click=False)
        pwd = self.xpathClick('//*[@id="web-ui2"]', click=False)
        usrnme.send_keys(username)
        time.sleep(10)
        pwd.send_keys(password)
        time.sleep(5)
        for i in range(1):
            time.sleep(random.randrange(0,200)/100)
            self.xpathClick("/html/body/div[2]/div[3]/div/div/form/div[1]/button") 

    def changeToFrench(self):
        time.sleep(5)
        print("slept")
        self.browser.get("https://www.duolingo.com/courses/fr")
        time.sleep(1)
        self.xpathClick("/html/body/div[1]/div[2]/div/div[3]/div/div[2]/a[1]")
        time.sleep(5) # this needs to be long otherwise duo will load wrong lang without a stories section
        self.browser.get("https://www.duolingo.com/practice-hub/stories")
        print("french?")

    def changeToChinese(self):
        time.sleep(5)
        self.browser.get("https://www.duolingo.com/courses/en")
        self.xpathClick("/html/body/div[1]/div[2]/div/div[3]/div/div[2]/a[8]")

    def startCourse(self):
        self.browser.get("https://www.duolingo.com/practice-hub/stories")
        time.sleep(10)
        self.xpathClick("/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div")
        print("click Le passeport")
        time.sleep(1)
        self.xpathClick("/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/a")
        self.xpathClick("/html/body/div[1]/div[1]/div/div/div/div[3]/button")

    def quiz(self):
        self.repContinuers(3)
        for i in ["q1:1", "q1:2", "q1:3"]:
            self.xpathClick(self.cE[i])
        self.repContinuers(5)
        for i in ["q2:1", "q2:2"]:
            self.xpathClick(self.cE[i])
        self.repContinuers(5)
        self.xpathClick(self.cE["runs"])
        print("clicked runs")
        self.repContinuers(11)
        self.xpathClick(self.cE["hand"])
        self.repContinuers(4)
        for i in ["q3:1", "q3:2", "q3:3"]:
            self.xpathClick(self.cE[i])
        self.repContinuers(1)
        self.match()
        self.repContinuers(2)

duck = duoBot()
duck.login()
duck.changeToFrench()
duck.startCourse()
duck.quiz()
duck.changeToChinese()