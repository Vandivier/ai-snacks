import requests
import json

# import openai
import os
import tiktoken

API_KEY = "<YOUR_API_KEY>"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
COMPLETIONS_MODEL = "gpt-4"

# ref: https://medium.com/codingthesmartway-com-blog/unlocking-the-power-of-gpt-4-api-a-beginners-guide-for-developers-a4baef2b5a81
def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


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
    sciam_raw_text_path = os.path.join(os.getcwd(), 'training-sci-american.txt')
    with open(sciam_raw_text_path, 'r', encoding='utf-8') as data_file:
        sciam_raw_text = data_file.read()

    # # ref: https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb
    # openai.Completion.create(
    #     prompt=sciam_raw_text_path,
    #     temperature=0,
    #     # max_tokens=300,
    #     model=COMPLETIONS_MODEL
    # )["choices"][0]["text"].strip(" \n")
