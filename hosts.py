class Hosts:

    def __init__(self):
        self.host_list = []

    def add_host_to_list(self, target_ip, hostname):

        target = {
            "target_ip": target_ip,
            "hostname": hostname
        }
        self.host_list.append(target)
