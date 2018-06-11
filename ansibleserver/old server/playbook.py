import os
import sys
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase


from resultcollector import ResultsCollector

currentdir = os.getcwd()

class Playbookrunner(CallbackBase):
    def __init__(self,filename):
        self.filename = filename
        self.loader = DataLoader()
        self.variable_manager = VariableManager()
        self.inventory = Inventory(loader=self.loader, variable_manager=self.variable_manager,  host_list='hosts')
        self.Options = namedtuple('Options',
                          ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection', 'module_path', 'forks',
                           'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args',
                           'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
        self.options = self.Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                            module_path=None, forks=100, remote_user=None, private_key_file=None, ssh_common_args=None,
                            ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                            become_method='sudo', become_user='root', verbosity=None, check=False)
        self.variable_manager.extra_vars = {"filename":self.filename , "source_json_directory":currentdir+"/jsonfiles/"+self.filename} #can accomodate various other command line arguments.`
        self.passwords = {}

    def genesisrunner(self):
        playbook_path = 'localgenesisdockerrunner.yml'

        callback = ResultsCollector()

        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.inventory, variable_manager=self.variable_manager,
                                loader=self.loader, options=self.options, passwords=self.passwords, stdout_callback=callback)
        results = pbex.run()

        os.remove(currentdir + "/jsonfiles/" + self.filename)