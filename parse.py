import tweepy
import time
import sys

from openpyxl import Workbook

auth = tweepy.OAuthHandler('ioVq2QrpDEreTHol2bwa7B5RT', '34zySkbtzaMS26O5vAlJKVDi9CWkxrXieJigFlZagFOxfZjFWL')
auth.set_access_token('3361355566-L4JgCU0DQZOxZyBFgbYLNGdADOKc1B2OP6N9CRV', 'jNePLU3Iuf8l7m5yvKw97eGcEcvUBlaQGshqSrlBmwsXk')

api = tweepy.API(auth)

followers = []

user = tweepy.Cursor(api.followers, screen_name="IRCE_Official").items()

row_count = 2
wb = Workbook()
ws1 = wb.active

ws1["A1"] = 'Twitter handle/screen name'
ws1["B1"] = 'Number of followers'
ws1["C1"] = 'Number following'
ws1["D1"] = 'Location'
ws1["E1"] = "Link"
ws1["F1"] = "Description"

wb.save("result.xlsx")

def write_to_sheet(name, number_of_followers, number_following, location, description):
    global row_count

    ws1["A%d" % row_count] = name
    ws1["B%d" % row_count] = number_of_followers
    ws1["C%d" % row_count] = number_following
    ws1["D%d" % row_count] = location
    #Link
    ws1["E%d" % row_count] = "https://twitter.com/%s" % name
    ws1["F%d" % row_count] = description

    wb.save("result.xlsx")
    row_count += 1




while True:
    try:
        u = next(user)
        write_to_sheet(u.screen_name, u.followers_count, u.friends_count, u.location, u.description)

    except :
        e = sys.exc_info()[0]
        print (e)
        print('We got a timeout ... Sleeping for 15 minutes')
        time.sleep(15*60)

        u = next(user)
        write_to_sheet(u.screen_name, u.followers_count, u.friends_count, u.location, u.description)
