import json
import uuid
import requests


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def post_new_register(self) -> json:
        """Запрос к Swagger сайта для регистрация нового пользователя"""
        # e = uuid.uuid4().hex  # генерация для email
        data = {"email": 'test@21.by',
                "password": '12345',
                "confirm_password": '12345'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json()
        reg_id = my_id.get('id')
        reg_status = res.status_code
        return reg_status, reg_id

    def post_go_to_login(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": 'test@21.by',
                "password": '12345'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        login_token = res.json()['token']
        login_id = res.json()['id']
        log_status = res.status_code
        return log_status, login_id, login_token

    def delete_go_to_users(self) -> json:
        """Запрос к Swagger сайта для удаление юзера по его ID"""
        my_id = str(Pets().post_go_to_login()[1])
        my_token = Pets().post_go_to_login()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers)
        status = res.status_code
        return status

    def get_list_users(self) -> json:
        """Запрос к Swagger сайта для получения id пользователей"""
        my_token = Pets().post_go_to_login()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.text
        return status, my_id

    def post_pet_save(self) -> json:
        """Запрос к Swagger сайта для cоздание нового питомца"""
        my_token = Pets().post_go_to_login()[2]
        my_id = Pets().post_go_to_login()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": "Tosha",
                "type": "dog",
                "gender": "male",
                "age": 50,
                "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return status, pet_id

    def post_pet_photo(self) -> json:
        """Запрос к Swagger сайта для добавление фото к питомцу"""
        my_token = Pets().post_go_to_login()[2]
        pet_id = Pets().post_pet_save()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        # pic = open('tests\Photos\dog.jpg', 'rb')  # Для нормальной передачи.
        files = {'pic': ('что-угодно.jpg',
                         open('C:\\Users\\Scribl\\PycharmProjects\\API_TT\\tests\\photos\\dog.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def put_pet_like(self) -> json:
        """Запрос к Swagger сайта для добавления лайка питомцу"""
        my_token = Pets().post_go_to_login()[2]
        pet_id = str(Pets().post_pet_save()[1])   # вернулся другой id пета
        headers = {'Authorization': f'Bearer {my_token}'}
        # data = {"id": 557}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        # res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status, pet_id

    def patch_pet_save(self) -> json:
        """Запрос к Swagger сайта для обновлении информации о питомце"""
        my_token = Pets().post_go_to_login()[2]
        my_id = Pets().post_go_to_login()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": "Tosha",
                "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']  # вернулся другой id пета
        status = res.status_code
        return status, pet_id

    def put_pet_comment(self) -> json:
        """Запрос к Swagger сайта для добавления комментария питомцу"""
        my_token = Pets().post_go_to_login()[2]
        pet_id = Pets().get_pet_info()[1]
        my_id = Pets().get_list_users()[1]
        message = 'Hello world!'
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 0,
                "pet_id": pet_id,
                "date": "2022-11-27T17:06:46.956Z",
                "message": message,
                "user_id": my_id,
                "user_name": "string"}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        id_comment = res.json()['id']
        return status, id_comment

    def get_pet_info(self) -> json:
        """Запрос к Swagger сайта для получения инфо о питомце"""
        my_token = Pets().post_go_to_login()[2]
        pet_id = Pets().post_pet_save()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        id_pet = res.json()['pet']['id']
        name_pet = res.json()['pet']['name']
        gender = res.json()['pet']['gender']
        owner_id = res.json()['pet']['owner_id']
        types = res.json()['pet']['type']
        return status, id_pet, name_pet, gender, owner_id, types

    def post_pet_list(self) -> json:
        """Запрос к Swagger сайта для получения информации о питомцах пользователя"""
        my_token = Pets().post_go_to_login()[2]
        # my_id = str(Pets().get_list_users()[1])
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"skip": 0,
                "num": 10,
                "type": "string",
                "petName": "string",
                "user_id": 0}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_go_to_pets(self) -> json:
        """Запрос к Swagger сайта для удаление питомца по его ID"""
        pet_id = Pets().post_pet_save()[1]
        my_token = Pets().post_go_to_login()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def post_registered_and_delete(self) -> json:
        e = uuid.uuid4().hex
        data = {"email": f'test1@{e}.ru',
                "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status_delete_user = res.status_code
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        deletion_verification_status = res.status_code
        detail = res.json()['detail']
        return deletion_verification_status, status_delete_user, detail

    def register_add_pet_delete_pet_to_user(self) -> json:
        e = uuid.uuid4().hex
        data = {"email": f'test1@{e}.ru',
                "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": "Tosha",
                "type": "dog",
                "age": 50,
                "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status_delete_pet = res.status_code
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status_delete_user = res.status_code
        return status_delete_user, status_delete_pet

# Pets().register_add_pet_delete_pet_to_user()
# Pets().post_registered_and_delete()
# Pets().post_new_register()
# Pets().post_go_to_login()
# Pets().delete_go_to_users()
# Pets().get_list_users()
# Pets().post_pet()
# Pets().post_pet_photo
# Pets().get_pet_like()
# Pets().patch_pet_save()
# Pets().put_pet_comment()
# Pets().get_pet_info()
# Pets().post_pet_list()
# Pets().delete_go_to_pets()
