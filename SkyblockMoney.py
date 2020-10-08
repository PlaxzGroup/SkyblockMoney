from re import findall
from urllib import request, error

money = 0
name = input('Enter Player ID:')
url = "http://sky.shiiyu.moe/api/v2/coins/" + name
headers = {'User-Agent': ''}
try:
    response = request.urlopen(request.Request(url, headers=headers)).read().decode('utf-8')
except error.HTTPError as e:
    if e.code == 500:
        print(e.read().decode('utf-8')[10:-2])
    else:
        print('Wrong connection, Please retry.')
else:
    # print(response)
    finding = [r'purse', r'bank']
    adding = [7, 6]
    for i in range(len(finding)):
        temp = findall(finding[i] + '\":.*?(?=[,.}])', response)
        for j in temp:
            money += int(j[adding[i]:])
    print(name, ' has ', int(money), ' coins in Skyblock.')
