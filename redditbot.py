import praw
import config
import time
import os

marthmoves=["bair","dair","dashattack","dsmash","fsmash","ftilt","grab","jab",
"nair","upair","upsmash","uptilt"]

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "yoshixii's frame data bot v0.1")
	print("Logged in")
	return r
			
def run_bot(r, commentsReplied):
	for comment in r.subreddit('test').comments(limit=2):
		if "marf" in comment.body and comment.id not in commentsReplied and comment.author != r.user.me():
			print("String w/ 'marf' found in comment " + comment.id)
			for move in marthmoves:
				if move in comment.body and comment.id not in commentsReplied and comment.author != r.user.me():
					print("move found")
					file=open("marth/"(move+".txt"),"r")
					comment.reply(file.read())
					file.close
					break
			#comment.reply("marfmina")
			print("Replied to comment " + comment.id)
			commentsReplied.append(comment.id)
			with open("commentIDs.txt", "a") as f:
				f.write(comment.id + "\n")
			
	print("sleeping for 10 sec")
	time.sleep(10)
	
def get_saved_comments():
	if not os.path.isfile("commentIDs.txt"):
		commentsReplied = []
	else:	
		with open("commentIDs.txt", "r") as f:
			commentsReplied = f.read()
			commentsReplied = commentsReplied.split("\n")
			commentsReplied = list(filter(None, commentsReplied))
			
	return commentsReplied

r = bot_login()
commentsReplied = get_saved_comments()
print(commentsReplied)
while True:
	run_bot(r, commentsReplied)
