from paramiko_multi_client.paramiko_custom_client import ParamikoClient


class MultiHostSSH:

    key_files = {
        'micozdtest.lo': {
            'key': "/Users/christopherfossto/.ssh/id_rsa",
            "username": 'test_user'}
    }

    def connect_multiple_hosts(self,command):
        p = ParamikoClient()
        try:
            for host in self.key_files.keys():
                print(f"Output from server - {host}:")
                key = self.key_files.get(host).get('key')
                username = self.key_files.get(host).get('username')
                p.create_client(host,username,key,command)
        except:
            print("Multihost function failed.")
