data = {
  "A": [24.4, 19.8, 23.3, 10.0],
  "B": [19.8, 49.2, 23.3, 56.9],
  "C": [17.5, 17.9, 18.8, 19.8]
}

for x in data["A"]:
    for y in data["B"]:
        for z in data["C"]:
            if x == y and x == z:
                print(x)
for x in data["A"]:
    if x in data['B'] and x in data["C"]:
        print(x)