"""
13/01/2021

Resample all rasters in given folder (default from 1m to 10m).
"""

from osgeo import gdal
import glob
from os.path import join
from os.path import splitext
from os.path import basename


def resample_raster(raster):
    out_name, e = splitext(basename(raster))
    out_raster = join(out_path, f"{out_name}_10m.tif")
    # ds = gdal.Translate(out_raster, raster, xRes=10, yRes=10, resampleAlg="bilinear", format="GTiff")
    ds = gdal.Warp(out_raster, raster, xRes=10, yRes=10, resampleAlg="bilinear", format="GTiff", targetAlignedPixels=True)


if __name__ == "__main__":
    # Folder containing tiles (*.tif) and shapes (*.shp) with the same filename
    src_path = ".//DEM_D96_1m_test//"
    out_path = ".//DEM_D96_10m//"


    # Create a list of all tiles
    tif_list = glob.glob(join(src_path, "*.tif"))

    # Run function over the entire list
    [resample_raster(raster) for raster in tif_list]

