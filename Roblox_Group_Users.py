import requests
import json

groupId = int(input("groupId: " ));
next_page_cursor = ""
previousPageCursor = None

while next_page_cursor is not None:
    URL = f"https://groups.roblox.com/v1/groups/{groupId}/users?sortOrder=Asc&limit=100&Cursor={next_page_cursor}"
    response = requests.get(URL)
    data = response.json()
    with open(f"{groupId}.txt", "a") as f:
        for  member_data in data['data']:
            print(member_data['user']['userId'], file=f)
    f.close()
    next_page_cursor = data['nextPageCursor']
