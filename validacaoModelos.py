import pandas as pd
import numpy as np

from PyRadioLoc.Utils.GeoUtils import GeoUtils
"""
from PyRadioLoc.Pathloss.Models import FreeSpaceModel
from PyRadioLoc.Pathloss.Models import FlatEarthModel
from PyRadioLoc.Pathloss.Models import LeeModel
from PyRadioLoc.Pathloss.Models import EricssonModel
from PyRadioLoc.Pathloss.Models import Cost231Model
from PyRadioLoc.Pathloss.Models import Cost231HataModel
from PyRadioLoc.Pathloss.Models import OkumuraHataModel
from PyRadioLoc.Pathloss.Models import Ecc33Model
from PyRadioLoc.Pathloss.Models import SuiModel
"""

# Le os arquivos de dados
def read_input():
	erbs = pd.read_csv('dados/erbs.csv')
	measures = pd.read_csv('dados/medicoes.csv')
	return (erbs, measures)

# Calcula o pathloss para todas as erbs 
# em cada ponto de medicao e retorna um
# data frame onde cada coluna representa 
# uma erb e cada linha um ponto de medicao
def calculate_pathloss_measures(erbs, measures):
	erbs_pt = erbs['eirp'].values.reshape((1,6))
	indexes = erbs['nr'].values.reshape((1,6))[0]
	
	pathloss_dict = {}
	
	for i in range(measures.shape[0]):
		user_pr = measures.iloc[i][2:].values.reshape((1,6))
		pathloss = erbs_pt - user_pr
		pathloss_dict[i] = pathloss[0]
	
	return pd.DataFrame(data = pathloss_dict, index = indexes).T

# Calcula as distancias de cada ponto para a erb dada
def calculate_distances(erb, users_lat, users_lon):
	return GeoUtils.distanceInKm(erb['lat'], erb['lon'], users_lat, users_lon)

# Monta um dataframe com as distancias dos 
# pontos de medicao para cada uma das erbs
def distances_dataframe(erbs, measures):
	users_lat = measures['lat'].values.reshape((1,measures.shape[0]))[0]
	users_lon = measures['lon'].values.reshape((1,measures.shape[0]))[0]

	distances_dict = {}

	for i in range(erbs.shape[0]):
		distances_dict[i] = calculate_distances(erbs.iloc[i], users_lat, users_lon)

	return pd.DataFrame(data = distances_dict)



# Calcula o pathloss utilizando o modelo passado
def calculate_pathloss_models(distances, model):
	pass


def main():
	erbs, measures = read_input()
	pathloss_df = calculate_pathloss_measures(erbs, measures)
	print(distances_dataframe(erbs, measures))
	

if __name__ == '__main__':
	main()