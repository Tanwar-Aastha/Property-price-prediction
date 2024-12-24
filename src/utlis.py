# It will include for functionalities that are written in a common way
# that are used in the entire application.

import os
import sys
from src.exception import CustomException

import pandas as pd
import numpy as np
import dill


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)