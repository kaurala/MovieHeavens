from .searchers import movie_heaven, tl95

def get_all_down_url_list(movie_name):
    heaven = movie_heaven.MovieHeaven()
    try:
        heaven_list = heaven.get_display_content(movie_name)
    except Exception as e:
        heaven_list = []
    Tl95 = tl95.TL95()
    tl95_list = Tl95.get_display_content(movie_name)
    all_list = tl95_list + heaven_list
    return all_list