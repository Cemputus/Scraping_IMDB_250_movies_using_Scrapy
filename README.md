

# IMDb Top 250 Movies Scraper 🎬  

This project is a web scraping tool built with **[Scrapy](https://scrapy.org/)** to extract data from IMDb's Top 250 Movies list. The scraper retrieves key movie details, including ranking, genre, release date, runtime, ratings, and more.  

## Features 🚀  

✔ Scrapes the **Top 250 movies** from IMDb  
✔ Extracts **detailed movie information**, including:  
   - 🎬 **Title**  
   - 🏆 **Rank**  
   - 🎭 **Genres**  
   - 📅 **Release Date (Day, Month, Year)**  
   - ⏳ **Movie Length (in seconds)**  
   - ⭐ **IMDb Rating**  
   - 🗳 **Vote Count**  
   - 📝 **Description**  

✔ Stores data in a structured format for further analysis  

## Installation 🛠  

Ensure you have Python installed, then follow these steps:  

```sh
# Clone the repository
git clone https://github.com/Cemputus/Scraping_IMDB_250_movies_using_Scrapy.git

# Navigate to the project directory
cd Scraping_IMDB_250_movies_using_Scrapy

# Install dependencies
pip install -r requirements.txt
```

## Usage ▶  

Run the Scrapy spider to start scraping IMDb data:  

```sh
scrapy crawl imdbspider -o movies.json
```

This will generate a `movies.json` file containing the extracted movie details.

## Extracted Fields 📝  

The scraper extracts the following fields from IMDb:  

| Field Name       | Description                                      |
|-----------------|--------------------------------------------------|
| `title`         | Movie title                                      |
| `movie_rank`    | Movie's current ranking in the Top 250 list      |
| `genres`        | List of genres associated with the movie         |
| `release_day`   | Day of movie release                             |
| `release_month` | Month of movie release                           |
| `release_year`  | Year of movie release                            |
| `movie_length`  | Duration of the movie (in seconds)               |
| `rating`        | IMDb aggregate rating                            |
| `vote_count`    | Number of votes received                         |
| `description`   | Short plot summary of the movie                  |

## Example Output 📊  

```json
{
    "title": "The Shawshank Redemption",
    "movie_rank": 1,
    "genres": ["Drama"],
    "release_day": 23,
    "release_month": 9,
    "release_year": 1994,
    "movie_length": 8520,
    "rating": 9.3,
    "vote_count": 2700000,
    "description": "Two imprisoned men bond over a number of years..."
}
```

## Contributing 🤝  

Feel free to fork this repository and contribute by submitting pull requests. Any improvements, bug fixes, or enhancements are welcome!  

## Author ✍  

Developed by **EMMANUEL NSUBUGA**  

For more details on Scrapy, visit **[Scrapy's official documentation](https://scrapy.org/)**.  


