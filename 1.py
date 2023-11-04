import requests
GREEN = '\033[32m'
RED = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[0m'
YELLOW = '\033[33m'

banner = """
 /$$                                     /$$                                   
| $$                                    | $$                                   
| $$        /$$$$$$  /$$$$$$$$ /$$   /$$| $$        /$$$$$$   /$$$$$$  /$$$$$$ 
| $$       |____  $$|____ /$$/| $$  | $$| $$       |____  $$ /$$__  $$|____  $$
| $$        /$$$$$$$   /$$$$/ | $$  | $$| $$        /$$$$$$$| $$  \__/ /$$$$$$$
| $$       /$$__  $$  /$$__/  | $$  | $$| $$       /$$__  $$| $$      /$$__  $$
| $$$$$$$$|  $$$$$$$ /$$$$$$$$|  $$$$$$$| $$$$$$$$|  $$$$$$$| $$     |  $$$$$$$
|________/ \_______/|________/ \____  $$|________/ \_______/|__/      \_______/
                               /$$  | $$                                       
                              |  $$$$$$/                                       
                               \______/                                        
"""
print(BLUE + banner + RESET)
print(YELLOW + 'just for educational purposes' + RESET)
print('The URL should be like "http://example.com"')
target = input('url :')
url = target + ':80' 
laravel = 'laravel.txt'
with open(laravel, 'r') as file:
    laravels = file.read().strip().split('\n')

for laravel_url in laravels:
    urls = url + laravel_url
    response = requests.get(urls)
    if response.status_code == 200:
        print(GREEN +'Vuln :' + RESET + urls)
    else:
        print(RED +'Not Vuln :'+ RESET + urls)