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
    
    Y_Label_names = Y.name
    if len(X.shape) > 1:
        X_Label_names = list(X.columns)
    else:
        X_Label_names = X.name

    print(X)

    if X.shape[1] == 1:
        plt.scatter(X, Y, c = color, s = size, marker= shape)
        plt.savefig(save) if save else None
        plt.title(title)
        plt.xlabel(X_Label_names[0]) 
        plt.ylabel(Y_Label_names[0])
        plt.show()
                  
    elif X.shape[1] == 2:
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        if size == None: 
            size = 20 
        axis.scatter(X[X.columns[0]], X[X.columns[1]], Y, s= size, c = color, marker = shape)
        plt.savefig(save) if save else None
        plt.title(title)
        axis.set_xlabel(X_Label_names[0])
        axis.set_ylabel(X_Label_names[1])
        axis.set_zlabel(Y_Label_names[0])
        plt.show()

    elif X.shape[1] == 3:  
        figure = plt.figure()
        axis = figure.add_subplot(111, projection = '3d')
        if size == None: 
            size = 20 
        scatter = axis.scatter(X[X.columns[0]], X[X.columns[1]], X[X.columns[2]], s = size, marker = shape, c = Y, cmap = 'plasma')
        plt.colorbar(scatter, label=Y_Label_names[0])
        plt.savefig(save) if save else None
        axis.set_xlabel(X_Label_names[0])
        axis.set_ylabel(X_Label_names[1])
        axis.set_zlabel(X_Label_names[2])
        if title != None:
            plt.title(title)                                                                                                                    
        plt.show()

    else:
        print("Warning: Unable to plot more than 4 Dimension.")


