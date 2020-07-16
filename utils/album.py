import requests

import props.properties as prop

from props.constants import BASE_URL
from utils.account import Account
from utils.misc import get_user_config, get_username


class Album:
    """Imgur Album utils"""

    def __init__(self, user):
        self.user = user
        self.api_url = BASE_URL + "album/"
        self.account = Account(self.user)

        self.config = get_user_config(user)
        self.client_id = self.config.get("client_id")
        self.access_token = self.config.get("access_token")

    def create_album_with_auth(self, album_name, album_description="Foo"):
        """create empty album with self.user access token"""

        payload = {
            "title": album_name,
            "description": album_description,
            "privacy": "public"
        }
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.post(self.api_url, headers=headers, data=payload)
        assert response.status_code == requests.codes.ok
        prop.ALBUM_HASH = response.json().get("data").get("id")
        return response

    def get_album_details(self, album_hash=None):
        """Get album details of album_hash if provided else use from properties.py"""

        album_hash = album_hash if album_hash else prop.ALBUM_HASH
        headers = dict(Authorization="Client-ID {}".format(self.client_id))
        response = requests.get(self.api_url + "/" + album_hash, headers=headers)
        assert response.status_code == requests.codes.ok
        return response

    def add_images(self, album_hash=None, image_ids=None):
        """add already uploaded images to given album else use from properties.py"""

        album_hash = album_hash if album_hash else prop.ALBUM_HASH
        image_ids = image_ids if image_ids else prop.IMAGE_IDS
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        payload = {
            "ids[]": image_ids
        }
        response = requests.post(self.api_url + album_hash + "/add", headers=headers, data=payload)
        assert response.status_code == requests.codes.ok
        return response.json()

    def get_album_images(self, album_hash=None):
        """get the list of images for album_hash"""

        album_hash = album_hash if album_hash else prop.ALBUM_HASH
        headers = dict(Authorization="Client-ID {}".format(self.client_id))
        response = requests.get(self.api_url + "/" + album_hash + "/images", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json()

    def list_album_images(self, album_hash=None):
        """list of image ids under album_hash"""

        image_ids = []
        for block in self.get_album_images(album_hash).get("data"):
            image_ids.append(block.get("id"))
        return image_ids

    def get_album_count(self):
        """get total count of albums for self.user"""
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.get(self.account.api_url + get_username(self.account.account_id) + "/albums/count", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json().get("data")

    def delete_album(self, album_hash):
        """delete album for given hash"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.delete(self.api_url + album_hash, headers=headers)
        assert response.status_code == requests.codes.ok
        return response

    def delete_all_albums(self):
        """delete all albums for self.user"""

        for album_id in self.account.list_album_ids():
            self.delete_album(album_id)

    def mark_fav(self, album_hash=None):
        """mark album of given hash as fav if provided else use from properties.py"""

        album_hash = album_hash if album_hash else prop.ALBUM_HASH
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.post(self.api_url + album_hash + "/favorite", headers=headers)
        assert response.status_code == requests.codes.ok
        return response

    def get_favourites(self):
        """get favourites for user"""

        headers = dict(Authorization="Client-ID {}".format(self.client_id))
        response = requests.get(self.account.api_url + get_username(self.account.account_id) + "/unorganized_favorites", headers=headers)
        assert response.status_code == requests.codes.ok
        return response

    def comment(self):
        pass

    def vote(self):
        pass

    def reply(self):
        pass


if __name__ == "__main__":
    pass
