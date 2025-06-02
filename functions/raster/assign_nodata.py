"""
Created on 12/01/2021
Author: Nejc Čož

Assigns nodata to pixels that lie outside the polygon bounds.

Finds all TIFF files in the folder. Shapefiles must have the same filename as the raster file!
Saves in the same folder and adds "_clipped" suffix to the end of the filename.
"""

import fiona
import rasterio
from rasterio.mask import mask
import glob
from os.path import join


def assign_nodata(raster):
    # Open shapefile
    shape = raster.replace(".tif", ".shp")
    with fiona.open(shape, "r") as shapefile:
        polygon = [feature["geometry"] for feature in shapefile]

    # Open raster and apply mask
    with rasterio.open(raster, "r") as src:
        profile = src.profile
        # Apply nodata to area outside polygon
        out_image, out_transform = mask(src, polygon)

    # Update metadata
    profile.update(
        driver="GTiff",
        compress="lzw",
        width=out_image.shape[2],
        height=out_image.shape[1],
        transform=out_transform
    )

    # Save output, append "_clipped" to filename
    output_file = raster.replace(".tif", "_clipped.tif")
    with rasterio.open(output_file, "w", **profile) as dst:
        dst.write(out_image)


if __name__ == "__main__":
    # Folder containing tiles (*.tif) and shapes (*.shp) with the same filename
    tif_folder = ".//data2"

    # Create a list of all tiles
    tif_list = glob.glob(join(tif_folder, "*.tif"))

    # Run function over the entire list
    [assign_nodata(raster) for raster in tif_list]
