def create_youtube_video(title, description):
	new_youtube_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return new_youtube_video

def likes(new_youtube_video):
	if "likes" in new_youtube_video:
		new_youtube_video["likes"] += 1
	return new_youtube_video


def dislikes(new_youtube_video):
	if "dislikes" in new_youtube_video:
		new_youtube_video["dislikes"] += 1
	return new_youtube_video

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return new_youtube_video

first_youtube_video = create_youtube_video("space_dog","with_music")
first_youtube_video = likes(first_youtube_video)
first_youtube_video = dislikes(first_youtube_video)
first_youtube_video = add_comment(first_youtube_video, "malakmiari", "jameel_is_dancing")
print(first_youtube_video)
