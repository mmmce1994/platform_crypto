from playbook import Playbookrunner
import sys

request_id = str(sys.argv[1])

runner1 = Playbookrunner()

test = runner1.genesisrunner(request_id)