import json
from pathlib import Path

PROMPTS_FILE = Path("prompts.json")


def load_prompts():
    if not PROMPTS_FILE.exists():
        return []

    with open(PROMPTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_prompts(prompts):
    with open(PROMPTS_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, indent=2, ensure_ascii=False)


def add_prompt(title, prompt):
    prompts = load_prompts()

    prompts.append({
        "title": title,
        "prompt": prompt
    })

    save_prompts(prompts)


def search_prompts(query):
    prompts = load_prompts()
    query = query.lower()

    return [
        item for item in prompts
        if query in item["title"].lower()
        or query in item["prompt"].lower()
    ]


if __name__ == "__main__":
    add_prompt(
        "Coding Assistant",
        "Help me understand and improve this piece of code."
    )

    results = search_prompts("coding")

    for item in results:
        print(f"\n{item['title']}")
        print(item["prompt"])
