import os
from datetime import datetime
from scrape_utils import scrape_and_screenshot as scrape_chapter
from ai_writer import spin_chapter
from human_review import edit_in_editor as human_review
from chromadb_manager import save_version
from rl_policy import update_score, get_ranked_versions

# 1. Try Web Scraping First
use_scrape = input("🌐 Use web scraping to get chapter? (y/n): ").strip().lower()

if use_scrape == "y":
    url = input("🔗 Enter chapter URL: ")
    chapter_input = scrape_chapter(url)
    if not chapter_input:
        print("⚠️ Scraping failed. Falling back to manual input.")
        chapter_input = input("📘 Paste the chapter text manually:\n")
else:
    chapter_input = input("📘 Paste the chapter text manually:\n")

# 2. AI Writer
print("\n✍️ Generating AI-written version...")
ai_output = spin_chapter(chapter_input, role="AI Writer")
print("\n🔹 AI Version Preview:\n", ai_output[:1000], "..." if len(ai_output) > 1000 else "")

# 3. Human Review
print("\n🧠 Launching Human Review...")
reviewed_output = human_review(ai_output)

if not reviewed_output:
    print("⚠️ Human review returned nothing. Using AI version instead.")
    reviewed_output = ai_output

print("\n🔹 Reviewed Version Preview:\n", reviewed_output[:1000], "..." if len(reviewed_output) > 1000 else "")

# 4. Save to ChromaDB
print("\n💾 Saving all versions to ChromaDB...")
now = str(datetime.now())
save_version("final_version", reviewed_output, metadata={"source": "final", "time": now})
save_version("ai_writer_output", ai_output, metadata={"source": "ai", "time": now})
save_version("user_input", chapter_input, metadata={"source": "input", "time": now})
print("✅ All versions saved to ChromaDB.\n")

# 5. RL Feedback
while True:
    feedback = input("⭐ Was the reviewed version helpful? (y/n/skip): ").strip().lower()
    if feedback == "y":
        update_score("final_version", +1)
        print("✅ Rewarded version.\n")
        break
    elif feedback == "n":
        update_score("final_version", -1)
        print("⚠️ Penalized version.\n")
        break
    elif feedback == "skip":
        break
    else:
        print("❓ Invalid input. Please type y/n/skip.")

# 6. Show Leaderboard
print("\n🏆 Most helpful versions (by user feedback):")
for doc_id, stats in get_ranked_versions().items():
    avg_score = stats['reward'] / max(stats['count'], 1)
    print(f"  - {doc_id}: {avg_score:.2f} avg (votes: {stats['count']})")