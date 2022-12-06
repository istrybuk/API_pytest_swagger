import pytest
from api import Pets


pt = Pets()


@pytest.mark.regression
def test_go_to_login():
    """Проверка статуса кода когда пользователь вошел в систему"""
    status = pt.post_go_to_login()[0]
    token = pt.post_go_to_login()[2]
    assert token
    assert status == 200, f'User is not logined {status}'


@pytest.mark.xfail(reason='Возвращается id пользователя, должен выводиться список пользователей')
def test_get_list_users():
    """Проверка статуса кода при получении списка пользователей"""
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


@pytest.mark.smoke
def test_post_new_pet():
    """Проверка статуса кода при создании нового питомца"""
    status = pt.post_pet_save()[0]
    pet_id = pt.post_pet_save()[1]
    assert status == 200
    assert pet_id


@pytest.mark.smoke
def test_get_pet_photo():
    """Проверка статуса кода при добавлении фота к питомцу"""
    status = pt.post_pet_photo()[0]
    link = pt.post_pet_photo()[1]
    assert status == 200
    assert link


@pytest.mark.xfail(reason='При обновлении информации о питомце, создается новый питомец с другим ID')
def test_get_pet_info():
    status = pt.get_pet_info()[0]
    pet_id = pt.post_pet_save()[1]
    get_pet_id = pt.get_pet_info()[1]
    assert get_pet_id == pet_id, f' ID pet response {get_pet_id} is not correct {pet_id}'
    assert status == 200


@pytest.mark.smoke
def test_pet_comment():
    """Проверка статуса кода при добавлении комментария к питомцу"""
    status = pt.put_pet_comment()[0]
    id_comment = pt.put_pet_comment()[1]
    assert status == 200
    assert id_comment


@pytest.mark.smoke
def test_pet_delete():
    """Проверка статуса кода при удалении питомца"""
    status_pet = pt.register_add_pet_delete_pet_to_user()[1]
    status_user = pt.register_add_pet_delete_pet_to_user()[0]
    assert status_user
    assert status_pet == 200


@pytest.mark.regression
def test_register_user_and_delete():
    """Проверка статуса кода при удалении юзера"""
    status = pt.post_registered_and_delete()[1]
    assert status == 200


@pytest.mark.regression
def test_check_delete_pet_and_user():
    """Проверка статуса кода при удалении питомца и юзера"""
    status = pt.register_add_pet_delete_pet_to_user()[0]
    assert status == 200


@pytest.mark.regression
def test_check_delete_user():
    """Проверка статуса кода и ответа при удалении юзера"""
    detail = pt.post_registered_and_delete()[2]
    status = pt.post_registered_and_delete()[0]
    assert status != 200
    assert detail == 'Username is taken or pass issue'


@pytest.mark.smoke
def test_get_pet_id():
    """Проверка статуса кода при получении инфо о питомце через запрос get: /pet/id_pet"""
    status = pt.get_pet_info()[0]
    id_pet = pt.get_pet_info()[1]
    name_pet = pt.get_pet_info()[2]
    gender = pt.get_pet_info()[3]
    assert status == 200
    assert id_pet
    assert name_pet
    assert gender
