Automated Book Workflow
An AI-powered pipeline that automates book content generation, rewriting, human review, version storage, and intelligent search using Google Gemini, ChromaDB, and Reinforcement Learning-based feedback ranking.

Features
Web Scraping: Fetch chapter content directly from URLs (e.g., Wikisource)

AI Writer: Rewrites and enhances chapter content using Google Gemini API

Human Reviewer Agent: Optional review step by a second AI for quality assurance

Version Storage: Save AI and reviewed outputs into ChromaDB

Semantic Search: Find the most relevant version using vector search

RL Feedback System: Let users upvote/downvote results to influence ranking

Leaderboard: Display most helpful versions based on cumulative feedback

Folder Structure
bash
Copy
Edit
automated-book-workflow/
│
├── chroma_db/                # ChromaDB persistent storage
├── output/                   # Screenshots or debug artifacts
│
├── ai_writer.py              # Gemini AI writer logic
├── chromadb_manager.py       # Save & search content in ChromaDB
├── human_review.py           # Gemini-based reviewer agent
├── scrape_utils.py           # Playwright web scraping logic
├── store_versions.py         # Manages saving versions
├── search_versions.py        # Search & feedback interaction
├── rl_policy.py              # Reinforcement learning policy (feedback scoring)
├── rl_scores.json            # Stores feedback scores
│
├── agent_pipeline.py         # Main pipeline runner
├── test_writer.py            # Gemini writer test script
├── test_scrape.py            # Scraping test script
│
├── requirements.txt
└── README.md
Setup Instructions
1. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
playwright install
3. Set Gemini API Key
Create a .env file or export the key manually:

bash
Copy
Edit
export GEMINI_API_KEY=your_key_here
How to Run
Run Full Pipeline
bash
Copy
Edit
python agent_pipeline.py
Options:

Paste raw chapter text manually

OR choose to scrape from a chapter URL

Run Search + Feedback
bash
Copy
Edit
python search_versions.py
Then:

Enter search queries

Provide feedback (up or down)

View top-ranked results

Reinforcement Learning Feedback
User feedback is saved in rl_scores.json and used to influence future search result ranking.

Example:

python
Copy
Edit
update_score(version_id, +1)  # Upvote
update_score(version_id, -1)  # Downvote
Example Flow
User provides or scrapes chapter content

AI rewrites chapter via ai_writer.py

Reviewer (optional) improves it using human_review.py

All versions stored via store_versions.py

search_versions.py handles semantic retrieval

User feedback is looped back via RL

TODO Suggestions
Add retry/error handling for API and scraping failures

Implement tagging and metadata for versions

Track sessions/users to improve personalization

Optional: Build a web dashboard using Flask or Streamlit

Credits
Built by Reetam Kole using:

Google Gemini

ChromaDB

Playwright

Reinforcement Learning from Human Feedback

License
MIT License
