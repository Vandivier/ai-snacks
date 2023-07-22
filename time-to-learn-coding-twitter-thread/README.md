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
