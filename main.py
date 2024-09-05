from compile_hosts import CompileHosts
from target_hosts import TargetHosts
from multihost_ssh import MultiHostSSH
from sys import argv


# Read and compile the command from CLI
argument = argv[1:]
command = ""
for word in argument:
    command = command + word + " "

# Start the program
mhssh = MultiHostSSH()
mhssh.connect_multiple_hosts_dict_strategy(command)

host1 = TargetHosts("10.0.0.1", "micozd1.lo", "mico")
host2 = TargetHosts("10.0.0.2", "micozd2.lo", "mico")
host_list = CompileHosts()

host_list.addHostToList(host1)
host_list.addHostToList(host2)

MultiHostSSH().connect_multiple_host_object_list_stategy(host_list.host_list)
