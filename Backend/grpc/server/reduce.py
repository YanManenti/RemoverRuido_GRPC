import noisereduce as nr
import numpy as np

def reduce(audio_bytes: bytes, rate: int):
    # Back to np.ndarray
    audio = np.frombuffer(audio_bytes, dtype=np.int16)
    # noisereduction
    reduced_noise = nr.reduce_noise(y=audio, sr=rate)  # WORKS
    return reduced_noise.tobytes()
