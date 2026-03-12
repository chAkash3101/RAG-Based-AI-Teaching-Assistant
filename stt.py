import whisper
import json
import os
print("Starting transcription...")
model = whisper.load_model("large-v2")

result = model.transcribe(
    "audios/1_recording1.mp3",
    task="translate",
    verbose=True,
    word_timestamps = False
)

chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks, f, indent=4)


