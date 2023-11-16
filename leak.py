import googlesearch
from googlesearch import search
import wget
import os
import argparse
import random
import ipaddress
import time
import urllib
global user_ip
import faker
from os.path import exists
from faker import Faker

user_ip = Faker()
ip_addr = user_ip.ipv4()
ip_address = user_ip.ipv6()
MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1


def random_ipv4():
    return  ipaddress.IPv4Address._string_from_ip_int(
        random.randint(0, MAX_IPV4)
    )

def random_ipv6():
    return ipaddress.IPv6Address._string_from_ip_int(
        random.randint(0, MAX_IPV6)
    )
random.seed(444)
random_ipv4()
'79.19.184.109'
random_ipv4()
'3.99.136.189'
random_ipv4()
'124.4.25.53'
random_ipv6()
'4fb7:270d:8ba9:c1ed:7124:317:e6be:81f2'
random_ipv6()
'fe02:b348:9465:dc65:6998:6627:1300:29c9'
random_ipv6()
'74a:dd88:1ff2:bfe3:1f3:81ad:debd:db88'    
address = random_ipv4()
ip6 = random_ipv6()

global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']

parser = argparse.ArgumentParser(description='usage : python3 leak.py -s <site> -f <file type>')

parser.add_argument('-s', type=str, help='Target Site')
parser.add_argument('-f', type=str, help='Database File Type')

# Mendapatkan argumen dari baris perintah
args = parser.parse_args()

success = '\033[1;32m'
info = '\033[1;33m'
fail = '\033[1;91m'

print("""\033[1;91m

░██╗░░░░░░░██╗██╗░░██╗██╗████████╗███████╗██████╗░░█████╗░░██████╗███████╗
░██║░░██╗░░██║██║░░██║██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
░╚██╗████╗██╔╝███████║██║░░░██║░░░█████╗░░██████╔╝██║░░██║╚█████╗░█████╗░░
░░████╔═████║░██╔══██║██║░░░██║░░░██╔══╝░░██╔══██╗██║░░██║░╚═══██╗██╔══╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗██║░░██║╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝

      Coded By whiterose
""")
a1 = args.s
a2 = args.f
os.makedirs(a1)
global file_types
file_types = [a2]
def dorker():
        request = 0
        path = a1
        isdir = os.path.isdir(path)
        if isdir == True:
            pass
        else:
            os.mkdir(a1)  
        os.chdir(a1)    
counter = 1
counter = counter + 1
for files in file_types:
       try: 
            file_exists = exists('.google-cookie')
            if file_exists == True:
             os.remove('.google-cookie')
            rand_user = random.choice(user_agents)
            rand_ipv4 = random.choice(address)
            rand_ipv6 = random.choice(ip6)
            print(info + f'\033[1;33m<!> Processing <!>: Searching Info For {files}..')
            for results in search(f'site:{a1} filetype:{files}', tld='com', lang='en', num=int(f'{counter}'), start=0, stop=None, pause=10):
             print(success + f'[+]Found[+] : ')
             print(success + f'\033[1;33m{results}')
             wget.download(results, out=a1)
             requ =+ 1
       except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
                 continue
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
                 continue
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
             else:
                 continue    
       except FileExistsError:
           print(fail + f'File {a1} Exists.')
           os.remove(a1)
           print(success + f'Deleted')
       except OSError:
                 continue
       except urllib.error.URLError:
                print(fail + f'[Error] File {a2} could not be downloaded. Skipping.')
                continue
       except ModuleNotFoundError:
                print(fail + f'[Error] Did you already install requirements.txt?')
       except UnicodeDecodeError:
                continue 

print ("Done...")
print ("\n\t\t\t\t\033[34whiteroseeee\033[0m")
print ("\t\t\033[1;91mExit\n\n")   
exit()
