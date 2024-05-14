from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import inspect
import tensorflow as tf
import pandas as pd
import numpy as np


def just_plot(
        Data, 
        size = None,
        color = None,
        shape = None,
        save = None, #plt.savefig
        title = None,
        label = None,
        ):
    
    Label_names = []
    
    for i in range(0,len(label)):
        calling_frame = inspect.currentframe().f_back
        variable_name = [var_name for var_name, var_value in calling_frame.f_locals.items() if var_value is label[i]][0]
        Label_names.append(variable_name)
    
    if (len(Data) == 2):
        plt.scatter(Data[0], Data[1], c = color, s = size, marker= shape)
        plt.savefig(save)
        plt.title(title)
        plt.xlabel(Label_names[0]) 
        plt.ylabel(Label_names[1])
            
        
    elif (len(Data) == 3):
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        axis.scatter(Data[0], Data[1], Data[2], s= size, c = color, marker=shape)
        plt.savefig(save)
        plt.title(title)
        axis.set_xlabel(Label_names[0])
        axis.set_ylabel(Label_names[1])
        axis.set_zlabel(Label_names[2])

    elif (len(Data) == 4):  
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        scatter = axis.scatter(Data[0], Data[1], Data[2], c = Data[3], cmap = 'plasma')
        plt.colorbar(scatter, label=Label_names[3])
        axis.set_xlabel(Label_names[0])
        axis.set_ylabel(Label_names[1])
        axis.set_zlabel(Label_names[2])
        axis.title(title)
        plt.show()
