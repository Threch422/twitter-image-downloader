import tweepy
import urllib.request
import API_Tokens as token
import user_info as user

# Authentication
auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret)
auth.set_access_token(token.access_token, token.access_token_secret)

# Granting access
api = tweepy.API(auth)

required_pages = int(input("How many pages you want to download? "))

for i in range(required_pages):

    # Getting info
    liked_tweets = api.favorites(user.userID, page = i + 1)
    image_url = []

    # Extracting image url 
    for tweets in liked_tweets:
        if tweets.entities.get('media', {}) != {}:
            media_list = tweets.entities.get('media', {})
            if media_list[0].get('media_url', {}) != {}:
                original_path = media_list[0].get('media_url', {})
                fixed_path = original_path.split('.jpg')[0] + '?format=png&name=4096x4096'
                image_url.append(fixed_path)        

    # Download it
    for images in image_url:
        file_name = user.path + images.split('?')[-2].split('/')[-1] + '.png'
        urllib.request.urlretrieve(images,file_name)
        print(file_name)
