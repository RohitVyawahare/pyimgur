import requests
import conf.properties as prop

from conf.constants import BASE_URL
from utils.misc import get_user_config


class Image:
    """Imgur Image utils"""

    def __init__(self, user):
        self.user = user
        self.config = get_user_config(user)
        self.client_id = self.config.get("client_id")
        self.access_token = self.config.get("access_token")

    def upload(self):
        """upload image using url of image"""
        payload = {
            "image": "https://homepages.cae.wisc.edu/~ece533/images/airplane.png",
            "type": "url"
        }
        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.post(BASE_URL + "upload", headers=headers, data=payload)
        assert response.status_code == requests.codes.ok
        prop.IMAGE_IDS.append(response.json().get("data").get("id"))
        return response.json()

    def get_all_images(self):
        """get the data block for all images for self.user"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.get(BASE_URL + "account/" + self.user + "/images", headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json()

    def list_all_image_ids(self):
        """list of all image ids for self.user"""

        image_ids = []
        for block in self.get_all_images().get("data"):
            image_ids.append(block.get("id"))
        return image_ids

    def delete_image(self, image_id):
        """delete image with image_id for self.user"""

        headers = dict(Authorization='Bearer {}'.format(self.access_token))
        response = requests.delete(BASE_URL + "image/{}".format(image_id), headers=headers)
        assert response.status_code == requests.codes.ok
        return response.json()

    def delete_all_images(self):
        """delete all images for self.user"""

        for image_id in self.list_all_image_ids():
            self.delete_image(image_id)
