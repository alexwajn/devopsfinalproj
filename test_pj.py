def test_home(client):
    response = client.get("/")
    assert b"<title>Basic Calculator by Alex!</title>" in response.data
    
def test_calc(client):
    response = client.post("/show_res", data={
        "a": "123",
        "b": "456",
        "operation": "add"})
    assert b"579" in response.data
    
