import json
import csv
from collections import defaultdict

def add_name(entries):
	entries.append({
		"osm_key": "name",
		"predicate": "osm:name"
	})

def add_maxspeed(entries):
	mapping = {}

	with open('speeds.json') as f:
		speeds = json.load(f)

	for entry in speeds["data"]:
		value = entry["value"]
		try:
			parsed_value = float(value)
			mapping[value] = parsed_value
		except:
			if len(value.split('mph')) == 2:
				    parsed_value = int(round(float(value.split('mph')[0]) * 1.609344))
				    mapping[value] = parsed_value

	entries.append({
		"osm_key": "maxspeed",
		"predicate": "osm:maxspeed",
		"mapping": mapping
	})

def read_entities():
	entity_keys = defaultdict(dict)

	with open('entities.csv') as csvfile:
		next(csvfile)
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			key = row[0].split('=')[0]
			entity_keys[key]["osm_key"] = key.strip()
			entity_keys[key]["predicate"] = row[1].strip()

			value = row[0].split('=')[1]
			mapped_value = row[2].strip()

			if 'mapping' not in entity_keys[key]:
				entity_keys[key]["mapping"] = {}
			
			entity_keys[key]["mapping"][value] = mapped_value

	return list(entity_keys.values())

result = read_entities()
add_maxspeed(result)
add_name(result)

print(json.dumps(result, indent=2, sort_keys=True))
