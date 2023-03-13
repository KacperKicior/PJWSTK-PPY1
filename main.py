import webbrowser

import requests

chosen_date = ["20221125", "20201125", "20181125"]

entered_url = input("Wprowadź adres strony: ")

for chosen_date in chosen_date:
    req_date = requests.get(f"https://archive.org/wayback/available?url={entered_url}&timestamp={chosen_date}").json()
    requested_url = req_date["archived_snapshots"]["closest"]["url"]
    web = requests.get(requested_url).text

    with open(f"{chosen_date}.html", "w") as writer:
        writer.write(web)
        webbrowser.open(f"{chosen_date}.html")
