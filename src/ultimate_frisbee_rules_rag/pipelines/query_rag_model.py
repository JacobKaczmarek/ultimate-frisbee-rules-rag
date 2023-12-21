from ultimate_frisbee_rules_rag.config.configuration import ConfigurationManager
from ultimate_frisbee_rules_rag.components.rag import RAG

class QueryRagModelPipeline:
    def __init__(self) -> None:
        pass


    def main(self, query: str) -> str:
        config = ConfigurationManager().get_rag_config()
        rag = RAG(config)
        return rag.invoke(query)
