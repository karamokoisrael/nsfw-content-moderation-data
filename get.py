import requests
req = requests.get("http://localhost:8055/items/feedbacks?filter[moderation_classes][_nnull]=true&filter[downloaded_for_dataset][_eq]=false&filter[image][_nnull]=true")
data = req.json()
print(data)