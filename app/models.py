
class TwitterRequest:
    """search class to define search Objects"""

    def __init__(self, id, name,description, profile_image_url_https, statuses_count, followers_count, favourited_count, list_count):
        self.id = id
        self.name = name
        self.description = description
        self.profile_image_url_https = profile_image_url_https
        self.statuses_count = statuses_count
        self.followers_count = followers_count
        self.favourited_count = favourited_count
        self.list_count = list_count
