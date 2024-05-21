from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def ez_LinearRegression(
        X,
        Y,
        split_size,
        ploting = None,
        actual_predict_ploting = None,
        normalize = None
    ):

    # labels of the attributes
    X_labels = X.columns
    Y_label = Y.name

    # changing type of variables into Pandas DataFrame
    # type casting for X
    if isinstance(X, pd.Series):
        X = X.to_frame()
    elif not isinstance(X, pd.DataFrame):
        X = pd.DataFrame(X)
    
    # type casting for Y
    if isinstance(Y, pd.Series):
        Y = Y.to_frame()
    elif not isinstance(Y, pd.DataFrame):
        Y = pd.DataFrame(Y)

    # normalizing the data
    if normalize == True:
        scalar = StandardScaler()
        X_scaled = pd.DataFrame(scalar.fit_transform(X))
    else:
        X_scaled = X
    
    # split the data
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size = split_size, random_state = 42 )

    # creating and training linear regression model
    model = LinearRegression()
    model.fit(X_train, Y_train)
           
    # predict the test set
    Y_pred_test = model.predict(X_test)
    Y_pred_train = model.predict(X_train)

    # converting these numpy arrays into pandas dataframe
    Y_pred_train = pd.DataFrame(Y_pred_train, columns=['Y_Train_prediction'])
    Y_pred_test = pd.DataFrame(Y_pred_test, columns=['Y_Test_prediction'])

    Y_predict = Y_pred_train + Y_pred_test

    # variance and bias
    if X.shape[1] == 1:
        slope = model.coef_[0]
        intercept = model.intercept_
    else:
        slope = model.coef_[0]
        intercept = model.intercept_

    # ploting regression line or plane along with scatter plot.
    if ploting == True:

        if X_scaled.shape[1] == 1:
            
            # calculating minimum and maximum of regression line to be drawn
            min_x = X_scaled.values.min()
            max_x = X_scaled.values.max()
            
            # regression line ploting
            x_values = np.linspace(min_x, max_x, 1000)
            y_values = slope * x_values + intercept
            plt.plot(x_values, y_values, color='red', label='Line: y = {}x + {}'.format(slope, intercept))
            plt.scatter(X_scaled,Y)
            plt.xlabel(X_labels[0])
            plt.ylabel(Y_label)
            plt.legend()
            plt.grid(True)
            plt.title("Regression Line")
            plt.show()

        elif X_scaled.shape[1] == 2:
            
            # calculating minimum and maximum of regression line to be drawn
            min_x1 = X_scaled[X_scaled.columns[0]].values.min()
            max_x1 = X_scaled[X_scaled.columns[0]].values.max()
            min_x2 = X_scaled[X_scaled.columns[1]].values.min()
            max_x2 = X_scaled[X_scaled.columns[1]].values.max()
            
            # regression plane
            x = np.linspace(min_x1, max_x1, 10)
            y = np.linspace(min_x2, max_x2, 10)
            x, y = np.meshgrid(x, y)
            z = intercept + slope[0] * x + slope[1] * y
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(x, y, z, alpha=0.6)
            ax.scatter(X_scaled[X_scaled.columns[0]], X_scaled[X_scaled.columns[1]], Y, c='r', marker='o')
            ax.set_xlabel(X_labels[0])
            ax.set_ylabel(X_labels[1])
            ax.set_zlabel(Y_label) 
            plt.title("Regression Plane")           
            plt.show()

        else:
            print("Warning: Unable to plot more than 3 Dimension.")

    # plotting 2 scatter plots in a graph - currently not possible with our function
    if actual_predict_ploting == True:    
        plt.scatter(Y_train, Y_pred_train, color='blue', label='Train Dataset', alpha=0.6)
        plt.scatter(Y_test, Y_pred_test, color='red', label='Test Dataset', alpha=0.6)

        plt.xlabel(f'{Y_label} predicted')
        plt.ylabel(f'{Y_label} actual')
        plt.title(f'Scatter Plots of actual and predicted {Y_label}')
        plt.grid(True)
        plt.show()

    # evaluating errors
    MAE = mean_absolute_error(Y_test, Y_pred_test)
    MSE = mean_squared_error(Y_test, Y_pred_test)
    R2 = r2_score(Y_test, Y_pred_test)

    # returning model so that user can use that trained model elsewehre
    # MSE - Mean squared error
    # MAE - Mean absolute error
    # R2 - r2 score
    return model, Y_predict, MSE, MAE, R2

