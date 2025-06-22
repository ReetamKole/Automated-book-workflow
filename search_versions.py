from chromadb_manager import search_version
from rl_policy import update_score, get_ranked_versions


while True:
    query = input("\n🔍 Enter your search query (or type 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        break

    version_id, result = search_version(query)

    if result:
        print(f"\n📄 Most relevant version: {version_id}\n")
        print(result[:1000] + ("..." if len(result) > 1000 else ""))
    else:
        print("⚠️ No matching version found.")

from rl_policy import update_score

# After showing result:
feedback = input("👍 Did this help? (y/n): ").lower()
if feedback == "y":
    update_score(version_id, 1)
elif feedback == "n":
    update_score(version_id, -1)
    
    from rl_policy import get_ranked_versions

print("\n🏆 Most helpful versions (by user feedback):")
for version_id, stats in get_ranked_versions():
    avg_score = stats['reward'] / max(stats['count'], 1)
    print(f"🔹 {version_id}: {avg_score:.2f} (votes: {stats['count']})")