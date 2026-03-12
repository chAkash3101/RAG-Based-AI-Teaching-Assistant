import whisper
import json
import os
print("Starting transcription...")
model = whisper.load_model("large-v2")

audios = os.listdir("audios")
for audio in audios:
    #print("Audio: ", audio)
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)


        result = model.transcribe(audio = 
            f"audios/{audio}",
            task="translate",
            verbose=True,
            word_timestamps = False
        )

        chunks = []
        for segment in result["segments"]:
            chunks.append({"number":number, "title":title, "start":segment["start"], "end":segment["end"], "text":segment["text"]})

        chunked_with_metadata = {"chunks":chunks, "text":result["text"]}

        filename = audio.replace(".mp3", "")
        with open(f"jsons/{filename}.json", "w") as f:
            json.dump(chunked_with_metadata, f)





