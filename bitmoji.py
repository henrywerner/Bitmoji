import json
import urllib.request

# Discover, construct, and save bitmoji panels within the given catagory
def get_panels(catagory):
    t_ids = [] # template IDs
    t_urls = [] # template URLs
    
    # has_friends boolean used in url assembly
    has_friends = False
    if (catagory == 'friends'):
        has_friends = True
    
    # find items in given catagory
    for item in templates[catagory]:
        if search_tag in item['tags']:
            t_ids.append(item['template_id'])
            t_urls.append(item['src'])
    
    # loop through discovered comics
    name_counter = 0
    for t in t_urls:
        index1 = t.find("%s") # only first index is needed
        index2 = index1 + 2

        if has_friends:
            insert = userID[0] + "-" + userID[1]
            index2 += 3 # adjust index2 for addition "-%s"
        else:
            insert = userID[0]

        url = t[0:int(index1)] + insert + t[int(index2):] # replace userIDs with insert
        filename = t_ids[name_counter] + ".png" # build filename using comic ID
        urllib.request.urlretrieve(url, filename) # save png from url
        name_counter += 1

        print("[" + str(name_counter) + "]: " + url)

    # clear arrays in case of additional calls
    t_ids.clear()
    t_urls.clear()

    if (name_counter == 0):
        print('No templates found.')
    else:
        print('Templates found: ' + str(name_counter))


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
    #get_friendmojis()
    get_panels('friends')
else:
    #get_imoji()
    get_panels('imoji')
