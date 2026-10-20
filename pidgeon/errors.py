"""Contains shared errors types that can be raised from API functions"""

from typing import Any

import httpx


class PidgeonError(Exception):
    """The API answered with a failure, 400 or above.

    Raised rather than returned, so a refused call cannot be mistaken for one
    that worked. ``code`` is the API's own (``abuse_blocked``, ``not_found``,
    ``validation`` …) and is what to branch on; ``message`` is written for a
    person and safe to show one; ``field`` names the input at fault, when one
    was. ``retry_after`` is the ``Retry-After`` header in seconds, set on a
    rate limit or a daily allowance.

    A body that is not Pidgeon's error envelope — a proxy's, say — leaves
    ``code`` as ``None`` and ``message`` as the text it sent.
    """

    def __init__(
        self,
        status_code: int,
        code: str | None,
        message: str,
        *,
        field: str | None = None,
        retry_after: int | None = None,
        headers: httpx.Headers | None = None,
        content: bytes = b"",
    ):
        self.status_code = status_code
        self.code = code
        self.message = message
        self.field = field
        self.retry_after = retry_after
        self.headers = headers if headers is not None else httpx.Headers()
        self.content = content

        super().__init__(f"{status_code} {code}: {message}" if code else f"{status_code}: {message}")

    @classmethod
    def from_response(cls, response: httpx.Response) -> "PidgeonError":
        content = response.read()
        detail: Any = None
        try:
            detail = response.json().get("error")
        except (ValueError, AttributeError):
            pass

        retry_after = response.headers.get("Retry-After")

        if isinstance(detail, dict) and isinstance(detail.get("code"), str):
            return cls(
                response.status_code,
                detail["code"],
                str(detail.get("message", "")),
                field=detail.get("field") if isinstance(detail.get("field"), str) else None,
                retry_after=int(retry_after) if retry_after and retry_after.isdigit() else None,
                headers=response.headers,
                content=content,
            )

        return cls(
            response.status_code,
            None,
            content.decode(errors="ignore")[:500],
            retry_after=int(retry_after) if retry_after and retry_after.isdigit() else None,
            headers=response.headers,
            content=content,
        )


class UnexpectedStatus(Exception):
    """Raised when the API answers below 400 with a status the operation does not declare.

    Always, whatever ``Client.raise_on_unexpected_status`` says: an answer the
    client cannot read is not one to hand back as ``None``.
    """

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(
            f"Unexpected status code: {status_code}\n\nResponse content:\n{content.decode(errors='ignore')}"
        )


__all__ = ["PidgeonError", "UnexpectedStatus"]
