import subprocess

# This script is used to retrieve a specific Dataset version

cwd= "../"
dataset_version=2


p = subprocess.Popen(["git","checkout","v{}".format(str(dataset_version))], cwd=cwd)
p.wait()


p = subprocess.Popen(["dvc","pull"], cwd=cwd)
p.wait()

print("RETRIEVE DATASET v{}".format(dataset_version))



