"""Thinkific Authentication."""


from singer_sdk.authenticators import SimpleAuthenticator


class ThinkificAuthenticator(SimpleAuthenticator):
    """Authenticator class for Thinkific."""

    @classmethod
    def create_for_stream(cls, stream) -> "ThinkificAuthenticator":
        return cls(
            stream=stream,
            auth_headers={
                "Private-Token": stream.config.get("auth_token")
            }
        )
