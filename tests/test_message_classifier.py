from src.message_classifier import classify_message

def test_server_message():
    message = "[Server] 거래가 완료되었습니다"
    assert classify_message(message) == "server"

def test_client_message():
    message = "[Client] 안녕하세요"
    assert classify_message(message) == "client"

def test_unknown_message():
    message = "hello"
    assert classify_message(message) == "unknown"
