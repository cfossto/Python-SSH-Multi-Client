import paramiko
import socket


class ParamikoClient:

    # A custom SSH client
    def create_client(self, host, username, key, command):

        try:
            # Instantiate paramiko and set the parameters for connecting.
            parami = paramiko.client
            client = parami.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect and execute the command. Wait for a response from the connection and close when done.
            client.connect(host, 22, username, key_filename=key, timeout=5)
            (stdin_, stdout_, stderr_) = client.exec_command(command)
            stdout_.channel.recv_exit_status()
            client.close()

            # Fetch the stdout from the remote terminal and print it.
            lines = stdout_.readlines()
            for line in lines:
                print(line)

        # If something is wrong with the connection, it is probably a TimeOut.
        # Check connectivity to host.
        except socket.error:
            print(f"{host} probably timed out")
