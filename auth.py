"""User authentication module."""

import hashlib
import secrets


class AuthService:
    """Simple authentication service."""

    def __init__(self):
        self._users = {}
        self._sessions = {}

    def register(self, username: str, password: str) -> bool:
        if username in self._users:
            return False
        salt = secrets.token_hex(16)
        hashed = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
        self._users[username] = {"salt": salt, "password": hashed}
        return True

    def login(self, username: str, password: str) -> str | None:
        user = self._users.get(username)
        if not user:
            return None
        hashed = hashlib.sha256(
            f"{user['salt']}{password}".encode()
        ).hexdigest()
        if hashed != user["password"]:
            return None
        token = secrets.token_urlsafe(32)
        self._sessions[token] = username
        return token

    def verify(self, token: str) -> str | None:
        return self._sessions.get(token)

    def logout(self, token: str) -> bool:
        if token in self._sessions:
            del self._sessions[token]
            return True
        return False
