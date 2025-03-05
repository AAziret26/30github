with open("text.txt", "w") as f:
    f.write("Привет, мир!")

with open("text.txt", "r") as f:
    print(f.read())
