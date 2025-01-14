import os
import wave
import winsound
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import pyaudio
  

def lireSon():
    audio_file = os.path.abspath("audio.wav")
    winsound.PlaySound(audio_file, winsound.SND_ALIAS)

def EnresgistrerSon():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 10
    filename = "output.wav"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    print('Start Recording ...')
    stream = p.open(format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True)
    frames = []  # Initialize array to store frames
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    print('... Finished recording')
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()




def prompt_user(response):
    prompts = {
        "réseau": "informations sur le réseau",
        "incidents": "rapporter un incident",
        "aides": "assistance",
        "menu": "menu principal",
        "principal": "menu principal"
    }

    response_lower = response.lower()
    print(response_lower)
    for keyword, prompt_text in prompts.items():
        if keyword in response_lower:
            return f"Prompt: {prompt_text}"

    return "Prompt: Unknown"

