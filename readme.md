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

## Endpoints

| Method | Endpoint                  | Description                             |
|--------|---------------------------|-----------------------------------------|
| GET    | `/`                       | Health check                            |
| POST   | `/upload-csv/`           | Upload a CSV file                       |
| GET    | `/generate-sequence/`    | Generate DNA sequence by user ID       |
| GET    | `/compare-sequences/`    | Compare DNA sequences      |
| POST   | `/ask-me-anything/`      | Ask questions     |

---


