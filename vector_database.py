import chromadb 
import pypdf
from io import BytesIO
import pandas as pd
import kagglehub



def createCollection(client, documents, ids = list): #ids,metadata):
    # Create collection. get_collection, get_or_c  reate_collection, delete_collection also available!
    collection = client.create_collection("all-my-documents")
    
    if id == []:
        ids = ["doc_"+str(i) for i in range(len(documents))]

    #if metadata is None:
    #    metadata = ["doc_"+str(i) for i in range(len(documents))]


    # Add docs to the collection. Can also update and delete. Row-based API coming soon!
    collection.add(
        documents= [ item for item in documents], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
         # filter on these!
        ids = ids,
        #metadatas=metadata,
    )

    return collection
    #collection.add(
    #    documents=[ item for item in documents], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    #    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    #    ids=["doc"+str(i) for i in range(len(df))], # unique for each doc
    #)


def get_n_most_fitting_resumes(collection, job_description):#, filter):

    # Query/search 2 most similar results. You can also .get by id
    results = collection.query(
        query_texts=[job_description],
        n_results=4,
        #where={"metadata_field": filter}, # optional filter
        # where_document={"$contains":"search_string"}  # optional filter
    )

    return results





def print_resumes( results, truncate_number):
    print("The best 4 candidates are:" , results["ids"])

    for item in results["documents"][0]:
        print(item[:truncate_number]) 
    return


