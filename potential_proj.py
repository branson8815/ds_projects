#!/usr/bin/env python3
# test for initial commit on this file
import pandas as pd
import numpy as np
import os as os
from kaggle.api.kaggle_api_extended import KaggleApi


# Initialize the Kaggle API client
api = KaggleApi()
api.authenticate()  # This will use your credentials from the KAGGLE_CONFIG_DIR

dataset_name = 'nelgiriyewithana/top-spotify-songs-2023'
api.dataset_download_files(dataset_name, path="/Users/kerouac/Desktop/programming_projects/", unzip=True)