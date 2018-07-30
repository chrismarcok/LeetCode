import os, glob
import shutil

def extension(x):
    """
    >>> extension("asdf.asdf")
    '.asdf'
    """
    lst = x.split(".")
    return "." + lst[-1]

def removeExt(x):
    lst = x.split(".")
    return lst[0]

# os.remove("README.md")
f = open("README.txt","w+")

f.write("## LeetCode Solutions\n\n")

lst = []
for file in os.listdir("E:\Documents\GitHub\LeetCode\LeetCode"):
    lst.append(os.path.join(file))
lst.sort()

for x in lst:
    acceptedFileExts = [".py", '.java', '.sql', '.txt']

    if extension(x) not in acceptedFileExts:
        continue

    s = " (Unknown)"
    if x.endswith(".py"):
        s = " (Python)"
    elif x.endswith(".txt"):
        s = " (Text)"
    elif x.endswith(".sql"):
        s = " (SQL)"
    elif x.endswith(".java"):
        s = " (Java)"
    f.write("- **[Problem #" + removeExt(x) + s + "](LeetCode/" + x + ")**\n")
f.write("\n\n")
f.write("[Project Euler Solutions](https://github.com/chrismarcok/Project-Euler)\n\n")
f.write("[My LeetCode Profile](https://leetcode.com/chrismarcok/)")

f.close()
shutil.copyfile("README.txt", "README.md")
os.remove("README.txt")
