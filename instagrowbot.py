from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("myimage.jpg", caption="Expert AI")

######  follow someone #######
bot.follow("vipcodder")

######  send a message #######
bot.send_message("I am Mahendra from heymate.in", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("mahendrakumarribadiya")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
