dict1 = {"apple": 10, "banana": 20, "orange": 15}
dict2 = {"apple": 5, "banana": 10, "grapes": 25}

merged = dict1.copy()

for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print(merged)