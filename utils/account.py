import requests
import props.properties as prop
from props.constants import BASE_URL
from utils.misc import get_user_config, get_username


class Account:
    """Imgur Account utils"""

    def __init__(self, user):
        self.config = get_user_config(user)
        self.account_id = self.config.get("account_id")
        self.user = user
        self.update_account_mapping()
        self.client_id = self.config.get("client_id")
        self.access_token = self.config.get("access_token")
        self.api_url = BASE_URL + "account/"

    def update_account_mapping(self):
        prop.USER_ID_MAPPING[self.account_id] = self.user

    def get_details(self):
        """get details of self.user"""

        headers = dict(Authorization="Client-ID {}".format(self.client_id))
        response = requests.request("GET", self.api_url + get_username(self.account_id), headers=headers)
        assert response.status_code == requests.codes.ok
        return response

    def update_username(self, new_username):
        """update username from self.user -> new_username"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        payload = {"username": new_username}
        response = requests.put(self.api_url + get_username(self.account_id) + "/settings".format(new_username), headers=headers, data=payload)
        prop.USER_ID_MAPPING[self.account_id] = new_username
        assert response.status_code == requests.codes.ok
        return response

    def get_all_albums(self):
        """get count of total albums for account"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.get(self.api_url + get_username(self.account_id) + "/albums/count", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json().get("data")

    def list_album_ids(self):
        """list of album hashes"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.get(self.api_url + get_username(self.account_id) + "/albums/ids", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json().get("data")

    def get_comments_count(self):
        """get count of total comments for self.user"""

        headers = dict(Authorization="Client-ID {}".format(self.client_id))
        response = requests.get(self.api_url + get_username(self.account_id) + "/comments/count", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json().get("data")

    def get_all_comments(self):
        """get the response of all the comments for self.user"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.get(self.api_url + get_username(self.account_id) + "/comments/ids", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json().get("data")


if __name__ == "__main__":
    pass
