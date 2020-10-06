from urllib import request, error
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
    finding= ['purse','bank']
    adding=[7,6]
    for j in range(len(finding)):
        temp= response.decode('utf-8')
        while True:
            try:
                temp= temp[temp.index(finding[j])+adding[j]:]
            except ValueError:
                break
            else:
                _money= 0
                for i in range(len(temp)):
                    if temp[i]!=',' and temp[i]!='.' and temp[i]!='}':
                        _money= _money*10+int(temp[i])
                    else:
                        break
                money+=_money
    print(name,' has ',int(money),' coins in Skyblock.')
