from bs4 import BeautifulSoup
import json

file = open('input', 'r')

contents = ''
if file.mode == 'r':
    contents = file.read()
    file.close()
if not contents:
    exit
output = []
soup = BeautifulSoup(contents)
trs = soup.find('aside' , {'class' : 'inline inline-table'}).find('table').findAll('tr')
currentWeek = ''
matchNo = 1
for tr in trs:
    tds = tr.findAll('td')
    if len(tds):
        if "Week" in tds[0].get_text():
            currentWeek = tds[0].get_text()
            continue
        else:
            data = {}
            date = tds[0].get_text()
            title = tds[1].get_text()
            time = tds[2].get_text()
            place = tds[3].get_text()

            vs = title.split('vs.')

            if len(vs) == 2:
                data['team1'] = vs[0].strip()
                data['team2'] = vs[1].strip()
            data['match-number'] = matchNo
            data['date'] = date
            data['title'] = title
            data['time'] = time
            data['place'] = place         
            matchNo += 1   

            output.append(data)
jsonstring = json.dumps(output)

with open('output.json', 'w') as f:
    f.write(jsonstring)