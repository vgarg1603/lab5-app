from app import handler

def test_handler():
 result = handler({})
 assert result["status"] == "ok"
 assert result["version"] == "2.0"
