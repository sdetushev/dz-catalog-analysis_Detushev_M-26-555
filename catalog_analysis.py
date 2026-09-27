import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

#Stage 1

def average_rating(movies: list[dict]) -> float:
    """Return the average movie rating with round"""
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple:
    """Return the oldest, newest and average movie age with ceil"""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return oldest, newest, average


def duration_in_hours(minutes: int) -> str:
    """Convert duration in minutes to ##ч ##м"""
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"

#Stage 2

def rating_tier(rating: float) -> str:
    """Return movie category"""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

def decade_label(year: int) -> str:
    """Return category based on the movie year"""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

#Stage 3

def demonstrate_loops(movies: list[dict]) -> None:
    """for, continue, while, break and else"""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    """Count movies longer than duration threshold"""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

#Stage 4

def normalize_title(title: str) -> str:
    """Convert movie title to Title Case"""
    words = title.split()
    normalized_words = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized_words)

def make_slug(title: str) -> str:
    """Convert normalized movie title to slug"""
    return title.lower().replace(" ", "-")

def format_report_line(movie: dict) -> str:
    """Return formatted report line for movie"""
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {genres}'
    )

#Stage 5

def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    """Return movie titles sorted by rating in desc"""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple[str, float]]:
    """Return the top N movies as title and rating tuples"""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

#Stage 6

def count_by_genre(movies: list[dict]) -> dict[str, int]:
    """Return the number of movies for each genre"""
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts

def actor_filmography(movies: list[dict]) -> dict[str, list[str]]:
    """Return movie titles grouped by actor"""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography

def above_average_movies(movies: list[dict]) -> dict[str, float]:
    """Return titles and ratings of movies rated above average"""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

#Stage 7

def all_genres(movies: list[dict]) -> set[str]:
    """Return all unique genres in the movie catalog"""
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres

def common_actors(movie1: dict, movie2: dict) -> set[str]:
    """Return actors who appear in both movies"""
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2

def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    """Return genres found in movies_a but not in movies_b"""
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

#Stage 8

def iter_high_rated(movies: list[dict], min_rating: float = 8.0):
    """Iterate high rated movies"""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def demonstrate_high_rated(movies: list[dict]) -> None:
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

total_duration = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

#Stage 9

def build_report(movies: list[dict]) -> None:
    average = average_rating(movies)
    _, _, average_age = catalog_age_stats(movies)
    top_movies = top_n_by_rating(movies)
    genre_counts = count_by_genre(movies)
    genres = all_genres(movies)
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print("\nТоп-3 фильма:")
    for title, _ in top_movies:
        movie = next(movie for movie in movies if movie["title"] == title)
        print(f"  {format_report_line(movie)}")
    print("\nФильмов по жанрам:")
    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: item[1],
        reverse=True,
    )
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print(f"\nВсе жанры каталога: {', '.join(sorted(genres))}")

def main() -> None:
    build_report(movies)

if __name__ == "__main__":
    main()