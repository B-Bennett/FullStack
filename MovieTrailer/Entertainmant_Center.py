import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://bit.ly/2bYyLFy",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://bit.ly/2bzZLJW",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
deadpool = media.Movie("DeadPool",
                        "former Special Forces operative turned mercenary after being subjected to a rogue experiment",
                        "http://bit.ly/2bugnQ8",
                        "https://www.youtube.com/watch?v=ONHBaC-pfsk")

hunger_games = media.Movie("Hunger Games",
                        "A televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                        "http://bit.ly/1BDf3Rb",
                        "https://www.youtube.com/watch?v=C_Tsj_wTJkQ")

paycheck = media.Movie("Paycheck",
                        "What seemed like a breezy idea for an engineer to net him millions of dollars, leaves him on the run for his life and piecing together why he's being chased.",
                        "http://bit.ly/2bwSxFo",
                        "https://www.youtube.com/watch?v=yo_wPMW7U48")

breaking_bad = media.Movie("Breaking Bad",
                        "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's financial future.",
                        "http://bit.ly/2bfCP0h",
                        "https://www.youtube.com/watch?v=HhesaQXLuRY")

movies = [toy_story, avatar, deadpool, hunger_games, paycheck, breaking_bad]
fresh_tomatoes.open_movies_page(movies)
