import os, sys
os.system("git pull")
try:
    __import__("GMCV").clon_email()
except Exception as e:
    exit(str(e))
