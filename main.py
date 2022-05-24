from app import app
from app import db
from video.cloud import cloud

database = db.Db()
names, amount = database.names()
maxamount = database.maxamount
cloud.generate_cloud(names, amount, maxamount)
