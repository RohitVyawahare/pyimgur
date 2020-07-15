from pytest import fixture

import conf.constants as cons
from utils.imgur import Imgur


@fixture(scope='module')
def setup():
    user1 = Imgur(cons.USER1)
    user2 = Imgur(cons.USER2)

    print("\nSetup...")
    user1.delete_all()
    user2.delete_all()
    yield
    print("\nTeardown...")
    user1.delete_all()
    user2.delete_all()


@fixture(scope="module")
def user1():
    return Imgur(cons.USER1)


@fixture(scope="module")
def user2():
    return Imgur(cons.USER2)


@fixture(scope="module")
def user3():
    return Imgur(cons.USER3)