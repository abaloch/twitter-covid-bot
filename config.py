import tweepy
import os

"""
This function is used to access the api through tweepy
"""
def create_api():
    CONSUMER_KEY = os.environ.get('MY_CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('MY_CONSUMER_SECRET')
    ACCESS_KEY = os.environ.get('MY_ACCESS_KEY')
    ACCESS_SECRET = os.environ.get('MY_ACCESS_SECRET')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authenticated!")
    except:
        print("Error during authentication")

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    return api
