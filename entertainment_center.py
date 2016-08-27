import fresh_tomatoes
import media

# this file, entertainment_center.py imports the class Movie from the media file and creates 6 instnance of the Movie class.
# the fresh tomatoes file will create the webpage with the 6 instnance of the Movie class.

ferris_buellers_day_off = media.Movie("Ferris Bueller's Day Off",
						"One man's struggle to take it easy",
						"Matthew Broderick charms in Ferris Bueller's Day Off, a light and irrepressibly fun movie about being young and having fun.",
						"http://www.impawards.com/1986/posters/ferris_buellers_day_off.jpg",
						"https://www.youtube.com/watch?v=iqyxxMFOFa0")

the_breakfast_club = media.Movie("The Breakfast Club",
						"They only met once, but it changed their lives forever",
						"The Breakfast Club is a warm, insightful, and very funny look into the inner lives of teenagers.",
						"http://www.impawards.com/1985/posters/breakfast_club.jpg",
						"https://www.youtube.com/watch?v=BSXBvor47Zs")

fast_times_at_ridgemont_high = media.Movie("Fast Times at Ridgemont High",
						"It's Awesome! Totally Awesome!",
						"While Fast Times at Ridgemont High features Sean Penn's legendary performance, the film endures because it accurately captured the small details of school, work, and teenage life.",
						"http://www.impawards.com/1982/posters/fast_times_at_ridgemont_high.jpg",
						"https://www.youtube.com/watch?v=FKov1lmq_OU")

heathers = media.Movie("Heathers",
						"Best friends, social trends and occasional murder",
						"Dark, cynical, and subversive, Heathers gently applies a chainsaw to the conventions of the high school movie -- changing the game for teen comedies to follow.",
						"http://www.impawards.com/1989/posters/heathers_ver1.jpg",
						"https://www.youtube.com/watch?v=nyu2SCyr7ak")

better_off_dead = media.Movie("Better Off Dead",
						"Insanity doesn't run in the family, it gallops",
						"Better Off Dead is an anarchic mix of black humor and surreal comedy, anchored by John Cusack's winsome, charming performance.",
						"http://www.impawards.com/1985/posters/better_off_dead.jpg",
						"https://www.youtube.com/watch?v=DWTouGjZt6A")

sixteen_candles = media.Movie("Sixteen Candles",
						"It's the time of your life that may last a lifetime",
						"Significantly more mature than the teen raunch comedies that defined the era, Sixteen Candles is shot with compassion and clear respect for his characters and their hang-ups.",
						"http://www.impawards.com/1984/posters/sixteen_candles_ver1.jpg",
						"https://www.youtube.com/watch?v=HGLtBJupFFM")

movies = [sixteen_candles, better_off_dead, heathers, fast_times_at_ridgemont_high, the_breakfast_club, ferris_buellers_day_off]
fresh_tomatoes.open_movies_page(movies)
