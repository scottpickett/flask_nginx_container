import app.app as app

def test_root_get():
    response = app.app.test_client().get('/')
    assert response.status_code == 200
    assert 'Default Data' in str(response.data)
    

def test_root_post():
    response = app.app.test_client().post('/', data=dict(data='form test'))
    assert response.status_code == 200
    assert 'tset mrof' in str(response.data)
    

def test_api_get():
    response = app.app.test_client().get('/api')
    assert response.status_code == 200
    assert response.data == b'{"data":"Default Data","status":"Default"}\n'
    

def test_api_post_with_data():
    response = app.app.test_client().post('/api', data=dict(data='test'))
    assert response.status_code == 200
    assert response.data == b'{"data":"tset","status":"Success"}\n'


def test_api_post_with_ints():
    response = app.app.test_client().post('/api', data=dict(data=12345))
    assert response.status_code == 200
    assert response.data == b'{"data":"54321","status":"Success"}\n'
    
    
def test_api_post_without_data():
    response = app.app.test_client().post('/api')
    assert response.status_code == 200
    assert response.data == b'{"data":"Error - No Data Submitted","status":"Error"}\n'
    

