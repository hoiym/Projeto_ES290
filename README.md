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
| BTS1 | 17.625 | 79.976 | 27.461 | 24.931 | 46.498 | 27.002 | 20.432 | **15.038** | 15.640 |
| BTS2 | 16.445 | 80.288 | 26.454 | 27.055 | 45.265 | 27.319 | 18.842 | **13.568** | 14.602 |
| BTS3 | 20.902 | 89.334 | 31.461 | 41.222 | 33.838 | 23.447 | **8.749** | 16.451 | 18.802 |
| BTS4 | 19.572 | 84.145 | 30.123 | 30.051 | 41.737 | 24.106 | 16.549 | **16.097** | 16.631 |
| BTS5 | 15.155 | 79.371 | 25.179 | 26.031 | 45.625 | 28.462 | 18.712 | **12.336** | 13.205 |
| BTS6 | 12.561 | 75.198 | 21.643 | 20.857 | 49.526 | 32.287 | 21.857 | **10.966** | 11.463 |

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
| KNN | **144.5** | 852.3 | 193.8 | 184.4 | 194.4 | 239.5 |
| SVM | 756.5 | 780.2 | --- | **752.6** | --- | 779.5 | 
| RF | **463.4** | 825.9 | 536.6 | 784.3 | 535.7 | 725.4 |
| KNN + SVM | **433.1** | 758.3 | --- | 452.6 | --- | 472.2 |
| KNN + RF | **291.5** | 800.9 | 324.2 | 459.8 | 326.4 | 449.9 |
| SVM + RF | **585.4** | 716.4 | --- | 681.9 | --- | 684.4 |
| KNN + SVM + RF | **428.1** | 733.1 | --- | 503.4 | --- | 509.5 |

Resolução 10mx10m:

| Regressor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| KNN | **144.5** | 852.0 | 203.0 | 184.4 | 194.6 | 239.4 |
| SVM | 756.5 | 779.6 | ---  | **752.9** | --- | 778.3 | 
| RF | **463.4** | 831.1 | 539.2 | 761.2 | 531.4 | 701.1 |
| KNN + SVM | **433.1** | 757.5 | --- | 452.7 | --- | 472.2 |
| KNN + RF | **291.5** | 802.8 | 327.4 | 450.0 | 322.5 | 438.4 |
| SVM + RF | **585.4** | 718.2 | --- | 677.4 | --- | 673.0 |
| KNN + SVM + RF | **428.1** | 734.0 | --- | 500.5 | --- | 502.5 |

Resolução 20mx20m:

| Regressor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| KNN | **144.5** | 851.6 | 223.3 | 184.3 | 202.8 | 243.0 |
| SVM | 756.5 | 780.0 | 727.4 | 752.9 | **714.2** | 773.9 |
| RF | **463.4** | 824.4 | 522.8 | 651.0 | 500.2 | 720.1 |
| KNN + SVM | --- | --- | --- | --- | --- | --- |
| KNN + RF | --- | --- | --- | --- | --- | --- |
| SVM + RF | --- | --- | --- | --- | --- | --- |
| KNN + SVM + RF | --- | --- | --- | --- | --- | --- |
