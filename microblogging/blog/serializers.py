from marshmallow import Schema, fields


class PublicationsSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    content = fields.Str(required=True)
    date = fields.Method("get_date")
    up_votes = fields.Integer(required=True, data_key="upVotes")
    down_votes = fields.Integer(required=True, data_key="downVotes")
    shortContent = fields.Method("get_short_content")

    def get_date(self, obj):
        return obj.date.strftime("%d-%m-%Y @ %H:%M:%S")

    def get_short_content(self, obj):
        return obj.short_content()
