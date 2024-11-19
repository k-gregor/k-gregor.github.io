import rioxarray as rxr

data = rxr.open_rasterio('completely_random_data.tif', chunks={'x': 1000, 'y': 1000})
data = data * 2
