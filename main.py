import sys
import time
import json
import random
import http.client
import urllib.request
import urllib.error
import urllib.parse
from colorama import *
import os

# Color initialization
init(autoreset=True)
mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX

last_log_message = None

# Functions from deeplchain.py
def _banner():
    banner = r"""
╔════════════════DUCK═CHAIN═════════════════╗
║              Bot Automation               ║
║         Developed by @ItbaArts_Dev        ║
╚═══════════════════════════════════════════╝
""" 
    print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
    log_line()

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_config():
    config_path = 'config.json'
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}
        
def log(message, **kwargs):
    global last_log_message
    flush = kwargs.pop('flush', False)
    end = kwargs.pop('end', '\n')
    if message != last_log_message:
        print(f"║ ✇ ⥅ {message}", flush=flush, end=end)
        last_log_message = message

def log_line():
    print(pth + "═" * 45)

def countdown_timer(seconds):
    while seconds:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        print(f"{pth}Awaiting next operation. Time remaining: {h}:{m}:{s} ", flush=True, end="\r")
        seconds -= 1
        time.sleep(1)
    print(f"{pth}Operation commencing momentarily. Standby: {h}:{m}:{s} ", flush=True, end="\r")

# Functions from agent.py
def generate_random_user_agent(device_type='android', browser_type='chrome'):
    chrome_versions = list(range(110, 127))
    firefox_versions = list(range(90, 100))

    if browser_type == 'chrome':
        major_version = random.choice(chrome_versions)
        minor_version = random.randint(0, 9)
        build_version = random.randint(1000, 9999)
        patch_version = random.randint(0, 99)
        browser_version = f"{major_version}.{minor_version}.{build_version}.{patch_version}"
    elif browser_type == 'firefox':
        browser_version = random.choice(firefox_versions)

    if device_type == 'android':
        android_versions = ['10.0', '11.0', '12.0', '13.0']
        android_device = random.choice([
            'SM-G960F', 'Pixel 5', 'SM-A505F', 'Pixel 4a', 'Pixel 6 Pro', 'SM-N975F',
            'SM-G973F', 'Pixel 3', 'SM-G980F', 'Pixel 5a', 'SM-G998B', 'Pixel 4',
            'SM-G991B', 'SM-G996B', 'SM-F711B', 'SM-F916B', 'SM-G781B', 'SM-N986B',
            'SM-N981B', 'Pixel 2', 'Pixel 2 XL', 'Pixel 3 XL', 'Pixel 4 XL',
            'Pixel 5 XL', 'Pixel 6', 'Pixel 6 XL', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro',
            'OnePlus 8', 'OnePlus 8 Pro', 'OnePlus 9', 'OnePlus 9 Pro', 'OnePlus Nord', 'OnePlus Nord 2',
            'OnePlus Nord CE', 'OnePlus 10', 'OnePlus 10 Pro', 'OnePlus 10T', 'OnePlus 10T Pro',
            'Xiaomi Mi 9', 'Xiaomi Mi 10', 'Xiaomi Mi 11', 'Xiaomi Redmi Note 8', 'Xiaomi Redmi Note 9',
            'Huawei P30', 'Huawei P40', 'Huawei Mate 30', 'Huawei Mate 40', 'Sony Xperia 1',
            'Sony Xperia 5', 'LG G8', 'LG V50', 'LG V60', 'Nokia 8.3', 'Nokia 9 PureView'
        ])
        android_version = random.choice(android_versions)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (Linux; Android {android_version}; {android_device}) AppleWebKit/537.36 "
                    f"(KHTML, like Gecko) Chrome/{browser_version} Mobile Safari/537.36")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (Android {android_version}; Mobile; rv:{browser_version}.0) "
                    f"Gecko/{browser_version}.0 Firefox/{browser_version}.0")

    elif device_type == 'ios':
        ios_versions = ['13.0', '14.0', '15.0', '16.0']
        ios_version = random.choice(ios_versions)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) "
                    f"AppleWebKit/537.36 (KHTML, like Gecko) CriOS/{browser_version} Mobile/15E148 Safari/604.1")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) "
                    f"AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{browser_version}.0 Mobile/15E148 Safari/605.1.15")

    elif device_type == 'windows':
        windows_versions = ['10.0', '11.0']
        windows_version = random.choice(windows_versions)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    f"Chrome/{browser_version} Safari/537.36")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64; rv:{browser_version}.0) "
                    f"Gecko/{browser_version}.0 Firefox/{browser_version}.0")

    elif device_type == 'ubuntu':
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                    f"Chrome/{browser_version} Safari/537.36")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{browser_version}.0) Gecko/{browser_version}.0 "
                    f"Firefox/{browser_version}.0")

    return None

