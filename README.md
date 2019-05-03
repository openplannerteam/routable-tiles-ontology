# Routable tiles ontology

This is a draft version of the Routable Tiles ontology. Everything is open for feedback and comments. 

So far it only defines the three data elements: `Node`, `Way`, and `Relation`. 

There are only three OSM keys so far: 

* `highway=*`, with its most common values modeled as instances of `HighwayValue`
* `maxspeed=*`, with numeric values in km/h
* `name=*`, a plaintext field

There are two additional properties:

* `hasNodes`, to define which nodes are part of a way
* `hasTag`: raw tags in the `{key}={value}` format, should be useful for all the tags that don't have defined semantics (yet)

An additional file defines some mappings from OSM tags to their semantic counterparts. 

---

Files:

* `ontology.ttl`: the ontology file in Turtle format
* `rendered/`: folder with the rendered ontology using widoco
* `mapping_config.json`: the mapping file