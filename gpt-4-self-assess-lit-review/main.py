import os
import tiktoken

# ref: https://platform.openai.com/docs/guides/embeddings/embedding-models
# ref: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_string(str_to_encode: str, should_print: bool =False, model_name: str = "gpt-4") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(str_to_encode))

    if should_print:
        print(num_tokens)

    return num_tokens

if __name__ == '__main__':
    training_text_path = os.path.join(os.getcwd(), 'training-data.txt')
    with open(training_text_path, 'r', encoding='utf-8') as data_file:
        training_text = data_file.read()
    num_tokens_from_string(str_to_encode=training_text, should_print=True)
    # print(training_data)
