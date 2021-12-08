from marshmallow import Schema,validate,ValidationError,fields

class Video(Schema):
    class Meta:
        ordered = True
    pass