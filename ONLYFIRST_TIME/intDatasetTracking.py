# This script is used to track Dataset and build incremental version

import subprocess

cwd= "../"
remoteDataset="/media/dati/RemoteDataset/simpleObjectDetectionVersioningRemote/"
dataset_version=1


p = subprocess.Popen(["dvc","init"], cwd=cwd)
p.wait()

p = subprocess.Popen(["dvc","remote","add","-d","dvc-remote",remoteDataset], cwd=cwd)
p.wait()


p = subprocess.Popen(["dvc","add","Data/Dataset"], cwd=cwd)
p.wait()


p = subprocess.Popen(["git","add","Data/Dataset.dvc","Data/.gitignore"], cwd=cwd)
p.wait()


p = subprocess.Popen(["git","commit","-m","add dataset version {}".format(str(dataset_version))], cwd=cwd)
p.wait()

p = subprocess.Popen(["git","tag","-a","v{}".format(str(dataset_version)),"-m","update dataset"], cwd=cwd)
p.wait()

p = subprocess.Popen(["dvc","push"], cwd=cwd)
p.wait()



