import pandas as pd
import os 

class Dataset:
    def __init__(self, fpath='AHRF_2020-2021_SAS/AHRF2021.sas7bdat'):
        self.path = fpath
        self.data = pd.read_sas(fpath)
        self.col_names = []

        self.geo_col_names = [
        'Blank',
        'Header - FIPS St & Cty Code',
        'Entity of File',
        'Secondary Entity Of File',
        'Date of File',
        'Date of Creation',
        'File Length',
        'State Name',
        'State Name Abbreviation',
        'County Name',
        'County Name w/State Abbrev',
        'FIPS State Code',
        'FIPS County Code',
        'Census Region Code', 
        'Census Region Name',
        'Federal Region Code',
        'SSA Beneficiary Code',
        'Core Based Stat Area Code(CBSA)',
        'Core Based Stat Area Name(CBSA)',
        'CBSA Indicator Code',
        'CBSA County Status',
        'Metropolitan Division Code', 
        'Metropolitan Division Name', 
        'Combined Statistical Area Code', 
        'Combined Statistical Area Name', 
        'Rural-Urban Continuum Code', 
        'Urban Influence Code',
        'Economic-Dependent Typology Code',
        'Farming-Dependent Typology Code', 
        'Manufacturing-Dep Typology Code', 
        'Fed/St Govt-Depdnt Typology Code',
        'Recreation Typolpgy Code', 
        'Nonspecializd-Dep Typology Code', 
        'Low Education Typology Code', 
        'Low Employment Typology Code', 
        'High Poverty Typology Code', 
        'Persistent Povrty Typology Code', 
        'Persistent Child Pov Typol Code', 
        'Population Loss Typology Code', 
        'Retirement Destnatn Typlgy Code', 
        'BEA Economic Area Code', 
        'BEA Component Economc Area Code', 
        'BEA Economic Area Name', 
        'BEA Component Economc Area Name'
]

    '''
    Loads all column names rather than codes.
    colpath: (str) path to the file containing column information and lookup code.
    '''
    def load_all_names(self, colpath='AHRF_2020-2021/DOC/AHRF2020-2021'):
        f = open(colpath)
        lines = f.readlines()
        f.close()
        for i in lines[6:-3]:
            self.col_names.append(i[34:65])

        all_renamed = dict(zip(self.data.columns, self.col_names))
        self.data = self.data.rename(columns=all_renamed)

        self.data = self.data.drop(columns=['Blank'])
        

    '''
    Converts object columns from bitwise to string for processing.
    col: (str) column name.
    '''
    def dtype_organizer(self, col):
        if self.data[col].dtype == 'O':
            self.data[col] = self.data[col].astype(str)

    '''
    Quick data cleaning for string dtype columns.
    x: (str) string to be cleaned.
    '''
    def string_cleaner(self, x):
        if isinstance(x, str) != True: 
            return x
        x = x.strip('b')
        x = x.strip("'")
        return x

    '''
    Applies the dtype_organizer function.
    '''
    def apply_dtype_organizer(self):
        for i in self.data.columns[:44]: self.dtype_organizer(i)

    '''
    Applies the string_cleaner function
    '''
    def apply_string_cleaner(self):
        for i in self.data.columns[:44]: self.data[i] = self.data[i].apply(self.string_cleaner)

    '''
    Renames first 44 columns (geo columns), drops the first one
    '''
    def rename_geo(self):
        geo_renamed = dict(zip(self.data.columns[:44], self.geo_col_names))
        self.data = self.data.rename(columns=geo_renamed)

        self.data = self.data.drop(columns=['Blank'])

    '''
    Calls the dataset.
    '''
    def dataset(self):
        return self.data

    '''
    Exports data as csv.
    filename = (str) desired name of file.
    fpath = (str) path of file, default is current directory.
    '''
    def export(self, filename, fpath=''):
        if fpath == '':
            fullpath = filename
        else: 
            fullpath = '/'.join((fpath, filename))

        self.data.to_csv(fullpath, index=False, index_label=False)
