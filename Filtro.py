import numpy as np
import librosa
import soundfile as sf
import noisereduce as nr
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# ==========================================
# 1. FUNÇÕES DO FILTRO PASSA-FAIXA
# ==========================================
def criar_filtro_passa_faixa(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def aplicar_filtro(data, lowcut, highcut, fs, order=5):
    b, a = criar_filtro_passa_faixa(lowcut, highcut, fs, order=order)
    return filtfilt(b, a, data)

# ==========================================
# 2. PROCESSAMENTO DO ÁUDIO
# ==========================================
arquivo_entrada = '263626000.wav' # Use o seu arquivo WAV aqui
arquivo_saida = 'audio_russo_espectral_limpo.wav'

print(f"Carregando o arquivo {arquivo_entrada}...")
y, taxa_amostragem = librosa.load(arquivo_entrada, sr=None)

# ETAPA A: Filtro Passa-Faixa (Corta fora dos 300Hz-3000Hz)
print("1. Aplicando Filtro Passa-Faixa (300 Hz - 3000 Hz)...")
y_filtrado = aplicar_filtro(y, 300.0, 3000.0, taxa_amostragem, order=6)

# ETAPA B: Redução de Ruído Espectral (Mata o chiado contínuo do rádio)
# stationary=True indica que o chiado do rádio é contínuo/constante
# prop_decrease=0.8 é a agressividade (80% do ruído será removido). Se distorcer a voz, abaixe para 0.6.
print("2. Aplicando Subtração Espectral de Ruído...")
y_limpo = nr.reduce_noise(y=y_filtrado, sr=taxa_amostragem, stationary=True, prop_decrease=0.8)

# ==========================================
# 3. SALVAR RESULTADO
# ==========================================
print(f"Salvando o arquivo final como {arquivo_saida}...")
sf.write(arquivo_saida, y_limpo, taxa_amostragem)


