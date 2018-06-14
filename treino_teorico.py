import pandas as pd
import numpy as np

from PyRadioLoc.Utils.GeoUtils import GeoUtils
import validacaoModelos as vm

from PyRadioLoc.Pathloss.Models import FreeSpaceModel
from PyRadioLoc.Pathloss.Models import FlatEarthModel
from PyRadioLoc.Pathloss.Models import LeeModel
from PyRadioLoc.Pathloss.Models import EricssonModel
from PyRadioLoc.Pathloss.Models import Cost231Model
from PyRadioLoc.Pathloss.Models import Cost231HataModel
from PyRadioLoc.Pathloss.Models import OkumuraHataModel
from PyRadioLoc.Pathloss.Models import Ecc33Model
from PyRadioLoc.Pathloss.Models import SuiModel

EIRP = 55.59

# Cria um dict com os modelos de pathloss por erb
def get_models():
    return {
        'BTS1' : vm.MODELS_DICT['OkumuraHataModel'],
        'BTS2' : vm.MODELS_DICT['OkumuraHataModel'],
        'BTS3' : vm.MODELS_DICT['LeeModel'],
        'BTS4' : vm.MODELS_DICT['OkumuraHataModel'],
        'BTS5' : vm.MODELS_DICT['OkumuraHataModel'],
        'BTS6' : vm.MODELS_DICT['OkumuraHataModel'],
    }

def main():
    cells = pd.read_csv('grids/grid20.csv')
    erbs = pd.read_csv('dados/erbs.csv')

    distances_df = vm.distances_dataframe(erbs, cells)
    models = get_models()

    pathloss_dict = dict()

    for erb_name, model in models.items():
        pathloss_dict[erb_name] = vm.calculate_pathloss_model(distances_df[erb_name].values, model)

    pathloss_df = pd.DataFrame(data = pathloss_dict)
    pathloss_df = EIRP - pathloss_df

    print("lat,lon,RSSI_1,RSSI_2,RSSI_3,RSSI_4,RSSI_5,RSSI_6")

    for i in range(len(cells)):
        print('{},{},{},{},{},{},{},{}'.format(cells.iloc[i, 0], cells.iloc[i, 1],
                                               pathloss_df.iloc[i, 0], pathloss_df.iloc[i, 1],
                                               pathloss_df.iloc[i, 2], pathloss_df.iloc[i, 3],
                                               pathloss_df.iloc[i, 4], pathloss_df.iloc[i, 5]))


if __name__ == '__main__':
    main()