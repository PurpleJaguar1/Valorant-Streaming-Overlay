import valclient
import requests

maps = {
    "Port": "Icebox",
    "Duality": "Bind",
    "Bonsai": "Split",
    "Ascent": "Ascent",
    "Triad": "Haven",
    "Foxtrot": "Breeze",
    "Range": "Range"
}

teams = {
    "Blue": "Defence",
    "Red": "Offence"
}

agent_ids = {
    "5f8d3a7f-467b-97f3-062c-13acf203c006": "Breach",
    "f94c3b30-42be-e959-889c-5aa313dba261": "Raze",
    "6f2a04ca-43e0-be17-7f36-b3908627744d": "Skye",
    "117ed9e3-49f3-6512-3ccf-0cada7e3823b": "Cypher",
    "320b2a48-4d9b-a075-30f1-1f93a9b638fa": "Sova",
    "1e58de9c-4950-5125-93e9-a0aee9f98746": "Killjoy",
    "707eab51-4836-f488-046a-cda6bf494859": "Viper",
    "eb93336a-449b-9c1b-0a54-a891f7921d69": "Phoenix",
    "41fb69c1-4189-7b37-f117-bcaf1e96f1bf": "Astra",
    "9f0d8ba9-4140-b941-57d3-a7ad57c6b417": "Brimstone",
    "7f94d92c-4234-0a36-9646-3a87eb8b5c89": "Yoru",
    "569fdd95-4d10-43ab-ca70-79becc718b46": "Sage",
    "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc": "Reyna",
    "8e253930-4c05-31dd-1b6c-968525494517": "Omen",
    "add6443a-41bd-e414-f6ad-e58d267f4e95": "Jett",
    "63057041-4f65-5579-e5a6-d88ae7007ebb": "?"
}

client = valclient.Client()
client.hook()
matchid = client.coregame_fetch_player()['MatchID']
match = client.coregame_fetch_match(matchid)
map = maps[match["MapID"].split('/')[-1]]

print(map)

for player in match["Players"]:
    print(player["PlayerIdentity"]["AccountLevel"],
          agent_ids[player["CharacterID"]])
