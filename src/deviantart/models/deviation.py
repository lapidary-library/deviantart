import datetime as dt
from typing import Annotated
from uuid import UUID

import pydantic

from .base import ApiSession, ModelBase


class DeviationStats(ModelBase):
    comments: int
    favourites: int


class DeviationTag(ModelBase):
    tag_name: str
    sponsored: bool
    sponsor: str


class DeviationStats2(ModelBase):
    views: int
    views_today: int
    favourites: int
    comments: int
    downloads: int
    downloads_today: int


class DeviationMetadata(ModelBase):
    id: Annotated[UUID, pydantic.Field(alias='deviationid')]
    tags: list[DeviationTag]
    is_favourited: bool
    stats: DeviationStats2 | None = None


class MetadataResponse(ModelBase):
    metadata: list[DeviationMetadata]
    session: ApiSession | None = None


class DeviationPreview(ModelBase):
    src: str
    height: int
    width: int
    transparency: bool


class DeviationContent(DeviationPreview):
    filesize: int


class EditorTextContentBody(ModelBase):
    type: str
    markup: str | None = None
    features: str


class EditorTextContent(ModelBase):
    excerpt: str
    body: EditorTextContentBody


class DeviationWithSessionResolved(ModelBase):
    deviation_id: Annotated[UUID, pydantic.Field(alias="deviationid")]
    stats: DeviationStats | None = None
    is_mature: bool | None = None
    url: str | None = None
    published_time: dt.datetime | None = None
    title: str | None = None
    preview: DeviationPreview | None = None
    content: DeviationContent | None = None
    text_content: EditorTextContent | None = None


class TagsResponse(ModelBase):
    has_more: bool
    next_offset: int | None
    next_cursor: str | None = None
    prev_cursor: str | None = None
    error_code: int | None = None
    results: list[DeviationWithSessionResolved]
    session: ApiSession | None = None
    mature_content: bool | None = False
