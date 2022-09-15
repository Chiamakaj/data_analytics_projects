import numpy as np
import pandas as pd


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        newList = np.array(list)
        new_List = newList.reshape((3, 3))
        calculations = {'mean': [[np.mean(new_List[:,0]), np.mean(new_List[:,1]), np.mean(new_List[:,2])], [np.mean(new_List[0,:]), np.mean(new_List[1,:]), np.mean(new_List[2,:])], np.mean(new_List)], 'variance': [[np.var(new_List[:,0]), np.var(new_List[:,1]), np.var(new_List[:,2])], [np.var(new_List[0,:]), np.var(new_List[1,:]), np.var(new_List[2,:])], np.var(new_List)], 'standard deviation': [[np.std(new_List[:,0]), np.std(new_List[:,1]), np.std(new_List[:,2])], [np.std(new_List[0,:]), np.std(new_List[1,:]), np.std(new_List[2,:])], np.std(new_List)], 'max': [[np.max(new_List[:,0]), np.max(new_List[:,1]), np.max(new_List[:,2])], [np.max(new_List[0,:]), np.max(new_List[1,:]), np.max(new_List[2,:])], np.max(new_List)], 'min': [[np.min(new_List[:,0]), np.min(new_List[:,1]), np.min(new_List[:,2])], [np.min(new_List[0,:]), np.min(new_List[1,:]), np.min(new_List[2,:])], np.min(new_List)], 'sum': [[np.sum(new_List[:,0]), np.sum(new_List[:,1]), np.sum(new_List[:,2])], [np.sum(new_List[0,:]), np.sum(new_List[1,:]), np.sum(new_List[2,:])], np.sum(new_List)]}
        return(calculations)
    
    
calculate([0,1,2,3,4,5,6,7,8])