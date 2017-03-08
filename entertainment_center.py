# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

#Creating instances of my movie class with a list of my favorite movies
shape_of_you = media.Movie(
		"Shape of You",
		"https://img.youtube.com/vi/_dK2tDK9grQ/0.jpg",
		"https://www.youtube.com/watch?v=_dK2tDK9grQ"
	)

closer = media.Movie(
		"Closer",
		"https://www.inbuzzup.com/wp-content/uploads/2016/08/the-chainsmokers-closer-ft-halsey-lyrics-1024x576.jpg",
		"https://www.youtube.com/watch?v=PT2_F-1esPk"
	)

cheap_thrills = media.Movie(
		"Cheap Thrills",
		"https://i.ytimg.com/vi/nYh-n7EOtMA/maxresdefault.jpg",
		"https://www.youtube.com/watch?v=nYh-n7EOtMA"
	)

hymn_for_the_weekend = media.Movie(
		"Hymn For The Weekend",
		"http://cdn2.pitchfork.com/news/62322/6f67f916.jpg",
		"https://www.youtube.com/watch?v=YykjpeuMNEk"
	)

lean_on = media.Movie(
		"Lean On",
		"http://refitrev.com/wp-content/uploads/2015/10/lean-on.jpg",
		"https://www.youtube.com/watch?v=YqeW9_5kURI"
	)

emptiness = media.Movie(
		"Emptiness",
		"http://2.bp.blogspot.com/-xmxsZKwq_vo/VMdb4Ubb_nI/AAAAAAAAAFE/hwQDAe-30c0/s1600/ce7864977a84dddb73823b5911cb9c65.jpg",
		"https://www.youtube.com/watch?v=1nk-T2EfJ6g"
	)

#Putthing the movies in a list to pass on to the script that creates our page.
movies = [shape_of_you, closer, cheap_thrills, hymn_for_the_weekend, lean_on, emptiness]

def main():
	#Creates the movies web page.
	fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
	main()