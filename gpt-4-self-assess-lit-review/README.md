# self assess lit review

Using GPT-4 to ask GPT-4 if GPT-4 is bad

## usage

```
# prereq == install poetry globally
poetry install
poetry run python main.py
```

## about main.py

this script does four things:

1. sends `training-data.txt` to GPT-4
2. confirms GPT-4 responds as expected
3. sends `main-query.txt` to GPT-4
4. prints the response to `raw.tex`

`raw.tex` then allows us to build a research report with two more steps:

1. manually update `raw.tex` to `updated.tex`
2. compile `updated.tex` to `report.pdf`

## about training-data.txt

it's a stripped down version of three sources, omitting graphs and stuff:

1. https://openai.com/research/gpt-4
2. https://www.scientificamerican.com/article/we-asked-gpt-3-to-write-an-academic-paper-about-itself-mdash-then-we-tried-to-get-it-published/
3. https://elicit.org/faq
