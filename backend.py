from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from pinecone import Pinecone
import nest_asyncio
from langchain_community.document_loaders.sitemap import SitemapLoader

# Apply nest_asyncio to handle event loops in Streamlit
nest_asyncio.apply()


# Fetch data from sitemap URL
def get_web_data(url):
    loader = SitemapLoader(url)
    return loader.load()


# Split documents into chunks
def split_data(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return splitter.split_documents(docs)


# Create embedding model
def create_embeddings():
    return SentenceTransformerEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# Push documents and embeddings to Pinecone
def push_to_pine(api_key, embeddings, docs):
    pine = Pinecone(api_key=api_key)
    vectorstore = PineconeVectorStore(index=pine.Index("chatbot"), embedding=embeddings)
    vectorstore.add_documents(documents=docs)
    return vectorstore


# Retrieve existing Pinecone index
def pull_to_pine(api_key, embeddings):
    pine = Pinecone(api_key=api_key)
    vectorstore = PineconeVectorStore(index=pine.Index("chatbot"), embedding=embeddings)
    vectorstore.from_existing_index(index_name="chatbot", embedding=embeddings)
    return vectorstore


# Perform similarity search
def similar_doc(index, query, k=2):
    return index.similarity_search(query=query, k=k)
