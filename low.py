import random
import os
os.system('pip install selenium chromedriver-autoinstaller requests fake-useragent ')
os.system('apt install chromium-chromedriver -y')
os.system('wget https://dl.google.com/linux/linux_signing_key.pub')
os.system('sudo apt-key add linux_signing_key.pub')
os.system('echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list')
os.system('sudo apt-get -y update')
os.system('sudo apt-get install -y google-chrome-stable')
os.system('apt-get update')

from fake_useragent import UserAgent
import concurrent.futures
import time
import random
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import threading
import os
import json
import chromedriver_autoinstaller
from datetime import datetime



https = ["https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
         "https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/https",
         "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
         "https://raw.githubusercontent.com/Master-Mind-007/Auto-Parse-Proxy/main/https.txt",
         "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt"]
http = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/http",
       "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
       "https://raw.githubusercontent.com/snrtro/proxy/main/proxylist/http.txt",
       ]
socks5 = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
          "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
          "https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/socks5",
          "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",
          "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
          "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
          "https://raw.githubusercontent.com/Master-Mind-007/Auto-Parse-Proxy/main/socks5.txt",
          "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
          "https://raw.githubusercontent.com/snrtro/proxy/main/proxylist/socks5.txt",
          "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
          "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
          "https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks5",
          "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
          "https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/socks5.txt",
         
         ]
socks4 = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
          "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
          "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
          "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt", "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",
          "https://raw.githubusercontent.com/Master-Mind-007/Auto-Parse-Proxy/main/socks4.txt",
          "https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/socks4",
          "https://raw.githubusercontent.com/snrtro/proxy/main/proxylist/socks4.txt",
          "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
          "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
          "https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks4",
          "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
          "https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/socks4.txt",
         ]


class Proxy:
    def get_load(self):
        print("Getting Proxies")
        self.proxylists = []
        self.load_proxies(http, "http")
        self.load_proxies(https, "https")
        self.load_proxies(socks4, "socks4")
        self.load_proxies(socks5, "socks5")
        self.proxylists = list(set(self.proxylists))
        print(len(self.proxylists))
        threading.Thread(target=self.check_proxies).start()

    def __init__(self, target_url="https://www.quora.com/"):
        self.proxylists = []
        self.working_proxies= []
        self.target_url = target_url
        self.get_load()

    def get(self):
       
        if len(self.working_proxies) >= 1:
            return self.working_proxies.pop()
           
        if not self.proxylists:
            self.get_load()
           
        time.sleep(2)
        return self.get()
    def load_proxies(self, proxy_urls, ptype):
        for url in proxy_urls:
            contents = requests.get(url).text.split("\n")
            for line in contents:
                try:
                    c = line.split(":")
                    proxy = c[0]
                    port = c[1]
                    self.proxylists.append(f"{ptype}://{proxy}:{port}")
                except:
                    pass

    def check_proxy(self, proxy):
        self.proxylists.remove(proxy)
        try:
            session = requests.Session()
            session.proxies = {'http': proxy, 'https': proxy}
            response = session.get(self.target_url, timeout=10)
            if response.status_code == 200:
                 with open("working.txt", 'a') as f:
                    f.write(proxy + "\n")
                 self.working_proxies.append(proxy)
                 return True
        except Exception as e:
            pass
           
    def check_proxies(self, max_workers=50):
        self.proxylists = list(set(self.proxylists))
        random.shuffle(self.proxylists)
        with open("working.txt", "w")as d:
            d.write("")
        print(f"Loaded {len(self.proxylists)} proxies")
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self.check_proxy, proxy)
                       for proxy in self.proxylists]


ua = UserAgent(safe_attrs=('__injections__',))

