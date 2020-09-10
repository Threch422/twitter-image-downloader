import timeline as tl
import tweepy
import API_Tokens as token
import user_info as user
import favourites as f
import multiprocessing
from functools import partial

# Authentication
auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret)
auth.set_access_token(token.access_token, token.access_token_secret)

# Granting access
api = tweepy.API(auth)

if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    
    function1 = "1. Download images from specifc user favourited tweets\n"
    function2 = "2. Download images from specified user timeline\n"
    print("Here is the menu of this tool:\n", function1, function2)
    choice = int(input("What do you want to do with this tool? \n"))
    if (choice == 1):
        target = input("Which user do you want to download from? If you want to download from your favourites, enter nth. Otherwise enter UserID \n")
        if (target != ""):
            img_dict = f.user_liked_images(api, target)
            pool_output = pool.starmap(partial(f.download, length = len(img_dict)), enumerate(img_dict, 1))
        else:
            img_dict = f.user_liked_images(api, user.userID)
            pool_output = pool.starmap(partial(f.download, length = len(img_dict)), enumerate(img_dict, 1))
    elif (choice == 2):
        timeline_user = input("Which user do you want to download from? Default is @muni_gurume \n")
        if (timeline_user != ""):
            img_dict = tl.timeline_images(api, timeline_user)
            pool_output = pool.starmap(partial(tl.download, length = len(img_dict)), enumerate(img_dict, 1))
        else:
            img_dict = tl.timeline_images(api, "muni_gurume")
            pool_output = pool.starmap(partial(tl.download, length = len(img_dict)), enumerate(img_dict, 1))
    else:
        print("Invalid input. The program will be terminated.\n")
    pool.close()
    pool.join()
    print("Downloading process is ended.")