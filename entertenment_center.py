import fresh_tomatoes
import media
# Toy Story movie: movie title, storyline, poster image, movie trailer.
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    )

# Avatar movie: movie title, storyline, poster image, movie trailer.
avatar = media.Movie(
    "Avatar",
    "a story of a marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=M8Mi0elohJw",
    )

# School of rock movie: movie title, storyline, poster image, movie trailer.
school_of_rock = media.Movie(
    "school of rock",
    " The story of a music teacher",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
    )

# Game of thrones TV series: series title,  movie title, storyline,
# poster image,
# trailer of the seventh season.
game_of_thrones = media.Movie(
    "The Game of Thrones",
    "A story about power and authority, light and darkness",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Game_of_Thrones_%28soundtrack%29_cover.jpg",  # NOQA
    "https://www.youtube.com/watch?v=giYeaKsXnsI",
    )

# the hobbit movie:  movie title, storyline, poster image, movie trailer.
back_of_the_hobbits = media.Movie(
    "The Back of The hobbits",
    "An imaginary story",
    "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Hobbit_trilogy_dvd_cover.jpg",  # NOQA
    "https://www.youtube.com/watch?v=DaGGZ7bBkYI",
    )

# lord of the ring movie:  movie title, storyline, poster image, movie trailer.
lord_of_the_rings = media.Movie(
    "The Lord of The Rings",
    "an imaginary story",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",  # NOQA
    "https://www.youtube.com/watch?v=V75dMMIW2B4",
    )

movies = [
    toy_story,
    avatar,
    school_of_rock,
    game_of_thrones,
    back_of_the_hobbits,
    lord_of_the_rings
    ]
fresh_tomatoes.open_movies_page(movies)
