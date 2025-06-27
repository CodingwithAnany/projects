import sounddevice as sd
import wave
import numpy as np
import os
import time
from datetime import datetime

# Define storage path
samples_dir = "D:\\code\\samples"

# Ensure directory exists
if not os.path.exists(samples_dir):
    os.makedirs(samples_dir)

def record_audio(duration=60, samplerate=16000):
    """Records a 60-second audio sample and saves it properly."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{samples_dir}\\voice_sample_{timestamp}.wav"

    print(f"Starting recording: {filename}")

    # Start recording and ensure it's processed properly
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Ensure recording completes before proceeding

    # Debug: Check if data is recorded properly
    print(f"Audio data shape: {audio_data.shape}")

    # Ensure file is written correctly
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

    print(f"Saved: {filename}")

# Record **60** separate 60-second segments
for i in range(60):
    print(f"Recording {i+1}/60...")
    record_audio()

print(f"All 60 recordings saved in '{samples_dir}'.")