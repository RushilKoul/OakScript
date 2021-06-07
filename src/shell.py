#!/usr/local/bin/python3
import oak
from termcolor import colored
import os
import sys

from datetime import date
today = date.today();

version = "0.0.1 (v01aa)"
try:
    path = sys.argv[1]
    
    f = open(path.split("/")[-1], "r")
    code = f.read()

    text = code
    result, error = oak.run('<stdin>', text)

    if error: 
        print(colored(error.as_string(), 'red'))
    else: 
        print(result)        

except Exception:
    print(colored(f'Oak {version} {today.strftime("%b-%d-%Y")} \n type "help" for information, "exit" to exit.', 'yellow'))
    while True:
        text = input(colored('oak > ', 'blue'))
        if text == 'exit':
            break
        elif text == 'help':
            print(colored(f'OakScript {version}\n A compiler made in python that can do basic arthmetic operations like addition, subratraction, etc. You can use negative numbers.', 'green'))
            continue
        result, error = oak.run('<stdin>', text)

        if error: 
            print(colored(error.as_string(), 'red'))
        else: 
            print(result)


      