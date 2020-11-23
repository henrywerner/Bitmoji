import json
import urllib.request

# Discover, construct, and save bitmoji panels within the given category
def get_panels(category):
    panels = []
    
    # has_friends boolean used in url assembly
    has_friends = False
    if (category == 'friends'):
        has_friends = True
    
    # find items in given category
    for item in templates[category]:
        if search_tag in item['tags']:
            panels.append(item)
    
    # loop through discovered comics
    counter = 0
    for x in panels:
        src = x.get("src")
        index1 = src.find("%s") # only first index is needed
        index2 = index1 + 2

        if has_friends:
            insert = userID[0] + "-" + userID[1]
            index2 += 3 # adjust index2 for addition "-%s"
        else:
            insert = userID[0]

        url = src[0:int(index1)] + insert + src[int(index2):] # replace userIDs with insert
        filename = x.get("template_id") + ".png" # build filename using comic ID
        urllib.request.urlretrieve(url, filename) # save png from url
        counter += 1

        # This code sucks. I hate it. I'll fix it later.
        print("[" + str(counter) + "]\tid: " + x.get("template_id"), end = "\t")
        j = len(x["tags"]) - 1
        start_text = " "
        tags = "tags:"
        k = 0
        while (k < j and k < 3):
            tags += start_text + x["tags"][k]
            start_text = ", "
            k += 1
        print(tags)


####  Initial Set Up  ####

userID = []
search_tag = input("search tag: ")

# read userIDs from file
f = open("bitmoji_id.txt", "r")
l = f.readline()
while l:
    userID.append(l.rstrip())
    l = f.readline()
# userID = f.readlines()
f.close()

# pull updated bitmoji templates from api
urllib.request.urlretrieve('https://api.bitmoji.com/content/templates', '_templates.json')
f = open("_templates.json", 'r', encoding='utf8')
templates = json.load(f)
f.close()


####  Main Logic  ####

# call appropriate method based on number of provided userIDs
if (len(userID) > 1):
    get_panels('friends')
else:
    get_panels('imoji')
