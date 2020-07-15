from pytest import fixture

from utils.imgur import Imgur


def load_test_data():
    pass


@fixture(scope="module")
def user1():
    return Imgur("rohitvyaw1")


@fixture(scope="module")
def user2():
    return Imgur("rohitvyaw2")


@fixture(scope="module")
def user3():
    return Imgur("rohitvyaw3")