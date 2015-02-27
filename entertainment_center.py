import media

toy_story = media.Movie("Toy Story", "Story of a boy and his toys",
						"Pic.jpg",
						"Link")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","Marine on Alien Planet","Pic","https://www.youtube.com/watch?v=cRdxXPV9GNQ")

print(avatar.storyline)

avatar.show_trailer()