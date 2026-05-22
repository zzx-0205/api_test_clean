import pytest
from utils.api_client import APIClient
#pytest 的"公共夹具",所有测试共享的前置条件
@pytest.fixture(scope="session")#整个测试会话只执行一次
def api_client():
    client = APIClient()
    yield client#yield:把对象传给测试用例，结束后自动清理
    client.close()