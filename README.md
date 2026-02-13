# Simple Recommendation System (Class Demo)

**content-based recommendation system** in Python.

- TF-IDF over item text (title + genres + overview)
- Cosine similarity for recommendations

## Run

### Install:
-pip install -r requirements.txt


### Interactive:
-python main.py

## Results 
Simple Recommendation System (content-based)
Available titles:
 - The Space Between Us
 - Quantum Heist
 - Coastal Kitchen
 - Laugh Track
 - City Sprint
 - Forest Whisper
 - Midnight Manuscript
 - Pocket Planet
 - Silent Signals
 - Retro Arcade

Choose an option:
  1) Recommend by title
  2) Recommend from free text
Enter 1 or 2: 1
How many recommendations? (default 5): Coastal Kitchen
Enter a title exactly as shown above: Coastal Kitchen
1. The Space Between Us | Sci-Fi|Romance | score=0.062
   A teen raised on Mars travels to Earth and discovers friendship and love.

2. Retro Arcade | Comedy|Family | score=0.058
   A family restores an old arcade and reconnects through games.

3. Quantum Heist | Sci-Fi|Thriller | score=0.000
   A hacker uses quantum tricks to steal data from a powerful corporation.

4. Laugh Track | Comedy | score=0.000
   A struggling comedian finds success after an unexpected viral moment.

5. City Sprint | Action|Crime | score=0.000
   A courier gets caught in a citywide chase after delivering the wrong package.
