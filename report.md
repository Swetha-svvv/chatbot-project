# Customer Support Chatbot using Local LLM (Ollama + Llama 3.2)

## 1. Introduction
The objective of this project is to build an offline customer support chatbot using Ollama and the Llama 3.2 (3B) model. The goal is to evaluate the feasibility of using a locally deployed Large Language Model (LLM) for handling e-commerce customer queries while ensuring data privacy.

This project also compares two prompt engineering techniques:
- Zero-shot prompting
- One-shot prompting

---

## 2. Methodology

### Data Preparation
A total of 20 customer queries were created by adapting realistic support queries into an e-commerce context (e.g., order tracking, returns, payments).

### Prompt Design
Two prompt templates were used:

- **Zero-shot Prompt:**  
  Contains instructions but no example.

- **One-shot Prompt:**  
  Contains instructions along with one example to guide the model.

### Evaluation Criteria
Each response was evaluated based on:

- **Relevance (1-5):** How well the response answers the query  
- **Coherence (1-5):** Clarity and grammatical correctness  
- **Helpfulness (1-5):** Practical usefulness of the response  

---

## 3. Results & Analysis

### Average Scores (Approximate)

| Method     | Relevance | Coherence | Helpfulness |
|------------|----------|-----------|-------------|
| Zero-Shot  | 4.4      | 5.0       | 3.8         |
| One-Shot   | 4.9      | 5.0       | 4.6         |

### Observations

- **One-shot prompting performed better overall**
- One-shot responses were:
  - More structured
  - More direct
  - More helpful

- Zero-shot responses often:
  - Asked for additional information instead of solving the problem
  - Were slightly less actionable

### Example Insight

- For queries like *“How do I track my order?”*:
  - Both performed well
- For queries like *“Discount code not working”*:
  - One-shot gave better structured help

---

## 4. Conclusion & Limitations

### Conclusion
The Llama 3.2 (3B) model running locally via Ollama is capable of handling basic customer support queries effectively. One-shot prompting significantly improves response quality compared to zero-shot prompting.

### Limitations

- No access to real-time order or user data  
- Occasional vague or generic responses  
- Slower performance compared to cloud-based models  

### Future Improvements

- Integrate with real database (orders, users)  
- Use Retrieval-Augmented Generation (RAG)  
- Try larger models for better accuracy  

---

## 5. Final Verdict

Local LLMs like Llama 3.2 are a **viable, privacy-safe, and cost-effective solution** for customer support automation, especially when combined with effective prompt engineering techniques.