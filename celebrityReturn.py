from pytwitter import Api
import random

api = Api(bearer_token="AAAAAAAAAAAAAAAAAAAAAB6IbAEAAAAA0gDcM41vMR7lUKhtilWMSYDtSI0%3DZOlouSAEbiSM1q7aAVSuR1lBIeEsWlejgLvOT44o84WcdrnhHZ")

class tweeting:
  @staticmethod
  def searchTweet(celebrity):
    try:
      resp = api.search_tweets(celebrity)
      allTweets = resp.__getattribute__("data")
      rIndex = random.randint(0, len(allTweets) -1)
      return allTweets[rIndex].__getattribute__("text")
    except:
      return "Looks like no one is talking about " + celebrity 
  @staticmethod
  def returnTweet(myUsername):
    try:
      target_resp = api.get_user(username = myUsername) 
      target =  target_resp.__getattribute__("data")
      target_id =  target.__getattribute__("id")
      return api.get_timelines(user_id=target_id , exclude = ["replies","retweets"]).__getattribute__("data")[0].__getattribute__("text")
    except:
      return "Hmm didn't get anything, the username " + myUsername + " might not exist, remember, usernames are case-sensitive."
  @staticmethod
  def props(cls):   
    return [i for i in cls.__dict__.keys() if i[:1] != '_']

