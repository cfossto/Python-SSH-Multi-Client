import yaml


class Hosts:

    def __init__(self):
        self.host_list = []

    def add_host_to_list(self, target_ip: str, hostname: str, domain=None):

        target = {
            "target_ip": target_ip,
            "target_domain_name": domain,
            "hostname": hostname
        }
        self.host_list.append(target)

    def get_hosts_from_config(self):
        conf_file = open("hosts.yaml", "r")
        host_list = yaml.load(conf_file, Loader=yaml.BaseLoader)

        hosts = host_list

        for i in hosts:
            self.host_list.append(i)

        conf_file.close()
