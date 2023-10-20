from paramiko_multi_client.multihost_ssh import MultiHostSSH
from sys import argv

# Read and compile the command from CLI
argument = argv[1:]
command = ""
for word in argument:
    command = command + word + " "

# Start the program
mhssh = MultiHostSSH()
mhssh.connect_multiple_hosts(command)
