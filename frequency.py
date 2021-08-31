import pandas as pd


def frequency_table(data, grouping_col, col1_name, col2_name):
    
    # DocString
    '''
        FUNCTION DISCRIPTION
        -----------------------

        Takes input dataframe, and finds frequency of specified group.
        Then converts frequency into percentage (ie. number of occurance to % of occurance).

        Parameters
        -------------
        data : dataframe
        This is the input dataframe that will be used for process the function

        grouping_col : string
        Name of the column what is used to build frequency table
        
        col1_name : string
        Rename of column 1 in the returned dataframe. This is rename of the column for which the frequency table is built for. 
        
        col2_name : string
        This is the name of columns where frequency values are displayed. It is for internal functional calculation. 
        Column name for the dataframe that will be returned will be called frequency_percent. 

        Returns 
        -----------
        Sample: dataframe
        Dataframe that contains frequency of identified column. Frequency is listed in percentage (i.e percentage of total). 

        Examples
        -----------
        >>>frequency_table(director_earning, 'director','Movie Director', 'Frequency')
        movies_director

    '''
    
    # Exceptions 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("You are not using a dataframe for data input.")
    
    if grouping_col not in data.columns:
        raise Exception("The column name does not exist in the dataframe.")
    
    if type(col1_name) != str:
        raise Exception("The column name must be strings.")
     
    if type(col2_name) != str:
        raise Exception("The column name must be strings.")
   
        
    # Building frequency table, and renaming columns
    freq_table = data[grouping_col].value_counts().reset_index().rename_axis('', axis='columns').rename(
        columns={'index':col1_name, grouping_col:col2_name})
    
    # Converting frequency number into frequency percentage 
    total = freq_table[col2_name].sum()
    freq_percent = freq_table.assign(frequency_percent = (freq_table[col2_name] / total) * 100 ).drop(columns = col2_name)
 
    return freq_percent
