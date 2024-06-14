from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("car.jpg", caption="Cocacola drinking")

######  follow someone #######
bot.follow("ritikroshan")

######  send a message #######
bot.send_message("I am Mahendra from Vipcodder", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("mahendrakumarribadiya")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
