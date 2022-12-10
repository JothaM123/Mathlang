import os

os.system("color 0a")

def add(n1,n2):
    print(n1+n2)
    print("")    

def subtract(n1,n2):
    print(n1-n2)
    print("")

def multiply(n1,n2):
    print(n1*n2)
    print("")

def divide(n1,n2):
    print(n1/n2)
    print("")

def help():
    print("""
╭─COMMANDS : ─────────╮                                                               
│ add(n1,n2)          │
│                     │ 
│ subtract(n1,n2)     │
│                     │
│ multiply(n1,n2)     │
│                     │
│ divide(n1,n2)       │
│                     │
│ help()              │                                                               
╰─────────────────────╯      
    """)


print("Mathlang v1.0")

while 1:
    command = input(">>>")
    exec(command)

