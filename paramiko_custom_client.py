import paramiko

class paramiko_client:


    def create_client(self,host,username,key,command):

        try:
            parami = paramiko.client
            client = parami.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,22,username,key_filename=key)
            print("before execute")
            (stdin_, stdout_, stderr_) = client.exec_command(command)
            stdout_.channel.recv_exit_status()
            print("after execute")
            client.close()
            lines = stdout_.readlines()
            for line in lines:
                print(line)
        except paramiko.ssh_exception as e:
            print("Woops from paramiko"+ e)