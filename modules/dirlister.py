import os

def run(**args):
    print("[*] In dirlister module")
    files = os.listdir(path=".") 
    return str(files)
