"""Script to seed database."""

import os
# don't need this now
# import json
import crud
import model
import server

os.system('dropdb knitalong')
os.system('createdb knitalong')

model.connect_to_db(server.app)
model.db.create_all()

