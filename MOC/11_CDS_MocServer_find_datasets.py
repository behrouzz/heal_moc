# https://astroquery.readthedocs.io/en/latest/cds/cds.html#getting-started

"""
find_datasets()
---------------
This methodsearches data-sets on the whole sky. If you want to get the MOCs
or meta-datas from some specific data-sets this is the method to use.
"""

from astroquery.cds import cds

# Example: retrieve all 'moc_access_url' of the Hubble surveys

a = cds.find_datasets(meta_data='ID=*HST*',
                      fields=['ID', 'moc_access_url'])
