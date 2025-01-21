from sys import argv
argument = argv[1:]

command = ""

for word in argument:
    command = command + word + " "

print(command)
