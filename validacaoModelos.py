import pandas as pd
import numpy as np

from PyRadioLoc.Utils.GeoUtils import GeoUtils

from PyRadioLoc.Pathloss.Models import FreeSpaceModel
from PyRadioLoc.Pathloss.Models import FlatEarthModel
from PyRadioLoc.Pathloss.Models import LeeModel
from PyRadioLoc.Pathloss.Models import EricssonModel
from PyRadioLoc.Pathloss.Models import Cost231Model
from PyRadioLoc.Pathloss.Models import Cost231HataModel
from PyRadioLoc.Pathloss.Models import OkumuraHataModel
from PyRadioLoc.Pathloss.Models import Ecc33Model
from PyRadioLoc.Pathloss.Models import SuiModel


FREQ_ERBS = 1800

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
    indexes = erbs['nr'].values.reshape((1,6))[0]    

    distances_dict = {}

    for i in range(erbs.shape[0]):
        distances_dict[indexes[i]] = calculate_distances(erbs.iloc[i], users_lat, users_lon)

    return pd.DataFrame(data = distances_dict)

# Calcula o pathloss utilizando o modelo passado
def calculate_pathloss_model(distances, model):
    return model.pathloss(distances)

# Calcula a raiz do erro quadrático médio por
# erb do modelo em relação ao valor medido
def calculate_errors(pathloss_measures_df, pathloss_model_df):
    squaredError = ((pathloss_measures_df - pathloss_model_df) ** 2)
    rmse = squaredError.mean(axis=0) ** (0.5)

    return rmse

# Cria um dict com os modelos de pathloss
def get_models():
    return {
        'FreeSpace' : FreeSpaceModel(FREQ_ERBS),
        'FlatEarth' : FlatEarthModel(FREQ_ERBS),
        'LeeModel' : LeeModel(FREQ_ERBS),
        'EricssonModel' : EricssonModel(FREQ_ERBS, False),
        'Cost231Model' : Cost231Model(FREQ_ERBS, False),
        'Cost231HataModel' : Cost231HataModel(FREQ_ERBS, False),
        'OkumuraHataModel' : OkumuraHataModel(FREQ_ERBS, False),
        'Ecc33Model' : Ecc33Model(FREQ_ERBS, False),
        'SuiModel' : SuiModel(FREQ_ERBS, False)
    }

def main():
    erbs, measures = read_input()
    pathloss_measures_df = calculate_pathloss_measures(erbs, measures)
    distances_df = distances_dataframe(erbs, measures)
    models = get_models()
    
    errors_dict = dict()
    
    for name, model in models.items():
        pathloss_model_df = calculate_pathloss_model(distances_df, model)
        errors_dict[name] = calculate_errors(pathloss_measures_df, pathloss_model_df)

    indexes = erbs['nr'].values.reshape((1,6))[0]
    errors_df = pd.DataFrame(data = errors_dict, index = indexes)

    print(errors_df)
    


if __name__ == '__main__':
    main()