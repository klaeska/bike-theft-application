from marshmallow import Schema, fields

# aka GitHubRepoSchema class in the tut, incoming request payload


class BikeInfoSchema(Schema):
    id = fields.Int(required=True)
    bike_name = fields.Str()
    bike_colour = fields.Str()
    bike_model = fields.Str()
    description = fields.Str()
    registration = fields.Str()
    manufacturor = fields.Str()

# aka KudoSchema class in the tut, the object persists in the database


class BikeSchema(BikeInfoSchema):
    user_id = fields.Email(required=True)