import time
import re
from configparser import ConfigParser


def split_into_sentences(text):
    # Use a simple regex to split the text into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return sentences


def read_lorem_ipsum_from_file(file_path):
    with open(file_path) as file:
        return file.read()


def load_config():
    config = ConfigParser()
    config.read("config/config.ini")
    return config


def write_logs(file_path):
    lorem_ipsum_text = read_lorem_ipsum_from_file(file_path)
    sentences = split_into_sentences(lorem_ipsum_text)

    while True:
        # Log sentences one by one
        for sentence in sentences:
            print(sentence)
            # Sleep for a short duration (e.g., 1 second)
            time.sleep(1)
