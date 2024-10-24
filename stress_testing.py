import whisper
import warnings


warnings.filterwarnings("ignore", category=FutureWarning)
model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")

print(result["text"])