"""Stream type classes for tap-thinkific."""

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

from singer_sdk import typing as th  # JSON Schema typing helpers

from .client import ThinkificStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class GroupsStream(ThinkificStream):
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_method = "INCREMENTAL"
    replication_key = "created_at"
    schema_filepath = SCHEMAS_DIR / "groups.json"

class GroupsUsersStream(ThinkificStream):
    name = "users_groups"
    parent_stream_type = GroupsStream
    path = "/users?query[group_id]={group_id}"
    primary_keys = ["id", "group_id"]
    schema_filepath = SCHEMAS_DIR / "users_groups.json"

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
