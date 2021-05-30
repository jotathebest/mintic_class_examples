my_dict = {"key-1": 1, "key-2": True, "key-3": "name"}
print(my_dict["key-2"])

my_dict = {"name": "jose", "surname": "garcia", "email": "test@test.com"}
print(my_dict["email"])

my_dict = {1: "jose", 2: "garcia"}
print(my_dict[1])

my_dict = {"name": "jose", "surname": "garcia",
           "class_scores": [5, 1, 1, 0, 2]}

note = my_dict['class_scores'][2]
print(
    f"the class note from Jose at the third day is : {note}")

my_dict = {"name": "jose", "surname": "garcia",
           "class_scores": {1: 5, 2: 1, "third-day-note": 1, 4: 0, 5: 2}}

note = my_dict["class_scores"]["third-day-note"]
print(note)
