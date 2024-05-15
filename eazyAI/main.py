from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import inspect
import tensorflow as tf
import pandas as pd
import numpy as np

version = "1.1.4"

# +++++++++++++++++++++++++++++++++++++ MAIN HELP FUNCTION ++++++++++++++++++++++++++++++++++++++++++++++++

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
    print("2. just_plot_dataframe()")
    print("3. gen_data()")

# ==================================== DATA SET GENREATOR ==================================================

def gen_data(download=False,random=False):
    print("=" * 67)
    print("                      DATA SET GENERATOR                      ")
    print("=" * 67)
    
    data_dict = {}
    
    if random == True:
        data = pd.DataFrame(
            {
                'x': np.random.randint(15,95,size=100),
                'y': np.random.randint(95,150,size=100)
            }
        )
    else:
        while True:
            try:
                no_of_attrs = int(input("Number of attributes you want: "))
                no_of_rows = int(input("Number of rows to generate: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")


        for i in range(no_of_attrs):
            print(f"\n---------- Attribute No. {i + 1} Details ----------\n")
            name = input("Enter the name of the attribute: ")

            while True:
                try:
                    LRange = int(input("Enter lower limit range: "))
                    URange = int(input("Enter upper limit range: "))

                    if LRange < URange:
                        break
                    else:
                        print("Upper limit must be greater than lower limit. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        data_dict[name] = np.random.randint(LRange, URange, size=no_of_rows)
        data = pd.DataFrame(data_dict)
    
    print("\nSuccessfully Generated Your Data.\n")
    
    if download == True:
        name_of_file = input("Enter file name (e.g., 'example.csv'): ")
    
        data.to_csv(name_of_file, index=False)
        print(f"\n{name_of_file} File Saved Successfully.")
    
    return data

# ==================================== JUST PLOT DATA FRAME ================================================

def just_plot_dataframe(
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
        if (size == None): 
            size = 20 
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
        if size == None: 
            size = 20 
        scatter = axis.scatter(Data[0], Data[1], Data[2], s = size ,c = Data[3], cmap = 'plasma')
        plt.colorbar(scatter, label=Label_names[3])
        plt.savefig(save) if save else None
        axis.set_xlabel(Label_names[0])
        axis.set_ylabel(Label_names[1])
        axis.set_zlabel(Label_names[2])
        if title != None:
            axis.title(title)                                                                                                                    
        plt.show()

    else:
        print("Warning: Unable to plot more than 4 Dimension.")

# ==================================== JUST PLOT CSV FILE ==================================================

def just_plot_csv(
        file, 
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
    
    Data = pd.read_csv(file)
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
        if (size == None): 
            size = 20 
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
        if size == None: 
            size = 20 
        scatter = axis.scatter(Data[0], Data[1], Data[2], s = size ,c = Data[3], cmap = 'plasma')
        plt.colorbar(scatter, label=Label_names[3])
        plt.savefig(save) if save else None
        axis.set_xlabel(Label_names[0])
        axis.set_ylabel(Label_names[1])
        axis.set_zlabel(Label_names[2])
        if title != None:
            axis.title(title)                                                                                                                    
        plt.show()

    else:
        print("Warning: Unable to plot more than 4 Dimension.")
