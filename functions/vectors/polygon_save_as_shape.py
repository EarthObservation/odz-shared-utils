# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:25:11 2019

@author: ncoz

Create polygon with extents and save it as shape file.

"""

from shapely.geometry import box
import geopandas as gpd
from pyproj import CRS

#Extents [xmin, ymin, xmax, ymax]
xy = [8.42433133722371, 51.9733014073156, 8.72679379375017, 52.0927310934638]

# Create polygon
polygon_geom = box(xy[0],xy[1],xy[2],xy[3])
crs = CRS.from_epsg(4326)
polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])

# Save polygon to shape file
polygon.to_file('C:\\Users\\ncoz\\ESA OrthoVHR\\aoi_DE_BF.shp', driver='ESRI Shapefile')

# EPSG:3794 is Slovenia D96
# EPSG:4326 is WGS84