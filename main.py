import whisper
import gradio as gr
import requests
import json
import sounddevice as sd
import wave
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

# Audio recording parameters
SAMPLERATE = 16000
CHANNELS = 1
DURATION = 5  # seconds
FILENAME = "recorded_audio.wav"

def record_audio():
    print("Recording...")
    audio_data = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=CHANNELS, dtype=np.int16)
    sd.wait()
    
    with wave.open(FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(SAMPLERATE)
        wf.writeframes(audio_data.tobytes())
    
    print("Recording saved as", FILENAME)
    return "Recording complete!"

# Load Whisper model
model = whisper.load_model("small")

def transcribe_audio():
    result = model.transcribe(FILENAME)
    return result["text"]

def send_single_message(message):
    api_url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 4000,
        "stream": False,
        "model": "local-model"
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}\nMake sure LM Studio is running and the API is enabled."

def text_to_speech(text):
    url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"
    headers = {
        "Authorization": "Token e55b8fff991cd4f7d4f3ce5d3670faae9e596c4a",
        "Content-Type": "application/json"
    }
    
    payload = {"text": text}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        output_file = "output_audio.mp3"
        with open(output_file, "wb") as f:
            f.write(response.content)
        
        print("Playing audio...")
        audio = AudioSegment.from_mp3(output_file)
        play(audio)
        return "Audio played successfully!"
    else:
        return f"Error: {response.status_code} - {response.text}"

def full_process():
    transcribed_text = transcribe_audio()
    response_text = send_single_message(transcribed_text)
    return text_to_speech(response_text)

# Gradio UI with improved styling
with gr.Blocks(css="body { background-color: #1e1e2e; color: white; font-family: Arial, sans-serif; }") as demo:
    gr.Markdown("# 🎤 Live Speech-to-Text and AI Response")
    gr.Markdown("### Record your voice, transcribe, and get an AI response with audio playback.")
    
    with gr.Row():
        record_btn = gr.Button("🎙️ Record", variant="primary")
        generate_btn = gr.Button("🤖 Generate Response", variant="secondary")
    
    output_text = gr.Textbox(label="Transcription & Response", interactive=False)
    
    record_btn.click(fn=record_audio, inputs=[], outputs=output_text)
    generate_btn.click(fn=full_process, inputs=[], outputs=output_text)

demo.launch(share=True,pwa=True) 
