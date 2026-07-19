import json 
import chromadb 
from chromadb.utils import embedding_functions

# Create or load ChromaDB collection
def get_collection():
    client=chromadb.PersistentClient(path="./chroma_db")
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
    collection=client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_function 
    )
    return collection

# Read sports facts from JSON
def read_json_file():
    with open("./data/sports_facts.json","r") as file:
        data=json.load(file)
    return data

# Store facts in ChromaDB
def load_data_into_chromadb():
    client=chromadb.PersistentClient(path="./chroma_db")
    try:
        client.delete_collection("sports_history")
    except:
        pass
    collection=get_collection()
    
    facts = read_json_file()
    for index,item in enumerate(facts):
        collection.add(
            documents=[item["fact"]],
            metadatas=[{"sport":item["sport"]}],
            ids=[f"fact_{index}"]
        )
        print(f"Added_fact_{index}")

# Retrieves historical facts from ChromaDB
def query_chromadb(query):
    collection=get_collection()
    results=collection.query(
        query_texts=[query],
        n_results=2
    )
    documents=results["documents"][0]
    historical_context = "Historical Facts:\n\n"
    for document in documents:
        historical_context += f"-{document}\n"
    return historical_context

if __name__ == "__main__":
    query_chromadb("Football history")