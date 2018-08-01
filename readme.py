import os, glob
import shutil

def extension(x):
    """
    >>> extension("asdf.asdf")
    '.asdf'
    """
    lst = x.split(".")
    return "." + lst[-1]

def getProbNum(x):

    return x[0:3]

# os.remove("README.md")
f = open("README.txt","w+")

f.write("## LeetCode Solutions\n\n")

lst = []
for file in os.listdir("E:\Documents\GitHub\LeetCode\LeetCode"):
    lst.append(os.path.join(file))
lst.sort()

f.write("Problem # | Language | Difficulty\n")
f.write(":---: | :---: | :---:\n")

for x in lst:
    acceptedFileExts = [".py", '.java', '.sql', '.txt']

    if extension(x) not in acceptedFileExts:
        continue

    difficulty = ""
    language = " (Unknown)"
    multipleSolutions = ""

    if "E" in x:
        difficulty = " Easy "
    elif "M" in x:
        difficulty = "Medium"
    else:
        difficulty = " Hard "

    if "PLUS" in x:
        multipleSolutions = " (Multiple Solutions)"

    if x.endswith(".py"):
        language = "Python"
    elif x.endswith(".txt"):
        language = "Text"
    elif x.endswith(".sql"):
        language = "SQL"
    elif x.endswith(".java"):
        language = "Java"

    f.write("[" + getProbNum(x) +"](LeetCode/" + x  + ") | " + language + " | " + difficulty + "\n")


f.write("\n\n")
f.write("[Project Euler Solutions](https://github.com/chrismarcok/Project-Euler)\n\n")
f.write("[My LeetCode Profile](https://leetcode.com/chrismarcok/)")

f.close()
shutil.copyfile("README.txt", "README.md")
os.remove("README.txt")
