from paramiko_multi_client.paramiko_custom_client import ParamikoClient



class MultiHostSSH:
    """ A multihost SSH client that uses RSA-keys for authentication. """
    # Unique keyfiles per host
    # Hosts can also be IPs
    key_files = {

        # Host
        'micozdtest.lo': {
            # Host key
            'key': "/Users/christopherfossto/.ssh/id_rsa",
            # Username to connect with
            "username": 'test_user'}
    }

    def connect_multiple_hosts(self,command):
        p = ParamikoClient()
        try:
            # Loop through all keys (hosts) in the key_files.
            # Then set the parameters for making a connection with the custom client.
            for host in self.key_files.keys():
                print(f"Output from server - {host}:")
                key = self.key_files.get(host).get('key')
                username = self.key_files.get(host).get('username')

                # Use the custom client
                p.create_client(host,username,key,command)
        except:
            print("Multihost function failed.")