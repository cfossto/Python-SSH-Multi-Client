from paramiko_multi_client.multihost_ssh import MultiHostSSH

#from sys import argv

#argument = argv[1:]
#command = ""
#for word in argument:
#    command = command + word + " "

mhssh = MultiHostSSH()

command = "ls -l /"
mhssh.connect_multiple_hosts(command)
