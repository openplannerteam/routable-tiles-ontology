# Routable tiles ontology

This is a draft version of the Routable Tiles ontology. It is a best-effort attempt at defining OSM tags and their semantics. It is largely based on the definitions on the OSM wiki, and there are `prov:wasInfluencedBy` triples pointing to the Wiki pages. 

There are three core classes, representing the OSM data elements: `Node`, `Way`, and `Relation`. 

OSM keys are predicates, sticking as close to the familiar OSM format as possible:

| OSM Key            | Predicate            |
| ------------------ | -------------------- |
| `access=*`         | `osm:access`         |
| `barrier`=*        | `osm:barrier`        |
| `bicycle=*`        | `osm:bicyle`         |
| `construction=*`   | `osm:construction`   |
| `crossing=*`       | `osm:crossing`       |
| `cycleway=*`       | `osm:cycleway`       |
| `highway=*`        | `osm:highway`        |
| `maxspeed=*`       | `osm:maxspeed`       |
| `motor_vehicle=*`  | `osm:motor_vehicle`  |
| `motorcar=*`       | `osm:motorcar`       |
| `name=*`           | `osm:name`           |
| `oneway:bicycle=*` | `osm:oneway_bicycle` |
| `oneway=*`         | `osm:oneway`         |
| `smoothness=*`     | `osm:smoothness`     |
| `surface=*`        | `osm:surface`        |
| `tracktype=*`      | `osm:tracktype`      |
| `vehicle=*`        | `osm:vehicle`        |

There are two additional predicates:

* `hasNodes`, to define which nodes are part of a way
* `hasTag`: raw tags in the `{key}={value}` format, should be useful for all the tags that don't have defined semantics (yet)

---

There is an incomplete set of defined tags:

