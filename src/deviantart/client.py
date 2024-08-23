from typing import Annotated, Self
from uuid import UUID

from lapidary.runtime import Body, ClientBase, Path, Query, Response, Responses, get

from .models.deviation import DeviationWithSessionResolved, MetadataResponse, TagsResponse
from .models.error import ErrorModel
from .models.placebo import PlaceboBody

MEDIA_JSON = 'application/json'
ERRORS = {
    '4XX': Response(Body({MEDIA_JSON: ErrorModel})),
    '5XX': Response(Body({MEDIA_JSON: ErrorModel})),
}


class DeviantArt(ClientBase):
    def __init__(self, ):
        super().__init__(
            base_url='https://www.deviantart.com/api/v1/oauth2/',
            timeout=30,
            security=(
                {'oauth': []},
                {'open': []},
            ),
        )

    @get('/browse/tags', (
        {'oauth': ['browse']},
        {'open': ['browse']}
    ))
    async def browse_tags(
        self: Self,
        tag: Annotated[str, Query],
        cursor: Annotated[str | None, Query] = None,
        offset: Annotated[int | None, Query] = None,
        limit: Annotated[int | None, Query] = None,
        with_session: Annotated[bool, Query] = False,
        mature_content: Annotated[bool, Query] = False,
    ) -> Annotated[
        tuple[TagsResponse, None],
        Responses({
            '200': Response(Body(
                {MEDIA_JSON: TagsResponse}
            )),
            **ERRORS,
        })
    ]:
        pass

    @get('/placebo')
    async def placebo(self: Self, mature_content: Annotated[bool, Query] = False) -> Annotated[
        tuple[PlaceboBody, None],
        Responses({
            '200': Response(Body({MEDIA_JSON: PlaceboBody})),
            **ERRORS
        })
    ]:
        pass

    @get('/deviation/{deviationId}')
    async def get_deviation(
        self: Self,
        deviation_id: Annotated[UUID, Path('deviationId')],
        with_session: Annotated[bool, Query] = False,
    ) -> Annotated[
        tuple[DeviationWithSessionResolved, None],
        Responses({
            '200': Response(Body({MEDIA_JSON: DeviationWithSessionResolved})),
            **ERRORS,
        })
    ]:
        pass

    @get('/deviation/metadata')
    async def deviation_metadata(
        self: Self,
        deviation_ids: Annotated[list[UUID], Query('deviationids[]')],
        ext_stats: Annotated[bool, Query] = False,
    ) -> Annotated[
        tuple[MetadataResponse, None],
        Responses({
            '200': Response(Body({MEDIA_JSON: MetadataResponse})),
            **ERRORS,
        })
    ]:
        pass
