import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests

df = joblib.load('embeddings.joblib')

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={"model": "bge-m3",
                                                                 "input": text_list})
    
    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2",
                                                                 "prompt": prompt,
                                                                 "stream": False})
    
    response= r.json()
    print(response)
    return response


incoming_query = input("Ask a question: ")
question_embedding = create_embedding([incoming_query])[0]
print(question_embedding)


#Find similarities of question _embedding with other embeddings
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding'].shape))
doc_embeddings = np.vstack(df['embedding'].values)

similarities = cosine_similarity(
    doc_embeddings,
    [question_embedding]
).flatten()

print(similarities)

top_results = 3
max_indx = similarities.argsort()[-top_results:][::-1]

print(max_indx)

new_df = df.loc[max_indx]
print(new_df[["title", "number", "text"]])

prompt = f''' Here are video chunks containing video title, video number, text in the chunk, start timestamp and end timestamp:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
------------------------------------------------------

"{incoming_query}"
User asked this question realted to the video chunks, you have to answer where the answer can  be found (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, then you can say that the answer is not found in the video chunks.
'''

with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)
# for index, item in new_df.iterrows():
#     print(index, item["title"], item["number"], item["text"], item["start"], item["end"])