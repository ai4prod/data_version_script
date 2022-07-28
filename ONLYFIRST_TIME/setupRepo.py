# This script is used to setup what to track inside git for dataset management
# This script needs to be executed from Script Folder otherwise change cwd

import subprocess

dataset_name= "simpleObjectDetection"
cwd= "../"

p = subprocess.Popen(["git","init"], cwd=cwd)
p.wait()

p = subprocess.Popen(["git","add", "DatasetArchitecture.graphml", 
                        "LICENSE","Metadata/",
                        "Readme.md",
                        "Script",
                        "Tests/"], cwd=cwd)
p.wait()

p = subprocess.Popen(["git","commit", "-m", "init dataset {}".format(dataset_name)], cwd=cwd)
p.wait()


