from api import Pets

pt = Pets()


def test_register_new_users():
    status = pt.post_new_register()[0]
    id = pt.post_new_register()[1]
    assert id
    assert status == 200


def test_to_login():
    status = pt.post_go_to_login()[0]
    assert status == 200


def test_get_token():
    status = pt.post_go_to_login()[0]
    token = pt.post_go_to_login()[2]
    assert token
    assert status == 200

def test_delete():
    pt.post_go_to_login()
    status = pt


# def test_list_users():
#     status = pt.get_list_users()[0]
#     my_id = pt.get_list_users()[1]
#     assert status == 200
#     assert my_id
#
#
# def test_post_new_pet():
#     status = pt.post_pet()[1]
#     pet_id = pt.post_pet()[0]
#     assert status == 200
#     assert pet_id
#
#
# def test_get_pet_photo():
#     status = pt.get_pet_photo()[0]
#     link = pt.get_pet_photo()[1]
#     assert status == 200
#     assert link
