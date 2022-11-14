"""REST client handling, including ThinkificStream base class."""

import time
import requests
import singer
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable, Callable, Generator

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from .auth import ThinkificAuthenticator

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
LOGGER = singer.get_logger()


class ThinkificStream(RESTStream):
    @property
    def url_base(self) -> str:
        return self.config["api_url"]

    records_jsonpath = "$.items[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.meta.pagination.next_page"  # Or override `get_next_page_token`.
    extra_retry_statuses: List[int] = [429]

    @property
    def http_headers(self) -> dict:
        headers = {}
        headers["X-Auth-API-Key"] = self.config.get("auth_token")
        headers["X-Auth-Subdomain"] = self.config.get("subdomain")
        headers["Content-Type"] = "application/json"
        return headers

    def backoff_wait_generator() -> Callable[..., Generator[int, Any, None]]:
        return backoff.constant(interval=60)

    def get_next_page_token(
            self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            next_page_token = response.headers.get("X-Next-Page", None)

        return next_page_token

    def get_url_params(
            self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["limit"] = 1000
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        return row

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        if self.name == "groups":
            return {
                "group_id": record["id"]
            }
