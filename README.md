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

1) Longitude de -34.905396 a -34.885067  

2) Latitude de -8.077546 a -8.060549

* Novos limites adotados:

1) Longitude de -34.91 a -34.885 

2) Latitude de -8.080 a -8.060


## Metodologia

### Seleção do Modelo Teórico para cada ERB

Primeiramente utilizamos os modelos teóricos da biblioteca pyRadioloc para calcular o valor do pathloss em todas as medições da área de cobertura. Utilizando a raíz do erro quadrático médio (rmse) do valor estimado por cada modelo, escolhemos aquele que melhor representou cada ERB separadamente.

| ERB | Cost231HataModel | Cost231Model | Ecc33Model | EricssonModel | FlatEarth | FreeSpace |  LeeModel | OkumuraHataModel | SuiModel |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| BTS1     |    17.624943  |   79.975581 |  27.461432  |    24.931280 | 46.497849 | 27.002408  | 20.432320  |       15.038467 | 15.640246 |
| BTS2   |      16.445045  |   80.288233 |  26.454093   |   27.055422 | 45.264987 | 27.319475 | 18.842004     |    13.567555 | 14.601927 |
| BTS3   |      20.902424  |   89.334480 |  31.460972  |    41.221744 | 33.838294 | 23.447016 |  8.748844  |       16.451115 | 18.801550 |
| BTS4   |      19.571935   |  84.145123 |  30.123367  |    30.050532 | 41.737090 | 24.105663 | 16.549362  |       16.096583 | 16.630893 |
| BTS5  |       15.154986  |   79.370620 |  25.178888 |     26.031283  | 45.624992 | 28.461849 | 18.711919    |     12.336439 | 13.204896 |
| BTS6  |       12.560865  |   75.198362 |  21.643488  |    20.856594 | 49.525607 | 32.287251 |  21.857261   |      10.965627 | 11.462824 |

Na tabela observamos que o modelo de Okumura-Hata teve melhor desempenho para todas as ERBs, exceto a BTS3, na qual o modelo de Lee foi melhor. Estes modelos foram utilizados para o treinamento teórico do grid.


### Geração das coordenadas dos grids

Considerando as resoluções informadas na especificações do projeto, para a geração das coordenadas no grid, o seguinte procedimento foi adotado.


1) Conversão da altura (delta\_lat) e largura (delta\_long) do retângulo de coordenadas geográficas para cartesianas.

2) Divisão da distância obtida em Km para o delta\_lat pela resolução do grid obtendo div\_lat e divisão da distância obtida em Km para o delta\_long pela resolução do grid obtendo div\_long.

3) Divisão do delta\_lat pelo div\_lat obtendo a largura (inc\_lat) da célula unitária do grid e divisão do delta\_long pelo div\_long obtendo a altura (inc\_long) da célula do grid.

4) Interpolação da região de cobertura utilizando incrementos de tamanho inc\_lat e inc\_long nos eixos vertical e horizontal, respectivamente.

### Treino do grid teórico

Utilizando o melhor modelo teórico de pathloss para cada ERB (descrito anteriormente) calculamos o valor previsto de RSSI para cada célula do grid gerado.

### Treino do grid utilizando ML

Pra geração do grid treinado com ML foi utilizado KNN com k = 5 e com peso na distância.


### Experimento

Os modelos escolhidos para predição foram os seguintes: KNN Regressor, SVM Regressor e Random Forest Regressor.

Para o KNN foi considerado o k = 5 e com peso na distância.

Para o SVM foi realizado um processo de busca (grid search) para estimativa dos melhores valores para os parâmetros _C_ e _epsilon_.

Para o Random Forest a altura das árvores escolhidas foi 3. 

Foram usadas as seguintes combinações de dados de entradas:

* 1: Apenas medições
* 2: Apenas grid teórico
* 3: Apenas grid ML
* 4: Medições + grid teórico
* 5: Medições + grid ML
* 6: Média dos valores do grid teórico e grid ML
 

## Resultados

Para a resolução 5mx5m:

| Regressor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| KNN | 0.14446414541730232 | 0.8523449830255787 | 0.19385809020733116 | 0.18442363355325134 | 0.1944177026693642 | 0.23948646756694203 |
| SVM | 0.7564987793599119 | 0.7801965317264745 | ---  | 0.7526594630662313 | --- | 0.7795132074313813 | 
| RF | --- | --- | --- | --- | --- | --- |

Resolução 10mx10m:

| Regressor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| KNN | 144.5 | 852.0 | 203.0 | 184.4 | 194.6 | 239.4 |
| SVM | 756.5 | 779.6 | ---  | 752.9 | --- | 778.3 | 
| RF | 463.4 | 831.1 | 539.2 | 761.2 | 531.4 | 701.1 |

Resolução 20mx20m:

| Regressor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| KNN | 0.14446414541730232 | 0.8515506931041525 | 0.2233488453106654 | 0.1843372144382984 | 0.2027873970277777 | 0.24303338164279928 |
| SVM | 0.7564987793599119 | 0.7800183686718692 | 0.7273876974758953 | 0.7529093556387751 | 0.7142446465294074 | 0.7738708170783751 |
| RF | 0.46339675958731297 | 0.8243564124399828 | 0.522757530029323 | 0.6509913922545643 | 0.500203659581987 | 0.7200805314863628 |
