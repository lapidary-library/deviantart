import pydantic


class ModelBase(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        # I'm not mapping all the fields, so at least lets have the chance to view them as a dict
        extra='allow',
        populate_by_name=True,
    )


class ApiSession(ModelBase):
    ...
