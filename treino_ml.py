import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsRegressor
from sklearn.multioutput import MultiOutputRegressor

def knn_grid(cells, measures):
	cells_len = len(cells)
	
	measures_data = measures.iloc[:, 0:2]
	measures_labels = measures.iloc[:, 2:]
	
	existing_pos = list(zip(measures.iloc[:, 0], measures.iloc[:, 1]))
	
	knn_reg = KNeighborsRegressor(n_neighbors=5, weights='distance')
	multi_knn_reg = MultiOutputRegressor(knn_reg).fit(measures_data, measures_labels)
	
	for i in range(cells_len):
		if (cells.iloc[i, 0], cells.iloc[i, 1]) in existing_pos:
			continue
		else:
			cur_pos = [[cells.iloc[i, 0], cells.iloc[i, 1]]]
			pred_labels = multi_knn_reg.predict(cur_pos)
			
			print('{},{},{},{},{},{},{},{}'.format(cells.iloc[i, 0], cells.iloc[i, 1],
												   pred_labels[0, 0], pred_labels[0, 1],
												   pred_labels[0, 2], pred_labels[0, 3],
												   pred_labels[0, 4], pred_labels[0, 5]))

def main():
	cells = pd.read_csv('grids/grid5.csv')
	measures = pd.read_csv('dados/medicoes.csv')
	
	print("lat,lon,RSSI_1,RSSI_2,RSSI_3,RSSI_4,RSSI_5,RSSI_6")
	
	knn_grid(cells, measures)

if __name__ == '__main__':
    main()
