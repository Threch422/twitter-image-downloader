# twitter-image-downloader
For self-use and for fun

**Remark: As twitter has updated the API policy, it is no longer that we can retrieve the tweet data with free access. This repo will be stopped for further update and development**

### Last Update: 02/10/2023

## Update History
Ver 1.0
1.  Support download images from authenticated user

Ver 1.1
1. Support download images from specified user.

Ver 1.2
1. Added checking file existance function. The tool will not download the same image again if that one already exists in directory. (Using default file name to check)
2. Bugs fixed.

Ver 1.3 10/9/2020
1. Multiprocessing downloading is used, increasing speed of program.


This tool is used to download the pictures you have liked in your Twitter account or from specific user.

## Requirments:
1. Python 3.3 or above is required to run the tool.
2. tweepy is required for this tool.

### Tutorial to install tweepy:
1. Open your cmd and type (pip install tweepy). If the installation is completed. Then it is okay.
2. If pip is not a command in your cmd, add python and Scripts file in PATH of your computer.

## How to use?
1.  Apply for Twitter developer account to get your own API tokens and access tokens.
    It can be used to access your information in your twitter account.
2.  Copy it to API_Tokens.py 
3.  Enter the path where you want the images store in your computer and your userID in user_info.py
4.  run the twitter-image-downloader.py
5.  Follow the instructions given by twitter-image-downloader.py.

## Remark
1.  The file is saved in png format with original resolution of the image on twitter. Be aware on the size of multiple images downloaded.
2.  The filename is saved in the format {imageID}.png. ID should be unique and tool can identify that image is saved in the target file by checking the imageID. Thus changing the     name of images downloaded may cause repetitive downloading in next time.
3.  As multiprocessing lib is used, the image downloading is NOT in order due to working principle of multiprocessing. Thus the progress showing is NOT a bug.

## Future Update (Maybe...?)
1.  Downloading according to the media category of user.
...

## Disclaimer:
It is just for fun and may contains bug which user is expected to anticipate it.
