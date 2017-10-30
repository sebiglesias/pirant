from __future__ import absolute_import, division, print_function
import colander

class News(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int(), missing=colander.drop)
    type = colander.SchemaNode(colander.String(), missing=colander.drop)
    headline = colander.SchemaNode(colander.String(), missing=colander.drop)
    body = colander.SchemaNode(colander.String(), missing=colander.drop)
    footer = colander.SchemaNode(colander.String(), missing=colander.drop)
    height = colander.SchemaNode(colander.Int(), missing=colander.drop)
    action = colander.SchemaNode(colander.String(), missing=colander.drop)

class Tags(colander.SequenceSchema):
    tag = colander.SchemaNode(colander.String())

class Image(colander.MappingSchema):
    url = colander.SchemaNode(colander.String())
    width = colander.SchemaNode(colander.Int())
    height = colander.SchemaNode(colander.Int())

    def deserialize(self, cstruct):
        if cstruct == "":
            cstruct = {}
        return cstruct

class UserAvatar(colander.MappingSchema):
    b = colander.SchemaNode(colander.String(), missing=colander.drop)
    i = colander.SchemaNode(colander.String(), missing=colander.drop)

class Rant(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    text = colander.SchemaNode(colander.String())
    score = colander.SchemaNode(colander.Int())
    created_time = colander.SchemaNode(colander.Int())
    attached_image = Image(missing=colander.drop)
    user_avatar = UserAvatar(missing=colander.drop)
    user_id = colander.SchemaNode(colander.Int())
    upvotes = colander.SchemaNode(colander.Int(), missing=colander.drop)
    downvotes = colander.SchemaNode(colander.Int(), missing=colander.drop)
    tags = Tags(missing=colander.drop)
    num_comments = colander.SchemaNode(colander.Int())
    user_username = colander.SchemaNode(colander.String())
    user_userscore = colander.SchemaNode(colander.Int(), missing=colander.drop)
    edited = colander.SchemaNode(colander.Boolean(), missing=colander.drop)

    # The below attributes only exist for collabs
    link = colander.SchemaNode(colander.String(), missing=colander.drop)
    c_type = colander.SchemaNode(colander.Int(), missing=colander.drop)
    c_type_long = colander.SchemaNode(colander.String(), missing=colander.drop)
    c_description = colander.SchemaNode(colander.String(), missing=colander.drop)
    c_tect_stack = colander.SchemaNode(colander.String(), missing=colander.drop)
    c_team_size = colander.SchemaNode(colander.Int(), missing=colander.drop)
    c_url = colander.SchemaNode(colander.String(), missing=colander.drop)


class Rants(colander.SequenceSchema):
    rant = Rant()

class RantsResponse(colander.MappingSchema):
    rants = Rants()
    news = News(missing=colander.drop)
    success = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    error = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    settings = colander.SchemaNode(colander.String(), missing=colander.drop)
    set = colander.SchemaNode(colander.String(), missing=colander.drop)
    wrw = colander.SchemaNode(colander.Int(), missing=colander.drop)

class Comment(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    rant_id = colander.SchemaNode(colander.Int())
    body = colander.SchemaNode(colander.String())
    upvotes = colander.SchemaNode(colander.Int(), missing=colander.drop)
    downvotes = colander.SchemaNode(colander.Int(), missing=colander.drop)
    score = colander.SchemaNode(colander.Int())
    created_time = colander.SchemaNode(colander.Int())
    user_id = colander.SchemaNode(colander.Int())
    user_username = colander.SchemaNode(colander.String())
    user_userscore = colander.SchemaNode(colander.Int(), missing=colander.drop)

class Comments(colander.SequenceSchema):
    comment = Comment()

class RantResponse(colander.MappingSchema):
    comments = Comments()
    rant = Rant()
    success = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    error = colander.SchemaNode(colander.Boolean(), missing=colander.drop)

class SearchResponse(colander.MappingSchema):
    success = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    error = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    results = Rants()
