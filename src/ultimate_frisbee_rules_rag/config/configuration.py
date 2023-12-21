from ultimate_frisbee_rules_rag.constants import *
from ultimate_frisbee_rules_rag.entity.config_entity import InitialiseVectorstoreConfig, RAGConfig
from ultimate_frisbee_rules_rag.utils.common import read_yaml

import os

class ConfigurationManager:
    def __init__(self, config_path = CONFIG_FILE_PATH) -> None:
        self.config = read_yaml(config_path)

    def get_initialise_vectorstore_config(self) -> InitialiseVectorstoreConfig:
        config = self.config.initialise_vectorstore
        
        return config
    
    def get_rag_config(self) -> RAGConfig:
        config = self.config.query_rag

        return config