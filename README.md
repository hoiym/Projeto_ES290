# Projeto_ES290
Projeto para disciplina de Comunicações Móveis (ES290)


## Roteiro 

* Área de Cobertura
* Metodologia
* Resultados

## Área de Cobertura

* Podemos assumir que a região de cobertura tem formato retangular, pois os lados paralelos possuem tamanhos semelhantes.

* No conjunto de dados de treinamento, percebe-se que há 345 instâncias com valores da latitude maiores do que o limite superior de -8.065 especificado e há 94  instâncias com valores da longitude maiores do que o limite superior de -34.887.

* Dos dados de treinamento, nota-se os seguintes limites:
a) Longitude -34.905396 a -34.885067  
b) Latitude de -8.077546 a -8.060549

* Novos limites adotados:
a) Longitude -34.91 a -34.885 
b) Latitude de -8.080 a -8.060


## Metodologia

* modelo pra erb
* geracao com grids


Primeiramente utilizamos os modelos teóricos da biblioteca pyRadioloc para calcular o valor do pathloss em todas as medições da área de cobertura. Utilizando a raíz do erro quadrático médio (rmse) do valor estimado por cada modelo, escolhemos aquele que melhor representou cada ERB separadamente.

| ERB | Cost231HataModel | Cost231Model | Ecc33Model | EricssonModel | FlatEarth | FreeSpace |  LeeModel | OkumuraHataModel | SuiModel |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| BTS1     |    17.624943  |   79.975581 |  27.461432  |    24.931280 | 46.497849 | 27.002408  | 20.432320  |       15.038467 | 15.640246 |
| BTS2   |      16.445045  |   80.288233 |  26.454093   |   27.055422 | 45.264987 | 27.319475 | 18.842004     |    13.567555 | 14.601927 |
| BTS3   |      20.902424  |   89.334480 |  31.460972  |    41.221744 | 33.838294 | 23.447016 |  8.748844  |       16.451115 | 18.801550 |
| BTS4   |      19.571935   |  84.145123 |  30.123367  |    30.050532 | 41.737090 | 24.105663 | 16.549362  |       16.096583 | 16.630893 |
| BTS5  |       15.154986  |   79.370620 |  25.178888 |     26.031283  | 45.624992 | 28.461849 | 18.711919    |     12.336439 | 13.204896 |
| BTS6  |       12.560865  |   75.198362 |  21.643488  |    20.856594 | 49.525607 | 32.287251 |  21.857261   |      10.965627 | 11.462824 |


## Resultados