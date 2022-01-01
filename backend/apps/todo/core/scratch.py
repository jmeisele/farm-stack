from motor.motor_asyncio import AsyncIOMotorClient

mongodb_client = AsyncIOMotorClient("localhost:27071")

mongodb = mongodb_client["my_db"]

task = {"foo": "bar"}
mongodb["tasks"].insert_one(task)