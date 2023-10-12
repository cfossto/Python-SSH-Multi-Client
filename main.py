import multihost_ssh
#from sys import argv

# Prepared for command line work

# Get the Linux command
#argument = argv[1:]
#command = ""

#for word in argument:
#    command = command + word + " "

mhssh = multihost_ssh.multi_host_ssh()

command = "ls -l /"
mhssh.connect_multiple_hosts(command)