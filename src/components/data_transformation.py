import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pk1")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transfomer_object(self):
        try:
            numerical_columns =['reading_score', 'writing_score'] 
            categorical_columns =['gender', 
                                 'race_ethnicity',
                                 'parental_level_of_education', 
                                 'lunch', 
                                 'test_preparation_course']
            num_pipeline = Pipeline(
                steps = [
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
             )
            
            cat_pipeline = Pipeline(
                steps = [
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler())
                
                ]

            )
            return (
                
                
            )

        
        except:
            pass


 