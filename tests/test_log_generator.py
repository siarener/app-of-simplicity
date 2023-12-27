from src.log_writer import split_into_sentences, read_lorem_ipsum_from_file, load_config

def test_split_into_sentences():
    text = "Sentence 1. Sentence 2? Sentence 3! Sentence 4."
    sentences = split_into_sentences(text)
    expected = ["Sentence 1.", "Sentence 2?", "Sentence 3!", "Sentence 4."]
    assert sentences == expected

def test_read_lorem_ipsum_from_file():
    config = load_config()
    file_path = config['files']['test_log_text']
    with open(file_path, 'w') as file:
        file.write("Test Lorem Ipsum Text.")
    text = read_lorem_ipsum_from_file(file_path)
    assert text == "Test Lorem Ipsum Text."
