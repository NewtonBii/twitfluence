
import urllib.request
import json
from .models import Search,

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['TWITTER_API_KEY']
    base_url = app.config['TWITTER_API_BASE_URL']

def get_searches(search):
    """
    Function to retrieve news searches list from the News api
    """

    get_searches_url = base_url.format(search, api_key)
    #get_searches_url = 'https://newsapi.org/v1/searches'.format(search, api_key)

    with urllib.request.urlopen(get_searches_url) as url:
        get_searches_data = url.read()
        get_searches_response = json.loads(get_searches_data)

        searches_results = None

        if get_searches_response['searches']:
            searches_results_list = get_searches_response['searches']
            searches_results = process_results(searches_results_list)

    return searches_results


def process_results(searches_list):
    """Function that process the results list and transforms them into a list of objects
    Args: searches_list: A list of dictionaries that contains news searches details
    Returns:
    searches_results: a list of news searches objects"""

    searches_results = []
    for search_item in searches_list:
        id = search_item.get('id')
        name = search_item.get('name')
        description = search_item.get('description')
        url = search_item.get('url')
        category = search_item.get('category')

        search_object = Search(id, statuses_count, followers_count, favourited_count, list_count)
        searches_results.append(search_object)

    return searches_results
