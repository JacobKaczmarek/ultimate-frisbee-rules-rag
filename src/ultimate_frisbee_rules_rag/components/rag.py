import pinecone
import os
from ultimate_frisbee_rules_rag.config.configuration import ConfigurationManager
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Pinecone
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate

from ultimate_frisbee_rules_rag.utils.common import format_docs

class RAG:
    def __init__(self, config) -> None:
        embeddings = OpenAIEmbeddings()

        template = "You are an assistant for question-answering on ultimate frisbee rules. Use the following fragment of rules to answer the question. If you don't know the answer, just say that you don't know. Keep the answer short but also include the rule that the answer is based on.\nQuestion: {question} \Rules: {context} \nAnswer:"
        prompt = ChatPromptTemplate(
            input_variables=["question", "context"],
            messages=[
                HumanMessagePromptTemplate(
                    prompt=PromptTemplate(
                        input_variables=["question", "context"], template=template
                    )
                )
            ]
        )

        pinecone.init(api_key=os.environ['PINECONE_API_KEY'], environment=os.environ['PINECONE_ENV'])

        retriever = Pinecone.from_existing_index(config.index_name, embeddings).as_retriever()
        llm = OpenAI(model_name="gpt-3.5-turbo",temperature=0)

        self.chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    def invoke(self, query: str) -> str:
        return self.chain.invoke(query)