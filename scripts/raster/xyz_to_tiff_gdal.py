# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:05:21 2019

@author: ncoz
"""

import rasterio
from matplotlib import pyplot

f_xyz = 'D:\\OrthoVHR\\Germany\\Haan\\dgm1_32356_5672_2_nw.xyz'

f_tif = 'D:\\OrthoVHR\\Germany\\Haan_TIF\\dgm1_32356_5672_2_nw.tif'

f_new = 'D:\\OrthoVHR\\03_AM_NL\\IMG_PH1A_PHR_MS__2A_20180708T105739_20180708T105745_TOU_1234_e9f9_R1C1.TIF'

file = rasterio.open(f_new)

print(file)

array = file.read(1)
ar2 = file.read(4)
file.shape
array.shape
array.view

pyplot.imshow(array, cmap='pink')

pyplot.show()


pyplot.imshow(ar2, cmap='pink')

pyplot.show()


file.close()

#gdal.Translate(file, f_xyz, dstSRS='EPSG:4647')


#version_num = int(gdal.VersionInfo('VERSION_NUM'))
