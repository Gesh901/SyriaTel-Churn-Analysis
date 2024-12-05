#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(data):
    """
    Loads the data and saves the data as a datframe
    
    Parameter: The path of the data to be loaded
    
    Returns: The top  five rows of the dataframe
    
    """
    
    df = pd.read_csv(data)
    
    return df


# In[6]:


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


# In[7]:


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
    
    


# In[8]:


def boxplot(x,y,data):
    sns.boxplot(x= x, y= y, data=data)
    plt.title(f"{y} vs {x}")
    plt.show()


# In[9]:


def countplot(x,data):
    sns.countplot(x= x , hue='churn', data=data)
    plt.title(f"{x} vs churn")
    plt.show()

