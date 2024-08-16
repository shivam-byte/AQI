

import pandas as pd
import os
import logging

from src.exception import CustomException

# Set up logging
logging.basicConfig(level=logging.INFO)

class DataIngestion:
    def __init__(self, data_path: str, train_data_path: str, test_data_path: str):
        self.data_path = data_path
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path


    def fetch_data(self):
        try:
            logging.info(f"Reading data from {self.data_path}")
            df = pd.read_csv(self.data_path)
            logging.info("Data successfully read into DataFrame.")
            return df
        except Exception as e:
            logging.error(f"Error occurred while fetching data: {str(e)}")
            raise CustomException("Data fetching failed", e)

    def split_data(self, df: pd.DataFrame):
        try:
            from sklearn.model_selection import train_test_split

            logging.info("Splitting data into training and testing sets.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)
            train_set.to_csv(self.train_data_path, index=False)
            test_set.to_csv(self.test_data_path, index=False)

            logging.info(f"Training data saved to {self.train_data_path}")
            logging.info(f"Testing data saved to {self.test_data_path}")

            return self.train_data_path, self.test_data_path

        except Exception as e:
            logging.error(f"Error occurred while splitting data: {str(e)}")
            raise CustomException("Data splitting failed", e)




