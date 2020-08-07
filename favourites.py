import tweepy
import urllib.request
import os
import API_Tokens as token
import user_info as user

def user_liked_images(api,target):
    required_tweets = int(input("How many tweets you want to download? "))
    image_url = []

    # Main Progress
    # Getting info of your favourite tweets
    liked_tweets = tweepy.Cursor(api.favorites, id = target, tweet_mode = "extended").items(required_tweets)

    # Extracting image url 
    for tweets in liked_tweets:
        if tweets.entities.get('media', {}) != {}:
            media_list = tweets.extended_entities.get('media', {})
            for i in range(len(media_list)):
                if media_list[i].get('media_url', {}) != {} and media_list[i].get('type') == 'photo':
                    original_path = media_list[i].get('media_url', {})
                    if ".jpg" in original_path:
                        fixed_path = original_path.split('.jpg')[0] + '?format=png&name=4096x4096'
                    elif ".png" in original_path:
                        fixed_path = original_path.split('.png')[0] + '?format=png&name=4096x4096'
                    image_url.append(fixed_path)
                    #print(tweets.extended_entities['media'])  # Debug use  

    # Download it
    for index, images in enumerate(image_url, 1):
        file_name = user.path + images.split('?')[-2].split('/')[-1] + '.png'
        # Check image existance in directory. Preventing reprtitive downloading.
        if (os.path.isfile(file_name)):
            continue
        urllib.request.urlretrieve(images,file_name)
        #print(file_name + "   " + str(index) + " / " + str(len(image_url))) # Debug use
        print("Downloading: " + str(index) + " / " + str(len(image_url)))
    print("The download progress has been done.")
