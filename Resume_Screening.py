from vector_database import createCollection, get_n_most_fitting_resumes, print_resumes
import chromadb 
import pypdf
from io import BytesIO
import pandas as pd
import kagglehub


# Download latest version
path = kagglehub.dataset_download("snehaanbhawal/resume-dataset")

print("Loading the resume's database...")

df = pd.read_csv(path+"\\Resume\\Resume.csv").iloc[:100,:]
  
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!

print("Setting up the vector database...")
client = chromadb.Client()

collection = createCollection(client, df["Resume_str"],["doc_"+str(i) for i in range(len( df["Resume_str"]))])


with open("job_description.txt","r") as file:
    job_description = file.read()
if len(job_description) == 0:
    job_description = input("Please insert the job description: ")

#print(job_description)

print("Obtaining the n most fitting resumes for the given job description...")
results = get_n_most_fitting_resumes(collection, job_description)


print_resumes( results, truncate_number = 85)


