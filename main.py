import numpy as np

# --- SES VE EFEKT PARAMETRELERİ ---
MOD = "YUKSEK"  # "DUSUK", "ORTA", "YUKSEK" (Sövüş/Earrape Modu)

if MOD == "DUSUK":
    PITCH_FACTOR = 0.8
    GAIN = 3.0
elif MOD == "ORTA":
    PITCH_FACTOR = 0.7
    GAIN = 6.0
else:  # YUKSEK Modu
    PITCH_FACTOR = 0.55
    GAIN = 15.0

last_sample = 0.0
alpha = 0.85

def process_audio_chunk(audio_data):
    """
    Mikrofondan gelen PCM verisini anlık işler:
    1. Pitch Shift (Sesi Kalınlaştırma)
    2. Bass Boost & Clipping (Aşırı Ses Patlatma)
    """
    global last_sample
    
    indices = np.round(np.arange(0, len(audio_data), PITCH_FACTOR)).astype(int)
    indices = indices[indices < len(audio_data)]
    pitched = audio_data[indices]
    
    if len(pitched) < len(audio_data):
        pitched = np.pad(pitched, (0, len(audio_data) - len(pitched)), 'constant')
    else:
        pitched = pitched[:len(audio_data)]
        
    processed = np.zeros_like(pitched)
    for i in range(len(pitched)):
        curr = pitched[i]
        bass = alpha * last_sample + (1 - alpha) * curr
        last_sample = bass
        
        amp = (curr + bass * 3.5) * GAIN
        if amp > 1.0: 
            amp = 1.0
        elif amp < -1.0: 
            amp = -1.0
        processed[i] = amp
        
    return processed

if __name__ == "__main__":
    print(f"Bass & Pitch Changer Core Running [{MOD} Mode]...")
