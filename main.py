from ultimate_frisbee_rules_rag import logger
from ultimate_frisbee_rules_rag.pipelines.initialise_vectorstore import InitialiseVectorStorePipeline

try:
    logger.info("Initialising vectorstore")
    InitialiseVectorStorePipeline().main()
    logger.info("Initialised vectorstore")
except Exception as e:
    logger.exception(f"Error while initialising vectorstore: {e}")
    raise e