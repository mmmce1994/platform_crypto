from playbook import Playbookrunner
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
filename = str(sys.argv[3])
platform = str(sys.argv[4])

runner1 = Playbookrunner()

test = runner1.apacheserver(username,password,filename,platform)