import tweepy

auth = tweepy.AppAuthHandler('rexWuhMhntgtj0L8BJarfx0e7','SRVBomlDWHxnWdIL9bL9ULtlmTnRdbIwUXOS6hZhAd9GpbAniC')
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='bovespa').items(10):
    print(tweet.text)

