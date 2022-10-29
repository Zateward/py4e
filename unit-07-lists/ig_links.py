data = open('instagram_links.txt')
#print(data)

for lines in data:
    links = lines.split('"')
    #print('Debug:', lines)
    if len(links) <= 2:
        continue
    else:
        print(links[3])
