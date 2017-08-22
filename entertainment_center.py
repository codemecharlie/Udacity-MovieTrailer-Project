import fresh_tomatoes
import media

dark_knight = media.Movie("The Dark Knight",
                          "The Dark Knight must accept one of the greatest psychological and "
                          "physical tests of his ability to fight injustice.",
                          "https://static.comicvine.com/uploads/original/0/4115/885630-1new_joker_poster_for_the_dark_knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

devil_wears_prada = media.Movie("Devil Wears Prada",
                                "A smart but sensible new graduate lands a job as an assistant to"
                                "Miranda Priestly, the demanding editor-in-chief of a high fashion magazine.",
                                "https://pmcdeadline2.files.wordpress.com/2017/01/the_devil_wears_prada_poster.jpg",
                                "https://www.youtube.com/watch?v=LG0xYJJbko8")

little_women = media.Movie("Little Women", 
                           "Louisa May Alcott's classic, the March sisters confront growing pains,"
                           "financial shortages, family tragedies and romantic rivalries in mid-19th-century Massachusetts.",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcSfdH24TUIxSoWPKDJaXOrYqV17U1Skb32OnPHRBn-8KdVoNdTv",
                           "https://www.youtube.com/watch?v=uKqi9edJVQY")

black_panther = media.Movie("Black Panther",
                            "Black Panther springs into action when an old enemy threatens the fate "
                            "of his nation and the world.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcS9XmH8C4x242GdYwyZtIOFOUqaZ5XMPSxY5zc2nVR_pbteQcSq",  
                            "https://www.youtube.com/watch?v=yLNLPECROMA")

remember_the_titans = media.Movie("Remember the Titans", 
                                  "Two football coaches overcome their differences to turn a group of "
                                  "hostile young men into gridiron champions.",
                                  "http://www.gstatic.com/tv/thumb/movieposters/25848/p25848_p_v8_as.jpg",
                                  "https://www.youtube.com/watch?v=Jk6RhCr1a_A")

ten_things = media.Movie("10 Things I Hate About You", 
                         "90s interpretation of Shakespeare's 'The Taming of the Shrew'",
                         "http://www.gstatic.com/tv/thumb/movieposters/22802/p22802_p_v8_af.jpg",
                         "https://www.youtube.com/watch?v=uE7qjQlfoRs")

movies = [dark_knight, devil_wears_prada, little_women, black_panther, remember_the_titans, ten_things]
fresh_tomatoes.open_movies_page(movies)

