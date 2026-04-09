import os
import time

from pyfiglet import Figlet

os.makedirs("lab4_data/input", exist_ok=True)
os.makedirs("lab4_data/output", exist_ok=True)
os.makedirs("lab4_data/logs", exist_ok=True)

print("files inside folder:")
for item in os.listdir("lab4_data"):
    print(item)

if os.path.exists("lab4_data/logs"):
          os.rename("lab4_data/logs", "lab4_data/history")

f = open("lab4_data/input/notes.txt", "w")
f.write("python is easy\n")
f.write("we are learning files\n")
f.write("this is lab 4\n")
f.write("practice makes better\n")
f.write("finish\n")
f.close()

f = open("lab4_data/input/notes.txt", "r")
lines = f.readlines()
print("lines number:", len(lines))
f.close()

f = open("lab4_data/output/summary.txt", "w")
f.writelines(lines)
f.close()

fonts = ["slant", "big", "block"]

name = "QUEEN FATIMAH"

text_all = ""

for font in fonts:
    f = Figlet(font=font)
    t = f.renderText(name)
    print(t)
    text_all += t
    time.sleep(1)
words = ["THE BEST", "NEVER GIVE UP"]

for w in words:
    f = Figlet(font="slant")
    t = f.renderText(w)
    print(t)
    text_all += t
    time.sleep(1)

f = open("lab4_data/output/ascii.txt", "w")
f.write(text_all)
f.close()

if os.path.exists("lab4_data/history"):
    if len(os.listdir("lab4_data/history")) == 0:
        os.rmdir("lab4_data/history")
        print("deleted history")
    else:
        print("not empty")