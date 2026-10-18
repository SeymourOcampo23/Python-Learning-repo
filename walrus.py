d = [
    {"userId": 1, "name": "marc", "completed": False},
    {"userId": 1, "name": "josef", "completed": False},
    {"userId": 1, "name": "irwin", "completed": False},
    {"userId": 1, "name": "jamal", "completed": True}
]

for i in d:
    if name := i.get("name"):
        print(name)

num = 0
while (num_square := num ** 2) < 1000:
    print(num_square)
    num += 1

    