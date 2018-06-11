import os
import sys
import json
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase

from resultcollector import ResultsCollector

currentdir = os.getcwd()

class Playbookrunner(CallbackBase):
    def __init__(self):
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
        self.passwords = {}

    def genesisrunner(self,filename):

        variable_manager = self.variable_manager

        variable_manager.extra_vars = {"filename": filename,
                                       "source_json_directory": currentdir+"/jsonfiles/"+filename+".json"}

        playbook_path = 'localgenesisdockerrunner.yml'

        callback = ResultsCollector("genesisRunner")

        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.inventory, variable_manager=variable_manager,
                                loader=self.loader, options=self.options, passwords=self.passwords, stdout_callback=callback)

        results = pbex.run()

        os.remove(currentdir + "/jsonfiles/" + filename + ".json")

        return results

    def ping(self):

        variable_manager = self.variable_manager

        playbook_path = 'ping.yml'

        callback = ResultsCollector("ping")

        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.inventory, variable_manager=variable_manager,
                                loader=self.loader, options=self.options, passwords=self.passwords, stdout_callback=callback)

        results = pbex.run()

        return  results

    def corebuilder(self,link,filename,platform):

        variable_manager = self.variable_manager

        variable_manager.extra_vars = {"github_link": link,"filename": filename, 'platform': platform}

        playbook_path = 'corebuilder.yml'

        callback = ResultsCollector("coreBuilder")

        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.inventory, variable_manager=variable_manager,
                               loader=self.loader, options=self.options, passwords=self.passwords,
                               stdout_callback=callback)


        results = pbex.run()

        return results

    def apacheserver(self,username,password,filename,platform):
        variable_manager = self.variable_manager

        variable_manager.extra_vars = {"username": username, "password": password, "filename": filename,'platform': platform}

        playbook_path = 'apacheserver.yml'

        callback = ResultsCollector("apacheServer")

        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.inventory, variable_manager=variable_manager,
                                loader=self.loader, options=self.options, passwords=self.passwords,
                                stdout_callback=callback)

        results = pbex.run()

        playbook_path2 = 'apacheuser.yml'

        pbex2 = PlaybookExecutor(playbooks=[playbook_path2], inventory=self.inventory, variable_manager=variable_manager,
                                loader=self.loader, options=self.options, passwords=self.passwords,
                                stdout_callback=callback)
        results2 = pbex2.run()

        return results

    def androidbuilder(self, link, filename):
        variable_manager = self.variable_manager

        variable_manager.extra_vars = {"github_link": link, "filename": filename}

        playbook_path = 'androidbuilder.yml'

        callback = ResultsCollector("androidbuilder")

        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.inventory, variable_manager=variable_manager,
                                loader=self.loader, options=self.options, passwords=self.passwords,
                                stdout_callback=callback)

        results = pbex.run()