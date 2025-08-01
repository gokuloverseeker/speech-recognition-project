import whisper
import os

try:
    audio_files = ["/content/drive/MyDrive/Colab Notebooks/project/nothing.wav"]  # Updated path
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