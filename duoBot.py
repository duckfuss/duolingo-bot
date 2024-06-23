from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time

class duoBot():
    def __init__(self) -> None:
        self.options = Options()
        self.options.set_preference("browser.privatebrowsing.autostart", True)
        self.browser = webdriver.Firefox(options=self.options)
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
    def repContinuers(self, n, t=1):
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
        self.browser.get("https://www.duolingo.com/practice-hub/stories") # the sole point of this url is to login reliably
        self.xpathClick('//*[@id="sign-in-btn"]')
        usrnme = self.xpathClick('//*[@id="web-ui1"]', click=False)
        pwd = self.xpathClick('//*[@id="web-ui2"]', click=False)
        usrnme.send_keys("dtfussey@icloud.com")
        pwd.send_keys("duolingoG0ldf!sh")
        self.xpathClick("/html/body/div[2]/div[3]/div/div/form/div[1]/button")

    def changeToFrench(self):
        time.sleep(5)
        print("slept")
        self.browser.get("https://www.duolingo.com/courses/fr")
        time.sleep(1)
        self.xpathClick("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/a[1]")
        time.sleep(1)
        self.browser.get("https://www.duolingo.com/practice-hub/stories")
        print("french?")

    def changeToChinese(self):
        time.sleep(5)
        self.browser.get("https://www.duolingo.com/courses/en")
        self.xpathClick("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/a[8]")

    def startCourse(self):
        self.xpathClick("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[1]/button")
        self.xpathClick("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/a")
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