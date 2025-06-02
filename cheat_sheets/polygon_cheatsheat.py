# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 09:47:05 2020

@author: ncoz
"""

# For test use the AOI from NL (OrthoVHR project)
#
# POLYGON ((172740 399435, 172365 405371, 176717 405646, 177093 399710, 172740 399435))
# Local CRS EPSG:28992 (Amersfoort / RD New)


#==============================================================================
# Create Shapely Poygon object
#==============================================================================
from shapely.geometry import Polygon

poly1 = Polygon([(172740, 399435),
                 (172365, 405371),
                 (176717, 405646),
                 (177093, 399710),
                 (172740, 399435)
                 ])

# Find extents/bounds in Shapely
#  ---> simpley use the bounds method on the Shapely object
#       returns a TUPLE with (minx, miny, maxx, maxy)
bounds = poly1.bounds

# A new polgon object with Coordinates of the bounding box
envelope = poly1.envelope

# Polygon coordinates in WKT (well-known-text) in STRING FORMAT
wkt1 = poly1.wkt

#==============================================================================
# Rectangular polygons using shapely
#==============================================================================
from shapely.geometry import box

# From bounds obtained with shapely
poly2 = box(bounds[0], bounds[1], bounds[2], bounds[3])
# or by manually assigning minx, miny, maxx, maxy
poly3 = box(172365, 399435, 172740, 405371)

#==============================================================================
# Create polygon from WKT string
#==============================================================================
wkt2 = 'POLYGON ((172740 399435, 172365 405371, 176717 405646, 177093 399710, 172740 399435))'

from shapely import wkt

poly4 = wkt.loads(wkt2)

#==============================================================================
# Shapely's Python Geo Interface
#==============================================================================
#from shapely.geometry import asShape, shape




#$$$$$$$$$$$$$$$
#$$ GeoPandas $$
#$$$$$$$$$$$$$$$

#==============================================================================
# Data formats
#==============================================================================
import geopandas

# GeoDataFrame (contains multiple GeoSeries),
# example imported from GeoPandas database
df_1 = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# 1\ A GeoDataFrame containing a single GeoSeries

gdf_1a = df_1[0:1] # One geometry feature in the GDF
# gdf1 = df1.loc[0:0] same as df1[0:1]
gdf_1b = df_1[0:3] # Multiple (3) geometry features in GDF

# 2\ A GeoSeries (A column containing only the geometry data)
gs_1a = gdf_1a.geometry
gs_1b = gdf_1b.geometry

# 3\ A Polygon in the GS/GDF in the Shapely format
gp_poly1 = gs_1a[0] # or gs1.iloc[0] 
gp_poly2 = gdf_1a.loc[0,'geometry']




#==============================================================================
# Creating GeoSeries and GeoDataFrame
#==============================================================================
# To create a GeoDataFrame or GeoSeries, the polygon has to be first saved
# to a Pandas' DataFrame or Series


#------------------------------------------------------------------------------
#                               GeoSeries 
#------------------------------------------------------------------------------

# OPTION A (Polygon in Shapely format):
#--------------------------------------
# To create a GeoPandas Series you need:
#   1\ Polygon in the Shapely format
#   2\ Create Pandas Series, where polygon is one of the attributes
#   3\ Assign a crs
#   4\ Convert to a GeoPandas Series
#
import geopandas
import pandas as pd
from shapely.geometry import Polygon
#======--- 1 ---======
polygon = Polygon([(172740, 399435),
                   (172365, 405371),
                   (176717, 405646),
                   (177093, 399710),
                   (172740, 399435)
                   ])
#======--- 2 ---======
pds_a = pd.Series(polygon, name='Feature')
#======--- 3 ---======
crs = {'init': 'epsg:28992'} # Amersfoort / RD New for Netherlands
#======--- 4 ---======
gs_2a = geopandas.GeoSeries(pds_a, crs=crs)



# OPTION B (Polygon in WKT string format):
#-----------------------------------------
# To create a GeoPandas Series you need:
#   1\ Polygon in WKT string format
#   2\ Create Pandas Series
#   3\ Convert WKT to Shapely feature
#   4\ Assign a CRS
#   5\ Convert to a GeoPandas Series
#
import geopandas
import pandas as pd
from shapely import wkt
#======--- 1 ---======
polygon_b = 'POLYGON ((172740 399435, 172365 405371, 176717 405646, 177093 399710, 172740 399435))'
#======--- 2 ---======
pds_b = pd.Series(polygon_b, name='geometry')
#======--- 3 ---======
pds_b[0] = wkt.loads(pds_b[0])
#======--- 4 ---======
crs = {'init': 'epsg:28992'} # Amersfoort / RD New for Netherlands
#======--- 4 ---======
gs_2b = geopandas.GeoSeries(pds_b, crs=crs)



# OPTION C (Multiple polygons):
#------------------------------
# To create a GeoPandas Series you need:
#   1\ Polygon in WKT string format
#   2\ Create Pandas Series
#   3\ Convert WKT to Shapely feature
#   4\ Assign a CRS
#   5\ Convert to a GeoPandas Series
#
import geopandas
import pandas as pd
from shapely import wkt
#======--- 1 ---======
polygon_b = 'POLYGON ((172740 399435, 172365 405371, 176717 405646, 177093 399710, 172740 399435))'
polygon_c = 'POLYGON ((176717 405646, 176817 405646, 176817 405746, 176717 405746, 176717 405646))'
#======--- 2 ---======
pds_c = pd.Series([polygon_b, polygon_c], name='geometry')
#======--- 3 ---======
for i, val in enumerate(pds_c):
    pds_c[i] = wkt.loads(val)
#======--- 4 ---======
crs = {'init': 'epsg:28992'} # Amersfoort / RD New for Netherlands
#======--- 4 ---======
gs_2c = geopandas.GeoSeries(pds_c, crs=crs)




#------------------------------------------------------------------------------
#                                GeoDataFrame
#------------------------------------------------------------------------------


# OPTION A: Convert GeoSeries to GeoDataFrame and add attributes
#---------------------------------------------------------------
import geopandas
import pandas as pd
# Convert GeoSeries to GeoDataFrame
gdf_2a = geopandas.GeoDataFrame(geometry=gs_2c, crs=crs)

# Create lists (columns) to be added to the gdf
country = ['Netherlands', 'Slo']
url = ['https://fakesite.com', None]
# Insert lists as new columns
gdf_2a.insert(0, "country", country, True)
gdf_2a.insert(1, "url", url, True)


# OPTION B: Save a single GeoSeries as GeoDataFrame
#--------------------------------------------------
import geopandas
import pandas as pd
pdf_2b = pd.DataFrame({'country': ['Netherlands'],
                     'type': ['aoi'],
                     'url': ['https://fakesite.com'],
                     'Feature': gs_2a
                     })
gdf_2b = geopandas.GeoDataFrame(pdf_2b, crs=crs, geometry='Feature')


# OPTION C: Multiple rows/polygons in a GeoDataFrame
#---------------------------------------------------
import geopandas
import pandas as pd
pdf_2c = pd.DataFrame({'country': ['Netherlands','UK'],
                     'type': 2*['aoi'],
                     'url': ['https://fakesite.com',''],
                     'Feature': gs_2c
                     })
gdf_2c = geopandas.GeoDataFrame(pdf_2c, crs=crs, geometry='Feature')



#------------------------------------------------------------------------------
#                      Write GDF and GS to file
#------------------------------------------------------------------------------

# Writo to SHP:
gs_2a.to_file(".\\chtsht_polygons\\gs2a_Shapely.shp")
gs_2b.to_file(".\\chtsht_polygons\\gs2b_WKT.shp")
gs_2c.to_file(".\\chtsht_polygons\\gs2c_Multi.shp")
gdf_2a.to_file(".\\chtsht_polygons\\gdf_Multi.shp")
gdf_2b.to_file(".\\chtsht_polygons\\gdf_Single.shp")
gdf_2c.to_file(".\\chtsht_polygons\\gdf_Multi2.shp")


# WRITE to GeoJson
gs_2a.to_file(".\\chtsht_polygons\\gj_gs2a_Shapely.geojson", driver="GeoJSON")
gs_2b.to_file(".\\chtsht_polygons\\gj_gs2b_WKT.geojson", driver="GeoJSON")
gs_2c.to_file(".\\chtsht_polygons\\gj_gs2c_Multi.geojson", driver="GeoJSON")
gdf_2a.to_file(".\\chtsht_polygons\\gj_gdf_Multi.geojson", driver="GeoJSON")
gdf_2b.to_file(".\\chtsht_polygons\\gj_gdf_Single.geojson", driver="GeoJSON")
gdf_2c.to_file(".\\chtsht_polygons\\gj_gdf_Multi2.geojson", driver="GeoJSON")



#------------------------------------------------------------------------------
#                      Read from GeoJSON and SHP
#------------------------------------------------------------------------------

# ALWAYS READS TO GeoDataFrame!
gdf_3a = geopandas.read_file(".\\chtsht_polygons\\gs2a_Shapely.shp") # GeoSeries, SHP
gdf_3b = geopandas.read_file(".\\chtsht_polygons\\gj_gdf_Multi.geojson") # gdf, GeoJSON

# READ GeoJSON directly from url:
gdf_3c = geopandas.read_file('https://opendata.arcgis.com/datasets/9039d4ec38ed444587c46f8689f0435e_0.geojson')






