# Hardware e Montagem da Antena

## 1- RTL SDR 
Como receptor foi utilizado o RTL-SDR Blog V3.

## 2- Cabo coaxial 
Para conexão entre antena e SDR, foi utilizado um cabo coaxial de 3m e impedância de 50ohms.
## 3 - conector 
Apenas um conector sma j3 macho foi utilizado para conectar o cabo ao SRD.
## 4 - Materiais de solda 
O cabo coaxial que conecta as duas antenas e também o que chega no rádio foram diretamente soldados nos terminais dos elementos.
## 5 - Dipolo cruzado e cálculos
Antes de tudo, é necessário calcular o compromento dos elementos da antena, como são dois dipolos de meia onda, cada elemento individual deve possuir 1/4 
de comprimento de onda. Dada a frequência central de 255MHz, é possível calcular o comprimento de onda, por: 
$ \lambda = \frac{c}{f} = \frac{300}{255} \approx 1,176 \text{ metros} $
