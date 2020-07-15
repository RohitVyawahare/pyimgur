
class TestUser1Account:

    def test_user1_details(self, user1):
        print(user1.account.get_details())

    def test_update_username(self, user1):
        user1.account.update_username("rohitvyaw3")  # user1 -> user3


class TestUser1Album:

    def test_create_album(self, user3):
        pass

    def test_add_images_to_album(self, user1):
        pass

    def test_fav_album(self, user1):
        pass


class TestUser2Comment:

    def test_add_comment_on_album(self, user2):
        pass


class TestUser1Comment:

    def test_vote_comment(self, user1):
        pass

    def test_reply(self, user1):
        pass


