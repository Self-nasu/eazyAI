from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import inspect
import tensorflow as tf
import pandas as pd
import numpy as np
from eazyAI.main import gen_data


def just_plot(
        X,
        Y,
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
    

    # 
    if len(X) > 1:
        X_Label_names = list(X.columns)
    X_Label_names = X.columns

    calling_frame = inspect.currentframe().f_back
    Y_Label_names = [var_name for var_name, var_value in calling_frame.f_locals.items() if var_value is Y][0]     


    if isinstance(X, pd.DataFrame) is True:
        Y = Y.values
    Y = np.transpose(Y)







    if (len(X) == 1):
        plt.scatter(X, Y, c = color, s = size, marker= shape)
        plt.savefig(save) if save else None
        plt.title(title)
        plt.xlabel(X_Label_names[0]) 
        plt.ylabel(Y_Label_names[0])
        plt.show()
            
        
    elif (len(X) == 2):
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        if (size == None): 
            size = 20 
        axis.scatter(X[0], X[1], Y[0], s= size, c = color, marker=shape)
        plt.savefig(save) if save else None
        plt.title(title)
        axis.set_xlabel(X_Label_names[0])
        axis.set_ylabel(X_Label_names[1])
        axis.set_zlabel(Y_Label_names[0])
        plt.show()

    elif (len(X) == 3):  
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        if size == None: 
            size = 20 
        scatter = axis.scatter(X[0], X[1], X[2], s = size ,c = Y[0], cmap = 'plasma')
        plt.colorbar(scatter, label=Y_Label_names[0])
        plt.savefig(save) if save else None
        axis.set_xlabel(X_Label_names[0])
        axis.set_ylabel(X_Label_names[1])
        axis.set_zlabel(X_Label_names[2])
        if title != None:
            axis.title(title)                                                                                                                    
        plt.show()

    else:
        print("Warning: Unable to plot more than 4 Dimension.")

