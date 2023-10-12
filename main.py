import paramiko

parami = paramiko.client

try:

    client = parami.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("micozdtest.lo",username="test_user",port=22,key_filename="/Users/christopherfossto/.ssh/id_rsa")
    print("before execute")
    (stdin_,stdout_,stderr_) = client.exec_command('ls -l /')
    stdout_.channel.recv_exit_status()
    print("after execute")
    client.close()
    lines = stdout_.readlines()
    for line in lines:
        print(line)
except:
    print("Woops")