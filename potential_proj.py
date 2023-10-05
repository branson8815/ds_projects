# test for initial commit on this file
import pandas as pd
import numpy as np
import os
from kaggle.api.kaggle_api_extended import KaggleApi

os.environ['KAGGLE_CONFIG_DIR'] = '/Users/kerouac/Desktop/project_work/programming_projects/kaggle.json'

# Initialize the Kaggle API client
api = KaggleApi()
api.authenticate()  # This will use your credentials from the KAGGLE_CONFIG_DIR

