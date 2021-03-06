from datetime import datetime

db.define_table('entry',
        Field('date_posted', 'datetime'),
        Field('title'),
        Field('body', 'text'), 
        Field('is_lucid', 'boolean'),
        Field('category'),
        Field('user_id', db.auth_user),
        )

db.entry.id.readable = False
db.entry.date_posted.default = datetime.utcnow()
db.entry.date_posted.writable = False 
db.entry.is_lucid.default = False
db.entry.user_id.default = auth.user_id
db.entry.user_id.writable = db.entry.user_id.readable = False

db.entry.category.requires = IS_IN_SET(['Normal', 'Nightmare', 'Lucid'])