# Functions from headers.py
def headers(authorization):
    return {
            "accept": "*/*",
            "authorization": f'tma {authorization}',
            "origin": "https://tgdapp.duckchain.io",
            "referer": "https://tgdapp.duckchain.io/",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Android WebView\";v=\"127\", \"Chromium\";v=\"127\"",
            "user-agent": generate_random_user_agent()
        }

# Classes and functions from core.py
class DuckChainAPI:
    def __init__(self, authorization, proxy=None, timeout=10):
        self.base_url = "https://ppp.duckchain.io"
        self.headers = headers(authorization)
        self.proxy = proxy
        self.timeout = timeout

    def _make_request(self, endpoint, params=None, retries=3):
        try:
            url = f"{self.base_url}{endpoint}"

            if params:
                url += '?' + urllib.parse.urlencode(params)

            req = urllib.request.Request(url, headers=self.headers)

            if self.proxy:
                proxy_handler = urllib.request.ProxyHandler({'http': self.proxy, 'https': self.proxy})
                opener = urllib.request.build_opener(proxy_handler)
                urllib.request.install_opener(opener)

            for attempt in range(retries):
                try:
                    with urllib.request.urlopen(req, timeout=self.timeout) as response:
                        return json.load(response)
                except urllib.error.HTTPError as e:
                    log(f"HTTP Error encountered: {e.code} - {e.reason}")
                    return None
                except urllib.error.URLError as e:
                    log(f"URL Error encountered: {e.reason}")
                    log(htm + "═" * 39)
                    return None
                except http.client.RemoteDisconnected:
                    log(f"Remote disconnection occurred. Attempt {attempt + 1} unsuccessful. Initiating retry...")
                    time.sleep(2)
                    continue
                except TimeoutError:
                    log(f"Operation timed out. Attempt {attempt + 1} unsuccessful. Initiating retry...")
                    time.sleep(2)
                    continue
        except Exception as e:
            log(f"Caught an exception: {e}")     

        log("All retry attempts have been exhausted without success.")
        return None

    def get_user_info(self):
        return self._make_request("/user/info")
    
    def check_in(self):
        return self._make_request("/task/sign_in?")
    
    def check_egg(self):
        return self._make_request("/property/daily/finish?taskId=1")
    
    def spin(self):
        return self._make_request("/draw/do?size=1")

    def execute_tap(self):
        return self._make_request("/quack/execute")
    
    def perform_sign(self):
        check_in_response = self.check_in()
        if check_in_response and check_in_response.get("code") == 200:
            log(hju + f"Daily check-in procedure completed successfully")
        elif check_in_response.get("code") == 500:
            log(hju + f"Daily check-in status: {kng}Already completed")
        else:
            log(mrh + f"Daily check-in procedure encountered an error.")

    def open_all_boxes(self, open_type=1):
        while True:
            endpoint = "/box/open"
            params = {'openType': open_type}

            response = self._make_request(endpoint, params)
            if response and response['code'] == 200 and response['message'] == "SUCCESS":
                data = response['data']
                quantity = data.get('quantity', 0)
                obtain = data.get('obtain', 0)
                boxes_left = data.get('boxesLeft', 0)
                log(hju + f"Box opening operation executed successfully!")
                log(hju + f"Quantity: {pth}{quantity} {hju}| Points acquired: {pth}{obtain} {hju}| Remaining boxes: {pth}{boxes_left}")

                if boxes_left == 0:
                    log(f"{kng}All boxes have been opened. {pth}No additional boxes available.")
                    break
            elif response['code'] == 500:
                log(f"{kng}Current box count: {pth}0 {kng}. Operation skipped.")
                break
            else:
                log(f"{Fore.RED}Box opening operation failed. Error code: {response.get('code', 'N/A')}, Error message: {response.get('message', 'Unknown error')}")
                break

    def handle_tasks(self):
        tasks_response = self._make_request("/task/task_list")
        
        if not isinstance(tasks_response, dict):
            log(f"Unexpected task data format received: {tasks_response}")
            return

        tasks = tasks_response.get('data')
        if not tasks:
            log("No task data found in the 'data' field.")
            return

        for category, task_list in tasks.items():
            if isinstance(task_list, list):
                for task in task_list:
                    try:
                        task_id = task.get('taskId')
                        content = task.get('content')
                        integral = task.get('integral')
                        log(hju + f"Initiating task completion: {pth}{content}")
                        completion_response = self._make_request(f"/task/{category}", {'taskId': task_id})
                        if completion_response and completion_response.get("code") == 200:
                            log(kng + f"Task completed successfully. {bru}Reward: {pth}{integral} {bru}Points")
                        elif completion_response.get("code") == 500:
                            log(kng + f"Task {pth}{content} {kng}has already been completed.")
                        else:
                            log(mrh + f"Task completion failed. Task: {pth}{content} {htm}Response: {completion_response}.")
                    except Exception as e: 
                        log(f"Caught an exception: {e}")
            else:
                log(htm + f"Unexpected task list format encountered for category {kng}{category}: {pth}{task_list}")


