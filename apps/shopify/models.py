from tortoise import fields, models


class ShopifySession(models.Model):
    id = fields.CharField(pk=True, max_length=255)
    shop = fields.CharField(max_length=255)
    state = fields.CharField(max_length=255)
    isOnline = fields.BooleanField()
    scope = fields.TextField()
    expires = fields.IntField()
    onlineAccessInfo = fields.CharField(max_length=255)
    accessToken = fields.CharField(max_length=255)

    class Meta:
        table = "shopify_sessions"
