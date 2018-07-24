# Description
Scraping tool that uses `tweepy` library to stream tweets from Twitter public API. The user can easily impose limit on streaming rate and choose different filter options of incoming tweets. Tweets are returned in convenient json format.
# Instructions
### Step 1: Create a Twitter Application
1.	Go to [Twitter Developer’s site](https://developer.twitter.com/) and sign in with the Twitter account that you will associate with your app (usually your own twitter account).
2.	Go to [Twitter Apps](https://apps.twitter.com/) and click ‘’Create New App”. On this page you will see a list of all your applications (if you already have registered Twitter apps).
3.	Fill in your application details:
	
	•	**Name** – here you should provide a unique name of your app. If your app is for personal use only – you can simply put your user name here. 
	
	•	**Description** – here you provide a simple description of what your app will be used for (example: “Stream tweets and analyze them later.”). You can edit this field later.  
	
	•	**Website** – if you don’t have website or this field is not applicable you can simply enter a placeholder value like https://www.site.com.
	
	•	**Callback URL** - you can leave empty this field especially if you will be the only user of the app.
	
4.	After you click the “Create your Twitter Application” button, the next page gives you details on your newly created app. Click on the ‘Keys and Access Tokens’ tab. Then, scroll down to the “Your Access Token” section and click “Create my access token” button. You may need to refresh the page if you don’t see your access tokens.
5.	Finally, you are ready to get your credentials. You will need to take the values from the following fields:
	
	•	Consumer Key (API Key)
	
	•	Consumer Secret (API Secret)
	
	•	Access Token
	
	•	Access Token Secret
	
Keep in mind that this information is private and should be protected (be careful and do not publish your credentials). 
### Step 2: Create `authenticate.py` file
In this file you should place your credentials in the following format:
```
api_key = 'xxxxxxxxxxxxxxxx' # Here you place your “Consumer Key (API Key)”
api_Secret = 'xxxxxxxxxxxxxxxx' # Here you place your “Consumer Secret (API Secret)”
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Here you place your “Access Token”
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Here you place your “Access Token Secret”
```
### Step 3: Open `scrapeoptions.py` 
Here you can customize your stream of tweets. The default options are:
```python
nameoutputfile = 'exampleoutput.json'
setlimit = 100
keywords = [‘world’]
tweetlang = ['en']  
```
Brief explanation of the options (in the python scripts you can find comments with useful links for more information):
	
	‘nameoutputfile’ – choose the name of the output file that will store the tweets.
	
	‘setlimit’ – set limit of the incoming tweets according to your needs, the default is 100.
	
	‘keywords’ – choose keywords according to which you will filter the stream of tweets. 
	
	‘tweetlang’ – here you can choose the language of the incoming tweets. 
	
### Step 4: Place all the necessary files (`scrape-tweets.py`, `scrapeoptions.py`, `authenticate.py`) into one directory (your working folder) on your computer. 
### Step 5: Open your command prompt, change the directory (to match your working folder) and run:
```
python scrape.py
```
Then a new json file will be created in your working folder – python will append to this file the incoming tweets based on your filter and when reaching the limit that you have manually set – the program will stop (you will receive a message in your command prompt). 
The tweets contain all available information and are in json format. 

**Important Note**: The streaming speed heavily depends on the rate limits imposed on Twitter Streaming API (https://developer.twitter.com/en/docs/basics/rate-limiting.html ), your internet connection and used keywords.

