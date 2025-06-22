
# Automated Book Workflow

An AI-powered pipeline that automates book content generation, rewriting, reviewing, storage, and intelligent search using Google Gemini, ChromaDB, and Reinforcement Learning-based feedback.

---

## Features

- **Web Scraping**: Fetch chapter content directly from URLs (e.g. Wikisource)
- **AI Writer**: Rewrites and enhances chapter content using Google Gemini API
- **Human Reviewer Agent**: Optional review step by a second AI for quality assurance
- **Version Storage**: Save AI and reviewed outputs into ChromaDB
- **Semantic Search**: Find the most relevant version using vector search
- **RL Feedback System**: Let users upvote/downvote results to influence ranking
- **Leaderboard**: Display most helpful versions based on cumulative feedback

---

## WORKING OF THE PROJECT

### 1. Web Scraping
The project allows users to input either raw text or a URL to automatically fetch book chapters from online sources such as Wikisource. This step is handled using the Playwright library, which automates a browser instance to navigate to the webpage and extract relevant content from predefined selectors. It ensures that users can work with real, structured web data without manually copying and pasting the text. The scraped content is then passed down the pipeline for AI processing. This design simplifies content acquisition, especially for open-source literary or historical texts.

### 2. AI Writer
Once the chapter is collected (either manually or via scraping), it is passed to the AI Writer module, which uses the Google Gemini API. This module enhances the original content by improving narrative structure, flow, and clarity while maintaining the original meaning. The AI is instructed to make the text more engaging and polished for readers, serving as an automatic rewrite agent. This step is key to transforming raw content into a refined draft suitable for review, publication, or further improvement.

### 3. Human Reviewer Agent
Following the AI writing phase, an optional review module can be invoked. This human reviewer agent can be another AI layer or a logic wrapper simulating a second pass of revision. Its purpose is to simulate what a real human editor might do—such as correcting subtle flaws, rechecking context, or improving phrasing. The existence of this step enhances trust in the AI output and provides another opportunity to boost quality before final storage or publication.

### 4. Version Storage
All outputs from the different pipeline stages—original text, AI-written version, and optionally reviewed version—are stored using ChromaDB, a vector-based document storage system. This allows the system to not only archive content versions but also to index them semantically. This persistent and queryable storage makes it possible to track how content evolves over time and enables advanced search and feedback mechanisms to operate effectively.

### 5. Semantic Search
ChromaDB enables vector-based semantic search, allowing users to retrieve previously stored versions based on similarity rather than keyword matching. When a user inputs a query, it is converted into an embedding and compared against stored versions. This method ensures that even if the exact words differ, the conceptually closest matches are returned. It’s especially useful in creative writing contexts where phrasing can vary while retaining the same intent.

### 6. RL Feedback System
The system includes a reinforcement learning (RL)-inspired feedback loop, allowing users to upvote or downvote search results. Each version has an associated score stored in a local JSON (`rl_scores.json`), and this score is updated based on user feedback. Over time, this cumulative feedback influences the rank and visibility of versions returned in semantic searches. It turns passive usage into active learning, gradually optimizing the content returned to users.

### 7. Leaderboard
To provide transparency and motivation for improvement, the system includes a leaderboard view that ranks stored content based on total feedback score. This feature displays the top-performing versions and helps identify which rewritten outputs were most appreciated by users. It not only guides future content retrieval but also helps in benchmarking how AI and review steps are performing over time.

---

## Folder Structure

```
automated-book-workflow/
├── chroma_db/                  # ChromaDB persistent storage
├── output/                     # Screenshots or debug artifacts
├── ai_writer.py                # Gemini AI writer logic
├── human_review.py            # Gemini-based reviewer agent
├── scrape_utils.py            # Playwright web scraping logic
├── store_versions.py          # Manages saving versions
├── search_versions.py         # Search & feedback interaction
├── rl_policy.py               # Feedback scoring policy
├── rl_scores.json             # Scores feedback scores
├── agent_pipeline.py          # Main pipeline runner
├── test_writer.py             # Gemini writer test script
├── test_scrape.py             # Scraping test script
└── requirements.txt           # Dependencies
```

---

## Setup Instructions

1. Create Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # or use .\venv\Scripts\activate on Windows
```

2. Install Dependencies:
```bash
pip install -r requirements.txt
playwright install
```

3. Set Gemini API Key:
```bash
export GEMINI_API_KEY=key
```

---

## Usage

### Run Main Pipeline
```bash
python agent_pipeline.py
```

Choose to input text manually or provide a chapter URL to scrape.

### Search + Feedback
```bash
python search_versions.py
```



## Reinforcement Learning Feedback

User feedback is saved in `rl_scores.json` and used to influence future search result ranking.

Example:
```python
update_score(version_id, +1)  # Upvote
update_score(version_id, -1)  # Downvote
```

## Example Flow

1. User provides or scrapes chapter content
2. AI rewrites chapter via `ai_writer.py`
3. Reviewer (optional) improves it using `human_review.py`
4. All versions stored via `store_versions.py`
5. `search_versions.py` handles semantic retrieval
6. User feedback is looped back via RL

Search content, view ranked results, and provide feedback.

---

## Feedback Flow

User feedback is saved in `rl_scores.json` and affects ranking in future searches.

```bash
python edit_score.py --version_id "v1" --score 1
```

---


