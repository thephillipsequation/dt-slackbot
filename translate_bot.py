from slackclient import SlackClient
from googleapiclient.discovery import build


 
token = "xoxp-38048444512-38061548402-38056658581-a49ea97e83"
sc = SlackClient(token)
lyrics = """
The snow glows white on the mountain tonight
Not a footprint to be seen
A kingdom of isolation,
And it looks like I'm the queen.

The wind is howling like this swirling storm inside
Couldn't keep it in, heaven knows I tried!

Don't let them in, don't let them see
Be the good girl you always have to be
Conceal, don't feel, don't let them know
Well, now they know!

Let it go, let it go
Can't hold it back anymore
Let it go, let it go
Turn away and slam the door!
"""

def translate(inputString, inLang, outLang):


    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('translate', 'v2',
                                    developerKey='AIzaSyCrPl1LCUbBtQjnnJ67UYKUaLp_k5eRqQ8')

    wordArray = inputString.split(' ')
    response = service.translations().list(
                    source=inLang,
                    target=outLang,
                    q=wordArray
    			 ).execute()

    translations = response['translations']

    replyString = ''
    for wordDict in translations:
        replyString = replyString + wordDict['translatedText'] + ' '

    return replyString

inputString = lyrics
outString1 = translate(inputString, 'en', 'fr')
outString2 = translate(outString1, 'fr', 'de')
outString3 = translate(outString2, 'de', 'it')
outString4 = translate(outString3, 'it', 'es')
outString5 = translate(outString4, 'es', 'en')

response = outString5
sc.api_call('chat.postMessage', username='joshua', icon_emoji=':ghost:', as_user='false', channel='general', text=response)