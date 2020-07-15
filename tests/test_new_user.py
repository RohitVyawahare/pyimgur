

class TestNewUser:
    """Validates that we are running tests on clean setup"""

    def test_no_album_user1(self, user1):
        assert user1.account.get_all_albums() == 0

    def test_no_album_user2(self, user2):
        assert user2.account.get_all_albums() == 0

    def test_no_images_user1(self, user1):
        assert len(user1.image.list_all_image_ids()) == 0

    def test_no_images_user2(self, user2):
        assert len(user2.image.list_all_image_ids()) == 0

    def test_no_comments_user1(self, user1):
        assert user1.account.get_comments_count() == 0

    def test_no_comments_user2(self, user2):
        assert user2.account.get_comments_count() == 0
