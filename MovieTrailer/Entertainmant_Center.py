import fresh_tomatoes
import media

# movie title, story line, box art and trailer link

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://bit.ly/2bYyLFy",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

big_hero_6 = media.Movie("Big Hero 6",
                        "Robotics prodigy Hiro closest companion is Baymax,"
                        " a robot whose sole purpose is to take care of people.",
                        "http://bit.ly/2bPgKIH",
                        "https://www.youtube.com/watch?v=bT8qmoCgxZg")

deadpool = media.Movie("DeadPool",
                        "former Special Forces operative turned mercenary"
                        " after being subjected to a rogue experiment",
                        "http://bit.ly/2bugnQ8",
                        "https://www.youtube.com/watch?v=ONHBaC-pfsk")

hunger_games = media.Movie("Hunger Games",
                        "A televised competition in which two teenagers from each of"
                        " the twelve Districts of Panem are chosen at random to fight to the death.",
                        "http://bit.ly/1BDf3Rb",
                        "https://www.youtube.com/watch?v=C_Tsj_wTJkQ")

paycheck = media.Movie("Paycheck",
                        "A top-notch reverse engineer cracks secrets of competitors' products."
                       " When the job is done, he has his memory of it erased.",
                        "http://bit.ly/2bwSxFo",
                        "https://www.youtube.com/watch?v=yo_wPMW7U48")

m_300 = media.Movie("300",
                        "King Leonidas of Sparta and a force of 300 men fight the"
                        " Persians at Thermopylae in 480 B.C.",
                        "http://bit.ly/19EVhgC",
                        "https://www.youtube.com/watch?v=wDiUG52ZyHQ")

movies = [toy_story, big_hero_6, deadpool, hunger_games, paycheck, m_300]
# Uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

