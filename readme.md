#  DNA Sequence FastAPI Application

This FastAPI based project provides endpoints to
- Upload user data via CSV.
- Generate DNA sequences.
- Compare sequences using hash based similarity.
- Ask natural language questions about the application.
- Deployed via **Render**

---

## Live Demo

[Visit Live App on Render](https://dna-api-x8iv.onrender.com)  
[View Source Code on GitHub](https://github.com/azal17/dna_api)

---

##  Features

- **CSV Upload** for user data
- **DNA Sequence Generation** using ID, region, age, and seed
- **Sequence Comparison** with hashing and similarity score
- **Ask Me Anything** endpoint using OpenAI GPT
- **Deployed on Render**

---

##  Installation
- Clone the repository.
- Create a virtual environment.
- Install dependencies.
- Set an OpenAI API Key.
- Run the app

---

## Testable Endpoints

| Method | Endpoint                  | Description                             |
|--------|---------------------------|-----------------------------------------|
| GET    | `/`                       | Health check                            |
| POST   | `/upload-csv/`           | Upload a CSV file                       |
| GET    | `/generate-sequence/`    | Generate DNA sequence by user ID       |
| GET    | `/compare-sequences/`    | Compare DNA sequences      |
| POST   | `/ask-me-anything/`      | Ask questions     |

Tested using postman application for the above endpoints.

---
##  How Comparisons Work

- DNA sequences are generated using the s() function based on user attributes (id, region, age, seed).
- Each sequence is split into substrings of length k and are converted into hash values.
- Uses IOU for similarity score.

---

##  Project Flow
- Cleaned Dataset: Preprocessed in Google Colab (nulls/outliers removed).
- Upload: CSV uploaded via FastAPI.
- Generate: DNA sequences generated using provided s() function.
- Compare: Sequences are compared.
- AMA: "Ask Me Anything" endpoint.
- Deployed: Final app deployed on Render.

---
.

