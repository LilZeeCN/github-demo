"""Tests for authentication module."""

from auth import AuthService


def test_register():
    auth = AuthService()
    assert auth.register("alice", "password123") is True
    assert auth.register("alice", "password123") is False


def test_login():
    auth = AuthService()
    auth.register("bob", "secret")
    token = auth.login("bob", "secret")
    assert token is not None
    assert auth.login("bob", "wrong") is None
    assert auth.login("unknown", "secret") is None


def test_verify():
    auth = AuthService()
    auth.register("carol", "pass")
    token = auth.login("carol", "pass")
    assert auth.verify(token) == "carol"
    assert auth.verify("invalid-token") is None


def test_logout():
    auth = AuthService()
    auth.register("dave", "pass")
    token = auth.login("dave", "pass")
    assert auth.logout(token) is True
    assert auth.verify(token) is None
    assert auth.logout(token) is False
