# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# [1, 2, 3, 4, 5, 4, 3, 7, 9]
# [1, 2, 3, 4, 5, 7, 9]

# Camilo
mi_listica = [1,2,3,"a","c","e",2,"c",2,2,"a"]
def borrar_repetidos(lista):
    lista_2 = []
    for i in lista:
        if not i in lista_2:
            lista_2.append(i)
    return lista_2

print(borrar_repetidos(mi_listica)) 

# Enrique
def uniqueList(first_list):
    return list(set(first_list))

lista = ['d', 's', '6', '4', '5', '6', '4', '5', '6', '4', '5', 'f', 'd', 's', 'f', 'd', 's', 
         'f', 'd', 's', 'f', 'd']
print(uniqueList(lista))

# Gidneth
def lista_manual(lista_1):
    lista_2 = []
    for item in lista_1:
        if item not in lista_2:
            lista_2.append(item)
        return lista_2
print(lista_manual([1,2,3,3,3,3,4,5]))

# John
def unique(List_1):
    print(list(set(List_1)))
List_1 = [1,2,3,'a','a','b',2,3,4,5]
unique(List_1) 
