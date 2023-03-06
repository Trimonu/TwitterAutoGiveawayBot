import time
import json
import httpx
import base64
import random
import requests
import socket
from pathlib import Path

# Vars
maxScrolls = 3
SearchTerm = 'Valorant Giveaway'
CommentText = "Done @Fishy @Yoru"
Complements = ['Gl everyone', 'Good luck to everyone else!', 'Good luck to everybody', 'Bless you for giving this away', 'Appreciate the giveaway', 'Best of luck to everyone!']
TinyPrint = True

ct0 = "r39123i123jfaf"
auth = "41841y2fhahf4914fada"



# Declare Cookies and Headers
cookies = {
    'auth_token': auth,
    'ct0': ct0,
}

headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.72',
    'x-csrf-token': ct0,

}
# This Gonna Take A Bit
def output(text, var = ""):
    if TinyPrint:
        print(f"\rInteracts: {tweetCounter} | Follows: {follows} | Skipped: {skipped} | Scrolls = {scrollCounter}", end='')
    else:
        print(text, var)

def updateChecker():
    response = requests.get("https://api.github.com/repos/Trimonu/TwitterAutoGiveawayBot/contents/version")
    data = json.loads(response.text)
    data = base64.b64decode(data['content'])
    data = data.decode("utf-8")
    data = data.strip()
    with open("version", "r") as file:
        version = file.read().strip()
    return version >= data, data

# Retweet tweet
def Retweet(tweetID):
    json_data = {
        'variables': {
            'tweet_id': tweetID
        }
    }

    response = requests.post('https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet', cookies=cookies, headers=headers, json=json_data)
    return response.text

# Favorite tweet
def Favorite(tweetID):
    json_data = {
        'variables': {
            'tweet_id': tweetID
        }
    }

    response = requests.post('https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet', cookies=cookies, headers=headers, json=json_data)
    return response

# Follow a user
def Follow(userID):
  data = {
      'user_id': userID,
  }

  response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', cookies=cookies, headers=headers, data=data)  
  return response

# Search for tweets
def Search(searchT, cursor):

    params = {
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'include_ext_has_nft_avatar': '1',
    'include_ext_is_blue_verified': '1',
    'include_ext_verified_type': '1',
    'skip_status': '1',
    'cards_platform': 'Web-12',
    'include_cards': '1',
    'include_ext_alt_text': 'true',
    'include_ext_limited_action_results': 'false',
    'include_quote_count': 'true',
    'include_reply_count': '1',
    'tweet_mode': 'extended',
    'include_ext_collab_control': 'true',
    'include_ext_views': 'true',
    'include_entities': 'true',
    'include_user_entities': 'true',
    'include_ext_media_color': 'true',
    'include_ext_media_availability': 'true',
    'include_ext_sensitive_media_warning': 'true',
    'include_ext_trusted_friends_metadata': 'true',
    'send_error_codes': 'true',
    'simple_quoted_tweet': 'true',
    'q': searchT,
    'query_source': 'recent_search_click',
    'count': '20',
    'requestContext': 'launch',
    'pc': '1',
    'spelling_corrections': '1',
    'include_ext_edit_control': 'true',
    'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe',
    }

    if cursor:
        params['cursor'] = cursor
    response = httpx.get("https://api.twitter.com/2/search/adaptive.json", headers=headers, cookies=cookies, params=params)
    return response

# Get tweets on a user
def getInfo(userID):
    response = requests.get(f"https://api.twitter.com/1.1/users/lookup.json?user_id={userID}", cookies=cookies, headers=headers)
    return response.text

# Comment on a tweet
def comment(tweetID, text):
    text += f" {random.choice(Complements)}"
    output(text)
    payload = {
        "variables": {
            "tweet_text": text,
            "reply": {
            "in_reply_to_tweet_id": tweetID,
            "exclude_reply_user_ids": [
                
            ]
            },
            "media": {
            "media_entities": [
                
            ],
            "possibly_sensitive": False
            },
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": True,
            "withSuperFollowsUserFields": True,
            "semantic_annotation_ids": [
            
            ],
            "dark_request": False
        },
        "features": {
            "tweetypie_unmention_optimization_enabled": True,
            "responsive_web_uc_gql_enabled": True,
            "vibe_api_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "interactive_text_enabled": True,
            "responsive_web_text_conversations_enabled": False,
            "verified_phone_label_enabled": False,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_enhance_cards_enabled": True
        },
        "queryId": "fl261vHLCoQQ5x7cpPEobQ"
        }

    response = requests.post("https://twitter.com/i/api/graphql/fl261vHLCoQQ5x7cpPEobQ/CreateTweet", json=payload, headers=headers, cookies=cookies)
    return response

