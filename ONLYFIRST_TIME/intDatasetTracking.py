# This script is used to track Dataset and build incremental version

import subprocess
from pathlib import Path
from utils import loadCfgParameters

runtime_params= loadCfgParameters()

cwd= "../../"
remoteDatasetPath=runtime_params["remote_path"]
dataset_version=1


Path().mkdir(
        parents=True, exist_ok=True)


try:
    p = subprocess.Popen(["git","rm","-r","--cached","Data/Dataset"], cwd=cwd)
    p.wait()


    if(p.returncode!=0):
        raise Exception("Cannot untrack Data Dataset")

    p = subprocess.Popen(["git","commit","-m","stop tracking Data/Dataset"], cwd=cwd)
    p.wait()

    if(p.returncode!=0):
        raise Exception("Cannot commit")

except:
     print("File already untracked.CONTINUE")

p = subprocess.Popen(["dvc","init"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot init dvc")

p = subprocess.Popen(["dvc","remote","add","-d","dvc-remote",remoteDatasetPath], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot add dvc Remote")

p = subprocess.Popen(["dvc","add","Data/Dataset"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot Add Dataset to dvc track")

p = subprocess.Popen(["git","add","Data/Dataset.dvc"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot add Dvc")

p = subprocess.Popen(["git","commit","-m","add dataset version {}".format(str(dataset_version))], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot Commit dvc Track ")

p = subprocess.Popen(["git","tag","-a","v{}".format(str(dataset_version)),"-m","update dataset"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot ad correct tag")

p = subprocess.Popen(["dvc","push"], cwd=cwd)
p.wait()

if(p.returncode!=0):
    raise Exception("Cannot update remote dataset")

print("SUCCESSFUL START TRACKING YOUR DATASET")
