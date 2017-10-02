import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "a story of a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=M8Mi0elohJw")

school_of_rock = media.Movie("school of rock",
                             " The story of a music teacher",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

game_of_thrones = media.Movie("The Game of Thrones",
                              "A story about power and authority,light and darkness",
                              "https://upload.wikimedia.org/wikipedia/en/7/7a/Game_of_Thrones_%28soundtrack%29_cover.jpg",
                              "https://www.youtube.com/watch?v=giYeaKsXnsI")

back_of_the_hobbits = media.Movie("The Back of The hobbits",
                                      "An imaginary story",
                                      "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Hobbit_trilogy_dvd_cover.jpg",
                                      "https://www.youtube.com/watch?v=DaGGZ7bBkYI")

lord_of_the_rings = media.Movie("The Lord of The Rings",
                                    "an imaginary story",
                                    "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                                    "https://www.youtube.com/watch?v=V75dMMIW2B4")

movies = [toy_story, avatar, school_of_rock, game_of_thrones, back_of_the_hobbits, lord_of_the_rings]
fresh_tomatoes.open_movies_page(movies)
