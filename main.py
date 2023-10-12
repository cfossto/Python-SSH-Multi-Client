import multihost_ssh

mhssh = multihost_ssh.multi_host_ssh()

mhssh.connect_multiple_hosts("ls -l /")