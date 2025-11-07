from scraper import fetch_truth_posts
from sentiment import analyze_post

PROFILE_URL = "https://truthsocial.com/@realDonaldTrump"
MAX_POSTS = 2

def main():
    posts = fetch_truth_posts(PROFILE_URL, max_posts=MAX_POSTS)

    if not posts:
        print("No new posts. Waiting for the next Truth...")
        return

    print(f"\nFound {len(posts)} new post(s):\n")
    for p in posts:
        raw = p["text"]
        if raw.startswith("<p>") and raw.endswith("</p>"):
            raw = raw[3:-4]
        text = raw.replace("<br/>", "\n")
        sentiment = analyze_post(text)

        print(f"[{p['timestamp']}] (ID: {p['id']}) | Sentiment: {sentiment}\n{text}\n")
        print("-" * 80)

if __name__ == "__main__":
    main()
