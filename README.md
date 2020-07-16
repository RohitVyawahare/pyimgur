# Pyimgur

Python implementation of Imgur using https://apidocs.imgur.com/?version=latest#31c72664-59c1-426f-98d7-ac7ad6547cc2 and test infrastructure to validate various workflows using pytest

# Techstack:

- Python3
- Pytest
- Docker/Containers

# Pre-requisites:

- Docker installation (Refer https://docs.docker.com/engine/install/)
- config.json (This file basically json holds client id, client secret, access token, refresh token which is required for authentication and authorization)

# Directory structure:

```
|--conf
|  |-- config.json          -> this json holds client id, client secret, access token, refresh token for test users
|  |-- config.json.template -> template
|--props
|  |-- constants.py         -> constants e.g. base api url
|  |-- properties.py        -> place to hold run time variables
|--tests
|  |-- test_new_user.py     -> validate setup is clean
|  |-- test_workflow.py     -> validate problem statement
|--utils
|  |-- account.py           -> user account utils
|  |-- album.py             -> album utils
|  |-- auth.py              -> auth utils
|  |-- comment.py           -> comment utils
|  |-- gallery.py           -> gallery utils
|  |-- image.py             -> image utils
|  |-- imgur.py             -> imgur utils
|  |-- misc.py              -> misc utils e.g. read config for user etc
|-- .dockerignore           -> don't add conf/config.json to docker image
|-- .gitignore              -> ignore pycache, conf/config.json etc
|-- Dockerfile              -> Dockerfile to build image for the code. Used python:alpine image which is very lightweight
|-- run.sh                  -> entry point for container
|-- api.py                  -> just a test script for debugging
```

# How to build:

Run command:

```docker build -t rohitvyaw/pyimgur:latest .```

# How to run tests

Run command:

```docker run -v conf:/pyimgur/conf -v /tmp/report:/report rohitvyaw/pyimgur:latest```

Sample output:

```
rohit@Rohits-MacBook-Pro ~/c/pyimgur> docker run -v conf:/pyimgur/conf rohitvyaw/pyimgur:latest
Executing tests...
============================= test session starts ==============================
platform linux -- Python 3.8.4, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.8.4', 'Platform': 'Linux-4.9.125-linuxkit-x86_64-with', 'Packages': {'pytest': '5.4.3', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.1.1', 'metadata': '1.10.0'}}
rootdir: /pyimgur
plugins: html-2.1.1, metadata-1.10.0
collecting ... collected 16 items

tests/test_new_user.py::TestNewUser::test_no_album_user1 PASSED
tests/test_new_user.py::TestNewUser::test_no_album_user2 PASSED
tests/test_new_user.py::TestNewUser::test_no_images_user1 PASSED
tests/test_new_user.py::TestNewUser::test_no_images_user2 PASSED
tests/test_new_user.py::TestNewUser::test_no_comments_user1 PASSED
tests/test_new_user.py::TestNewUser::test_no_comments_user2 PASSED
tests/test_workflow.py::TestUser1Account::test_user1_details PASSED
tests/test_workflow.py::TestUser1Account::test_update_username PASSED
tests/test_workflow.py::TestUser1Album::test_create_album PASSED
tests/test_workflow.py::TestUser1Album::test_image_upload PASSED
tests/test_workflow.py::TestUser1Album::test_add_images_to_album PASSED
tests/test_workflow.py::TestUser1Album::test_fav_album PASSED
tests/test_workflow.py::TestUser2Comment::test_add_comment_on_album PASSED
tests/test_workflow.py::TestUser1Comment::test_vote_comment PASSED
tests/test_workflow.py::TestUser1Comment::test_reply PASSED
tests/test_workflow.py::TestUser1Comment::test_restore_username PASSED

--------------- generated html file: file:///report/report.html ----------------
======================== 16 passed in 81.93s (0:01:21) =========================
Please check report.html at /tmp/report
```
Note that at the end of test execution, html report gets created as follows:


# Pending items:

Note that this repository is _work-in-progress_. Following are high level pending items.

- Schema validations
- Negative tests
- CI/CD integration? 

