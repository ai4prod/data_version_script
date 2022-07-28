# This script is used to update a database version.

These scripts are tools to help tracking dataset version and update using automatic script


## How to use


### ONLY FIRST TIME

1) setupRepo.py -> Execute this script only the first time you initialize the tracking of your dataset. WARNING This will execute git initialization. If you execute this 

2) initDatasetTracking.py-> Use this when you want to start tracking your dataset. 


Why 2 Script?

- You need to use setupRepo.py when you start your project, even if you have not yet a full dataset to track. This is useful because you can update code to check dataset integrity and so on and only when you are ready, you can start track your dataset



### COMMON TRACKING 

Script inside this folder have to be used after initDatasetTracking.py is executed. All these scripts simplify update and retrieve different dataset version

 updateDatasetVersion.py->

 you need to specifiy incremental number for your dataset. WARNING if number is not incremental will be more difficult to retrive different dataset version.


