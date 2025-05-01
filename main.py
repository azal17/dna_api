import pandas as pd
from func import s
from fastapi import FastAPI, UploadFile, File, HTTPException
import io
import openai
from pydantic import BaseModel
import os



app = FastAPI()
DATA = None  

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    global DATA
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        DATA = df
        return {"message": "CSV uploaded successfully.", "rows": len(DATA)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




@app.get("/generate-sequence/")
def get_sequence(id: str):
    global DATA
    if DATA is None:
        raise HTTPException(status_code=400, detail="No data uploaded.")
    record = DATA[DATA["id"] == id]
    if record.empty:
        raise HTTPException(status_code=404, detail="ID doesn't exist.")
    
    row = record.iloc[0]
    dna = s(row["id"], row["region"], int(row["age"]), row["seed"])
    return { "id": id, "dnaseqto100": dna[:100],  "length": len(dna) }



def rhash(seq, k, base=256, mod=10**9+7):
    hashes = []
    n = len(seq)
    if n < k:
        return hashes
    current_hash = 0
    for i in range(k):
        current_hash = (current_hash * base + ord(seq[i])) % mod
    hashes.append(current_hash)

    base_k_minus_1 = pow(base, k-1, mod)

    for i in range(k, n):
        current_hash = (current_hash - ord(seq[i - k]) * base_k_minus_1) % mod
        current_hash = (current_hash * base + ord(seq[i])) % mod
        hashes.append(current_hash)
    return hashes

@app.get("/compare-sequences/")
def compare_sequences(id1: str, id2: str, k: int = 4):
    global DATA
    if DATA is None:
        raise HTTPException(status_code=400, detail="No data uploaded.")

    record1 = DATA[DATA["id"] == id1]
    record2 = DATA[DATA["id"] == id2]

    if record1.empty or record2.empty:
        raise HTTPException(status_code=404, detail="One or both IDs not found.")

    row1 = record1.iloc[0]
    row2 = record2.iloc[0]

    seq1 = s(row1["id"], row1["region"], int(row1["age"]), row1["seed"])
    seq2 = s(row2["id"], row2["region"], int(row2["age"]), row2["seed"])


    hashes1 = set(rhash(seq1, k))
    hashes2 = set(rhash(seq2, k))

    intersection = hashes1 & hashes2
    union = hashes1 | hashes2


    score = len(intersection) / len(union) if union else 0
    
    return {
        "id1": id1,
        "id2": id2,
        "similarity_score": round(score, 4),
        "common_kmers": len(intersection),
        "total_kmers_1": len(hashes1),
        "total_kmers_2": len(hashes2)
    }





class QuestionInput(BaseModel):
    question: str

openai.api_key = os.getenv("OPENAI_API_KEY")
@app.post("/ask-me-anything/")
def ask_me(input: QuestionInput):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant helping users understand this server."},
                {"role": "user", "content": input.question}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return {
            "question": input.question,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")