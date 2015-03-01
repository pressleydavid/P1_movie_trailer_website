import media
import fresh_tomatoes

"""These movies are Hollywood's attempt at cinematic representation of the true cost of war"""
Charlie_Wilsons_War = media.Movie("Charlie Wilson's War", 
									"The seminal US history lesson of Afghanistan",
									"http://ia.media-imdb.com/images/M/MV5BMTgwMDgwMDc4MF5BMl5BanBnXkFtZTYwOTU3MDM4._V1_SY317_CR0,0,214,317_AL_.jpg", 
									"https://www.youtube.com/watch?v=OHNZUmdqdv8")

zero_dark_thirty = media.Movie("Zero Dark Thirty", 
							   	"Story about the operation to kill UBL", 
								"https://bizzam.files.wordpress.com/2012/10/zero-dark-thirty.jpg",
								"https://www.youtube.com/watch?v=YxC_JNz5Vbg")

american_sniper = media.Movie("American Sniper", 
								"Story of the cost of War",
								"http://ia.media-imdb.com/images/M/MV5BMTkxNzI3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_SX214_AL_.jpg",
								"https://www.youtube.com/watch?v=KYz2wyBy3kc")

lone_survivor = media.Movie("Lone Survivor", 
							"A story about being your brother's keeper", 
							"http://tryptryp.com/wp-content/uploads/2014/05/lonesurvivor.jpg", 
							"https://www.youtube.com/watch?v=yoLFk4JK_RM")

"""This is a list containing the instances created of type Movie to be rendered by fresh_tomatoes method"""
movies = [Charlie_Wilsons_War, american_sniper, lone_survivor, zero_dark_thirty]

"""This method opens the webpage using the movies list as an argument"""
fresh_tomatoes.open_movies_page(movies)
