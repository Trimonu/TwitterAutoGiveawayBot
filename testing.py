import requests
import time
import json


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



# Search for tweets
def Search(topic):
  response = requests.get("https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_ext_limited_action_results=false&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=ION%20%22GIVEAWAY%22&count=500&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=true&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe", cookies=cookies, headers=headers)
  return response
