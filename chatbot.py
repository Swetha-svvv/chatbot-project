import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# Load prompt templates
def load_template(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Query function
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "Error"

# Main function
def main():
    zero_template = load_template("prompts/zero_shot_template.txt")
    one_template = load_template("prompts/one_shot_template.txt")

    # Sample queries (we will expand later)
    queries = [
    "How do I track my order?",
    "My discount code is not working.",
    "Can I return an item?",
    "Where is my shipment?",
    "How to cancel my order?",
    "I received a damaged product, what should I do?",
    "How long does delivery take?",
    "Can I change my shipping address?",
    "I was charged twice for my order.",
    "How do I apply a coupon code?",
    "My order is delayed, what should I do?",
    "Can I exchange my item?",
    "How do I contact customer support?",
    "I forgot my account password.",
    "Why was my payment declined?",
    "Can I order without creating an account?",
    "Do you offer free shipping?",
    "How do I check my order history?",
    "Can I cancel after shipping?",
    "What payment methods do you accept?"
]

    with open("eval/results.md", "w", encoding="utf-8") as file:
        file.write("| Query # | Customer Query | Method | Response |\n")
        file.write("|---------|----------------|--------|----------|\n")

        for i, query in enumerate(queries, 1):
            print(f"Processing Query {i}...")

            zero_prompt = zero_template.replace("{query}", query)
            one_prompt = one_template.replace("{query}", query)

            zero_response = query_ollama(zero_prompt)
            one_response = query_ollama(one_prompt)

            # Write to file
            file.write(f"| {i} | {query} | Zero-Shot | {zero_response} |\n")
            file.write(f"| {i} | {query} | One-Shot | {one_response} |\n")

    print("✅ Done! Results saved in eval/results.md")

if __name__ == "__main__":
    main()