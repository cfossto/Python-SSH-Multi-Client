from paramiko_multi_client import multihost_ssh

'''
    We are trying out three things here:
        1. To get a string from argv to serve as a CLI-command
        2. Connect to a server via Paramiko and custom host-key
        3. Connect to a the same server with asynciossh

        Things are commented out because of testing.
'''

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