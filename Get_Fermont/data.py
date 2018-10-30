
from urllib.request import urlretrieve
import os
import pandas as pd

FERMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fermont_data(filename='Fremont.csv', url=FERMONT_URL, force_download=False):
    """
    Download and cache the fermont data.
    @param filename: string (optional)
        location to save the data
    @param url: string (optional)
        Url used to download the data
    @force_download: boolean (optional)
        Force redownload of the data.
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data