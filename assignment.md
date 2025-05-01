# Final Assignment: DNA Sequence Analysis and API Development
### **Context:**

You have been assigned a task by an **Advanced Forensic Research Team** involved in a critical investigation into ancient alien remains. During their investigation, the team obtained a **DNA sequence generation function** and a list of ancient remains that includes data such as the **region of origin**, **age**, and **genetic data** (encoded as a sequence seed). Some of this data is incomplete and requires expert attention for cleaning and addressing missing values. Additionally, the DNA sequence generation function is **costly to run**, so efficient utilization is important.

Your goal is to build a **FastAPI server** to assist researchers in analyzing and comparing DNA sequences based on the historical data provided. By leveraging the **DNA sequence generation function** and the data on ancient remains, you will help the team uncover connections between ancient populations and their genetic similarities.

This problem requires you to draw upon knowledge across multiple domains, from data parsing and API development to data retrieval.

---

### Problem Description:

1. **Upload Ancient Remains Data:**
    - You will be provided with a CSV file containing data about **ancient remains**. Each record includes:
        - **id**: A unique identifier for each sample (e.g., "id_0001").
        - **region**: The geographic region from which the sample was obtained.
        - **age**: The age of the sample (in decades).
        - **seed**: A DNA seed value, which, when processed, generates a DNA sequence.
    
    Your first task is to create an **API endpoint** that allows the upload of this CSV file.
2. **Generate DNA Sequences:**
    - A provided **function** (see the attached python file) uses **ID**, **region**, **age**, and **seed** to generate a **DNA sequence** for each ancient remain.
    - Develop an API endpoint where users can input the **ID** of a sample. The server should return the generated **DNA sequence** by utilizing the function.
3. **DNA Sequence Comparison:**
    - The team aims to compare DNA sequences across different ancient samples to identify **genetic similarities**.
    - Create an API endpoint that allows users to request a **comparison** between two samples using their **id**. The server should compute a **similarity score** between the DNA sequences of the two samples based on the sequences' **matching motifs**.
    - You need to deliberate on how to compare between two sequences and come up with a good comparison algorithm.

4. **"Ask Me Anything" General API:**
    - The team needs a way to inquire about the server’s capabilities and functionalities.
    - Implement an **"ask me anything"** API endpoint, where users can ask **natural language questions** like:
        - "What is this server used for?"
        - "How does this API work?"
        - "What data can I upload?"
    
    You can use the **Google AI Studio** for creating free API keys for Gemini LLM or any other LLM of your choice.
    The server should respond in natural language, helping the team understand the server's capabilities and how to interact with it.
    

---

### Requirements:

1. **FastAPI HTTP Server**:
Implement the server with the following endpoints:
    - **/upload-csv/**: To upload and parse the CSV of ancient remains.
    - **/generate-sequence/**: To generate a DNA sequence based on the seed.
    - **/compare-sequences/**: To compare the DNA sequences of two samples and return their similarity.
    - **/ask-me-anything/**: To respond to natural language queries about the server’s capabilities.

---

### Deliverables:

- **FastAPI Application** with the specified endpoints.
- **Documentation** on how to run the server, upload files, and interact with the API.
- **Testable endpoints** to verify functionality.
- **Explanation** of how the DNA sequences are generated and how the comparisons work.
- **Link to GitHub repository** with the code.
- **[Desired]** Deploy over any free platform like vercel.

---

### Evaluation Criteria:

- Correctness and completeness of the FastAPI server implementation.
- Accuracy of the DNA sequence generation and comparison logic.
- The ability to handle edge cases and errors effectively.
- Integration of **natural language understanding** to handle the "ask me anything" endpoint.
- Unit testing to ensure the reliability of the application.
- Creativity and innovation in solving the problem.
- **The assignment will be assigned based on the coding skills, problem solving skills and learning skills, since the assignment has all the components.**

---

### Additional Notes:

- If you encounter any difficulties or misunderstandings while working on the assignment, feel free to reach out.
- If you are unable to complete all tasks within the given time, submit your progress and findings. The solutions you've managed to implement are valuable.

---

## Good Luck!

Remember, you are helping an **advanced forensic research team** with a crucial investigation involving **ancient DNA**. Your work could reveal significant historical connections that may have been hidden for millennia.