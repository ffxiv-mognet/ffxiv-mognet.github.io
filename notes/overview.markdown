---
layout: markdown
title: Walkthrough Overview
permalink: /guide/overview
---


## A Realm Reborn [2.x]

### Realm Reborn Part 1 [lvl 4-15]
Gridania: "Close to Home"[65621] to "The Gridanian Envoy"[66043]..."Call of the Sea"[66209]
Lominsa: "Close to Home"[65644] to [66082] "Call of the Sea"[66209]
Uldah: "Close to Home"[66104] to [66064] "Call of the Sea"[66210]

### Realm Reborn Part 2 [lvl 15-24] 
from "It's Probably Pirates"[65781] to "Back from the Wood"[66282]  (38 quests)

### Realm Reborn Part 3 [lvl 24-34]
from "Shadow of Darkness"[66283] to "Lord of Crags"[66393] (42 quests)

### Realm Reborn Part 4 [lvl 34-50]
from "All Good Things"[66053] to "The Ultimate Weapon"[70058] (54 quests)

### Realm Reborn Part 5 [lvl 50]
from "The Price of Principles"[66711] to "Brave New Companions"[66996] (38 quests)

### Realm Reborn Part 6 [lvl 50]
from "Traitor in the Midst"[65588] to "Before the Dawn"[65964] (40 quests)


## Heavensward [3.x]
### Heavensward Part 1 [Lv.50-54]
from "Coming to Ishgard"[67116] to "Knights Be Not Proud"[67125]
 plus "onwards and upwards"[67126] to "a reward long in coming"[67132]
 from "divine intervention"[67133] to "Heart of Ice"[67163]
```
./scripts/xiv-quest-scraper.py questList --count 99 --firstRowId 67116 67125 | xc
./scripts/xiv-quest-scraper.py questList --count 99 --firstRowId 67126 67132 --partQuestNo 11 | tail -n +2 | xc
./scripts/xiv-quest-scraper.py questList --count 99 --firstRowId 67133 67163 --partQuestNo 18 | tail -n +2 | xc
```


### Heavensward Part 2 [Lv.54-60]
from "The Wyrm's Lair"[67164] to "Heavensward"[67205]

### Heavensward Part 3 [Lv.60]
from "An Uncertain Future"[67692] to "Litany of Peace"[67783]

### Heavensward Part 4 [Lv.60]
from "Promises Kept"[67877] to "The Far Edge of Fate"[67895]


## Stormblood [4.x]
### Stormblood Part 1 [Lv.60-64]
from "Beyond the Great Wall"[67982] to "All the Little Angels"[68035]

### Stormblood Part 2 [Lv.65-70]
from "Here There Be Xaela"[68166] to "Stormblood"[68089]

### Stormblood Part 3 [Lv.70]
from "Arenvald's Adventure"[68498] to "Emissary of the Dawn"[68612]

### Stormblood Part 4 [Lv.70]
from "Sisterly Act"[68679] to "A Requiem for Heroes"[68721]


## Shadowbringers [5.x]
### Shadowbringers Part 1 [Lv.70-76]
from "The Syrcus Trench"[68815] to "Out of the Wood"[68878]

### Shadowbringers Part 2 [Lv.76-80]
from "When It Rains"[69142] to "Shadowbringers"[69190]

### Shadowbringers Part 3 [Lv.80]
from "Shaken Resolve"[69209] to "Reflections in Crystal"[69318]

### Shadowbringers Part 4 [Lv.80]
from "Alisaie's Quest"[69543] to "Death Unto Dawn"[69602]


## Endwalker [6.x]
### Endwalker Part 1 [Lv.80-84]
from "The Next Ship to Sail"[69893] to "Returning Home"[69944]

### Endwalker Part 2 [Lv.85-90]
from "Skies Aflame"[69945] to "Endwalker"[70000]

### Endwalker Part 3 [Lv.90]
from "Newfound Adventure"[70062] to "Gods revel, Lands Tremble"[70214]

### Endwalker Part 4 [Lv.90]
from "Currying Flavor"[70271] to "The Coming Dawn"[70289]


## Dawntrail [7.x]
### Dawntrail Part 1 [Lv.90-95] 
from "A New World to Explore"[70396] to "Ever Greater, Ever Brighter"[70447]

### Dawntrail Part 2 [Lv.95-100] 
from "The Long Road To Xak Tural"[70448] to "Dawntrail"[70495]


## Crystal Tower
from "Legacy of Allag"[67245] to "The Light of Hope"[66031]