import paramiko
import socket


class ParamikoClient:
    def create_client(self, host:str, username:str, key:str, command:str):

        try:
            parami = paramiko.client
            client = parami.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(host, 22, username, key_filename=key, timeout=5)
            (stdin_, stdout_, stderr_) = client.exec_command(command)
            stdout_.channel.recv_exit_status()
            client.close()
            
            lines = stdout_.readlines()
            for line in lines:
                print(line)
                
        except socket.error:
            print(f"{host} probably timed out")
