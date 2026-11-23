---
layout: quest-table
expansion: A Realm Reborn
partNo: 1
partChapterNo: 1
title: A Realm Reborn - Part 1 - Limsa lominsa
permalink: /quests/msq/realm-reborn/part1/limsa-lominsa
links:
  next: /quests/msq/realm-reborn/part2
quests:
  - name: Close to Home
    level: 1
    rowId: 65644
    questId: ManSea002_00108
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa
      coords: (11.6, 11.1)
      name: Baderon
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (9.5, 11.2)
        name: Attune yourself to the aetheryte found on the lower decks.
      - location: Limsa Lominsa Lower Decks
        coords: (8.4, 11.5)
        name: Listen to Swozblaet's explanation of the markets.
      - location: Limsa Lominsa Upper Decks
        coords: (11.0, 6.3)
        name: Visit the Marauders' Guild.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Report to Baderon at the Drowning Wench.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Coming to Limsa Lominsa
        level: 1
        rowId: 65643
        questId: ManSea001_00107
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 400
        paramGrowId: '1'
        avg: 400
      gil: 107
    partQuestNo: 1
  - name: On to Summerford
    level: 4
    rowId: 65998
    questId: SubSea050_00462
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.6, 11.1)
      name: Baderon
    steps:
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Speak with Staelwyrn at Summerford Farms.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 65645
        questId: ManSea003_00109
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      optional:
        - item:
            name: Altered Thighboots
            id: '27634'
            icon: '49077'
            ilvl: '5'
            level: '5'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '32'
            name: Mole Brown
            color: '6378053'
        - item:
            name: Altered Leather Thighboots
            id: '27665'
            icon: '46102'
            ilvl: '5'
            level: '5'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '20'
            name: Russet Brown
            color: '5188895'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
    partQuestNo: 2
  - name: Dressed to Call
    level: 4
    rowId: 65999
    questId: SubSea051_00463
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (25.6, 17.0)
      name: Staelwyrn
    steps:
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Present yourself to Staelwyrn for inspection.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      gil: 161
      optional:
        - item:
            name: Bronze War Axe
            id: '1750'
            icon: '31401'
            ilvl: '5'
            level: '5'
            category:
              id: '3'
              name: Marauder's Arm
              icon: '60103'
          count: 1
        - item:
            name: Leather Grimoire
            id: '2143'
            icon: '33402'
            ilvl: '5'
            level: '5'
            category:
              id: '10'
              name: Arcanist's Grimoire
              icon: '60109'
          count: 1
        - item:
            name: Bronze Daggers
            id: '9184'
            icon: '33802'
            ilvl: '5'
            level: '5'
            category:
              id: '84'
              name: Rogue's Arm
              icon: '60106'
          count: 1
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
    partQuestNo: 3
  - name: Lurkers in the Grotto
    level: 5
    rowId: 66079
    questId: ManSea005_00543
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (25.6, 17.0)
      name: Staelwyrn
    steps:
      - location: Middle La Noscea
        coords: (20.3, 18.6)
        name: Investigate Seasong Grotto.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 9
      timeLimit: 30
      id: '35'
    rewards:
      xp:
        factor: 400
        paramGrowId: '5'
        avg: 1400
      gil: 128
      items:
        - item:
            name: Eye Drops
            id: '4565'
            icon: '20642'
            ilvl: '5'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 5
      optional:
        - item:
            name: Potion
            id: '4551'
            icon: '20601'
            ilvl: '10'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Ether
            id: '4555'
            icon: '20621'
            ilvl: '15'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
    partQuestNo: 4
  - name: Washed Up
    level: 5
    rowId: 66001
    questId: SubSea053_00465
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (25.6, 17.0)
      name: Staelwyrn
    steps:
      - location: Middle La Noscea
        coords: (22.0, 18.2)
        name: Speak with the slacking yeomen.
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Report to Staelwyrn.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '5'
        avg: 1400
      gil: 141
    partQuestNo: 5
  - name: Double Dealing
    level: 5
    rowId: 66002
    questId: SubSea054_00466
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (25.6, 17.0)
      name: Staelwyrn
    steps:
      - location: Middle La Noscea
        coords: (24.1, 24.1)
        name: Confront Sevrin and cast /doubt on his actions.
      - location: Middle La Noscea
        coords: (25.2, 23.9)
        name: Save Sevrin's henchmen.
      - location: Middle La Noscea
        coords: (24.1, 24.1)
        name: Speak with Sevrin.
      - location: Middle La Noscea
        coords: (24.1, 24.2)
        name: Retrieve the sack of oranges.
      - location: Middle La Noscea
        coords: (25.1, 27.4)
        name: Deliver the sack of oranges to Ossine at the La Thagran Checkpoint.
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Report to Staelwyrn at Summerford Farms.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '5'
        avg: 1400
      gil: 179
      items:
        - item:
            name: Hi-Potion
            id: '4552'
            icon: '20602'
            ilvl: '25'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 1
      optional:
        - item:
            name: Hempen Acton
            id: '3008'
            icon: '43012'
            ilvl: '8'
            level: '8'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '27'
            name: Acorn Brown
            color: '9328667'
        - item:
            name: Hempen Cowl
            id: '3000'
            icon: '43601'
            ilvl: '8'
            level: '8'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '18'
            name: Bark Brown
            color: '6966071'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
    partQuestNo: 6
  - name: Loam Maintenance
    level: 5
    rowId: 66003
    questId: SubSea055_00467
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (25.5, 17.2)
      name: Gurcant
    steps:
      - location: Middle La Noscea
        coords: (22.5, 17.7)
        name: Speak with Rhotwyda.
      - location: Middle La Noscea
        coords: (18.7, 17.2)
        name: Obtain the blackloam in the Cookpot.
      - location: Middle La Noscea
        coords: (21.5, 15.3)
        name: Take the blackloam to Pfrewahl at Tiller's Rest.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '5'
        avg: 1400
      optional:
        - item:
            name: Leather Wristbands
            id: '4092'
            icon: '55643'
            ilvl: '8'
            level: '8'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Copper Wristlets
            id: '4091'
            icon: '55601'
            ilvl: '8'
            level: '8'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
    partQuestNo: 7
  - name: Plowshares to Swords
    level: 5
    rowId: 66004
    questId: SubSea056_00468
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (21.5, 15.3)
      name: Pfrewahl
    steps:
      - location: Middle La Noscea
        coords: (20.3, 16.7)
        name: Recover the stolen farm tools from the pirates.
      - location: Middle La Noscea
        coords: (21.5, 15.3)
        name: Deliver the reclaimed farm tools to Pfrewahl.
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Report to Staelwyrn.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '5'
        avg: 1400
      items:
        - item:
            name: Eye Drops
            id: '4565'
            icon: '20642'
            ilvl: '5'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 5
      optional:
        - item:
            name: Bronze Labrys
            id: '1751'
            icon: '31403'
            ilvl: '8'
            level: '8'
            category:
              id: '3'
              name: Marauder's Arm
              icon: '60103'
          count: 1
        - item:
            name: Maple Picatrix
            id: '2144'
            icon: '33403'
            ilvl: '8'
            level: '8'
            category:
              id: '10'
              name: Arcanist's Grimoire
              icon: '60109'
          count: 1
        - item:
            name: Bronze Knives
            id: '9185'
            icon: '33803'
            ilvl: '8'
            level: '8'
            category:
              id: '84'
              name: Rogue's Arm
              icon: '60106'
          count: 1
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 4
    partQuestNo: 8
  - name: Just Deserts
    level: 9
    rowId: 66005
    questId: SubSea057_00469
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (25.6, 17.0)
      name: Staelwyrn
    steps:
      - location: Middle La Noscea
        coords: (26.1, 16.6)
        name: Speak with Grynewyda.
      - location: Middle La Noscea
        coords: (18.6, 14.7)
        name: Intercept Sevrin and his henchmen in Woad Whisper Canyon.
      - location: Middle La Noscea
        coords: (20.3, 13.2)
        name: Rescue Sevrin's henchmen.
      - location: Middle La Noscea
        coords: (20.8, 12.8)
        name: Rescue Sevrin's henchmen in the heart of Woad Whisper Canyon.
      - location: Middle La Noscea
        coords: (20.9, 12.7)
        name: Rescue Sevrin's henchmen in the heart of Woad Whisper Canyon.
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Speak with Staelwyrn.
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Speak with Staelwyrn.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Speak with Baderon at the Drowning Wench.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 13
      timeLimit: 30
      id: '29'
    rewards:
      xp:
        factor: 400
        paramGrowId: '9'
        avg: 3240
      gil: 177
    partQuestNo: 9
  - name: Sky-high
    level: 10
    rowId: 65933
    questId: SubSea100_00397
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.6, 11.1)
      name: Baderon
    steps:
      - location: Middle La Noscea
        coords: (15.8, 16.5)
        name: Speak with Wyrkrhit at the Skylift.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      optional:
        - item:
            name: Hempen Trousers
            id: '3318'
            icon: '45015'
            ilvl: '10'
            level: '10'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '14'
            name: Blood Red
            color: '9517863'
        - item:
            name: Amateur's Breeches
            id: '3316'
            icon: '45035'
            ilvl: '10'
            level: '10'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '4'
            name: Slate Grey
            color: '6645093'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
    partQuestNo: 10
  - name: Thanks a Million
    level: 10
    rowId: 65938
    questId: SubSea105_00402
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Middle La Noscea
      coords: (15.8, 16.5)
      name: Wyrkrhit
    steps:
      - location: Middle La Noscea
        coords: (15.0, 10.9)
        name: Recover the millioncorn seedling.
      - location: Western La Noscea
        coords: (34.5, 32.0)
        name: Deliver the millioncorn seedling to Lyulf in Swiftperch.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      optional:
        - item:
            name: Leather Jacket
            id: '3016'
            icon: '43026'
            ilvl: '10'
            level: '10'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '14'
            name: Blood Red
            color: '9517863'
        - item:
            name: Amateur's Dalmatica
            id: '3015'
            icon: '42017'
            ilvl: '10'
            level: '10'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '75'
            name: Shadow Blue
            color: '3618631'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
    partQuestNo: 11
  - name: Relighting the Torch
    level: 10
    rowId: 65939
    questId: SubSea106_00403
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western La Noscea
      coords: (34.6, 31.9)
      name: Fraeloef
    steps:
      - location: Western La Noscea
        coords: (30.3, 30.5)
        name: Speak with Khanswys.
      - location: Western La Noscea
        coords: (33.5, 28.7)
        name: Set the iron brazier on the ground near the scarecrow.
      - location: Western La Noscea
        coords: (33.5, 28.7)
        name: Light the brazier, and obtain a bomb claw from the torchlight that is
          drawn in by the flames.
      - location: Western La Noscea
        coords: (30.3, 30.5)
        name: Deliver the bomb claw to Khanswys.
      - location: Western La Noscea
        coords: (34.6, 31.9)
        name: Return to Swiftperch and report to Fraeloef.
      - location: Limsa Lominsa Upper Decks
        coords: (10.6, 15.4)
        name: Speak with Forgemaster H'naanza in Limsa Lominsa.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 101
      optional:
        - item:
            name: Bronze Sallet
            id: '2662'
            icon: '40020'
            ilvl: '10'
            level: '10'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '14'
            name: Blood Red
            color: '9517863'
        - item:
            name: Amateur's Hempen Coif
            id: '2661'
            icon: '41527'
            ilvl: '10'
            level: '10'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '75'
            name: Shadow Blue
            color: '3618631'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
    partQuestNo: 12
  - name: On to the Drydocks
    level: 10
    rowId: 65942
    questId: SubSea109_00406
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (10.6, 15.4)
      name: H'naanza
    steps:
      - location: Lower La Noscea
        coords: (26.4, 33.7)
        name: Deliver the missive to Ahtbyrm at the Moraby Drydocks.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 188
      optional:
        - item:
            name: Leather Jackboots
            id: '3770'
            icon: '46816'
            ilvl: '10'
            level: '10'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '14'
            name: Blood Red
            color: '9517863'
        - item:
            name: Amateur's Duckbills
            id: '3769'
            icon: '46109'
            ilvl: '10'
            level: '10'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '18'
            name: Bark Brown
            color: '6966071'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
    partQuestNo: 13
  - name: Without a Doubt
    level: 10
    rowId: 65948
    questId: SubSea115_00412
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Lower La Noscea
      coords: (26.4, 33.7)
      name: Ahtbyrm
    steps:
      - location: Lower La Noscea
        coords: (20.8, 38.7)
        name: Journey to Candlekeep Quay and relay Ahtbyrm's /doubt to Haldbroda.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 196
      optional:
        - item:
            name: Hempen Bracers
            id: '3539'
            icon: '44042'
            ilvl: '11'
            level: '11'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '10'
            name: Dalamud Red
            color: '7871002'
        - item:
            name: Hempen Dress Gloves
            id: '3538'
            icon: '44159'
            ilvl: '11'
            level: '11'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '66'
            name: Ceruleum Blue
            color: '5199718'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
    partQuestNo: 14
  - name: Righting the Shipwright
    level: 10
    rowId: 65951
    questId: SubSea118_00415
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Lower La Noscea
      coords: (20.8, 38.7)
      name: Haldbroda
    steps:
      - location: Lower La Noscea
        coords: (19.6, 36.2)
        name: Search the Salt Strand for survivors.
      - location: Lower La Noscea
        coords: (18.5, 35.6)
        name: Salvage the *Victory*'s helm wheel.
      - location: Lower La Noscea
        coords: (17.7, 35.4)
        name: Salvage the *Victory*'s rigging.
      - location: Lower La Noscea
        coords: (18.1, 34.6)
        name: Salvage the *Victory*'s sailcloth.
      - location: Lower La Noscea
        coords: (19.6, 36.2)
        name: Take the three items to Fyrilsmyd.
      - location: Lower La Noscea
        coords: (26.4, 33.7)
        name: Report to Ahtbyrm.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 234
    partQuestNo: 15
  - name: Do Angry Pirates Dream
    level: 10
    rowId: 65949
    questId: SubSea116_00413
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Lower La Noscea
      coords: (26.4, 33.7)
      name: Ahtbyrm
    steps:
      - location: Lower La Noscea
        coords: (24.8, 35.1)
        name: Speak with Ghimthota.
      - location: Lower La Noscea
        coords: (23.8, 36.2)
        name: Speak with C'nangho.
      - location: Lower La Noscea
        coords: (26.5, 36.9)
        name: Confront the suspicious individuals.
      - location: Lower La Noscea
        coords: (24.8, 35.1)
        name: Return to the Moraby Drydocks and report to Ghimthota.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 220
      optional:
        - item:
            name: Spiked Bronze Labrys
            id: '1753'
            icon: '31405'
            ilvl: '13'
            level: '13'
            category:
              id: '3'
              name: Marauder's Arm
              icon: '60103'
          count: 1
        - item:
            name: Ash Picatrix
            id: '2146'
            icon: '33404'
            ilvl: '13'
            level: '13'
            category:
              id: '10'
              name: Arcanist's Grimoire
              icon: '60109'
          count: 1
        - item:
            name: Brass Daggers
            id: '9186'
            icon: '33805'
            ilvl: '13'
            level: '13'
            category:
              id: '84'
              name: Rogue's Arm
              icon: '60106'
          count: 1
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 7
    partQuestNo: 16
  - name: Victory in Peril
    level: 14
    rowId: 65950
    questId: SubSea117_00414
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Lower La Noscea
      coords: (24.8, 35.1)
      name: Ghimthota
    steps:
      - location: Lower La Noscea
        coords: (21.4, 33.4)
        name: Speak with one of the guards.
      - location: Lower La Noscea
        coords: (23.2, 35.0)
        name: Find the shifty-eyed sailor.
      - location: Lower La Noscea
        coords: (24.8, 35.1)
        name: Report to Ghimthota at the Moraby Drydocks.
      - location: Lower La Noscea
        coords: (26.4, 33.7)
        name: Speak with Ahtbyrm.
      - location: Lower La Noscea
        coords: (24.8, 35.1)
        name: Speak with Ghimthota.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 18
      timeLimit: 30
      id: '24'
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 212
      items:
        - item:
            name: Antidote
            id: '4564'
            icon: '20641'
            ilvl: '10'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 5
    partQuestNo: 17
  - name: Men of the Blue Tattoos
    level: 14
    rowId: 66225
    questId: ManSea006_00689
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Lower La Noscea
      coords: (24.8, 35.1)
      name: Ghimthota
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Deliver the arcane epistle to Baderon in Limsa Lominsa.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 239
    partQuestNo: 18
  - name: Feint and Strike
    level: 14
    rowId: 66080
    questId: ManSea007_00544
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.6, 11.1)
      name: Baderon
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.1, 6.0)
        name: Deliver Baderon's note to Reyner.
      - location: Western La Noscea
        coords: (34.8, 32.1)
        name: Travel to Swiftperch and speak with Ryssfloh.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 18
      timeLimit: 30
      id: '36'
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 220
      items:
        - item:
            name: Lominsan Ring
            id: '4427'
            icon: '54407'
            ilvl: '15'
            level: '15'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
    partQuestNo: 19
  - name: High Society
    level: 14
    rowId: 66226
    questId: ManSea008_00690
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.1, 6.0)
      name: Reyner
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Speak with Baderon at the Drowning Wench.
      - location: Limsa Lominsa Lower Decks
        coords: (10.0, 11.3)
        name: Collect a package from J'nasshym at the Octant.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Show the raxa-lined box to Baderon.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 230
      items:
        - item:
            name: Dress Shoes
            id: '3760'
            icon: '46329'
            ilvl: '1'
            level: '1'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
    partQuestNo: 20
  - name: A Mizzenmast Repast
    level: 14
    rowId: 66081
    questId: ManSea009_00545
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.6, 11.1)
      name: Baderon
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (11.4, 10.9)
        name: Put on the dress shoes and speak with Zanthael.
      - location: Command Room
        coords: (3.5, 3.4)
        name: Speak with Merlwyb in the command room.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 319
    partQuestNo: 21
  - name: The Lominsan Envoy
    level: 14
    rowId: 66082
    questId: ManSea200_00546
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Command Room
      coords: (3.5, 3.4)
      name: Merlwyb
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Speak with Baderon.
      - location: Limsa Lominsa Upper Decks
        coords: (10.7, 11.1)
        name: Speak with L'nophlo at the airship landing.
      - location: Limsa Lominsa Upper Decks
        coords: (11.0, 11.5)
        name: Board the airship.
      - location: New Gridania
        coords: (11.9, 13.0)
        name: Speak with the serpent honor guard.
      - location: Old Gridania
        coords: (8.0, 11.1)
        name: Present Merlwyb's missive to the silent conjurer at Nophica's Altar.
      - location: New Gridania
        coords: (11.8, 13.3)
        name: Speak with Lionnellais at the airship landing.
      - location: New Gridania
        coords: (11.3, 13.7)
        name: Board the airship.
      - location: Ul'dah - Steps of Nald
        coords: (10.9, 11.3)
        name: Speak with the flame honor guard.
      - location: Ul'dah - Steps of Thal
        coords: (10.7, 12.9)
        name: Present Merlwyb's missive to Bartholomew on the Hustings Strip.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: 310
        name: Leaving Limsa Lominsa
        type: achievement
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 286
      items:
        - item:
            name: Wind-up Airship
            id: '6213'
            icon: '59445'
            ilvl: '1'
            level: '1'
            category:
              id: '81'
              name: Minion
              icon: '60155'
          count: 1
    partQuestNo: 22
  - name: Call of the Sea
    level: 14
    rowId: 66210
    questId: SubWil141_00674
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (10.7, 12.9)
      name: Bartholomew
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Speak with Baderon at the Drowning Wench in Limsa Lominsa.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Gridanian Envoy
        level: 14
        rowId: 66043
        questId: ManFst200_00507
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 286
      items:
        - item:
            name: Phoenix Down
            id: '4570'
            icon: '20650'
            ilvl: '50'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
      optional:
        - item:
            name: Bronze Cuirass
            id: '3026'
            icon: '48001'
            ilvl: '15'
            level: '15'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '6'
            name: Soot Black
            color: '2828579'
        - item:
            name: Cotton Shirt
            id: '3022'
            icon: '42105'
            ilvl: '14'
            level: '14'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '6'
            name: Soot Black
            color: '2828579'
        - item:
            name: Cotton Cowl
            id: '3024'
            icon: '43610'
            ilvl: '15'
            level: '15'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '6'
            name: Soot Black
            color: '2828579'
        - item:
            name: Allagan Bronze Piece
            id: '5824'
            icon: '26001'
            ilvl: '15'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 4
    partQuestNo: 23
---