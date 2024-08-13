import pydantic


class ModelBase(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra='ignore',
        populate_by_name=True,
    )


class ApiSession(ModelBase):
    ...
