import json

def save_posts_to_json(posts: list, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)
    print(f"Saved {len(posts)} post(s) to {filename}")
