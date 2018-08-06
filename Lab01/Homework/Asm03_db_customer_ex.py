from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

# refs = ["events", "ads", "wom"]

refs = {
    "From Events": "events",
    "From Avertisements": "ads",
    "From Word of mouth": "wom"
}

colors = ["lightskyblue", "yellowgreen", "lightcoral"]
values = []
my_labels = []

for group, ref in refs.items():
    numb_by_group = db.customers.count({"ref":ref}) # Count numbers of customer by group
    values.append(numb_by_group)
    my_labels.append(group)
    print("{} : {} customers".format(group,numb_by_group))

pyplot.pie(values, labels=my_labels, autopct="%1.1f%%", colors=colors, startangle=90) # Draw chart
pyplot.axis("equal")
pyplot.show()






