# Validate problem statement

import props.constants as cons
import props.properties as prop


class TestUser1Account:

    def test_user1_details(self, setup, user1):
        # Get account details of the logged in ‘User 1’.

        assert cons.USER1 == user1.account.get_details().json().get("data").get("url")

    def test_update_username(self, user1, user3):
        # Update the username and validate the new username.

        user1.account.update_username(cons.USER3)  # user1 -> user3
        assert cons.USER3 == user3.account.get_details().json().get("data").get("url")


class TestUser1Album:

    def test_create_album(self, user3):
        # As ‘User 1’ which is now 'User 3'(after rename) create a new album.

        user3.album.create_album_with_auth("new", "new").json()
        user3.album.get_album_details().json()
        assert user3.album.get_album_count() == 1

    def test_image_upload(self, user3):
        # Upload image to account

        user3.image.upload()
        assert len(user3.image.list_all_image_ids()) == 1
        assert sorted(prop.IMAGE_IDS) == sorted(user3.image.list_all_image_ids())

    def test_add_images_to_album(self, user3):
        # Add a few public images inside the newly created album.

        user3.album.add_images()
        user3.gallery.share_album()
        assert sorted(prop.IMAGE_IDS) == sorted(user3.album.list_album_images())

    def test_fav_album(self, user3):
        # Mark the album as your favourite.

        user3.album.mark_fav()
        assert user3.album.get_favourites().json().get("data")[0].get("favorite") is True
        assert user3.album.get_favourites().json().get("data")[0].get("favorite_count") == 1


class TestUser2Comment:

    def test_add_comment_on_album(self, user2):
        # Log in as a different user(User 2).
        # Comment on top of the new album that is created by ‘User 1’. Log out as ‘User 2’.

        user2.comment.add_comment(comment_text="Nice pic")
        assert user2.comment.list_all_comment_ids()[0] == prop.COMMENT_ID
        assert len(user2.comment.list_all_comment_ids()) == 1


class TestUser1Comment:

    def test_vote_comment(self, user3):
        user3.comment.vote_up()

    def test_reply(self, user3):
        # Log back as ‘User 1’ access the comment by ‘User 2’, vote it and reply back.

        user3.comment.reply("Thanks!")
        assert user3.comment.list_all_comment_ids()[0] == prop.COMMENT_ID
        assert len(user3.comment.list_all_comment_ids()) == 1

    def test_restore_username(self, user1, user3):
        # Restore the user3 -> user1

        user3.account.update_username(cons.USER1)
        assert cons.USER1 == user1.account.get_details().json().get("data").get("url")