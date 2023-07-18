import math

print(math.floor(1.5))

# tag BEGIN

print("where am I?")

content = []
with open("rewrite.py") as file:
    line = file.readline()
    content.append(line)
    skip = False
    while line:
        line = file.readline()

        if (line == "# tag BEGIN\n"):
            skip = True
        elif (line == "# tag END\n"):
            skip = False
            continue
        
        if skip:
            continue
        content.append(line)

with open("rewrite.py", "w") as file:
    for line in content:
        file.write(line)

# tag END


print("hello world")