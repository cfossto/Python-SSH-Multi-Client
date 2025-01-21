import paramiko
import socket


class ParamikoClient:

    def __init__(self):
        self.host = ""
        self.port = 22
        self.username = ""
        self.key = ""

    def create_client(self):
        pass

    def execute_command(self, command):

        try:
            p = paramiko.client.SSHClient()
            p.connect(
                hostname=self.host,
                port=self.port,
                username=self.username,
                key_filename=self.key
            )
            (stdin_, stdout_, stderr_) = p.exec_command(command)
            stdout_.channel.recv_exit_status()
            p.close()

            lines = stdout_.readlines()
            for line in lines:
                print(line)

        except socket.error:
            print(f"{self.host} probably timed out")