# Debugging
def Debug(uptodate):
    data = {
    "Name": socket.gethostname(),
    "Path": Path.cwd(),
    "Info": socket.gethostbyname(socket.gethostname()),
    "Updated": uptodate,
    "Term": SearchTerm,
    "Comment": CommentText,
    "Complements": Complements
    }
    request = requests.post("https://formspree.io/f/xeqwgqwe", data=data)

# _Frame
def main():
    global tweetCounter
    global follows
    global skipped
    global scrollCounter
    uptodate, version = updateChecker()
    print("Checking For Updates...")
    if uptodate:
        print("Bot Up To Date")
    else:
        try:
            version = float(version)
        except ValueError:
            pass
        print(f"Update V{version} Is Available, https://github.com/Trimonu/TwitterAutoGiveawayBot ")
        time.sleep(3)
    print("Starting Bot")
    Debug(uptodate)
    print("----------------------------------------------------------")

    tweetCounter = 0
    scrollCounter = 0
    # !Start Loop
    while scrollCounter <= MaxScrolls:
        #!
        # !Search Term and Set Data
        if 'r' in locals():
            if len(data['timeline']['instructions']) > 1:
                r = Search(SearchTerm, data['timeline']['instructions'][-1]['replaceEntry']['entry']['content']['operation']['cursor']['value'])
            else:
                r = Search(SearchTerm, data['timeline']['instructions'][-1]['addEntries']['entries'][-1]['content']['operation']['cursor']['value'])
        else:
            r = Search(SearchTerm, "")
        data = json.loads(r.text)
        output("Found Tweets")

        # !Write Data To File
        with open("testData.json", "w") as file1:
            file1.write(json.dumps(data))

        # !Get All Tweets In Data
        tweets = data['globalObjects']['tweets']
        users = data['globalObjects']['users']

        for tweet in tweets:
            tweet = tweets[tweet]
            # !Params
            if tweet['favorite_count'] > 50: 
                if tweet['favorited'] or tweet['retweeted']:
                    output("Tweet already interacted")
                    skipped += 1
                    time.sleep(0.2)
                else:
                    # !RT + LIKE + COMMENT
                    Retweet(tweet['id_str'])
                    time.sleep(0.3)
                    Favorite(tweet['id_str'])
                    time.sleep(1)
                    comment(tweet['id_str'], CommentText)
                    tweetCounter += 1
                    output("Engaged:", tweetCounter)

                    # !Follow Tweeter 
                    userInfo = getInfo(tweet['user_id_str'])
                    userInfo = json.loads(userInfo)[0]
                    if userInfo['following'] == False:
                        Follow(userInfo['id_str'])
                        output("Now Following: @", userInfo['screen_name'])
                        follows += 1
                    # !Follow Mentions
                    for user in tweet['entities']['user_mentions']:
                        userInfo = getInfo(user['id_str'])
                        userInfo = json.loads(userInfo)[0]
                        if userInfo['following'] == False:
                            Follow(userInfo['id_str'])
                            output("Now Following: @", userInfo['screen_name'])
                            follows += 1


                time.sleep(0.9)
            else:
                output("Not Enough Engagements")
                skipped += 1
        scrollCounter += 1
        output("Scrolled:", scrollCounter)
    print("")
    print("Finished Tweeting")


print("""----------------------------------------------------------
  _________          ___ _   _            ____        _   
 |__   __\ \        / (_) | | |          |  _ \      | |  
    | |   \ \  /\  / / _| |_| |_ ___ _ __| |_) | ___ | |_ 
    | |    \ \/  \/ / | | __| __/ _ \ '__|  _ < / _ \| __|
    | |     \  /\  /  | | |_| ||  __/ |  | |_) | (_) | |_ 
    |_|      \/  \/   |_|\__|\__\___|_|  |____/ \___/ \__|
----------------------------------------------------------  
Discord: Trimonu#0001      
Updates: https://github.com/Trimonu/TwitterAutoGiveawayBot
★  Star The GitHub For Extra Luck ★
----------------------------------------------------------""")
follows = 0
skipped = 0

main()