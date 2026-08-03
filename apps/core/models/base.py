from .uuid import UUIDModel
from .timestamp import TimeStampedModel
from .soft_delete import SoftDeleteModel


class BaseModel(
    UUIDModel,
    TimeStampedModel,
    SoftDeleteModel,
):
    class Meta:
        abstract = True