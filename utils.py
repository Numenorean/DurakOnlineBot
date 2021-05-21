import json
import requests


def toBytes(data):
    return data.encode()


def unMarshal(data):
    result = [{}]
    for i in data.strip().split('\n'):
        pos = i.find('{')
        command = i[:pos]
        try:
            message = json.loads(i[pos:])
        except Exception:
            message = {}
            continue
        message['command'] = command
        result.append(message)
    
    return result[1:] if len(result) > 1 else result


def marshal(data):
	return data.pop('command')+json.dumps(data, separators=(',', ':')).replace("{}", '')+'\n'


def getServers():
    data = requests.get('http://static.rstgames.com/durak/servers.json', headers={
        'User-Agent': 'Fool/1.9.1.2 CFNetwork/1220.1 Darwin/20.3.0'
        }
    ).json()
    return [(data['user'][server]['host'], data['user'][server]['port']) for server in data['user'] if server != "u0"]


def whoFirst(main_cards, bot_cards, trump):
	trumpM = trump[0]
	_minC = 14
	whos = ""
	for mainCard in main_cards:
		mainCard = mainCard.replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
		for botCard in bot_cards:
			botCard = botCard.replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
			if mainCard[0] == trumpM and botCard[0] == trumpM:
				if _minC > min(int(botCard[1:]), int(mainCard[1:])):
					_minC = min(int(botCard[1:]), int(mainCard[1:]))
					whos = "bot" if int(botCard[1:]) < int(mainCard[1:]) else "main"
	if whos == "":
		if trumpM in "".join(bot_cards):
			whos = "bot"
		else:
			whos = "main"
	return whos