import whisper
import pandas as pd
from google.colab import files
from datetime import timedelta
import textwrap

# 📁 Upload audio files
uploaded = files.upload()

# 🌐 Ask user for language code
print("\n🌐 Choose language for transcription (e.g., 'en' for English, 'ta' for Tamil, 'hi' for Hindi):")
chosen_lang = input("Enter language code: ").strip()

# 🧠 Load Whisper model
model = whisper.load_model("medium")  # You can also use "small" or "large"

def format_timestamp(seconds):
    return str(timedelta(seconds=int(seconds)))

# 📜 Transcribe each file
for filename in uploaded.keys():
    print(f"\n🎧 Processing: {filename}")
    result = model.transcribe(filename, language=chosen_lang)

    print(f"🌐 Detected language: {result['language']}")
    print("📝 Transcript:")
    wrapped_text = textwrap.fill(result["text"], width=80)  # Wrap at 80 characters
    print(wrapped_text)

    # Save timestamped segments
    segments = result.get("segments", [])
    rows = [{
        "start": format_timestamp(seg["start"]),
        "end": format_timestamp(seg["end"]),
        "text": seg["text"]
    } for seg in segments]

    df = pd.DataFrame(rows)
    txt_file = filename + "_transcript.txt"
    csv_file = filename + "_segments.csv"

    with open(txt_file, "w") as f:
        f.write(result["text"])
    df.to_csv(csv_file, index=False)

    files.download(txt_file)
    files.download(csv_file)