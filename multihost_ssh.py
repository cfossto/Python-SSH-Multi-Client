
# Prepared for multihost-setup

#List of hosts
hosts = ['micozdtest.lo']

# Unique keyfiles per host
key_files = {
    'micozdtest.lo': {
        'key':"/Users/christopherfossto/.ssh/id_rsa",
        "username":'test_user'}
}

print("List of hosts with keys")


#for hosts in key_files.keys():
#    print(hosts)

for host in hosts:
    key = key_files.get(host).get('key')
    username = key_files.get(host).get('username')
    print(
        key + "\n" + username
    )
