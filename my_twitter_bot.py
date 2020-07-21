import tweepy
import schedule
import time
from covid_api import get_data
from config import create_api


def tweet_cases(api):

    world_cases = get_data()
    world_cases = format(world_cases, ',d')
    try:
        api.update_status(f"{world_cases} people have recovered from #COVID19")
        print(f"Tweeting: {world_cases} people have recovered from #COVID19")


    except:
        print(f"Error: Same Amount of cases")


def user_info(api):
    user = api.get_user("cases_covid")
    print(f"User details: {user.name}\n{user.description}\n{user.location}")
    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)


def main():
    api = create_api()

    schedule.every().day.at("17:30").do(tweet_cases, api)

    # schedule.every(1).minutes.do(tweet_cases, api)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()
