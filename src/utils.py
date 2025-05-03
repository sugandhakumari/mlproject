import sys
import pickle
from src.exception import CustomException
import os

def save_object(obj, file_path):
    """
    Save the given object to a file using pickle.

    Parameters:
    obj: The object to be saved.
    file_path (str): The path where the object will be saved.

    Returns:
    None
    """
   
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        print(f"Object saved to {file_path}")
    except Exception as e:
        raise CustomException(e, sys)