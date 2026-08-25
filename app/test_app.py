"""Tests for the coffee API. You do not need to change this file either."""

from app import app


def client():
    return app.test_client()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_list_all_orders():
    r = client().get("/orders")
    assert r.status_code == 200
    assert r.get_json()["count"] == 4


def test_filter_by_status():
    r = client().get("/orders?status=ready")
    assert r.get_json()["count"] == 2


def test_one_order():
    r = client().get("/orders/2")
    assert r.get_json()["drink"] == "cappuccino"


def test_missing_order_is_404():
    r = client().get("/orders/99")
    assert r.status_code == 404
