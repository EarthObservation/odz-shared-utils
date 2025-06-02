# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:55:20 2019

@author: Nejc Coz
@copyright: ZRC SAZU (Novi trg 2, 1000 Ljubljana, Slovenia)

NOT FINISHED!

IDEA: procedure for extracting the files from ZIP
"""

selected = list() # set a list of files to be downloaded

# ZIP LOCATIONS
path_to_zip_file = selected[0] + '.zip'
#directory_to_extract_to = ''

# UNZIP FILES
import zipfile
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    print('Extracting the files now...')
    try:
        zip_ref.extractall()
    except ValueError:
        print('Extraction of this file failed!')
    print('Done!')

try:
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        print('Extracting the files now...')
        try:
            zip_ref.extractall()
            print('Done!')
        except ValueError:
            print('Extraction of this file failed!')
except zipfile.BadZipFile:
    print('This is not a ZIP file')