import requests 
import json 
import socket


url = 'https://api.twitter.com/1.1/guest/activate.json'

auth = {'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}

post = requests.post(url,  headers=auth )

"""
repalce the xxxxxxxxx in the next url with you account id 

to print get the number of tweets you want change the "count=1" in the end of next url with the number you want . 
"""

page = 'https://api.twitter.com/2/timeline/profile/xxxxxxxxxxxxxxxxxxxxxxxxxx.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&include_tweet_replies=false&userId=1173003764229443584&count=1&ext=mediaStats%2ChighlightedLabel'

guest_token  = json.loads(post.content)['guest_token']

auth = {'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'  , 'x-guest-token' : str(guest_token) }



def get_tweet() : 
	get = requests.get(page , headers = auth )
 

	TL =  json.loads(get.content)['timeline']['instructions']


	TR =  json.loads(get.content)['globalObjects']['tweets']

	tweets = [] 
	for i in TL :
		ss  = i[u'addEntries'][u'entries']
		for d in ss:
			try : 
				aaa =  d[u'content'][u'item'][u'content'][u'tweet'][u'id']
				tweets.append(aaa)
			except :
				cc = 0
	
	for i in tweets : 
		try : 
			
				
			data = TR[i][u'full_text']
					
			return   data
		
		except : 
			cc = 0  


Esp = "xxx.xxx.xxx.xxx" 
Port = 1337

qq = 0 ;
while 1 : 
	if qq == 0 :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((Esp  , Port ))
		qq = 1 
	data = get_tweet()
	if ('esp' in data and 'L1' in data ):
		x = open('stat.txt')
		
		r = x.readlines()
		#print r[len(r)-1]
		x.close()
		if 'on' in r and 'on' in data : 
			
			continue 
		elif 'off' in r and 'off' in data : 
			continue 
		elif 'off' in data :
			s.sendall(b'ds')
			st = open('stat.txt' , 'w')
			st.write('off')
			st.close()
			print 'off'
			qq = 0
			s.close()
		else :	
			s.sendall(b'ds')
			st = open('stat.txt' , 'w')
			st.write('on')
			st.close()
			print 'on'
			qq = 0 
			s.close()
	
			
		

"""

lang
quote_count
full_text
source
conversation_id_str
possibly_sensitive_editable
created_at
user_id_str
entities
reply_count
id_str
extended_entities
display_text_range
retweet_count
favorite_count
"""



"""
users
places
moments
media
topics
lists
cards
broadcasts
tweets
"""


"""
timeline
globalObjects
"""


"""
responseObjects
id
instructions
"""


