# Task 2 - Data Cleaning and CSV Conversion

import json
import os
import pandas as pd
from datetime import datetime

print("🔹 Starting Task 2...")

# Step 1: Check data folder
data_folder = "data"

if not os.path.exists(data_folder):
    print("❌ 'data/' folder not found. Run Task 1 first.")
    exit()

files = [f for f in os.listdir(data_folder) if f.endswith(".json")]

print("Files found in data/:", files)

if not files:
    print("❌ No JSON files found. Run Task 1 first.")
    exit()

# Get latest file
files.sort(reverse=True)
latest_file = files[0]

file_path = os.path.join(data_folder, latest_file)
print("📂 Loading file:", file_path)

# Step 2: Load JSON
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    print("❌ Error reading JSON:", e)
    exit()

print("Total records loaded:", len(data))

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Cleaning
print("🔹 Cleaning data...")

# Remove missing title/category
df = df.dropna(subset=["title", "category"])

# Remove duplicates
df = df.drop_duplicates(subset=["post_id"])

# Fill missing values
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)
df["author"] = df["author"].fillna("unknown")

# Convert types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Clean title
df["title"] = df["title"].str.strip()

print("Records after cleaning:", len(df))

# Step 4: Save CSV
output_folder = "cleaned"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

date_str = datetime.now().strftime("%Y%m%d")
csv_file = f"{output_folder}/trends_cleaned_{date_str}.csv"

df.to_csv(csv_file, index=False)

print("✅ Cleaned data saved to:", csv_file)
print("🎉 Task 2 completed successfully!")# Task 2 - Data Cleaning and CSV Conversion

import json
import os
import pandas as pd
from datetime import datetime

print("🔹 Starting Task 2...")

# Step 1: Check data folder
data_folder = "data"

if not os.path.exists(data_folder):
    print("❌ 'data/' folder not found. Run Task 1 first.")
    exit()

files = [f for f in os.listdir(data_folder) if f.endswith(".json")]

print("Files found in data/:", files)

if not files:
    print("❌ No JSON files found. Run Task 1 first.")
    exit()

# Get latest file
files.sort(reverse=True)
latest_file = files[0]

file_path = os.path.join(data_folder, latest_file)
print("📂 Loading file:", file_path)

# Step 2: Load JSON
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    print("❌ Error reading JSON:", e)
    exit()

print("Total records loaded:", len(data))

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Cleaning
print("🔹 Cleaning data...")

# Remove missing title/category
df = df.dropna(subset=["title", "category"])

# Remove duplicates
df = df.drop_duplicates(subset=["post_id"])

# Fill missing values
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)
df["author"] = df["author"].fillna("unknown")

# Convert types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Clean title
df["title"] = df["title"].str.strip()

print("Records after cleaning:", len(df))

# Step 4: Save CSV
output_folder = "cleaned"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

date_str = datetime.now().strftime("%Y%m%d")
csv_file = f"{output_folder}/trends_cleaned_{date_str}.csv"

df.to_csv(csv_file, index=False)

print("✅ Cleaned data saved to:", csv_file)
print("🎉 Task 2 completed successfully!")