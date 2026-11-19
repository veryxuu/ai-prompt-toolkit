
import json
from pathlib import Path

PROMPTS_FILE = Path(__file__).parent / "prompts.json"


def load_prompts():
    if not PROMPTS_FILE.exists():
        return []
    with open(PROMPTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_prompts(prompts):
    with open(PROMPTS_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, indent=2, ensure_ascii=False)


def show_prompts():
    prompts = load_prompts()
    if not prompts:
        print("No prompts found.")
        return

    for index, item in enumerate(prompts, 1):
        print(f"\n{index}. {item['title']}")
        print(item['prompt'])


def add_prompt():
    title = input("Enter prompt title: ").strip()
    prompt = input("Enter prompt text: ").strip()

    if not title or not prompt:
        print("Fields cannot be empty.")
        return

    prompts = load_prompts()
    prompts.append({"title": title, "prompt": prompt})
    save_prompts(prompts)
    print("Prompt saved successfully!")


def search_prompts():
    query = input("Search: ").strip().lower()
    results = [
        item for item in load_prompts()
        if query in item["title"].lower()
        or query in item["prompt"].lower()
    ]

    if not results:
        print("No matching prompts found.")
        return

    for item in results:
        print(f"\n{item['title']}")
        print(item['prompt'])


def delete_prompt():
    prompts = load_prompts()

    if not prompts:
        print("No prompts to delete.")
        return

    for index, item in enumerate(prompts, 1):
        print(f"{index}. {item['title']}")

    try:
        choice = int(input("Enter prompt number to delete: "))

        if choice < 1 or choice > len(prompts):
            print("Invalid prompt number.")
            return

        removed = prompts.pop(choice - 1)
        save_prompts(prompts)
        print(f"Deleted: {removed['title']}")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n==========================")
        print("      AI PROMPT TOOLKIT")
        print("==========================")
        print("1. Show all prompts")
        print("2. Add a new prompt")
        print("3. Search prompts")
        print("4. Delete a prompt")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            show_prompts()
        elif choice == "2":
            add_prompt()
        elif choice == "3":
            search_prompts()
        elif choice == "4":
            delete_prompt()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
