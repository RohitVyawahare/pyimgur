import json
import props.properties as prop

from os import path


def read_config():
    """Get Imgur configuration from json file"""

    config_json = path.join('/pyimgur/conf/config.json')
    with open(config_json) as json_file:
        return json.loads(json_file.read())


def get_user_config(user):
    """Get Imgur configuration for specific user """

    return read_config().get(user)


def get_username(account_id):
    """return user name for account_id"""

    return prop.USER_ID_MAPPING.get(account_id)
