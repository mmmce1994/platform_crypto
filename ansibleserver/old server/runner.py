from playbook import Playbookrunner
import os


runner1 = Playbookrunner(max(os.listdir("jsonfiles")))
runner1.genesisrunner()