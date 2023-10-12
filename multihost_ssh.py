from paramiko_custom_client import paramiko_client


class multi_host_ssh:
    # Prepared for multihost-setup

    #List of hosts
    hosts = ['micozdtest.lo']

    # Unique keyfiles per host
    key_files = {
        'micozdtest.lo': {
            'key':"/Users/christopherfossto/.ssh/id_rsa",
            "username":'test_user'}
    }

    def connect_multiple_hosts(self,command):
        p = paramiko_client()
        try:
            for host in self.hosts:
                key = self.key_files.get(host).get('key')
                username = self.key_files.get(host).get('username')
                p.create_client(host,username,key,command)
        except ():
            print("Fail")