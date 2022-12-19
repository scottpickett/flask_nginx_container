import app.server as server

def test_submit_data():
    assert server.submit_data('string') == 'gnirts'
