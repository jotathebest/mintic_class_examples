# Write a Python program to get the name of the operating system (Platform independent), information of current
# operating system, current working directory, print files and directories in the current directory
# and raises error in the case of invalid or inaccessible file names and paths.

import os

file_system = os.uname()
print(f"Operating system {file_system.sysname}")
current_path = os.getcwd()
print(f"Current path: {current_path}")

with open("/home/jota/repositorios/mintic_class_examples/P47/01-06-2021/test.txt", "r") as f:
    text = f.read()
    print(text)

# Write a Python program to list only directories, files and all directories, files in a specified path.

# Write a Python program to find the parent's process id, real user ID of the current process and
# change real user ID.

# Write a Python program to run an operating system command using the os module.
