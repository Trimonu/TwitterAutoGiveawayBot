import time
import json
import random
import requests

# Vars
tweetCount = 100
searchTerm = "Soulstrife"
commentText = "Done @Boe @Joe"
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


# Retweet tweet
def Retweet(tweetID):
    json_data = {
        'variables': {
            'tweet_id': tweetID
        }
    }

    response = requests.post('https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet', cookies=cookies, headers=headers, json=json_data)
    return response

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
def Search(search, cursor):
    search += "%20%22GIVEAWAY%22"
    if cursor != "":
        response = requests.get(f"https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=True&include_ext_limited_action_results=False&include_quote_count=True&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=True&include_entities=True&include_user_entities=True&include_ext_media_color=True&include_ext_media_availability=True&include_ext_sensitive_media_warning=True&include_ext_trusted_friends_metadata=True&send_error_codes=True&simple_quoted_tweet=True&q={search}&count=500&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=True&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe&cursor={cursor}", cookies=cookies, headers=headers)
        return response
    else:
        response = requests.get(f"https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=True&include_ext_limited_action_results=False&include_quote_count=True&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=True&include_entities=True&include_user_entities=True&include_ext_media_color=True&include_ext_media_availability=True&include_ext_sensitive_media_warning=True&include_ext_trusted_friends_metadata=True&send_error_codes=True&simple_quoted_tweet=True&q={search}&count=500&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=True&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe", cookies=cookies, headers=headers)
        return response 

# Get tweets on a user
def getInfo(userID):
    response = requests.get(f"https://api.twitter.com/1.1/users/lookup.json?user_id={userID}", cookies=cookies, headers=headers)
    return response

# Comment on a tweet
def comment(tweetID, text):
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

# Hivemind Meta
def tweetProcessing(tweet, usersData):
    tweetPro = False
    if tweet['favorited'] or tweet['retweeted'] == True:
        print("Tweet Already Liked/Retweeted")

    else:
        if searchTerm.lower() in tweet['full_text'].lower():
            Favorite(tweet['id_str'])
            print("Favorited")
            tweetPro = True
            
            time.sleep(random.randint(10, 20) / 10)
            Retweet(tweet['id_str'])
            print("Retweeted")

            time.sleep(random.randint(10, 20) / 10)
            comment(tweet['id_str'], commentText)
            print("Commented")

            time.sleep(random.randint(10, 20) / 10)
            for users in tweet['entities']['user_mentions']:
                if users['id_str'] in usersData:
                    if usersData[users['id_str']]['following'] == False:
                        Follow(users['id_str']) 
                        print("Followed")

                else:
                    response = getInfo(users['id_str'])
                    data = json.loads(response.text)
                    if data[0]['following'] == False:
                        Follow(users['id_str'])
                        print("Followed")

    return tweetPro
        



def main():
    # Search Term and Set Data
    tweetCounter = 0
    r = Search(searchTerm, "")
    data = json.loads(r.text)

    # Write Data To File
    with open("testData.json", "w") as file1:
        file1.write(json.dumps(data))

    # Process Data
    for i in data['globalObjects']['tweets']:
        if tweetProcessing(data['globalObjects']['tweets'][i], data['globalObjects']['users']):
            tweetCounter += 1
    time.sleep(random.randint(10, 20) / 10)

    # Process Data for max TweetCount
    while tweetCounter != tweetCount:
        if len(data['timeline']['instructions']) > 1:
            r = Search(searchTerm, data['timeline']['instructions'][-1]['replaceEntry']['entry']['content']['operation']['cursor']['value'])
        else:
            r = Search(searchTerm, data['timeline']['instructions'][-1]['addEntries']['entries'][-1]['content']['operation']['cursor']['value'])
        data = json.loads(r.text)
        
        with open("testData.json", "w") as file1:
            file1.write(json.dumps(data))

        for i in data['globalObjects']['tweets']:
            if tweetProcessing(data['globalObjects']['tweets'][i], data['globalObjects']['users']):
                tweetCounter += 1
                print(tweetCounter)
                
        time.sleep(random.randint(10, 20) / 10)

main()