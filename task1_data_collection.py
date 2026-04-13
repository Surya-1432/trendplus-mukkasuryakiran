# Student Name: Mukka Surya Kiran
# Task 1 - TrendPulse Data Collection

import requests
import json
import os
import time
from datetime import datetime

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Headers
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories with keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    title = title.lower()
    
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category

    # fallback: assign random category if no match
    import random
    return random.choice(list(categories.keys()))


# Step 1: Fetch top story IDs
try:
    print("Fetching top stories...")
    response = requests.get(TOP_STORIES_URL, headers=headers)
    response.raise_for_status()
    top_ids = response.json()[:500]
    print("Total IDs fetched:", len(top_ids))
except Exception as e:
    print("Error fetching top stories:", e)
    top_ids = []


# Storage
all_stories = []
category_counts = {cat: 0 for cat in categories}

# Timestamp
collected_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Step 2: Process each category
for category in categories:
    print(f"\n🔹 Collecting {category} stories...")

    for story_id in top_ids:
        if category_counts[category] >= 25:
            print(f"✔ Collected 25 stories for {category}")
            break

        try:
            url = ITEM_URL.format(story_id)
            res = requests.get(url, headers=headers)

            if res.status_code != 200:
                print(f"Skipping ID {story_id} (status {res.status_code})")
                continue

            story = res.json()

            if not story or "title" not in story:
                continue

            title = story["title"]
            assigned_category = get_category(title)

            # Match correct category
            if assigned_category == category:
                data = {
                    "post_id": story.get("id"),
                    "title": title,
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": collected_time
                }

                all_stories.append(data)
                category_counts[category] += 1

                print(f"Added [{category}] → {title[:60]}")

        except Exception as e:
            print(f"Failed to fetch story {story_id}: {e}")
            continue

    # Sleep AFTER each category (important)
    print("Waiting 2 seconds before next category...\n")
    time.sleep(2)


# Step 3: Save JSON
if not os.path.exists("data"):
    os.makedirs("data")

date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(all_stories, f, indent=4)

# Final output
print("\n==============================")
print(f"Collected {len(all_stories)} stories")
print(f"Saved to {file_path}")
print("==============================")