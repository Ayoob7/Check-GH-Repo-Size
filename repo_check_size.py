import requests
import json
import math
import sys


# Check whether a URL is a GitHub Repository
def return_url_from_github(url):
    if url.startswith('https://github.com/'):
        return url.split('https://github.com')[1]
    else:
        print('ERROR - ' + url + ' is not a GitHub repository')
        exit(0)


# Clean the URLs before
def url_cleaning(url):
    if url is not None:
        temp = url.split('/')
        org = temp[1]
        repo = temp[2]
        repo = repo.split('.git')[0]
        return 'https://api.github.com/repos' + '/' + org + '/' + repo


# Check the Repo size
def check_repo_size(url, json=json):
    cleaned_url = url_cleaning(return_url_from_github(url))
    r = requests.get(cleaned_url)
    json = json.loads(r.text)
    return json['size']


# Pretty print the Repo size.
def pretty_print_size(size):
    """"This method is based on the answer given by StackOverflow user - https://stackoverflow.com/users/2062973/james-sapam
    to the question posed here - https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    """
    size_bytes = size * 1024
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


if sys.argv[1]:
    print('\n')
    print("Size of "+sys.argv[1]+" is = "+pretty_print_size(check_repo_size(sys.argv[1])))
    print('\n')