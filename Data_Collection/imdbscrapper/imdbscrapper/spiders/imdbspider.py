import scrapy
import json
from imdbscrapper.items import Info


class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        raw_data = response.css("script[id='__NEXT_DATA__']::text").get()
        
        json_data = json.loads(raw_data)
        
        needed_data= json_data['props']['pageProps']['pageData']['chartTitles']['edges']
        
        
        information = Info()
        
        
        
        for movie in needed_data:
            
                information['title'] =  movie['node']['titleText']['text'],
                information['movie_rank'] =  movie['currentRank'],
                information['genres'] =  [genre['genre']['text'] for genre in movie['node'].get('titleGenres', {}).get('genres', [])],
                information['release_day'] =  movie['node']['releaseDate']['day'],
                information['release_month'] =  movie['node']['releaseDate']['month'],
                information['release_year'] =  movie['node']['releaseYear']['year'],
                information['movie_length'] =  movie['node']['runtime']['seconds'],
                information['rating'] =  movie['node']['ratingsSummary']['aggregateRating'],
                information['vote_count'] =  movie['node']['ratingsSummary']['voteCount'],
                information['description'] =  movie['node']['plot']['plotText']['plainText']
                
            
                yield information
        
        
        
        
        
        
        # for movie in needed_data:
        #     yield {
        #         'title': movie['node']['titleText']['text'],
        #         'movie_rank': movie['currentRank'],
        #         'genres': [genre['genre']['text'] for genre in movie['node'].get('titleGenres', {}).get('genres', [])],
        #         'release_day': movie['node']['releaseDate']['day'],
        #         'release_month': movie['node']['releaseDate']['month'],
        #         'release_year': movie['node']['releaseYear']['year'],
                
        #         'movie_length': movie['node']['runtime']['seconds'],
        #         'rating': movie['node']['ratingsSummary']['aggregateRating'],
        #         'vote_count': movie['node']['ratingsSummary']['voteCount'],
        #         'description': movie['node']['plot']['plotText']['plainText'],
                
        #     }
                
                
            
            
                
        
        
        
