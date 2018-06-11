from playbook import Playbookrunner
import sys

github_link = str(sys.argv[1])
request_id = str(sys.argv[2])
#platform = str(sys.argv[3])

runner1 = Playbookrunner()

test = runner1.androidbuilder(github_link,request_id)