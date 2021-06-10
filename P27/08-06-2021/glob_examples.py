import glob

# Show paths

# paths = glob.glob("./*", recursive=True)
# print(paths)

# for path in glob.iglob("./*", recursive=True):
#     print(path)


with open("/home/jota/repositorios/mintic_class_examples/P27/08-06-2021/data.csv", "r") as f:
    text = f.read()
    print(text)

# with open("/home/jota/repositorios/mintic_class_examples/P27/08-06-2021/data.csv", "w") as f:
#     f.write("Hola Jose")

with open("/home/jota/repositorios/mintic_class_examples/P27/08-06-2021/data.csv", "a") as f:
    f.write("william,aguilar,test3@test.com")

#windows
# E:\pyton\ejercicios de clase\datos.csv 
"documents\\descargas\\archivo.csv"

# name,surname,birthday
# jose,garcia,01/01/0
# gonzalo,garcia,01/02/20
