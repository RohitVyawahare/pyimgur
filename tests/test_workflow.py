import conf.properties as prop


class TestUser1Account:

    def test_user1_details(self, user1):
        assert "rohitvyaw1" == user1.account.get_details().json().get("data").get("url")

    def test_update_username(self, user1, user3):
        user1.account.update_username("rohitvyaw3")  # user1 -> user3
        assert "rohitvyaw3" == user3.account.get_details().json().get("data").get("url")


class TestUser1Album:

    def test_create_album(self, user3):
        user3.album.create_album_with_auth("new", "new").json()
        user3.album.get_album_details().json()
        assert user3.album.get_album_count() == 1

    def test_image_upload(self, user3):
        user3.image.upload()
        assert len(user3.image.list_all_image_ids()) == 1
        assert sorted(prop.IMAGE_IDS) == sorted(user3.image.list_all_image_ids())

    def test_add_images_to_album(self, user3):
        user3.album.add_images()
        user3.gallery.share_album()
        assert sorted(prop.IMAGE_IDS) == sorted(user3.album.list_album_images())

    def test_fav_album(self, user3):
        user3.album.mark_fav()
        assert user3.album.get_favourites().json().get("data")[0].get("favorite") is True
        assert user3.album.get_favourites().json().get("data")[0].get("favorite_count") == 1


class TestUser2Comment:

    def test_add_comment_on_album(self, user2):
        user2.comment.add_comment(comment_text="Nice pic")
        assert user2.comment.list_all_comment_ids()[0] == prop.COMMENT_ID
        assert len(user2.comment.list_all_comment_ids()) == 1


class TestUser1Comment:

    def test_vote_comment(self, user3):
        # with user1 vote and reply
        user3.comment.vote_up()

    def test_reply(self, user3):
        user3.comment.reply("Thanks!")
        assert user3.comment.list_all_comment_ids()[0] == prop.COMMENT_ID
        assert len(user3.comment.list_all_comment_ids()) == 1

    def test_cleanup(self, user1, user2, user3):
        # restore username
        user3.account.update_username("rohitvyaw1").json()

        # cleanup
        user1.album.delete_all_albums()
        user1.image.delete_all_images()
        user1.comment.delete_all_comments()
        user2.comment.delete_all_comments()
