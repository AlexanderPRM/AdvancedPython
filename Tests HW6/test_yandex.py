import pytest

from yandex import create_dir, get_all_info


@pytest.mark.parametrize('token, dirname', [('', 'test2')])
def test_check_status_code(token, dirname):
    response = create_dir(token, dirname)
    assert response.status_code == 201, 'Some error has occurred, the response code is not equal to 201'

@pytest.mark.parametrize('token, dirname', [('', 'test2')])
def test_check_floader_created(token, dirname):
    response = get_all_info(token, dirname)
    assert dirname in response.json()['_embedded']['path']

@pytest.mark.parametrize('token, dirname', [('', 'test2')])
def test_error_status_code(token, dirname):
    response = create_dir(token, dirname)
    assert response.status_code == '201'
