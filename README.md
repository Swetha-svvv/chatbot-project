# Offline Customer Support Chatbot (Ollama + Llama 3.2)

## 📌 Project Overview

This project implements an offline customer support chatbot using Ollama and the Llama 3.2 (3B) language model. The chatbot is designed for an e-commerce platform to handle common customer queries such as order tracking, returns, payments, and shipping.

The key goal is to demonstrate how AI can be used locally without sending any sensitive data to external servers.

---

## 🚀 Features

* Runs completely offline using Ollama
* Uses Llama 3.2 (3B) model
* Handles 20 customer support queries
* Compares Zero-shot and One-shot prompting
* Evaluates responses based on quality metrics

---

## 🧠 Technologies Used

* Python
* Ollama
* Llama 3.2 (3B)
* Requests library

---

## 📂 Project Structure

```
chatbot-project/
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
├── eval/
│   └── results.md
├── chatbot.py
├── setup.md
├── report.md
└── README.md
```

---

## ⚙️ How It Works

1. Customer queries are defined in `chatbot.py`
2. Prompt templates are loaded (zero-shot and one-shot)
3. Queries are inserted into prompts
4. Requests are sent to Ollama API (`http://localhost:11434`)
5. Llama 3.2 model generates responses
6. Results are stored in `eval/results.md`

---

## 📊 Evaluation Metrics

Each response is evaluated based on:

* **Relevance (1-5):** How well the answer matches the query
* **Coherence (1-5):** Clarity and readability
* **Helpfulness (1-5):** Practical usefulness of the response

---

## 📈 Key Findings

* One-shot prompting performs better than zero-shot prompting
* One-shot responses are more structured and helpful
* Zero-shot responses sometimes ask for more information instead of solving

---

## 🏁 Conclusion

This project demonstrates that local LLMs like Llama 3.2 can be effectively used for customer support tasks while ensuring data privacy and eliminating API costs.

---
## 👩‍💻 Author

**Swetha**  
B.Tech (CSE) Student  
Aditya College of Engineering and Technology (ACET)