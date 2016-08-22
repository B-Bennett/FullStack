import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://bit.ly/2bYyLFy",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
big_hero_6 = media.Movie("Big Hero 6",
                        "Robotics prodigy Hiro closest companion is Baymax, a robot whose sole purpose is to take care of people.",
                        "http://bit.ly/2bPgKIH",
                        "https://www.youtube.com/watch?v=bT8qmoCgxZg")
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

m_300 = media.Movie("300",
                        "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
                        "http://bit.ly/19EVhgC",
                        "https://www.youtube.com/watch?v=wDiUG52ZyHQ")

movies = [toy_story, big_hero_6, deadpool, hunger_games, paycheck, m_300]
fresh_tomatoes.open_movies_page(movies)
