
import json
from pathlib import Path

PROMPTS_FILE = Path(__file__).parent / "prompts.json"
EXPORT_FILE = Path(__file__).parent / "exported_prompts.txt"


def load_prompts():
    if not PROMPTS_FILE.exists():
        return []

    try:
        with open(PROMPTS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: prompts.json must contain a list.")
            return []

        return [
            item for item in data
            if isinstance(item, dict)
            and isinstance(item.get("title"), str)
            and isinstance(item.get("prompt"), str)
        ]

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load prompts: {error}")
        return []


def save_prompts(prompts):
    try:
        with open(PROMPTS_FILE, "w", encoding="utf-8") as file:
            json.dump(prompts, file, indent=2, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Could not save prompts: {error}")
        return False


def show_prompts():
    prompts = load_prompts()

    if not prompts:
        print("\nNo prompts found.")
        return

    print("\n--- SAVED PROMPTS ---")

    for index, item in enumerate(prompts, 1):
        print(f"\n{index}. {item['title']}")
        print(item["prompt"])


def add_prompt():
    title = input("\nPrompt title: ").strip()
    prompt = input("Prompt text: ").strip()

    if not title or not prompt:
        print("Title and prompt cannot be empty.")
        return

    prompts = load_prompts()
    prompts.append({"title": title, "prompt": prompt})

    if save_prompts(prompts):
        print("Prompt added successfully!")


def search_prompts():
    query = input("\nSearch query: ").strip().lower()

    if not query:
        print("Search query cannot be empty.")
        return

    prompts = load_prompts()

    results = [
        item for item in prompts
        if query in item["title"].lower()
        or query in item["prompt"].lower()
    ]

    if not results:
        print("No matching prompts found.")
        return

    print("\n--- SEARCH RESULTS ---")

    for item in results:
        print(f"\n{item['title']}")
        print(item["prompt"])


def edit_prompt():
    prompts = load_prompts()

    if not prompts:
        print("No prompts available to edit.")
        return

    for index, item in enumerate(prompts, 1):
        print(f"{index}. {item['title']}")

    try:
        choice = int(input("\nPrompt number to edit: "))

        if not 1 <= choice <= len(prompts):
            print("Invalid prompt number.")
            return

        item = prompts[choice - 1]

        print("Leave a field empty to keep its current value.")

        title = input(f"New title [{item['title']}]: ").strip()
        prompt = input("New prompt text: ").strip()

        if title:
            item["title"] = title

        if prompt:
            item["prompt"] = prompt

        if save_prompts(prompts):
            print("Prompt updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def delete_prompt():
    prompts = load_prompts()

    if not prompts:
        print("No prompts available to delete.")
        return

    for index, item in enumerate(prompts, 1):
        print(f"{index}. {item['title']}")

    try:
        choice = int(input("\nPrompt number to delete: "))

        if not 1 <= choice <= len(prompts):
            print("Invalid prompt number.")
            return

        removed = prompts.pop(choice - 1)

        if save_prompts(prompts):
            print(f"Deleted: {removed['title']}")

    except ValueError:
        print("Please enter a valid number.")


def export_prompts():
    prompts = load_prompts()

    if not prompts:
        print("No prompts available to export.")
        return

    try:
        with open(EXPORT_FILE, "w", encoding="utf-8") as file:
            for index, item in enumerate(prompts, 1):
                file.write(f"{index}. {item['title']}\n")
                file.write(f"{item['prompt']}\n\n")

        print(f"Export successful: {EXPORT_FILE.name}")

    except OSError as error:
        print(f"Export failed: {error}")


def main():
    while True:
        print("\n================================")
        print("        AI PROMPT TOOLKIT")
        print("================================")
        print("1. Show all prompts")
        print("2. Add a prompt")
        print("3. Search prompts")
        print("4. Edit a prompt")
        print("5. Delete a prompt")
        print("6. Export prompts to TXT")
        print("7. Exit")
        print("================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_prompts()
        elif choice == "2":
            add_prompt()
        elif choice == "3":
            search_prompts()
        elif choice == "4":
            edit_prompt()
        elif choice == "5":
            delete_prompt()
        elif choice == "6":
            export_prompts()
        elif choice == "7":
            print("Thank you for using AI Prompt Toolkit!")
            break
        else:
            print("Invalid option. Choose 1-7.")


if __name__ == "__main__":
    main()
