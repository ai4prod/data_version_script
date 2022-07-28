import subprocess
from utils import loadCfgParameters

# This script is used to track Dataset and build incremental version


runtime_params= loadCfgParameters()
dataset_version= runtime_params["update"]["dataset_version"]
cwd=runtime_params["update"]["cwd"]

# Each step need to be verified

p = subprocess.Popen(["dvc","add","Data/Dataset"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot Use dvc")

p = subprocess.Popen(["git","add","Data/Dataset.dvc","Data/.gitignore"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot add to git")

p = subprocess.Popen(["git","commit","-m","add dataset version {}".format(str(dataset_version))], cwd=cwd)
p.wait()


if(p.returncode!=0):
    raise Exception("Cannot commit to git")

p = subprocess.Popen(["git","tag","-a","v{}".format(str(dataset_version)),"-m","update dataset"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot tag")

p = subprocess.Popen(["dvc","push"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot Update Dataset")

print("UPDATE DATASET TO v{} SUCCESSFUL".format(dataset_version))
