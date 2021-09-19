# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:42:21 2021

@author: Aloisius
"""

import pandas as pd

## cleaning
def cleanData(raw_data,verbose = False):
    
    ### drop rows with null values from critical columns
    df_no_null = raw_data[(raw_data['Taxi ID'].notnull()) & (raw_data['Trip Seconds'].notnull()) & (raw_data['Trip Miles'].notnull()) & (raw_data['Fare'].notnull())]
    if(verbose): 
        print("Total rows dropped to remove null = ", (raw_data.shape[0]-df_no_null.shape[0]), "(% = ", 100.0*(raw_data.shape[0]-df_no_null.shape[0])/raw_data.shape[0],")")

    ### drop rows with duration > 3 hrs, distance > 100 miles and total fare > $500
    df_no_large = df_no_null[(df_no_null['Trip Seconds'] < 10800) & (df_no_null['Trip Miles'] < 100) & (df_no_null['Fare'] < 500)]
    if(verbose): 
        print("Total rows dropped to remove large numbers = ", (df_no_null.shape[0]-df_no_large.shape[0]), "(% = ", 100.0*(df_no_null.shape[0]-df_no_large.shape[0])/raw_data.shape[0],")")
                    
    ### drop rows with duration,distance and total fare = 0
    df_no_zero = df_no_large[(df_no_large['Trip Seconds'] > 30) & (df_no_large['Trip Miles'] > 0.05) & (df_no_large['Fare'] > 3)]
    if(verbose): 
        print("Total rows dropped to remove zeroes = ", (df_no_large.shape[0]-df_no_zero.shape[0]), "(% = ", 100.0*(df_no_large.shape[0]-df_no_zero.shape[0])/raw_data.shape[0],")")
    
    ### drop extreme miles per minute (>=1)
    df_no_extreme = df_no_zero [((df_no_zero ['Trip Miles'] / df_no_zero ['Trip Seconds']*60) < 1)]
    if(verbose): 
        print("Total rows dropped to remove large Miles per Minute = ", (df_no_zero.shape[0]-df_no_extreme.shape[0]), "(% = ", 100.0*(df_no_zero.shape[0]-df_no_extreme.shape[0])/raw_data.shape[0],")")

    
    clean_data = df_no_extreme
    return clean_data