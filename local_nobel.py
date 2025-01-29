from yaspin import yaspin
from langchain_community.document_loaders import JSONLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def main():
    with yaspin(text="Running...", color="yellow") as spinner:
        embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        loader = JSONLoader(file_path="./prizes.json", jq_schema=".prizes[]", text_content=False)

        documents = loader.load()

        db = Chroma.from_documents(documents, embedding_function)
        query = "What year did albert einstein win the nobel prize?"
        docs = db.similarity_search(query)
        if docs:
            spinner.ok("✅ ")
            print(docs[0].page_content)
        else:
            spinner.fail("❌ ")
            print("No documents found")


if __name__ == "__main__":
    main()

