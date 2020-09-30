import argparse 
import pickle
import numpy as np
# Path entry
parser = argparse.ArgumentParser(description ="This a demo for the argparse module!")
parser.add_argument('--path',metavar = "String",type = str , nargs = "+",help = "The list of String")
arguments = parser.parse_args()
if arguments.path:
    sources=""
    for index in arguments.path:
        if index[0]=="C" or index[0]=="D" or index[0]=="E":
            sources =index+":/"
            u=1
        else:
            sources+=index+"/"
    #Read the model
    loaded_model = pickle.load(open(sources+'model.sav','rb'))
#If the path is not entered as required
else:
    parser.print_help()
#Calculate the value
def Values(data):
    data1 = data
    x = np.array(data).reshape(1,6)
    result = loaded_model.predict(x)
    if x.shape[0] == 1:
        result = result[0]
    return str(result)
    