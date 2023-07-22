1. based on: https://twitter.com/hasan_3wada/status/1682416290684628992
2. see the youtube video at: [TODO]

## Related Public GPT Chat Records:

1. Scraping the raw text: https://chat.openai.com/share/67cd13e3-2916-4e03-a5e5-ffeee451ae77
2. Partial clean: https://chat.openai.com/share/d0d3e527-574b-4ade-9248-607a2684a01d
3. Cleaner data and viz: https://chat.openai.com/share/be297977-7add-41ad-8aec-d9852abd855a
4. Second pass with rescraped thread text: https://chat.openai.com/share/df755e01-51c1-4f76-8adb-8b3e03656995

## snapshot collection notes

I defined an empty array called snapofsnaps, scrolled twitter to activate virtual scrolling, and periodically ran `snapofsnaps.push([...document.querySelectorAll('article[data-testid=tweet]')].map(el => el.innerText))`

snapreader.py validates that every snap partially overlaps with the prior, so we know that there is an unbroken chain and no tweets are missed. then, the tweets are deduplicated and the array is flattened for further processing

`flat-json-to-user_responses.py` then writes the user_responses.csv used for viz

## summary results

| Statistic | Learning Time (days) | Job Landing Time (days) |
| --------- | -------------------- | ----------------------- |
| Count     | 9                    | 8                       |
| Mean      | 321                  | 253.125                 |
| Std       | 569.506585           | 346.203259              |
| Min       | 0                    | 0                       |
| 10%       | 11.2                 | 73.5                    |
| 25% (Q1)  | 90                   | 116.25                  |
| Median    | 180                  | 157.5                   |
| 75% (Q3)  | 180                  | 187.5                   |
| 90%       | 557                  | 475.5                   |
| Max       | 1825                 | 1095                    |

Please note, there is a ton of missing nuance that will be readable in the thread itself eg language and motivational complications, sarcastic or humorous answers, etc. Also, many samples simply couldn't be easily parsed so you can get more samples by manually reviewing the thread and compiling a CSV by hand. This project was in part to check GPT-4 code compiler efficacy at this task (it wasn't very effective imo).

![Histogram of Learning Time](./time-to-land-a-job.png)
