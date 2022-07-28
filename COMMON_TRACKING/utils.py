import yaml

def loadCfgParameters():

    runtime_params=None
    
    with open("parameters.yaml") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        runtime_params = yaml.load(file, Loader=yaml.FullLoader)

    return runtime_params
