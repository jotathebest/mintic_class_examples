my_dict = {"key-1": 1, "key-2": 2, "key-3": 3}
# print(my_dict)

my_dict = {"name": "Jose", "surname": "Garcia", "email": "test@test.com"}
# print(my_dict["name"])
# print(my_dict["email"])

my_dict = {"name": "Jose", "surname": "Garcia",
           "class_scores": [5, 1, 3, 0, 1]}

# print(my_dict["class_scores"])
note = my_dict["class_scores"][2]
# print(f"the Jose's note at the third day is {note}")

my_dict = {"name": "Jose", "surname": "Garcia",
           "class_scores": {"day-1": 1, "day-2": 4, "day-3": 2, "day-4": 5, "day-5": 0}}

# print(my_dict["class_scores"]["day-3"])

my_dict = {"key-1": input("value 1: "), "key-2": input("value 2: ")}
print(my_dict)
