import os
from dotenv import load_dotenv
import truthbrush
from datetime import datetime, timedelta, timezone
import json
import time

load_dotenv()

TRUTHSOCIAL_USERNAME = os.getenv("TRUTHSOCIAL_USERNAME")
TRUTHSOCIAL_PASSWORD = os.getenv("TRUTHSOCIAL_PASSWORD")

SINCE_ID_FILE = 'last_since_id.json'

def get_last_since_id():
    try:
        with open(SINCE_ID_FILE, 'r') as f:
            return json.load(f).get('last_since_id')
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_last_since_id(since_id):
    with open(SINCE_ID_FILE, 'w') as f:
        json.dump({'last_since_id': since_id}, f)

def fetch_truth_posts(profile_url, max_posts=2):
    username = profile_url.rstrip("/").split("/")[-1].replace("@", "")
    api = truthbrush.Api(username=TRUTHSOCIAL_USERNAME, password=TRUTHSOCIAL_PASSWORD)

    last_since_id = get_last_since_id()
    created_after = datetime.now(timezone.utc) - timedelta(days=7)  # Last week

    try:
        print(f"Checking @{username} for new posts")

        statuses_gen = api.pull_statuses(
            username=username,
            created_after=created_after,
            since_id=last_since_id
        )

        posts = []
        new_last_since_id = last_since_id

        for i, s in enumerate(statuses_gen):
            if i >= max_posts:
                break

            post_id = s.get("id")
            if post_id and (new_last_since_id is None or post_id > new_last_since_id):
                new_last_since_id = post_id

            posts.append({
                "id": post_id,
                "text": s.get("content", "").strip(),
                "timestamp": s.get("created_at")
            })

        if posts and new_last_since_id != last_since_id:
            save_last_since_id(new_last_since_id)
            print(f"Updated since_id → {new_last_since_id}")

        time.sleep(1)
        return posts

    except Exception as e:
        print("Error:", str(e))
        return []

if __name__ == "__main__":
    posts = fetch_truth_posts("https://truthsocial.com/@realDonaldTrump", max_posts=2)

    if posts:
        print(f"\nFound {len(posts)} new post(s):\n")
        for p in posts:
            raw = p["text"]
            if raw.startswith("<p>") and raw.endswith("</p>"):
                raw = raw[3:-4]
            text = raw.replace("<br/>", "\n")

            print(f"[{p['timestamp']}] (ID: {p['id']})\n{text}\n")
            print("-" * 80)
    else:
        print("No new posts. Waiting for the next Truth...")