| tag                        | predicate          | object                     |
| -------------------------- | ------------------ | -------------------------- |
| access=agricultural        | osm:access         | osm:Agricultural           |
| access=customers           | osm:access         | osm:Customers              |
| access=delivery            | osm:access         | osm:Delivery               |
| access=designated          | osm:access         | osm:Designated             |
| access=destination         | osm:access         | osm:Destination            |
| access=discouraged         | osm:access         | osm:Discouraged            |
| access=dismount            | osm:access         | osm:Dismount               |
| access=emergency           | osm:access         | osm:Emergency              |
| access=forestry            | osm:access         | osm:Forestry               |
| access=no                  | osm:access         | osm:NoAccess               |
| access=permissive          | osm:access         | osm:Permissive             |
| access=private             | osm:access         | osm:Private                |
| access=use_sidepath        | osm:access         | osm:UseSidepath            |
| access=yes                 | osm:access         | osm:FreeAccess             |
| barrier=block              | osm:barrier        | osm:Block                  |
| barrier=bollard            | osm:barrier        | osm:Bollard                |
| barrier=border_control     | osm:barrier        | osm:BorderControl          |
| barrier=bump_gate          | osm:barrier        | osm:BumpGate               |
| barrier=bus_trap           | osm:barrier        | osm:BusTrap                |
| barrier=cattle_grid        | osm:barrier        | osm:CattleGrid             |
| barrier=chain              | osm:barrier        | osm:Chain                  |
| barrier=cycle_barrier      | osm:barrier        | osm:CycleBarrier           |
| barrier=debris             | osm:barrier        | osm:Debris                 |
| barrier=entrance           | osm:barrier        | osm:Entrance               |
| barrier=gate               | osm:barrier        | osm:Gate                   |
| barrier=lift_gate          | osm:barrier        | osm:LiftGate               |
| barrier=sally_port         | osm:barrier        | osm:SallyPort              |
| barrier=swing_gate         | osm:barrier        | osm:SwingGate              |
| barrier=toll_booth         | osm:barrier        | osm:TollBooth              |
| barrier=turnstile          | osm:barrier        | osm:Turnstile              |
| bicycle=designated         | osm:bicycle        | osm:Designated             |
| bicycle=destination        | osm:bicycle        | osm:Destination            |
| bicycle=dismount           | osm:bicycle        | osm:Dismount               |
| bicycle=no                 | osm:bicycle        | osm:NoAccess               |
| bicycle=official           | osm:bicycle        | osm:OfficialAccess         |
| bicycle=permissive         | osm:bicycle        | osm:Permissive             |
| bicycle=private            | osm:bicycle        | osm:Private                |
| bicycle=use_sidepath       | osm:bicycle        | osm:UseSidepath            |
| bicycle=yes                | osm:bicycle        | osm:FreeAccess             |
| construction=yes           | osm:construction   | osm:UnderConstruction      |
| crossing=uncontrolled      | osm:crossing       | osm:Uncontrolled           |
| crossing=unmarked          | osm:crossing       | osm:Unmarked               |
| cycleway=lane              | osm:cycleway       | osm:Lane                   |
| cycleway=opposite          | osm:cycleway       | osm:Opposite               |
| cycleway=opposite_lane     | osm:cycleway       | osm:OppositeLane           |
| cycleway=opposite_track    | osm:cycleway       | osm:OppositeTrack          |
| cycleway=share_busway      | osm:cycleway       | osm:ShareBusway            |
| cycleway=shared            | osm:cycleway       | osm:Shared                 |
| cycleway=shared_lane       | osm:cycleway       | osm:SharedLane             |
| cycleway=track             | osm:cycleway       | osm:Track                  |
| footway=sidewalk           | osm:footway        | osm:Sidewalk               |
| highway=bridleway          | osm:highway        | osm:Bridleway              |
| highway=construction       | osm:construction   | osm:UnderConstruction      |
| highway=crossing           | osm:highway        | osm:HighwayCrossing        |
| highway=cycleway           | osm:highway        | osm:CycleHighway           |
| highway=footway            | osm:highway        | osm:FootHighway            |
| highway=give_way           | osm:highway        | osm:GiveWay                |
| highway=living_street      | osm:highway        | osm:LivingStreet           |
| highway=motorway           | osm:highway        | osm:Motorway               |
| highway=motorway_link      | osm:highway        | osm:MotorwayLink           |
| highway=path               | osm:highway        | osm:Path                   |
| highway=primary            | osm:highway        | osm:Primary                |
| highway=primary_link       | osm:highway        | osm:PrimaryLink            |
| highway=proposed           | osm:highway        | osm:Proposed               |
| highway=residential        | osm:highway        | osm:Residential            |
| highway=road               | osm:highway        | osm:Road                   |
| highway=secondary          | osm:highway        | osm:Secondary              |
| highway=secondary_link     | osm:highway        | osm:SecondaryLink          |
| highway=service            | osm:highway        | osm:Service                |
| highway=steps              | osm:highway        | osm:Steps                  |
| highway=stop               | osm:highway        | osm:Stop                   |
| highway=tertiary           | osm:highway        | osm:Tertiary               |
| highway=tertiary_link      | osm:highway        | osm:TertiaryLink           |
| highway=track              | osm:highway        | osm:Track                  |
| highway=traffic_signals    | osm:highway        | osm:TrafficSignals         |
| highway=trunk              | osm:highway        | osm:Trunk                  |
| highway=trunk_link         | osm:highway        | osm:TrunkLink              |
| highway=unclassified       | osm:highway        | osm:Unclassified           |
| motor_vehicle=agricultural | osm:motor_vehicle  | osm:Agricultural           |
| motor_vehicle=customers    | osm:motor_vehicle  | osm:Customers              |
| motor_vehicle=delivery     | osm:motor_vehicle  | osm:Delivery               |
| motor_vehicle=designated   | osm:motor_vehicle  | osm:Designated             |
| motor_vehicle=destination  | osm:motor_vehicle  | osm:Destination            |
| motor_vehicle=no           | osm:motor_vehicle  | osm:NoAccess               |
| motor_vehicle=official     | osm:motor_vehicle  | osm:Official               |
| motor_vehicle=permissive   | osm:motor_vehicle  | osm:Permissive             |
| motor_vehicle=private      | osm:motor_vehicle  | osm:Private                |
| motor_vehicle=yes          | osm:motor_vehicle  | osm:FreeAccess             |
| motorcar=agricultural      | osm:motorcar       | osm:Agricultural           |
| motorcar=customers         | osm:motorcar       | osm:Customers              |
| motorcar=delivery          | osm:motorcar       | osm:Delivery               |
| motorcar=designated        | osm:motorcar       | osm:Designated             |
| motorcar=destination       | osm:motorcar       | osm:Destination            |
| motorcar=forestry          | osm:motorcar       | osm:Forestry               |
| motorcar=no                | osm:motorcar       | osm:NoAccess               |
| motorcar=official          | osm:motorcar       | osm:Official               |
| motorcar=permissive        | osm:motorcar       | osm:Permissive             |
| motorcar=private           | osm:motorcar       | osm:Private                |
| motorcar=yes               | osm:motorcar       | osm:FreeAccess             |
| oneway:bicycle=-1          | osm:oneway_bicycle | osm:InReverseOrder         |
| oneway:bicycle=1           | osm:oneway_bicycle | osm:InOrder                |
| oneway:bicycle=no          | osm:oneway_bicycle | osm:Bidirectional          |
| oneway:bicycle=yes         | osm:oneway_bicycle | osm:InOrder                |
| oneway=-1                  | osm:oneway         | osm:InReverseOrder         |
| oneway=1                   | osm:oneway         | osm:InOrder                |
| oneway=yes                 | osm:oneway         | osm:Bidirectional          |
| oneway=no                  | osm:oneway         | osm:InOrder                |
| smoothness=bad             | osm:smoothness     | osm:BadSmoothness          |
| smoothness=excellent       | osm:smoothness     | osm:ExcellentSmoothness    |
| smoothness=good            | osm:smoothness     | osm:GoodSmoothness         |
| smoothness=horrible        | osm:smoothness     | osm:HorribleSmoothness     |
| smoothness=impassable      | osm:smoothness     | osm:ImpassableSmoothness   |
| smoothness=intermediate    | osm:smoothness     | osm:IntermediateSmoothness |
| smoothness=very_bad        | osm:smoothness     | osm:VeryBadSmoothness      |
| smoothness=very_horrible   | osm:smoothness     | osm:VeryHorribleSmoothness |
| surface=asphalt            | osm:surface        | osm:Asphalt                |
| surface=cobblestone        | osm:surface        | osm:Cobblestone            |
| surface=compacted          | osm:surface        | osm:Compacted              |
| surface=concrete           | osm:surface        | osm:Concrete               |
| surface=dirt               | osm:surface        | osm:Dirt                   |
| surface=earth              | osm:surface        | osm:Dirt                   |
| surface=fine_gravel        | osm:surface        | osm:FineGravel             |
| surface=grass              | osm:surface        | osm:Grass                  |
| surface=gravel             | osm:surface        | osm:Gravel                 |
| surface=ground             | osm:surface        | osm:Ground                 |
| surface=mud                | osm:surface        | osm:Mud                    |
| surface=paved              | osm:surface        | osm:Paved                  |
| surface=paving_stones      | osm:surface        | osm:PavingStones           |
| surface=pebblestone        | osm:surface        | osm:Pebblestone            |
| surface=sand               | osm:surface        | osm:Sand                   |
| surface=sett               | osm:surface        | osm:Sett                   |
| surface=unhewn_cobblestone | osm:surface        | osm:UnhewnCobblestone      |
| surface=unpaved            | osm:surface        | osm:Unpaved                |
| surface=wood               | osm:surface        | osm:Wood                   |
| tracktype=grade1           | osm:tracktype      | osm:Grade1                 |
| tracktype=grade2           | osm:tracktype      | osm:Grade2                 |
| tracktype=grade3           | osm:tracktype      | osm:Grade3                 |
| tracktype=grade4           | osm:tracktype      | osm:Grade4                 |
| tracktype=grade5           | osm:tracktype      | osm:Grade5                 |
| vehicle=customers          | osm:vehicle        | osm:Customers              |
| vehicle=delivery           | osm:vehicle        | osm:Delivery               |
| vehicle=designated         | osm:vehicle        | osm:Designated             |
| vehicle=destination        | osm:vehicle        | osm:Destination            |
| vehicle=forestry           | osm:vehicle        | osm:Forestry               |
| vehicle=no                 | osm:vehicle        | osm:NoAccess               |
| vehicle=permissive         | osm:vehicle        | osm:Permissive             |
| vehicle=private            | osm:vehicle        | osm:Private                |
| vehicle=yes                | osm:vehicle        | osm:FreeAccess             |

---

Files:

* `create_mapping.py`: Creates the mapping file using `speeds.json` and `entities.csv`.
* `entities.csv`: The above table of tags, in CSV format.
* `mapping_config.json`: A mapping file, can be used to translate OSM tags. Not really the best way of doing things.
* `ontology.ttl`: The ontology file
* `rendered/`: Folder with the rendered ontology
* `speeds.json`: List of 200 most common `maxspeed` values according to http://taginfo.openstreetmap.org/