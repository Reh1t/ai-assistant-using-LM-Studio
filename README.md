# Voice AI Chatbot

Welcome to the Voice AI Chatbot project! This repository contains a Python application that demonstrates a seamless voice-driven interaction by combining several cutting-edge technologies. Speak, get a transcription, receive an AI-generated response, and listen to it – all without typing a single word.

## Overview

The application performs the following tasks:

- **Voice Recording:** Uses Python libraries like `sounddevice` and `wave` to record a 5-second audio clip.
- **Transcription:** Leverages OpenAI's Whisper model to convert your speech into text.
- **AI Interaction:** Sends the transcribed text to a local AI model via LM Studio to generate a conversational response.
- **Text-to-Speech:** Utilizes Deepgram’s API to convert the AI response back into audible speech.
- **User Interface:** Provides an intuitive and styled web interface using Gradio.

## Features

- **Hands-Free Interaction:** Record your voice and get immediate AI responses without typing.
- **End-to-End Pipeline:** From recording to transcription, AI processing, and audio playback.
- **Modular Design:** Easily replace or upgrade individual components like the speech-to-text or text-to-speech services.
- **Real-Time Response:** Quick processing and playback of your spoken inputs.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or higher
- LM Studio running locally and accessible at `http://localhost:1234/v1/chat/completions`
- A Deepgram API key (the current token is hardcoded in the script; update it if needed)
- Necessary Python packages listed below

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/voice-ai-chatbot.git
   cd voice-ai-chatbot
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` is not provided, you can install the necessary packages manually:

   ```bash
   pip install whisper gradio requests sounddevice numpy pydub
   ```

4. **Ensure LM Studio and Deepgram API configurations are correct:**

   - **LM Studio:** The application sends requests to `http://localhost:1234/v1/chat/completions`. Make sure LM Studio is running and the API is enabled.
   - **Deepgram API:** Check and update the token in the code if necessary.

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Interact via the web interface:**

   - Open the URL provided by Gradio (usually `http://127.0.0.1:7860`) in your browser.
   - Click the **Record** button to capture your voice.
   - Click the **Generate Response** button to process the audio: it will transcribe your voice, generate a response using the AI model, and convert that response back to speech.

## How It Works

1. **Recording Audio:**  
   The application records a 5-second audio clip and saves it as `recorded_audio.wav`.

2. **Transcription with Whisper:**  
   The recorded audio is processed using the Whisper model to obtain a text transcription.

3. **AI Response Generation:**  
   The transcribed text is sent to LM Studio to get an AI-generated response.

4. **Text-to-Speech Conversion:**  
   The response text is converted into speech via Deepgram’s API and played back using the `pydub` library.

5. **User Interface:**  
   Gradio provides a simple yet effective UI to trigger these operations and display the transcription and AI response.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding and exploring the world of voice-driven AI!