class QuoraAutomation:
    def __init__(self, proxy=False,user_agent=False,space="https://windswept.quora.com/?sort=top"):
        self.user_agent=user_agent
        self.space= space
        self.proxy = proxy
        self.run_instance(proxy)
    
    def close_tabs_in_order(self,driver):
        driver.implicitly_wait(70)
        try:
            # Get the handles of all open tabs
            tab_handles = driver.window_handles
            print(f"{len(tab_handles)} - ads found...")
            try:
                self.update_advertisement(self.space,len(tab_handles)-1)
            except:
                pass
            # Close tabs in the order of last open first
            for tab_handle in reversed(tab_handles):
                driver.switch_to.window(tab_handle)
                driver.refresh()
                time.sleep(random.randint(1,5))
                driver.close()
           
            # Wait for a short duration before closing the first tab
            time.sleep(1)
           
            # Close the first tab
            driver.switch_to.window(tab_handles[0])
        except Exception as e:
            pass

    def run_instance(self, proxy):
       
        try:
            driver = self.get_browser_driver(proxy)
            print(driver)
            driver.implicitly_wait(150)
            if driver is None:
                return
            driver.maximize_window()
            driver.get(self.space)       
            print(driver)
            try:
                driver.save_screenshot("screen.png")
            except:
                pass
            try:
                driver.save_screenshot(f"{proxy.split(':')[2]}".png)
            except:
                pass
            time.sleep(10)
            for _ in range(random.randint(5,18)):
                self.scroll_bottom(driver)
                time.sleep(random.randint(1,3))
                           
            time.sleep(random.randint(20,40))
            self.click_on_add(driver)
            time.sleep(5)
            self.close_tabs_in_order(driver)
        except Exception as e:
            print(e)
        try:
            driver.quit()
        except:
            pass
    def click_on_add(self,driver):
        add= """
        document.querySelectorAll("div").forEach((el) => {
            if (el.style.backgroundImage) {
                console.log(el.click());
            }
        });
       
        document.querySelectorAll('a:not([href*="quora.com"])').forEach((el) => {
            el.click();
        });
       
        document.querySelectorAll('div[aria-label="ExternalLink"]').forEach((el) => { el.click() })
        """
        return driver.execute_script(add)
   
    def scroll_bottom(self,driver):
        body_element = driver.find_element(By.TAG_NAME, "body")
        actions = ActionChains(driver)
        actions.move_to_element(body_element).click().send_keys(Keys.END).perform()

        try:
            body_element = driver.find_element(By.ID, "root")
            actions = ActionChains(driver)
            actions.move_to_element(body_element).click().send_keys(Keys.END).perform()
        except:
            pass

    def update_advertisement(self, key, num, date=None):
        # Specify the path to the config file
        config_file_path = 'advertisement.json'
        
        try:
            # Try to open the existing file
            with open(config_file_path, 'r') as file:
                # Load existing data from the file
                config_data = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty dictionary
            config_data = {}

        if date is None:
            # Use the current date if no date is provided
            date = datetime.now().strftime('%Y-%m-%d')

        try:
            # Check if the date key already exists
            if date not in config_data:
                config_data[date] = {}
            config_data[date][key] = config_data[date].get(key, 0) + num
        except Exception as e:
            print(f"Error updating advertisement data: {str(e)}")

        # Write the updated data back to the file
        with open(config_file_path, 'w') as file:
            json.dump(config_data, file, indent=2)

    def get_browser_driver(self, proxy):
        print(proxy)
        options = ChromeOptions()
        if proxy:
            options.add_argument(f'--proxy-server={proxy}')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--gpu-memdown=128')
        options.add_argument('--gpu-memup=64')
        options.add_argument('--log-level=3')
        options.add_argument('--headless')
        options.add_argument("--mute-audio")
        if self.user_agent:
            options.add_argument(f'--user-agent={self.user_agent}')
       
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        # Set the maximum RAM limit to 100MB (in kilobytes)
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-gpu-compositing")
        options.add_argument("--system-memory-multiplier=0.01")
        options.add_experimental_option('prefs', {
            'profile.default_content_setting_values': {
                'images': 2,
                'javascript': 1,
                'css': 2
            }
        })
        return webdriver.Chrome(options=options)




Spaces_with_f = [
'https://lifelessio.quora.com/',
'https://wecodes.quora.com/',
'https://histnf.quora.com/',
'https://storyess.quora.com/',
'https://thehell.quora.com/',
'https://wearenotenemies.quora.com/',
'https://friendakabff.quora.com/',
'https://yvibes.quora.com/',
'https://wiredplace.quora.com/',
'https://trashtalks.quora.com/',
'https://explorebrain.quora.com/',
'https://stomach.quora.com/',
'https://aaarts.quora.com/',
'https://timeisneeded.quora.com/',
'https://veridian.quora.com/',
'https://veridian.quora.com/',
'https://stanza.quora.com/',
'https://simmer.quora.com/',
]

Spaces = []
for s in Spaces_with_f:
    rand = ["?sort=top","?sort=recent"]
    Spaces.append(s+random.choice(rand))


random.shuffle(Spaces)
counts = 0
change_space = len(Spaces)

if __name__ == "__main__":
    proxy = Proxy()
   
    # Set the number of instances to run concurrently
    max_concurrent_instances = 15

    #Create a list to store futures
    futures = []
    while True:
        # Check if any tasks are done and remove them
        done_futures = [future for future in futures if future.done()]
        for future in done_futures:
            futures.remove(future)

        # Add new tasks if there are avilable proxies
        while len(futures) < max_concurrent_instances:
            space = Spaces[change_space-1]
            try:
                proxy_get = proxy.get()
            except:
                proxy_get=False
            counts+=1
            future = concurrent.futures.ThreadPoolExecutor().submit(
                QuoraAutomation, proxy_get,user_agent=ua.random,space=space)
            futures.append(future)
            time.sleep(1)
           
        if counts >= 100:
            change_space-=1
            counts=0
           
        if change_space <= 0:
            random.shuffle(Spaces)
            counts = 0
            change_space = len(Spaces)
            break
        time.sleep(2)
