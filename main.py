from sys import argv
from hosts import Hosts


argument = argv[1:]

command = ""

for word in argument:
    command = command + word + " "


h = Hosts()

h.add_host_to_list("192.168.1.22", "ssh-server")
h.add_host_to_list("101.123.2.11", "prod", "prod.prod.net")
h.get_hosts_from_config("hosts.yaml")
