"""Stream type classes for tap-thinkific."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from .client import ThinkificStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class UsersStream(ThinkificStream):
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_method = "INCREMENTAL"
    replication_key = "created_at"
    schema_filepath = SCHEMAS_DIR / "users.json"


class CoursesStream(ThinkificStream):
    name = "courses"
    path = "/courses"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "courses.json"


class EnrollmentsStream(ThinkificStream):
    name = "enrollments"
    path = "/enrollments"
    primary_keys = ["id"]
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"
    created_timestamp = "activated_at"
    schema_filepath = SCHEMAS_DIR / "enrollments.json"

class ProductsStream(ThinkificStream):
    name = "products"
    path = "/products"
    primary_keys = ["id"]
    replication_method = "INCREMENTAL"
    replication_key = "created_at"
    schema_filepath = SCHEMAS_DIR / "products.json"
