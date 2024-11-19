import numpy as np
import xarray as xr
import rioxarray
from affine import Affine

# Define the dimensions and size of the data
width, height = 15000, 50000  # Size of the array
transform = Affine(0.1, 0, 10, 0, -0.1, 50)  # Create an Affine transform object

# Create a random array with completely random integers
data = np.random.randint(-1000, 1000, size=(height, width))  # Random integers in a wide range

# Create an xarray DataArray
data_array = xr.DataArray(
    data,
    dims=("y", "x"),
    coords={
        "x": np.arange(width) * transform.a + transform.c,
        "y": np.arange(height) * transform.e + transform.f,
    },
    name="completely_random_data"
)

# Set GeoTIFF metadata using rioxarray
data_array = data_array.rio.write_crs("EPSG:4326")  # Assign CRS
data_array = data_array.rio.write_transform(transform)  # Assign affine transform

# Write to a GeoTIFF file
data_array.rio.to_raster("completely_random_data.tif")

print("GeoTIFF file 'completely_random_data.tif' has been created!")
