# self assess lit review

Using GPT-4 to ask GPT-4 if GPT-4 is bad

## study reproduction steps

1. send `training-sci-american.txt` to the GPT-4 ChatGPT interface.
2. save the result to `sci-am-summarized.txt`
3. run `poetry run python main.py`
4. take the resulting three `query_with_context` files and send them sequentially to the GPT-4 ChatGPT interface.
5. save the result as final_result.txt

## usage

```
# prereq == install poetry globally
poetry install
poetry run python main.py
```

## about main.py

this script merges the main query with context for GPT-4 and writes the result to `query_with_context.txt`

in the future this can be automatically sent to the GPT-4 api.

## count-tokens.py

run like `poetry run python count-tokens.py`

this file reproduces the token count for the raw training data

because it exceeds the 8191 GPT-4 max input token limit, we ask GPT-4 to produce `sci-am-summarized.txt`

## about training-data.txt

it's a stripped down version of three sources, omitting graphs, table data, and some sample outputs like the Socratic tutor transcript:

1. https://openai.com/research/gpt-4
2. https://www.scientificamerican.com/article/we-asked-gpt-3-to-write-an-academic-paper-about-itself-mdash-then-we-tried-to-get-it-published/
3. https://elicit.org/faq

## about sci-am-summarized.txt

raw training text token count is 8234
i want ~200 tokens for my final query
i reclaim space by asking gpt to summarize the scientific american article
that article is ~1800 tokens in raw form
reclaim needed space by asking to summarize in 1500 tokens
gpt-4 doesn't understand how to precisely count tokens, so i will ask it to limit by word count
OpenAI states: "You can think of tokens as pieces of words, where 1,000 tokens is about 750 words."
this means 1500 tokens -> 1125 words
to be conservative wrt conversion, I reduce the summary allowance by 10%:
1350 tokens ~> 1010 words
