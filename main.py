import whisper
import os

try:
    audio_files = ["/content/nothing.wav"]  # Add more files here if needed
    model = whisper.load_model("medium")

    for file in audio_files:
        if os.path.exists(file):
            result = model.transcribe(file, language='ta')
            print(f"Transcribed Text for {file}:\n")
            print(result["text"])
        else:
            print(f"File not found: {file}")
except Exception as e:
    print(f"An error occurred: {e}")