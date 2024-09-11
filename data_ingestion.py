'''
This file takes in the NASA all exoplanets dataset and the IAC atmospheres dataset and combines them.
'''

import pandas as pd

def combine_csvs(atm_csv_path: str, exo_csv_path: str):
    '''
    Read in CSVs, clean them, and combine them.

    Args:
        atm_csv_path (str): The path to the csv that contains data on exoplanet atmospheres
        exo_csv_path (str): The path to the csv that contains data on all the exoplanets discovered so far
    '''
    atm_df = pd.read(atm_csv_path)
    all_exo_df = pd.read(exo_csv_path)

    a=1


if __name__ == '__main__':
    atm_csv_path = 'data/iac_exoplanet_atmospheres-2024.csv'
    exo_csv_path = 'data/PSCompPars_2024.09.11_03.30.09.csv'
    combine_csvs(atm_csv_path, exo_csv_path)