import os
import pinecone
from dotenv import load_dotenv
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader

from ultimate_frisbee_rules_rag.entity.config_entity import InitialiseVectorstoreConfig


class VectorStore:
    def __init__(self, config: InitialiseVectorstoreConfig) -> None:
        self.config = config
    

    def initialise(self) -> None:
        load_dotenv()

        self._load_documents()
        self._create_index()
        


    def _load_documents(self) -> None:
        loader = DirectoryLoader(self.config.documents_dir)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.splits = text_splitter.split_documents(documents)


    def _load_or_create_index(self) -> None:
        pinecone.init(
            api_key=os.environ['PINECONE_API_KEY'],
            environment=os.environ['PINECONE_ENV'],
        )

        embeddings = OpenAIEmbeddings()

        if self.config.index_name not in pinecone.list_indexes():
            Pinecone.from_documents(documents=self.splits, index_name=self.config.index_name, embedding=embeddings)