import pandas as pd
from frequency import frequency_table

"""
This function creates a helper data to test the sample script created for 
the sample solution to the Python Programmign for Data Science project.

"""

def test_sample_dataframe():
   
    # Helper data set
    data = {'Name': ['Tom', 'Jerry', 'Willow', 'Peter', 'Parker', 'Bailey' ,'Brooklyn', 'Scooby'], 
        'Age': [15, 20, 10, 5, 10, 35, 30, 28], 
        'Group': [2, 5, 3, 10, 5, 2, 5, 2], 
        'School': ['Crosby', 'Crosby', 'Bayfield', 'Crosby', 'Scarlett', 'Scarlett', 'Bayfield','Cruiser'], 
        'Ranks': ['FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH','SIXTH','SEVENTH','EIGHT']}

    helper_data = pd.DataFrame.from_dict(data)
    
    # Asset tests to check your function
    assert (frequency_table(helper_data, 'School', 'School', 'Frequency').shape[0] == 4), "incorrect output"
    assert (frequency_table(helper_data, 'Age', 'Age', 'Frequency').shape[0] == 7), "incorrect output"
    assert (frequency_table(helper_data, 'Age', 'Age', 'Frequency').max().reset_index().loc[0,0] == 35.0), "incorrect output"

    return

test_sample_dataframe()