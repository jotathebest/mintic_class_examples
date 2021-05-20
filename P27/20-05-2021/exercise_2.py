# Given the list below, print how many women have dark hair
# Dada la lista abajo, imprime cuántas mujeres tienen el cabello negro

women = [{'name': 'Betsy', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Paez'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Nohora', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Delgado'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Garcia'}, {'name': 'Carolina', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Carolina', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Nohora', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Martinez'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': 'dark', 'surname': 'Paez'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Nohora', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Martinez'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Paez'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Nohora', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Wendy', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Carolina', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Helena', 'hair-color': 'dark', 'surname': 'Martinez'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Helena', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Wendy', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Betsy', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Garcia'}, {'name': 'Wendy', 'hair-color': '--', 'surname': 'Paez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Alvarez'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Nohora', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Wendy', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Carolina', 'hair-color': '--', 'surname': 'Alvarez'}, {'name': 'Wendy', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Garcia'}, {'name': 'Nohora', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Betsy', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Nohora', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Wendy', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Carolina', 'hair-color': 'blonde', 'surname': 'Alvarez'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Paez'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Delgado'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Wendy', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Alvarez'}, {'name': 'Carolina', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Alvarez'}, {'name': 'Betsy', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Delgado'}, {'name': 'Betsy', 'hair-color': '--', 'surname': 'Garcia'}, {'name': 'Helena', 'hair-color': '--', 'surname': 'Alvarez'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Wendy', 'hair-color': 'dark', 'surname': 'Martinez'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Delgado'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Alvarez'}, {'name': 'Carolina', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Carolina', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': 'dark', 'surname': 'Paez'}, {'name': 'Nohora', 'hair-color': 'dark', 'surname': 'Delgado'}, {'name': 'Nohora', 'hair-color': 'blonde', 'surname': 'Martinez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Paez'}, {'name': 'Nohora', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Carolina', 'hair-color': '--', 'surname': 'Martinez'}, {'name': 'Nohora', 'hair-color': 'blonde', 'surname': 'Alvarez'}, {'name': 'Wendy', 'hair-color': 'blonde', 'surname': 'Alvarez'}, {'name': 'Helena', 'hair-color': 'blonde', 'surname': 'Delgado'}, {'name': 'Helena', 'hair-color': 'dark', 'surname': 'Paez'}]

contador = 0
for element in women:
    hair_color = element["hair-color"]
    if hair_color == "dark":
        contador += 1

print(f"Hay {contador} mujeres con el cabello negro")
