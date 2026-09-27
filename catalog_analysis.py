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
    """Count movies longer than the duration threshold"""
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


def main():
    print("Hello from dz-catalog-analysis-detushev-m-26-555!")

if __name__ == "__main__":
    main()
