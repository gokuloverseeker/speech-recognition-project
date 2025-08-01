from ipywidgets import FileUpload, Button, Output, Dropdown
import whisper
import os

out = Output()
model = whisper.load_model("medium")

def on_button_clicked(b):
    with out:
        out.clear_output()
        for uploaded_file in upload.value:
            file_name = uploaded_file['name']
            with open(file_name, 'wb') as f:
                f.write(uploaded_file['content'])
            result = model.transcribe(file_name, language=language_dropdown.value)
            print(f"Transcribed Text for {file_name}:\n")
            print(result["text"])

upload = FileUpload(accept='.wav', multiple=True)
language_dropdown = Dropdown(options={'Tamil': 'ta', 'English': 'en', 'Hindi': 'hi'}, value='ta', description='Language:')
button = Button(description="Transcribe")
button.on_click(on_button_clicked)

display(upload)
display(language_dropdown)
display(button)
display(out)