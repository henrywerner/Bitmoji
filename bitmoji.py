import json
import urllib.request

userID = ''
search_tag = input("search tag: ")
t_ids = [] # template IDs
t_urls = [] # template URLs

# read userID from file
f = open("bitmoji_id.txt", "r")
userID = f.readline()
f.close()

# pull updated bitmoji templates from api
urllib.request.urlretrieve('https://api.bitmoji.com/content/templates', '_templates.json')
f = open("_templates.json", 'r', encoding='utf8')
templates = json.load(f)
f.close()

# find items in the individual comics catagory
for item in templates['imoji']:
    if search_tag in item['tags']:
        t_ids.append(item['template_id'])
        t_urls.append(item['src'])


# loop through discovered comics
name_counter = 0
for t in t_urls:
    index = t.find("%s")
    if (index != -1):
        url = t[0:int(index)] + userID + t[int(index)+2:] # replace %s with userID
        print(url)
        filename = t_ids[name_counter] + ".png" # build filename using comic ID
        urllib.request.urlretrieve(url, filename) # save png from url
    else:
        print('item ignored.')
    name_counter += 1 # set next name to next item in list

if (name_counter == 0):
    print('No templates found.')
else:
    print('Templates found: ' + str(name_counter))