from app import app


def client():
    return app.test_client()


def test_health():
    resp = client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_greet_default():
    resp = client().get("/greet")
    assert resp.get_json()["message"] == "Hello, world!"


def test_greet_spanish():
    resp = client().get("/greet?lang=es&name=Daniela")
    assert resp.get_json()["message"] == "Hola, Daniela!"


def test_greet_unknown_lang_falls_back_to_english():
    resp = client().get("/greet?lang=xx&name=friend")
    assert resp.get_json()["message"] == "Hello, friend!"
