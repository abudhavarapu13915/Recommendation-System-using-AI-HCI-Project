# Simple Recommendation System 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#1) Load data 
CSV_FILE = "movies.csv"   
K_DEFAULT = 5

df = pd.read_csv(CSV_FILE)
df.columns = [c.lower() for c in df.columns]

# basic check
for col in ("title", "genres", "overview"):
    if col not in df.columns:
        raise ValueError(f"Missing column '{col}' in movies.csv")

#2) Build the model (TF-IDF + cosine similarity) 
text = (
    df["title"].fillna("") + " " +
    df["genres"].fillna("").str.replace("|", " ", regex=False) + " " +
    df["overview"].fillna("")
)

vectorizer = TfidfVectorizer(stop_words="english")
tfidf = vectorizer.fit_transform(text)
sim_matrix = cosine_similarity(tfidf)


#3) Helper functions 
def recommend_by_title(title, k=K_DEFAULT):
    titles = df["title"].str.lower().tolist()
    t = title.strip().lower()

    if t not in titles:
        raise KeyError(f"Title not found: {title}")

    idx = titles.index(t)
    scores = list(enumerate(sim_matrix[idx]))
    scores.sort(key=lambda x: x[1], reverse=True)

    recs = []
    for j, score in scores:
        if j == idx:
            continue
        recs.append((df.iloc[j]["title"], float(score), df.iloc[j]["genres"], df.iloc[j]["overview"]))
        if len(recs) >= k:
            break
    return recs


def recommend_from_text(prompt, k=K_DEFAULT):
    prompt = (prompt or "").strip()
    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    q = vectorizer.transform([prompt])
    scores = cosine_similarity(q, tfidf).flatten()
    ranked = scores.argsort()[::-1][:k]

    return [(df.iloc[i]["title"], float(scores[i]), df.iloc[i]["genres"], df.iloc[i]["overview"]) for i in ranked]


def print_recs(recs):
    for i, (title, score, genres, overview) in enumerate(recs, 1):
        print(f"{i}. {title} | {genres} | score={score:.3f}")
        print(f"   {overview}\n")


#4) Interaction 
print("Simple Recommendation System (content-based)")
print("Available titles:")
for t in df["title"].tolist():
    print(" -", t)

print("\nChoose an option:")
print("  1) Recommend by title")
print("  2) Recommend from free text")
choice = input("Enter 1 or 2: ").strip()

k_input = input(f"How many recommendations? (default {K_DEFAULT}): ").strip()
k = int(k_input) if k_input.isdigit() else K_DEFAULT

if choice == "1":
    user_title = input("Enter a title exactly as shown above: ").strip()
    results = recommend_by_title(user_title, k)
    print_recs(results)

elif choice == "2":
    user_prompt = input("Describe what you want (e.g., 'funny family movie about games'): ").strip()
    results = recommend_from_text(user_prompt, k)
    print_recs(results)

else:
    print("Invalid choice. Please run again and enter 1 or 2.")
