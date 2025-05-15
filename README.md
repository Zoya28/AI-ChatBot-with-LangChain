
# 🤖 AI ChatBot with LangChain & Pinecone

Welcome to your AI-powered chatbot that fetches, chunks, embeds, and retrieves data from a website sitemap using LangChain and Pinecone — all in a sleek Streamlit interface. Perfect for building a website assistant or crawling content for QA.

---

## 💡 Features

- 🔍 Scrapes data from a website's sitemap
- ✂️ Splits large documents into manageable chunks
- 🧠 Embeds data using `sentence-transformers`
- 🌲 Pushes and pulls vectors to/from Pinecone
- 🗣️ Lets users ask questions and returns the most relevant results
- 🤫 All API keys are kept secret via password input fields
- 🧃 Streamlit UI for easy interaction

---

## 🚀 Tech Stack

- **Streamlit** - UI framework
- **LangChain** - Framework for chaining NLP tasks
- **Pinecone** - Vector DB for storing and retrieving embeddings
- **Sentence Transformers** - For creating embeddings (`all-MiniLM-L6-v2`)
- **Sitemap Loader** - For scraping XML sitemap URLs

---

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Zoya28/AI-ChatBot-with-LangChain.git
   cd AI-ChatBot-with-LangChain

2. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Pinecone API key**
   You will enter this through the Streamlit sidebar, so no need to hardcode it.

---

## 🧪 Running the App

```bash
streamlit run app.py
```

---

## 🔐 Required APIs

| API              | Used For                             |
| ---------------- | ------------------------------------ |
| Pinecone API Key | Storing & querying vector embeddings |

**Note**: We don't currently use HuggingFace API key (it's just there for future plans or past copy-paste errors 🙃).

---

## 📌 Flow of the App

1. **User enters Pinecone API Key**
2. **Click "Load Data to Pinecone"**

   * Scrapes sitemap data
   * Splits into chunks
   * Embeds with Sentence Transformers
   * Pushes to Pinecone
3. **Ask a question**

   * Creates embedding for your prompt
   * Searches Pinecone for similar docs
   * Returns top-k results with content and source link