def get_proxy():
    try:
        with open('proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]

        if not proxies:
            log("No proxy configurations found in proxies.txt.")
            return None

        proxy = random.choice(proxies)

        if proxy.startswith("http://"):
            return proxy
        elif proxy.startswith("https://"):
            return proxy
        elif proxy.startswith("socks5://"):
            return proxy
        else:
            return f"http://{proxy}"
    except FileNotFoundError:
        log("The file 'proxies.txt' could not be located.")

def log_user_info(user_info):
    if user_info['code'] == 200 and user_info['message'] == "SUCCESS":
        data = user_info['data']
        log(hju + f"Duck identifier: {pth}{data['duckName']}")
        log(hju + f"Decibel count: {pth}{data['decibels']}{hju}| Box inventory: {pth}{data['boxAmount']} ")
    else:
        log(mrh + f"User information retrieval failed. Error code: {user_info['code']}, Error message: {user_info['message']}")

def log_quack_result(quack_result, quack_number):
    if quack_result['code'] == 200 and quack_result['message'] == "SUCCESS":
        data = quack_result['data']
        quack_records = data.get('quackRecords', [])
        A = quack_records[8] if len(quack_records) > 8 else None
        B = quack_records[0] if len(quack_records) > 0 else None

        result = A if A else B if B else "No record available"
        
        log(f"{bru}Quack operation {pth}{quack_number}: {pth}{data['result']} {hju}| Outcome: {pth}{result}")
        log(f"{hju}Decibel fluctuation: {pth}{data['decibel']} {hju}| Quack frequency: {pth}{data['quackTimes']}")
    else:
        log(mrh + f"Quack operation execution failed. Error code: {quack_result['code']}, Error message: {quack_result['message']}")

def main():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        log("Configuration file 'config.json' not found.")
        return

    use_proxy = config.get("use_proxy", False)
    quack_delay = config.get("quack_delay", 0)
    quack_amount = config.get("quack_amount", 10)
    complete_task = config.get("complete_task", False)
    account_delay = config.get("account_delay", 5)
    countdown_loop = config.get("countdown_loop", 3800)
    try:
        with open('query.txt', 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        log("Data file 'query.txt' not found.")
        return

    if not tokens:
        log("No token data found in query.txt")
        return

    total_accounts = len(tokens)
    for index, token in enumerate(tokens, start=1): 
        try:
            proxy = get_proxy() if use_proxy else None
            duck = DuckChainAPI(authorization=token, proxy=proxy)
            log(bru + f"Processing account {pth}{index} of {total_accounts}") 
            log(htm + "═" * 39)

            user_info = duck.get_user_info()
            if user_info:
                log_user_info(user_info)

                duck.perform_sign()
                duck.check_egg()
                duck.spin()
                duck.open_all_boxes()

                for i in range(quack_amount):
                    quack_result = duck.execute_tap()
                    if quack_result:
                        log_quack_result(quack_result, i + 1)
                    else:
                        log(f"{Fore.RED}Quack operation #{i+1} execution failed.")
                    time.sleep(quack_delay)

                if complete_task:
                    duck.handle_tasks()
                else:
                    log(kng + f"Automated task completion is currently disabled.")

                log_line()
                countdown_timer(account_delay)
        except Exception as e:
            log(f"Caught an exception: {e}")   

    countdown_timer(countdown_loop)

if __name__ == "__main__":
    _clear()
    _banner()
    log(hju + f"Bot initialization in progress...")
    log(pth + "═" * 39)
    while True:
        try:
            main()
        except KeyboardInterrupt:
            log(mrh + f"Logging out...\n")
            sys.exit()
