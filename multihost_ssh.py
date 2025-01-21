from paramiko_custom_client import ParamikoClient
from os import environ
from tasks import Tasks
from hosts import Hosts

class MultiHostSSH:
    """ A multihost SSH client that uses RSA-keys for authentication. """

    def __init__(self):
        self.host_list = Hosts().host_list
        self.task_list = Tasks().tasks

    def add_host(self, host: Hosts):
        self.host_list.append(host)

    def add_task(self, task: Tasks):
        self.task_list = task

    def execute_tasks(self):
        pass
