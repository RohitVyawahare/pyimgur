import requests

import props.properties as prop

from props.constants import BASE_URL
from utils.account import Account
from utils.misc import get_user_config


class Gallery:
    """Imgur Gallery utils"""

    def __init__(self, user):
        self.user = user
        self.api_url = BASE_URL + "gallery/"

        self.config = get_user_config(user)
        self.client_id = self.config.get("client_id")
        self.access_token = self.config.get("access_token")

    def share_album(self, album_id=None, album_title="foo", mature=0, tags="foo"):
        """Share an Album or Image to the Gallery"""

        album_id = album_id if album_id else prop.ALBUM_HASH
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        payload = {
            'title': album_title,
            'mature': mature,
            'tags': tags,
            'terms': 1
        }
        response = requests.post(self.api_url + "album/{}".format(album_id), headers=headers, data=payload)
        assert response.status_code == requests.codes.ok
        return response.json()