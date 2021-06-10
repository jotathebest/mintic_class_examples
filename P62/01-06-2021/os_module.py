# Write a Python program to get the name of the operating system (Platform independent), information of current
# operating system, current working directory, print files and directories in the current directory

import os

# os_information = os.uname()
# print(f"Operating system: {os_information.sysname}")
# current_dir = os.getcwd()
# print(f"Current directory: {current_dir}")
# list_dirs = os.listdir(".")
# print(f"list dirs: {list_dirs}")

# with open("/home/jota/repositorios/mintic_class_examples/P62/01-06-2021/data.csv", "r") as f:
#     text = f.read()
#     print(text)

# with open("/home/jota/repositorios/mintic_class_examples/P62/01-06-2021/data.csv", "w") as f:
#     f.write("hello jose!")

# with open("/home/jota/repositorios/mintic_class_examples/P62/01-06-2021/data.csv", "a") as f:
#     f.write("hello jose!")

# id,name,email,fecha actual
# 1,Jose,test@test.com,09-06-2021
# 2,Carolina,test2@test.com,09-06-2021
# 3,Juan,test3@test.com,09-06-2021
# 4,Camila,test4@test.com,09-06-2021

import datetime
names = ["jose", "Carolina", "Juan", "Camila"]
emails = ["test@test.com", "test2@test.com", "test3@test.com", "test4@test.com"]

with open("/home/jota/repositorios/mintic_class_examples/P62/01-06-2021/data.csv", "a") as f:
        f.write("id,name,email,fecha actual")
        f.write("\n")

for index, element in enumerate(names):
    with open("/home/jota/repositorios/mintic_class_examples/P62/01-06-2021/data.csv", "a") as f:
        name = names[index]
        email = emails[index]
        aux = index + 1
        date = datetime.datetime.now()
        f.write(f"{aux},{name},{email},{date.day}-{date.month}-{date.year}")
        f.write("\n")


# Write a Python program to list only directories, files and all directories, files in a specified path.

# Write a Python program to find the parent's process id, real user ID of the current process and
# change real user ID.

# Write a Python program to run an operating system command using the os module.
