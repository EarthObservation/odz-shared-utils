# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:31:20 2019
@author: ncoz

Calculate DEM from point clouds.

Workflow for running Las Tools from Python.
"""
import subprocess
from os.path import join
import multiprocessing

cores = str(multiprocessing.cpu_count()-1)


#==============================================================================
# Set Paths
#==============================================================================
# Set path to folder where LAZ files are
pth_laz = 'C:\\Users\\ncoz\\projects\\ancillary_data\\las'


#==============================================================================
# Get extents
'''
For testing the extents of the AOI are hard-coded, later they will be passed
from the main routine?
'''
#==============================================================================
aoi_xy = ['172366', '399435', '177092', '405645']


#==============================================================================
# 1\ lasindex

# Set arguments
#use_tool = 'lasindex.exe'
use_tool = 'lasindex'
# Arguments list
arg_list = [use_tool,
            '-i', join(pth_laz, '*.laz'),
            '-cores', cores]

#subprocess.run(arg_list, shell=True)
subprocess.run(arg_list)
#==============================================================================

#==============================================================================
# 2\ blast2dem - calculate DTM (5m resolution)

# Set arguments
use_tool = 'blast2dem'
out_dir = join(pth_laz, 'test')
# Arguments list (it has to be a list of STRINGS!!!)
arg_list = [use_tool,
            '-i', join(pth_laz, '*.laz'),
            '-kill', '1000',
            '-buffered', '20',
            '-step', '5',
            '-otif',
            '-odir', out_dir,
            '-odix', '"_dem_5m"',
            '-keep_class', '2', '8',
            '-keep_xy', aoi_xy[0], aoi_xy[1], aoi_xy[2], aoi_xy[3],
            '-cores', cores]

subprocess.run(arg_list)

# 2.1\ Merge and clip tif files

# 2.2\ Clean-up old files

#==============================================================================

#==============================================================================
# 3\ blast2dem - calculate Intesity

# Set arguments
use_tool = 'blast2dem'
out_dir = pth_laz
# Arguments list
arg_list = [use_tool,
            '-i', join(pth_laz, '*.laz'),
            '-kill', '1000',
            '-buffered', '20',
            '-step', '0.5',
            '-otif',
            '-odir', out_dir,
            '-odix', '"_intensity"',
            '-intensity',
            '-keep_class', '2', '8',
            '-keep_xy', aoi_xy[0], aoi_xy[1], aoi_xy[2], aoi_xy[3],
            '-cores', cores]

subprocess.run(arg_list)

# 3.1\ Merge and clip tif files

# 3.2\ Clean-up old files

#==============================================================================

# 4\ 







