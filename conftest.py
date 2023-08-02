import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in/shop")
    return driver

# def pytest_metadata(metadata):
#     # to add
#     metadata["class"]='credence123'
#     metadata['Batch']=ct_14_15
#     #to remove
#     metadata.pop('Python',None)

@pytest.fixture(params=[
    ("Credencetest@test.com","Credence@123"),
    ("Credencetest@test.com1","Credence@123"),
    ("Credencetest@test.com","Credence@1234"),
    ("Credencetest@test.com1","Credence@1234"),
    ("credencetest@test.com","credence@123")
])

def get_data_for_login(request):
    return request.param



@pytest.fixture()
def comm_file():
    # options=webdriver.ChromeOptions()
    # options.add_experimental_option('detach', True)
    driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.shopclues.com/")
    return driver


@pytest.fixture(params=[
    ("rahul.ipe@gmail.com","rahul1803sarda@#$%"),
    ("rahul.ipe@gmai.com","rahul1803sarda@#$%"),
    ("rahul.ipe@gmail.com","rahul1803sarda@#$"),
    ("rahulipe@gmail.com","rahul1803sarda@#$%"),
    ("rahul.ip@gmail.com","rahul1803sarrda@#")
])
def shopclue_login_data (request):
    return request.param