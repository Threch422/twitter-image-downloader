# twitter-image-downloader
For self-use and for fun

Update: 7/8/2020

Ver 1.0
1.  Support download images from authenticated user

Ver 1.1
1. Support download images from specified user.

Ver 1.2
1. Added checking file existance function. The tool will not download the same image again if that one already exists in directory.
2. Bugs fixed.


This tool is used to download the pictures you have liked in your Twitter account or from specific user.

Requirments:
1. Python 3.0 or above is required to run the tool.
2. tweepy is required for this tool.

Tutorial to install tweepy:
1. Open your cmd and type
pip install tweepy
If the installation is completed. Then it is okay.
If pip is not a command in your cmd, add python and Scripts file in PATH of your computer.

How to use?
1.  Apply for Twitter developer account to get your own API tokens and access tokens.
    It can be used to access your information in your twitter account.
2.  Copy it to API_Tokens.py 
3.  Enter the path where you want the images store in your computer and your userID in user_info.py
4.  run the twitter-image-downloader.py
5.  Follow the instructions given by twitter-image-downloader.py.

Disclaimer:
it is just for fun and may contains bug which user is expected to anticipate it.
