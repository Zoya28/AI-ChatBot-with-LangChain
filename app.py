import streamlit as st
from backend import *

# Fix typo in key name
if "Pinecone_API_key" not in st.session_state:
    st.session_state["Pinecone_API_key"] = ""

st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="wide",
)

st.header("🤖 ChatBot")
st.subheader("AI assistant for your website")
st.write(
    "This is a simple chatbot that can answer questions about a website. It uses the LangChain library to scrape the site and extract information."
)

# -------- SIDEBAR -------- #
st.sidebar.header("Enter API")

st.session_state["Pinecone_API_key"] = st.sidebar.text_input(
    "PINECONE_API_KEY", type="password"
)

if st.sidebar.button("Load Data to Pinecone"):
    if (
        not st.session_state["Pinecone_API_key"]
    ):
        st.sidebar.error("Please enter API key.")
    else:
        with st.spinner("Fetching data like a Coursera ninja..."):
            data = get_web_data("https://www.coursera.org/sitemap~www~certificates.xml")
        st.success("Data pulled successfully! 🎯")

        with st.spinner("Splitting data into brain-sized chunks..."):
            chunks = split_data(data)
        st.success("Data chunked! 🧠")

        with st.spinner("Creating embeddings using HuggingFace..."):
            embeddings = create_embeddings()
        st.success("Embeddings created! 🔐")

        with st.spinner("Pushing data to Pinecone vault..."):
            push_to_pine(
                st.session_state["Pinecone_API_key"], embeddings=embeddings, docs=chunks
            )
        st.sidebar.success("All set! Pinecone is now your chatbot's brain. 🎉")

# -------- USER QUERY SECTION -------- #
prompt = st.text_input("How can I help you today?")
doc_count = st.slider(
    "Number of links you want (1 LOW || 5 HIGH)", min_value=1, max_value=5
)

if st.button("Search"):
    if not st.session_state["Pinecone_API_key"]:
        st.error("Enter Pinecone API key first, babe!")
    elif not prompt.strip():
        st.warning("Ask something first, don’t ghost me 😭")
    else:
        with st.spinner("Searching the AI archives..."):
            embedding = create_embeddings()
            index = pull_to_pine(
                st.session_state["Pinecone_API_key"], embeddings=embedding
            )
            results = similar_doc(index=index, query=prompt, k=doc_count)

        st.success("Here's the tea ☕ on what I found:")

        for i, doc in enumerate(results, 1):
            st.markdown(f"### 🔹 Result {i}")
            st.markdown(f"**Info:** {doc.page_content}")
            st.markdown(f"**Link:** [Visit Source]({doc.metadata.get('source', '#')})")
