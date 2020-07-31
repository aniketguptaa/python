import json
data = '{"var1":"Tanisha","var2":"Sharma"}'

# parsed = json.loads(data)
# print(parsed['var1']) # Parsed the data with indexing

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
jscomps = json.dumps(data2)
print(jscomps)