from utils.imgur import Imgur

try:
    # get account details
    user1 = Imgur("rohitvyaw1")
    print(user1.account.get_details().json())

    # update username and get account details
    print(user1.account.update_username("rohitvyaw3").json())
    user1 = Imgur("rohitvyaw3")
    print(user1.account.get_details().json())

    # create new album
    print(user1.album.create_album_with_auth("new", "new").json())
    print(user1.album.get_album_details().json())

    # upload images
    print(user1.image.upload())

    # add image to album
    print(user1.album.add_images())
    print(user1.album.get_album_images())
    print(user1.gallery.share_album())

    # mark as fav
    print(user1.album.mark_fav())

    # with user2 comment on new album
    user2 = Imgur("rohitvyaw2")
    user2.comment.add_comment(comment_text="Nice pic")

    # with user1 vote and reply
    user1.comment.vote_up()
    user1.comment.reply("Thanks!")
except Exception:
    raise
finally:
    # restore username
    print(user1.account.update_username("rohitvyaw1").json())
    user1 = Imgur("rohitvyaw1")
    print(user1.account.get_details().json())

    # cleanup
    user1.album.delete_all_albums()
    user2.album.delete_all_albums()

    user1.image.delete_all_images()
    user2.image.delete_all_images()

    user1.comment.delete_all_comments()
    user2.comment.delete_all_comments()
