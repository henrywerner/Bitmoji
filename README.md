## Features
Finds currently available Bitmoji templates with tags that match the user's input. All located templates are saved as a PNG image.

## Setup
In `bitmoji_id.txt`, replace the existing text with a desired Bitmoji ID. 

[This guide](https://github.com/matthewnau/libmoji/wiki/Finding-Your-ID) explains how to find the ID for your own account, although some details are outdated. You can use [bitmoji.com/account_v2](https://www.bitmoji.com/account_v2/) if the `log in` button on Bitmoji's homepage is missing.

## Execution
```shell
C:\Users\Q\Desktop\Bitmoji>python bitmoji.py
search tag: dance
[1]     id: 10160       tags: halloween, dab, costume
[2]     id: 14463       tags: dancing, dancing*, whip nae nae
[3]     id: 13666       tags: breakdancing, breakdancing*, dancing
[4]     id: 24177       tags: dancing, pose, dance
[5]     id: 7119        tags: meme, dab, dabbing
[6]     id: 13666       tags: breakdancing, breakdancing*, dancing
[7]     id: 14463       tags: dancing, dancing*, whip nae nae
[8]     id: 14516       tags: nay nay, dancing, nae nae
[9]     id: 4997        tags: dancing, let's go, tgif
[10]    id: 9262        tags: dancing, dance party
[11]    id: 12983       tags: mardi gras, brazil, carnavale
[12]    id: 13664       tags: breakdancing, breakdancing*, dancing
[13]    id: 17019       tags: voguing, death drop, vogue
```

![Image aquired](https://sdk.bitmoji.com/render/panel/20041615-251425289_18-s5-v1.png?transparent=1&palette=1)
