import requests
import conf.properties as prop
from conf.constants import BASE_URL

from utils.account import Account
from utils.misc import get_user_config


class Comment:
    """Imgur Comment utils"""

    def __init__(self, user):
        self.user = user
        self.api_url = BASE_URL + "comment/"
        self.account = Account(self.user)

        self.config = get_user_config(user)
        self.access_token = self.config.get("access_token")
        self.client_id = self.config.get("client_id")

    def vote(self, vote_type, comment_id=None):
        """"""

        comment_id = comment_id if comment_id else prop.COMMENT_ID
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.request("POST", self.api_url + str(comment_id) + "/vote/" + vote_type, headers=headers)
        assert response.status_code == requests.codes.ok
        return response

    def vote_up(self, comment_id=None):
        """vote up comment_id"""

        comment_id = comment_id if comment_id else prop.COMMENT_ID
        self.vote("up", comment_id)

    def vote_down(self, comment_id=None):
        """vote down comment_id"""

        comment_id = comment_id if comment_id else prop.COMMENT_ID
        self.vote("down", comment_id)

    def add_comment(self, comment_text, image_id=None):
        """Creates a new comment, returns the ID of the comment"""

        image_id = image_id if image_id else prop.ALBUM_HASH
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        payload = {
            "image_id": image_id,
            "comment": comment_text
        }
        response = requests.post(self.api_url, headers=headers, data=payload)
        assert response.status_code == requests.codes.ok
        prop.COMMENT_ID = response.json().get("data").get("id")
        return response

    def reply(self, comment_text, comment_id=None, image_id=None):
        """Creates a new comment, returns the ID of the comment"""

        image_id = image_id if image_id else prop.ALBUM_HASH
        comment_id = comment_id if comment_id else prop.COMMENT_ID
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        payload = {
            "image_id": image_id,
            "comment": comment_text
        }
        response = requests.post(self.api_url + str(comment_id), headers=headers, data=payload)
        assert response.status_code == requests.codes.ok
        prop.COMMENT_ID = response.json().get("data").get("id")
        return response

    def list_all_comment_ids(self):
        """return the list of comment ids for self.user"""

        comment_ids = []
        for block in self.account.get_all_comments():
            comment_ids.append(block)
        return comment_ids

    def delete_comment(self, comment_id):
        """delete comment with comment_id for self.user"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.delete(self.api_url + str(comment_id), headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json()

    def delete_all_comments(self):
        """delete all comments for self.user"""
        for comment_id in self.list_all_comment_ids():
            self.delete_comment(comment_id)