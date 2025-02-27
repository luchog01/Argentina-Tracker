from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import pandas
import matplotlib.pyplot as plt

MONGO_URI = "mongodb+srv://lucigar01:4dRMIzQ3W7f26qFU@fcitrackercluster.hfnbd1z.mongodb.net/?retryWrites=true&w=majority&appName=FciTrackerCluster"
DATABASE = "fcitracker-database"
USERS_COLLECTION = "users"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE]
collection = database[USERS_COLLECTION]

async def get_all_users():
    users = []
    async for user in collection.find():
        users.append(user)
    return users

async def main():
    users = await get_all_users()
    dates = []
    for user in users:
        sessions_dates = [session["started_at"] for session in user["sessions"]]
        dates.extend(sessions_dates)
    df = pandas.DataFrame(dates, columns=["dates"])
    df["dates"] = pandas.to_datetime(df["dates"])
    df["dates"] = df["dates"].dt.date
    df = df.groupby("dates").size().reset_index(name="counts")
    df = df.set_index("dates")
    df = df.sort_index()
    df.plot()
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())





