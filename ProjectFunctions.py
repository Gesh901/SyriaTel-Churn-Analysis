#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import precision_score,recall_score, accuracy_score, f1_score, roc_curve, auc
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def load_data(data):
    """
    Loads the data and saves the data as a datframe
    
    Parameter: The path of the data to be loaded
    
    Returns: The top  five rows of the dataframe
    
    """
    
    df = pd.read_csv(data)
    
    return df


# In[4]:


def describe_data(df):
    """
    Summarizes a pandas DataFrame by displaying its shape, basic information, 
    and descriptive statistics.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to be described.
        
    Returns:
        None: Prints the dataset description.
    """
    print("------------------Data Shape-------------------")
    print(df.shape)  # Rows and columns
    print("\n----------------Data Info--------------------")
    print(df.info())  # Data types and non-null counts
    print("\n----------------Data Description-------------")
    print(df.describe())  # Descriptive statistics for numerical columns


# In[6]:


def analyse_data(df):
    
    """
    Summarizes a pandas DataFrame by displaying whether it's missing values, has duplicates, 
    
    Parameters:
        df (pd.DataFrame): The DataFrame to be described.
        
    Returns:
        None: Prints the dataset description.
    """
    
    print("---------------------Missing Values-----------------")
    print(df.isnull().sum())  # Missing values per column
    
    print("\n\n ----------------Duplicates---------------------")
    print(df.duplicated(keep = False).sum())  # Missing values per column
    
    


# In[7]:


def boxplot(x,y,data):
    sns.boxplot(x= x, y= y, data=data)
    plt.title(f"{y} vs {x}")
    plt.show()


# In[8]:


def countplot(x,data):
    sns.countplot(x= x , hue='churn', data=data)
    plt.title(f"{x} vs churn")
    plt.show()


# In[9]:



def roc_auc(model, X_train, X_test, y_train, y_test):
    
    # Probability scores for test set
    y_score = model.fit(X_train,y_train).decision_function(X_test)

    # False positive rate and true positive rate
    fpr, tpr, thresholds = roc_curve(y_test,y_score)

    # Seaborn's beautiful styling
    sns.set_style('darkgrid', {'axes.facecolor': '0.9'})

    # Print AUC

    print('AUC: {}'.format(auc(fpr, tpr)))

    # Plot the ROC curve

    plt.figure(figsize=(10, 8))
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.yticks([i/20.0 for i in range(21)])
    plt.xticks([i/20.0 for i in range(21)])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic (ROC) Curve for Test Set')
    plt.legend(loc='lower right')

    plt.show()


# In[10]:


def evaluation_metrics(y_test,y_pred, model):
    
    print(f"Precision for {model} = {precision_score(y_test, y_pred)}")
    print("\n")
    print(f"Recall for {model} = {recall_score(y_test, y_pred)}")
    print("\n")
    print(f"Accuracy for {model} = {accuracy_score(y_test, y_pred)}")
    print("\n")
    print(f"F1 score for {model}  = {f1_score(y_test, y_pred)}")


# In[11]:


def confusion_matrix(y_test,y_pred):
    cnf_matrix = confusion_matrix(y_test,y_pred)
    print('Confusion Matrix:\n', cnf_matrix)
    # Visualize your confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix)
    disp.plot();
    


# In[ ]:




