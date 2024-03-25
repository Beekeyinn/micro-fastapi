from tortoise import fields, models
from uuid import uuid4


class BaseModel(models.Model):
    """
    Abstract base model class.
    All other models should inherit from this class.
    """

    id = fields.UUIDField(pk=True, default=uuid4())
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)
