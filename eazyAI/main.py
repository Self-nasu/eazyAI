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
        save = None,
        title = None,
        ):
    
    # for i in range(0,len(Data)):
    #     calling_frame = inspect.currentframe().f_back
    #     variable_name = [var_name for var_name, var_value in calling_frame.f_locals.items() if var_value is Data[i]][0]
    #     Label_names.append(variable_name)
    
    Label_names = list(Data.columns)

    if isinstance(Data, pd.DataFrame) is True:
        Data = Data.values
    Data = np.transpose(Data)

    if (len(Data) == 2):
        plt.scatter(Data[0], Data[1], c = color, s = size, marker= shape)
        plt.savefig(save) if save else None
        plt.title(title)
        plt.xlabel(Label_names[0]) 
        plt.ylabel(Label_names[1])
        plt.show()
            
        
    elif (len(Data) == 3):
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        if (size == None): size = 20 
        axis.scatter(Data[0], Data[1], Data[2], s= size, c = color, marker=shape)
        plt.savefig(save) if save else None
        plt.title(title)
        axis.set_xlabel(Label_names[0])
        axis.set_ylabel(Label_names[1])
        axis.set_zlabel(Label_names[2])
        plt.show()

    elif (len(Data) == 4):  
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        if (size == None): size = 20 
        scatter = axis.scatter(Data[0], Data[1], Data[2], s = size ,c = Data[3], cmap = 'plasma')
        plt.colorbar(scatter, label=Label_names[3])
        plt.savefig(save) if save else None
        axis.set_xlabel(Label_names[0])
        axis.set_ylabel(Label_names[1])
        axis.set_zlabel(Label_names[2])
        axis.title(title)                                                                                                                                 
        plt.show()

    else:
        print("Warning: ")

def ezhelp():
    print("=====================================================")
    print("                     EazyAI "+ version +"                  ")
    print("                Life Should be Eazy                  ")
    print("=====================================================")
    print("")
    print("Authors: Puneet Dhankar, Naman Jain")
    print("Contact us: naman.researcher@gmail.com")
    print("Github: https://github.com/Self-nasu/eazyAI")
    print("")
    print("-----------------------------------------------------")
    print("")
    print("List of function")
    print("1. ezhelp()")
    print("2. just_plot()")