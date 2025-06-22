import json
import os
from collections import defaultdict

RL_DATA_PATH = "rl_scores.json"

# Load or initialize RL scores
def load_scores():
    if os.path.exists(RL_DATA_PATH):
        with open(RL_DATA_PATH, "r") as f:
            return json.load(f)
    return defaultdict(lambda: {"reward": 0, "count": 0})

def save_scores(scores):
    with open(RL_DATA_PATH, "w") as f:
        json.dump(scores, f, indent=2)

# Update score
def update_score(doc_id, reward):
    scores = load_scores()
    if doc_id not in scores:
        scores[doc_id] = {"reward": 0, "count": 0}
    scores[doc_id]["reward"] += reward
    scores[doc_id]["count"] += 1
    save_scores(scores)

# Rank by average reward
def get_ranked_versions():
    scores = load_scores()
    return sorted(scores.items(), key=lambda x: x[1]["reward"] / max(x[1]["count"], 1), reverse=True)
