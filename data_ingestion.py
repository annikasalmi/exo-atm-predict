'''
This file takes in the NASA all exoplanets dataset and the IAC atmospheres dataset and combines them.
'''
import pandas as pd
import numpy as np
from datetime import datetime as dt

def combine_csvs(atm_csv_path: str, exo_csv_path: str):
    '''
    Read in CSVs, clean them, and combine them.

    Args:
        atm_csv_path (str): The path to the csv that contains data on exoplanet atmospheres
        exo_csv_path (str): The path to the csv that contains data on all the exoplanets discovered so far
    '''
    atm_df = pd.read_csv(atm_csv_path,sep=';')
    all_exo_df = pd.read_csv(exo_csv_path,sep=',')

    # clean
    all_exo_df = all_exo_df[all_exo_df.pl_controv_flag == 0]
    atm_df = atm_df[atm_df['planet_status'] == 'Confirmed']

    # remove data that is repeated in exo df
    atm_df_clean = atm_df.drop(['planet_status', 'mass', 'radius', 'orbital_period', 'semi_major_axis',
                                'star_distance', 'star_teff', 'star_radius', 'mag_v', 'mag_j', 'mag_k',
                                'alternate_names'],axis=1)
    
    dates = atm_df_clean['updated'].values
    datetime_dates = [dt.strptime(t, '%m/%d/%y') for t in dates]
    atm_df_clean['updated'] = datetime_dates

    atm_df_clean = atm_df_clean.replace({'phase_curve': {'Yes': True, 'No': False}})

    # clean the dataframe - there are multiple repeat names so combine all the data into one row/name
    atm_df_clean = atm_df_clean.groupby(['name']).agg({'type': 'first',
                                                       'star_name': 'first',
                                                       'temp_calculated': 'mean',
                                                       'scale_factor': 'mean',
                                                       'tsm': 'mean',
                                                       'esm': 'mean',
                                                       'updated': 'max',
                                                       'observation_type': ', '.join,
                                                       'reference': ', '.join,
                                                       'molecules': ', '.join,
                                                       'albedo': ', '.join,
                                                       'phase_curve': 'max',
                                                       'comments': ', '.join,
                                                       })

    # Remove repeats in "molecules" column

    all_exo_df['name'] = all_exo_df['pl_name']
    all_exo_df['star_name'] = all_exo_df['hostname']
    all_exo_df = all_exo_df.drop(['pl_name', 'hostname'],axis=1)

    # combine
    df = pd.merge(all_exo_df, atm_df_clean, how='left', left_on=['name', 'star_name'], right_on=['name', 'star_name'])

    # for some reason this ends up with too many rows. Figure out what exactly is wrong


    # remove everything with flag "pl_controv_flag"
    df = df[df.pl_controv_flag == 0]

    # remove duplicate columns that are in atm_df -> we are going to rely on the NASA stuff b/c more recent
    a=1


if __name__ == '__main__':
    atm_csv_path = 'data/iac_exoplanet_atmospheres-2024.csv'
    exo_csv_path = 'data/PSCompPars_2024.09.11_03.30.09.csv'
    combine_csvs(atm_csv_path, exo_csv_path)