import time
import json
import random
import requests

# Vars
tweetCount = 150
searchTerm = "ION%20%22GIVEAWAY%22"

# Declare Cookies and Headers
cookies = {
    'auth_token': 'f5e8350933d4fe9e663d7c8f9b73040dba86026d',
    'ct0': 'e0d1841a77ba256d1b0fd29ebc1ee1936b105faf9329bf913e2f80c8b0c98950ddf86eff137c7064201a8a05588d973f2884fa0df974b6b0d89f9fef6d66b1a07a5a49b67dfdeb2b7fdbdfcbccf729c2',
}

headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.72',
    'x-csrf-token': 'e0d1841a77ba256d1b0fd29ebc1ee1936b105faf9329bf913e2f80c8b0c98950ddf86eff137c7064201a8a05588d973f2884fa0df974b6b0d89f9fef6d66b1a07a5a49b67dfdeb2b7fdbdfcbccf729c2',

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
    if cursor != "":
        response = requests.get(f"https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_ext_limited_action_results=false&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={search}&count=500&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=true&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe&cursor={cursor}", cookies=cookies, headers=headers)
        return response
    else:
        response = requests.get(f"https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_ext_limited_action_results=false&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={search}&count=500&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=true&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe", cookies=cookies, headers=headers)
        return response 

# Get tweets on a user
def getInfo(userID):
    response = requests.get(f"https://api.twitter.com/1.1/users/lookup.json?user_id={userID}", cookies=cookies, headers=headers)
    return response

# Hivemind Meta
def tweetProcessing(tweet, usersData):
    tweetPro = False
    if tweet['favorited'] or tweet['retweeted'] == True:
        print("Tweet Already Liked/Retweeted")

    else:
        if "ion" in tweet['full_text'].lower(): 
            Favorite(tweet['id_str'])
            print("Favorited")
            tweetPro = True
            
            time.sleep(random.randint(10, 20) / 10)
            Retweet(tweet['id_str'])
            print("Retweeted")
            
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
    tweetCounter = 0
    r = Search(searchTerm, "")
    data = json.loads(r.text)

    with open("testData.json", "w") as file1:
        file1.write(json.dumps(data))

    for i in data['globalObjects']['tweets']:
        if tweetProcessing(data['globalObjects']['tweets'][i], data['globalObjects']['users']):
            tweetCounter += 1
            time.sleep(random.randint(10, 20) / 10)

    while tweetCounter != tweetCount:
        print(len(data['timeline']['instructions']))
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