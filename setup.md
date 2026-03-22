# Setup Instructions

## 1. Install Ollama

Download and install Ollama from:
https://ollama.com

Verify installation:

```
ollama --version
```

---

## 2. Pull the Model

Download the Llama 3.2 model:

```
ollama pull llama3.2:3b
```

---

## 3. Create Project Environment

Navigate to your project folder:

```
cd chatbot-project
```

Create virtual environment:

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

---

## 4. Install Required Libraries

```
pip install requests datasets
```

---

## 5. Run the Chatbot

```
python chatbot.py
```

---

## 6. Output

After running the script, results will be saved in:

```
eval/results.md
```
