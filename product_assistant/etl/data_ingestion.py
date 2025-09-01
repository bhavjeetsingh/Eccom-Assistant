import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from prod_assistant.utils.model_loader import ModelLoader
from product_assistant.utils.config_loader import load_config

class DataIngestion:
    'class to handle data transformation and ingestion into AstraDB vector store'

    def __init__(self):
        'Initialize environment variables, embedding model, and set CSV file path'
        print('Initializing DataIngestion pipeline...')
        self.model_loader=ModelLoader()
        self._load_env_variable()
        self.csv_path = 