# 🛠 Hardware e Montagem da Antena

## 1. Receptor (RTL-SDR)
Como receptor de radiofrequência, foi utilizado o **RTL-SDR Blog V3**.

## 2. Cabo Coaxial
Para a ligação entre a antena e o SDR, foi utilizado um cabo coaxial com 3 metros de comprimento e impedância característica de 50 $\Omega$.

## 3. Conectores
Foi utilizado um conector SMA Macho na extremidade do cabo para a ligação direta ao SDR.

## 4. Soldagem e Ligações
O cabo coaxial de descida para o rádio e o cabo utilizado como linha de atraso entre os dipolos foram soldados diretamente nos terminais dos elementos irradiantes.

## 5. Dipolo Cruzado e Cálculos Eletromagnéticos
Antes da montagem física, foi necessário calcular o comprimento dos elementos da antena. Como o projeto consiste em dois dipolos de meia-onda ($\lambda/2$), cada elemento individual (braço) deve possuir $1/4$ de comprimento de onda ($\lambda/4$). Dada a frequência central de interesse de 255 MHz, o comprimento de onda calcula-se por:

```math
\lambda=\frac{c}{f}=\frac{300}{255}\approx1,176\text{ metros}
```

Dividindo o comprimento de onda obtido por 4, obtemos aproximadamente 0,294 m (ou 29,4 cm).

> **Nota de projeto:** Na prática, as ondas de rádio viajam ligeiramente mais devagar em materiais condutores do que no vácuo. Aplicando um fator de encurtamento típico de 0,95 para o material utilizado, o tamanho final de corte de cada braço fixou-se em torno de **28 cm**.

**Cálculo da linha de atraso (Delay Line):**
Para que os dois dipolos captem o sinal em Polarização Circular Direita (RHCP), estes, além de cruzados geometricamente a 90 graus no espaço, precisam de possuir uma defasagem elétrica de 90 graus na fase. Esse atraso é conseguido interligando-os com um pedaço de cabo coaxial com o comprimento exato de um quarto de comprimento de onda. Como o sinal viaja mais lentamente dentro do cabo coaxial, é imperativo aplicar o Fator de Velocidade ($VF$) específico do dielétrico. Assumindo o uso de um cabo RG-58 comum (dielétrico de polietileno sólido, $VF = 0,66$):

```math
L_{cabo}=\frac{\lambda}{4}\times VF=0,294\times0,66=0,194\text{ metros}
```

Para criar o atraso de fase exato, foi cortado um trecho de cabo coaxial com **19,4 cm**. Vale salientar que o comprimento calculado refere-se apenas à porção elétrica ativa onde o cabo mantém a sua blindagem intacta (não decapada para as ligações).

## 6. Esquema de Ligação
A união dos elementos foi realizada da seguinte forma para garantir o casamento de impedância e a polarização correta:

* **Dipolo 1 (Referência):** Conectado diretamente ao cabo coaxial principal (que desce para o SDR) e também a uma das extremidades do cabo de defasagem de 19,4 cm.
* **Dipolo 2 (Atrasado):** A outra extremidade do cabo de defasagem liga-se aos terminais deste segundo dipolo, fechando o circuito.

> **Importante:** Os elementos irradiantes não podem se tocar em ponto algum, embora seja desejado o menor espaçamento entre eles. Durante a montagem, a malha dos cabos coaxiais foi soldada aos elementos definidos como "terra", e o núcleo central aos elementos de "sinal". Os elementos correspondentes (sinal com sinal) foram posicionados mecanicamente a 90 graus um do outro. Devido ao espaçamento físico necessário no centro geométrico da cruzeta para evitar curtos-circuitos, a envergadura final da antena sofreu um ligeiro incremento, o qual pode ser compensado em ajustes.
