import yaml
from text_generation.exception import text_generationException
from text_generation.logger import logging
import os, sys



def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise text_generationException(e, sys) from e
