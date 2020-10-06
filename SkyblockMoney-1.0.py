from urllib import request, error
from json import loads
money= 0
name= input('Enter Player ID:')
url= "http://sky.shiiyu.moe/api/v2/coins/"+name
headers= {'User-Agent':''}
try:
    response= request.urlopen(request.Request(url,headers=headers)).read()
except error.HTTPError as e:
    if e.code==500:
        print('Wrong player ID or this player has no profile.')
    else:
        print('Wrong connection, Please retry.')
else:
    #print(response)
    data=loads(response.decode("utf-8"))['profiles']
    for i in data:
        money+=data[i]['purse']
        try:
            money+=data[i]['bank']
        except:
            pass
    print(name,' has ',int(money),' coins in Skyblock.')
