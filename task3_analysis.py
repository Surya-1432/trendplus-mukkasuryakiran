# Task 3 - Data Analysis using Pandas & NumPy

import pandas as pd
import numpy as np
import os

print("🔹 Starting Task 3...")

# Step 1: Check cleaned folder
cleaned_folder = "cleaned"

if not os.path.exists(cleaned_folder):
    print("❌ 'cleaned/' folder not found. Run Task 2 first.")
    exit()

files = [f for f in os.listdir(cleaned_folder) if f.endswith(".csv")]

print("Files found in cleaned/:", files)

if not files:
    print("❌ No CSV files found. Run Task 2 first.")
    exit()

# Get latest file
files.sort(reverse=True)
latest_file = files[0]

file_path = os.path.join(cleaned_folder, latest_file)
print("📂 Loading file:", file_path)

# Load CSV
try:
    df = pd.read_csv(file_path)
except Exception as e:
    print("❌ Error reading CSV:", e)
    exit()

print("Total records:", len(df))


# Step 2: Analysis

print("\n🔹 Performing analysis...")

# 1. Stories per category
category_counts = df["category"].value_counts()
print("\n📊 Stories per category:\n", category_counts)

# Top category
top_category = category_counts.idxmax()
print("\n🏆 Top trending category:", top_category)


# 2. Average score per category
avg_scores = df.groupby("category")["score"].apply(np.mean)
print("\n📈 Average score per category:\n", avg_scores)


# 3. Most commented story
top_comments = df.loc[df["num_comments"].idxmax()]
print("\n💬 Most commented story:")
print(top_comments[["title", "num_comments", "category"]])


# 4. Highest scored story
top_score = df.loc[df["score"].idxmax()]
print("\n⭐ Highest scored story:")
print(top_score[["title", "score", "category"]])


# 5. Top authors
top_authors = df["author"].value_counts().head(5)
print("\n👤 Top 5 active authors:\n", top_authors)


# Step 3: Statistics

median_score = np.median(df["score"])
std_dev = np.std(df["score"])

print("\n📊 Median score:", median_score)
print("📊 Score standard deviation:", std_dev)


# Step 4: Save summary

summary_file = "analysis_summary.txt"

with open(summary_file, "w", encoding="utf-8") as f:
    f.write("TrendPulse Analysis Summary\n")
    f.write("===========================\n\n")

    f.write(f"Total Records: {len(df)}\n\n")

    f.write("Stories per category:\n")
    f.write(str(category_counts) + "\n\n")

    f.write(f"Top Category: {top_category}\n\n")

    f.write("Average score per category:\n")
    f.write(str(avg_scores) + "\n\n")

    f.write("Top Authors:\n")
    f.write(str(top_authors) + "\n\n")

    f.write(f"Median Score: {median_score}\n")
    f.write(f"Std Deviation: {std_dev}\n")

print("\n✅ Analysis saved to analysis_summary.txt")
print("🎉 Task 3 completed successfully!")