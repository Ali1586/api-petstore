import pytest
import random
from api.petstore_client import PetstoreClient
from pages.page_login import LoginPage
from faker import Faker

@pytest.fixture
def pet_api():
    return PetstoreClient()

@pytest.fixture
def random_pet_id():
    return random.randint(10000, 99999)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def fake_person():
    f = Faker()
    return {"first_name": f.first_name()}