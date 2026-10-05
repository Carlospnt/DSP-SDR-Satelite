## Resumo
Este projeto teve como objetivo interceptar, demodular e processar sinais de radiofrequência provindos de satélites militares em órbita geoestacionária. A antena foi projetada especificamente para operar na banda UHF (centrada em 255 MHz), apresentando excelente recepção na faixa de 253 MHz a 264 MHz, onde os sinais de interesse foram captados. Para a digitalização do sinal, foi utilizado o receptor RTL-SDR Blog V3. A varredura do espectro e a demodulação do áudio foram realizadas através do software SDR# (SDRSharp). Posteriormente, na etapa de pós-processamento, scripts em Python foram desenvolvidos para aplicar técnicas de Processamento Digital de Sinais (DSP), filtrando a banda de voz e mitigando severamente o ruído de fundo (estática).

---

##  Conceitos Iniciais

### 1. Órbita Geoestacionária
Localizada a aproximadamente 35.786 km de altitude no plano equatorial, os satélites nessa órbita possuem um plano orbital sincronizado com a Terra. Isso significa que, para um observador em solo, o satélite se manterá sempre no mesmo ponto do céu, o que evita a necessidade de sistemas mecânicos de rastreamento e permite um enlace contínuo e duradouro.

### 2. Por que Polarização Circular?
Quando um sinal de radiofrequência atravessa a ionosfera terrestre, o campo magnético da Terra rotaciona o sinal em seu plano de polarização, distorcendo severamente sinais de polarização linear (efeito de Rotação de Faraday). Ao utilizar a polarização circular, independentemente do ângulo com que o sinal chegar à antena receptora, a energia será captada de forma constante e sem perdas por desvanecimento.

### 3. A Escolha da Antena: Dipolo Cruzado (Turnstile)
Para receber sinais de polarização circular, a antena receptora não deve operar apenas com polarização linear. Por isso, e pela simplicidade de fabricação, a escolha para o projeto foi a antena de Dipolos Cruzados (*Turnstile*). O arranjo consiste em dois dipolos de meia-onda cruzados em 90 graus e interligados por um cabo coaxial. O comprimento desse cabo é rigorosamente calculado para que a defasagem do sinal entre os dipolos seja de exatamente 90º (defasagem de fase). A união espacial e temporal dessas metades casa perfeitamente com a Polarização Circular Direita (RHCP) do satélite de origem.

### 4. O que é o RTL-SDR?
O RTL-SDR é um Rádio Definido por Software (SDR). Neste projeto, ele atua como o hardware responsável por receber o sinal analógico da antena, amplificá-lo, amostrá-lo e digitalizá-lo (conversão A/D). Esse fluxo de dados brutos é então enviado via USB para o software SDR#, que realiza a sintonia fina, a demodulação matemática (NFM) e a conversão final para áudio analógico.

### 5. Pós-processamento (DSP com Python)
Devido ao baixo SNR (Relação Sinal-Ruído) inerente à comunicação espacial, um dos sinais obtidos apresentava excesso de ruído branco, acarretando a necessidade de pós-processamento via software. O áudio extraído (.wav) foi processado por um script autoral desenvolvido em Python. 
Primeiramente, o sinal passou por um Filtro Passa-Faixa (BPF) com banda de 0.3 kHz a 3 kHz para remover frequências indesejadas fora do espectro da voz humana. Em seguida, a mensagem foi submetida a um processo de Subtração Espectral (*Spectral Gating*). Essa técnica consiste em decompor o sinal em frequências (utilizando a Transformada Rápida de Fourier - FFT) para aprender a assinatura do ruído estático contínuo. O algoritmo atenua apenas as componentes de frequência do ruído detectado, retornando um áudio limpo e inteligível através da transformada inversa (iFFT).
