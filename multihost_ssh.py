from paramiko_custom_client import ParamikoClient
from os import environ


class MultiHostSSH:
    """ A multihost SSH client that uses RSA-keys for authentication. """

    def connect_multiple_hosts_dict_strategy(self,command):

        # Unique keyfiles per host
        # Hosts can also be IPs
        key_files = {

            # Host
            'micozdtest.lo': {
                # Host key
                'key': f"{environ.get('micozdtest-key')}",
                # Username to connect with
                "username": 'test_user'}
        }

        p = ParamikoClient()
        try:
            # Loop through all keys (hosts) in the key_files.
            # Then set the parameters for making a connection with the custom client.
            for host in key_files.keys():
                print(f"Output from server - {host}:")
                key = key_files.get(host).get('key')
                username = key_files.get(host).get('username')

                # Use the custom client
                p.create_client(host,username,key,command)
        except:
            print("Multihost function failed.")

    def connect_multiple_host_object_list_stategy(self, host_list):
        for host in host_list:
            print(host.ip)



