from utils.account import Account
from utils.album import Album
from utils.comment import Comment
from utils.gallery import Gallery
from utils.image import Image


class Imgur:
    """Imgur utils"""

    def __init__(self, user):
        self.user = user
        self.account = Account(self.user)
        self.album = Album(self.user)
        self.comment = Comment(self.user)
        self.image = Image(self.user)
        self.gallery = Gallery(self.user)