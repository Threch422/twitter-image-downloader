import favourites as mf
import timeline as tl
import tweepy
import API_Tokens as token
import user_info as user

# Authentication
auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret)
auth.set_access_token(token.access_token, token.access_token_secret)

# Granting access
api = tweepy.API(auth)

function1 = "1. Download images from specifc user favourited tweets\n"
function2 = "2. Download images from specified user timeline\n"
print("Here is the menu of this tool:\n", function1, function2)
choice = int(input("What do you want to do with this tool? "))
if (choice == 1):
    target = input("Which user do you want to download from? If you want to download from your favourites, enter nth. Otherwise enter UserID ")
    if (user != {}):
        mf.user_liked_images(api, target)
    else:
        mf.user_liked_images(api, user.userID)
elif (choice == 2):
    tl.timeline_images(api, "muni_gurume")
else:
    print("Invalid input. The program will be terminated.")