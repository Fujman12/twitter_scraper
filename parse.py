import tweepy
import time

auth = tweepy.OAuthHandler('ioVq2QrpDEreTHol2bwa7B5RT', '34zySkbtzaMS26O5vAlJKVDi9CWkxrXieJigFlZagFOxfZjFWL')
auth.set_access_token('3361355566-L4JgCU0DQZOxZyBFgbYLNGdADOKc1B2OP6N9CRV', 'jNePLU3Iuf8l7m5yvKw97eGcEcvUBlaQGshqSrlBmwsXk')

api = tweepy.API(auth)

followers = []

user = tweepy.Cursor(api.followers, screen_name="IRCE_Official").items()

while True:
    try:
        u = next(user)
        print (u.screen_name)

    except:
        time.sleep(15*60)
        print('We got a timeout … Sleeping for 15 minutes')
        u = next(user)
        print (u.screen_name)
