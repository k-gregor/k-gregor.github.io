import rioxarray as rxr

data = rxr.open_rasterio('completely_random_data.tif')
data = data * 2
