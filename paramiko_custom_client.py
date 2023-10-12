import paramiko

class paramiko_client:

    parami = paramiko.client()

    def create_client(self,host,username,key):

        try:
            client = self.parami.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,username,key,port=22)
            print("before execute")
            (stdin_, stdout_, stderr_) = client.exec_command('ls -l /')
            stdout_.channel.recv_exit_status()
            print("after execute")
            client.close()
            lines = stdout_.readlines()
            for line in lines:
                print(line)
        except:
            print("Woops")