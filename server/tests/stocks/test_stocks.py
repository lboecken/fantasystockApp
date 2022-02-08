import json


def test_stock_response(test_app, test_db, create_login_fake_user):
    # GIVEN
    access_token = create_login_fake_user
    client = test_app.test_client()
    # WHEN
    response = client.get('/stocks/price/tsla',
                          headers={'Authorization': f'Bearer {access_token}'})
    data = json.loads(response.data.decode())
    # THEN
    assert response.status_code == 200
    assert data['data']['companyName'] == "Tesla Inc"


def test_stock_invalid_symbol(test_app, test_db, create_login_fake_user):
    # GIVEN
    access_token = create_login_fake_user
    client = test_app.test_client()
    # WHEN
    response = client.get('/stocks/price/tsasla',
                          headers={'Authorization': f'Bearer {access_token}'})
    data = json.loads(response.data.decode())
    # THEN
    assert response.status_code == 400
    assert data['message'] == 'Unknown symbol'
