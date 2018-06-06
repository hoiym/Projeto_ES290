# Projeto_ES290
Projeto para disciplina de Comunicações Móveis (ES290)


## TODO


* Rodar para todos os modelos para escolher o melhor e depois implementar o algoritmo de fingerprint utilizando o melhor dos modelos alem dos dados fornecidos.

* 1) descobrir formula real do path loss
* 2) roda os modelos e compara com os dados fornecidos calculando o erro quadrático médio.
* 3) calcular o erro quadrático para cada erb separadamente.(pode existir um modelo melhor diferente para cada erb).
* 4) Algoritmo fingerprint

## Argumentos

* Podemos assumir que a região de cobertura tem formato retangular, pois os lados paralelos possuem tamanhos semelhantes.

* No conjunto de dados de treinamento, percebe-se que há 345 instâncias com valores da latitude maiores do que o limite superior de -8.065 especificado e há 94  instâncias com valores da longitude maiores do que o limite superior de -34.887.

* Dos dados de treinamento, nota-se os seguintes limites:
a) Longitude -34.905396 a -34.885067  
b) Latitude de -8.077546 a -8.060549

* Novos limites adotados:
a) Longitude -34.91 a -34.885 
b) Latitude de -8.080 a -8.060
