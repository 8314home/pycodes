import tweepy
import time

auth = tweepy.OAuthHandler('ytX3FwXwrPZAks2ylWCKeaL38', 'W3TyuokgT9J1e59qEIQVCODESZAc3KjBtTI4LaQpMYOE3G4zvs')
auth.set_access_token('1264572549343543296-yjOL2zqQUpEnxw5oDmVglHQBsH4i7Z', '3HWamtkwULy5NOHk0Ao7oNF3v0gCIG6uLIkifcANUGBhO')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# print(f'api.me() = {api.me()}\n')
# user = api.me()
# print(f'api.followers = {user.followers_count}\n')


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)


dict_of_people = {}
search_string = 'Modi'
counter_val = 500

for tweet in tweepy.Cursor(api.search, search_string).items(counter_val):
    try:
        list_of_screens = tweet.entities['user_mentions']
        for i in list_of_screens:
            x = i['screen_name']
            # print(x)
            if dict_of_people.get(x.upper()) is None:
                dict_of_people[x.upper()] = 1
                # print(f'added screen name : {x}')
            else:
                dict_of_people[x.upper()] += 1
        # print(tweet.entities['user_mentions'])
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        print('breaking program')
        break

print("Collected tweets")

list_of_people = list(dict_of_people.items())

print("Converted dict to list")

list_of_people.sort(key=lambda t: t[1], reverse=True)

print("Sorted list")

print(f"Printing top 5 tweeters base on no of tweets for search string:->  {search_string} ")

for k in range(5):
    print(f"Name: {list_of_people[k][0]}  no of tweets : {list_of_people[k][1]}")

