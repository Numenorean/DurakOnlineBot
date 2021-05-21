import api
import config
from api import logger
import time
import random
from api import servers
import utils


@logger.catch
def start():
    main = api.DurakClient(_type="main")
    
    for _ in range(100):
        server = random.choice(servers)
        logger.info(f"[INFO] Connected to {server[0]+':'+str(server[1])} server")
        main.connect(server)
        key2 = main.getSessionKey()
        main.verifySession(key2)
        main.auth(config.TOKEN)

        bot = api.DurakClient(_type="bot")
        bot.connect(server)
        key = bot.getSessionKey()
        bot.verifySession(key)
        token = ""
        while not token:
            try:
                token = bot.register()
            except:
                continue
        bot.auth(token)
        bot.sendFriendRequest()
        _id1 = ""
        while not _id1:
            _id1 = main.getMessagesUpdate()
        main.acceptFriendRequest(_id1)
        pwd = bot.createGame()
        bot.inviteToGame()
        _id = ""
        while not _id:
            _id = main.getInvites()
        main.join(_id, pwd)
        bot.ready()
        main.ready()
        bot.waitingFor()
        main.waitingFor()
        turn = utils.whoFirst(main.cards, bot.cards, bot.trump)
        time.sleep(0.3)
        for i in range(5):
            if turn == "bot":
                bot.turn()
                main.waitingFor()
                main.take()
                bot.waitingFor()
                bot._pass()
                bot.waitingFor()
                main.waitingFor()
            elif turn == "main":
                main.turn()
                bot.waitingFor()
                bot.take()
                main.waitingFor()
                main._pass()
                main.waitingFor()
                bot.waitingFor()


        bot.exit()
        time.sleep(2)
        main.leave(_id)
        main.deleteFriend(_id1)

start()