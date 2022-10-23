import http
import json
from typing import Any, Dict, TypedDict

from sample import get_torch_version


class _Response(TypedDict):
    statusCode: int
    headers: Dict[str, str]
    body: str


def _response_json(
    http_status: http.HTTPStatus,
    body: Dict,
) -> _Response:
    return {
        "statusCode": int(http_status),
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(body),
    }


def sample_minimal_handler(event: Dict, context: Any) -> _Response:
    return _response_json(
        http.HTTPStatus.OK,
        {"torch_version": get_torch_version()},
    )
