import glob

# Show paths

# paths = glob.glob("./*", recursive=True)
# print(paths)

# for path in glob.iglob("./*", recursive=True):
#     print(path)

# with open("/home/jota/repositorios/mintic_class_examples/P47/08-06-2021/data.csv", "r") as f:
#     text = f.read()
#     print(text)

# with open("/home/jota/repositorios/mintic_class_examples/P47/08-06-2021/data.csv", "w") as f:
#     f.write("Hola Jose")

# with open("/home/jota/repositorios/mintic_class_examples/P47/08-06-2021/data.csv", "a") as f:
#     f.write("gonzalo,garcia,test2@test.com")

# name,surname,hora
# jose,garcia,6:24
# carolina,martinez,6:24
# gonzalo,garcia,6:25

# windows
# E:\pyton\ejercicios de clase\datos.csv -- > E:\\pyton\\ejercicios de clase\\datos.csv

import datetime

with open("/home/jota/repositorios/mintic_class_examples/P47/08-06-2021/data.csv", "a") as f:
    f.write("NAME, SURNAME, SCRIPT HOUR\n")
    run_time_script = datetime.datetime.now().hour
    f.write(f"Guillermo, Lopez, {run_time_script}\n")
    run_time_script = datetime.datetime.now().hour
    f.write(f"Isabel, Chaves, {run_time_script}\n")
    run_time_script = datetime.datetime.now().hour
    f.write(f"Alina, Neisa, {run_time_script}\n") 
