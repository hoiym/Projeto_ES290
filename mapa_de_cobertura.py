import pandas as pd
import numpy as np
import math

from PyRadioLoc.Utils.GeoUtils import GeoUtils

R = 5
LAT_INI = -8.080
LNG_INI = -34.91
LAT_FIM = -8.060
LNG_FIM = -34.885

def main():
	delta_x = max(GeoUtils.distanceInKm(LAT_INI, LNG_INI, LAT_INI, LNG_FIM),
		GeoUtils.distanceInKm(LAT_FIM, LNG_INI, LAT_FIM, LNG_FIM))
	delta_y = max(GeoUtils.distanceInKm(LAT_INI, LNG_INI, LAT_FIM, LNG_INI),
		GeoUtils.distanceInKm(LAT_INI, LNG_FIM, LAT_FIM, LNG_FIM))

	n_cells_x = math.ceil((delta_x * 1000) / R)
	n_cells_y = math.ceil((delta_y * 1000) / R)

	inc_lat = (LAT_FIM - LAT_INI) / n_cells_x
	inc_lng = (LNG_FIM - LNG_INI) / n_cells_y

	print('lat,lon')

	for i in range(n_cells_x):
		for j in range(n_cells_y):
			lat = LAT_INI + i * inc_lat
			lng = LNG_INI + j * inc_lng
			print('{},{}'.format(lat, lng))


if __name__ == '__main__':
    main()