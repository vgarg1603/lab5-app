from app import handler

def test_handler():
    result = handler({})
    assert result["status"] == "ok"
    assert result["version"] == "1.0"
