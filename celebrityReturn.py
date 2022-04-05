from pytwitter import Api
import random

api = Api(bearer_token="AAAAAAAAAAAAAAAAAAAAAB6IbAEAAAAA0gDcM41vMR7lUKhtilWMSYDtSI0%3DZOlouSAEbiSM1q7aAVSuR1lBIeEsWlejgLvOT44o84WcdrnhHZ")




class returnTest:
  @staticmethod
  def returnTweet(celebrity):
    resp = api.search_tweets(celebrity)
    allTweets = resp.__getattribute__("data")
    rIndex = random.randint(0, len(allTweets) -1)
    return allTweets[rIndex].__getattribute__("text")
  
  @staticmethod
  def props(cls):   
    return [i for i in cls.__dict__.keys() if i[:1] != '_']

