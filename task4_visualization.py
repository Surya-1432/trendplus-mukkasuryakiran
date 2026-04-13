# Task 4 - Data Visualization

import pandas as pd
import os
import matplotlib.pyplot as plt

print("🔹 Starting Task 4...")

# Step 1: Load cleaned CSV
cleaned_folder = "cleaned"

if not os.path.exists(cleaned_folder):
    print("❌ 'cleaned/' folder not found. Run Task 2 first.")
    exit()

files = [f for f in os.listdir(cleaned_folder) if f.endswith(".csv")]

print("Files found in cleaned/:", files)

if not files:
    print("❌ No CSV files found.")
    exit()

# Get latest file
files.sort(reverse=True)
latest_file = files[0]

file_path = os.path.join(cleaned_folder, latest_file)
print("📂 Loading file:", file_path)

df = pd.read_csv(file_path)

print("Total records:", len(df))


# Step 2: Create output folder
output_folder = "visuals"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# 📊 1. Bar Chart - Stories per Category
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

bar_path = f"{output_folder}/category_distribution.png"
plt.savefig(bar_path)
print("✅ Saved:", bar_path)


# 📊 2. Pie Chart - Category Distribution
plt.figure()
category_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Distribution")

pie_path = f"{output_folder}/category_pie.png"
plt.savefig(pie_path)
print("✅ Saved:", pie_path)


# 📊 3. Bar Chart - Average Score per Category
avg_scores = df.groupby("category")["score"].mean()

plt.figure()
avg_scores.plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")

avg_path = f"{output_folder}/avg_score.png"
plt.savefig(avg_path)
print("✅ Saved:", avg_path)


# 📊 4. Top 5 Authors
top_authors = df["author"].value_counts().head(5)

plt.figure()
top_authors.plot(kind="bar")
plt.title("Top 5 Active Authors")
plt.xlabel("Author")
plt.ylabel("Number of Posts")

authors_path = f"{output_folder}/top_authors.png"
plt.savefig(authors_path)
print("✅ Saved:", authors_path)


print("\n🎉 Task 4 completed successfully!")