#from astroquery.cds import cds
#tbl = cds.find_datasets(meta_data='ID=*sdss*')
#df = tbl.to_pandas()
#df.to_csv('../data/sdss_datasets.csv')

import pandas as pd

cols = ['obs_description', 'moc_access_url', 'web_access_url',
        'obs_initial_fov', 'dataproduct_type', 'obs_collection',
        'obs_release_date', 'obs_label', 'ID', 'obs_regime', 'obs_title']
        

df = pd.read_csv('../data/sdss_datasets.csv')


ti = 'Sloan Digital Sky Surveys (SDSS), Release 16 (DR16) (Ahumada+, 2020) (sdss16)'

a = df[df['obs_title']==ti].iloc[0]
