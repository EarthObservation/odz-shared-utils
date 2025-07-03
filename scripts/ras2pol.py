# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:36:13 2020

@author: ncoz
"""

import rasterio
import os
import glob
import geopandas as gpd
from shapely.geometry import box

folder = 'D:\\OrthoVHR\\data\\aoi\\08_AA_DK\\PH1A_PHR_MS__2A_20180628T103333_20180628T103336_TOU_1234_687a.DIMA'

# Set search for all TIF files in specified folder 
q = os.path.join(folder, '*.tif')
# List of all TIF files
dem_fps = glob.glob(q)
# Empty list for datafiles that will be part of mosaic
src_all = []
# Open TIF files and store them as Datasets in the created list
for fp in dem_fps:
    src = rasterio.open(fp)
    src_all.append(src)
    
bnds = src_all[0].bounds
crs = src_all[0].crs.data

polygon = box(bnds[0], bnds[1], bnds[2], bnds[3])

gs = gpd.GeoSeries(polygon, crs=crs)

# Polygon in WKT format
print(gs[0].wkt)

# Export GeoJSON
gs.to_file('aa_dk.geojson', driver='GeoJSON')


