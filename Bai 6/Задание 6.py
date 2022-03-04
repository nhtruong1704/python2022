import sys

def print(*objects, sep=' ', end='\n'):
    if len(objects) > 1:
        for i in range(len(objects) - 1):
            sys.stdout.write(str(objects[i])) #doesn’t switch to a new line
            sys.stdout.write(sep)
        sys.stdout.write(str(objects[i + 1]))
    else:
        sys.stdout.write(str(objects[0]))
    sys.stdout.write(end)


print("Dinh", "Nhat", "Truong", end=": ")
print("IKBO", "25", sep=" — ", end=";\n")
print("sum mus"[::-1], end=" = ")
print("sum mus")