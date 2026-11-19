---
layout: quest-table
expansion: A Realm Reborn
partNo: 1
partChapterNo: 1
title: A Realm Reborn - Part 1 - Ul Dah 
permalink: /quests/msq/realm-reborn/part1/ul-dah
links:
  next: /quests/msq/realm-reborn/part2
quests:
  - name: Close to Home
    level: 1
    rowId: 66104
    questId: ManWil002_00568
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.6, 9.6)
      name: Momodi
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (8.3, 7.8)
        name: Attune yourself to the aetheryte found inside the city.
      - location: Ul'dah - Steps of Thal
        coords: (9.2, 11.7)
        name: Visit the Gladiators' Guild.
      - location: Ul'dah - Steps of Thal
        coords: (14.0, 10.4)
        name: Listen to Seseroga's explanation of the markets.
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Report to Momodi at the Quicksand.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Coming to Ul'dah
        level: 1
        rowId: 66130
        questId: ManWil001_00594
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 400
        paramGrowId: '1'
        avg: 400
      gil: 107
    partQuestNo: 1
  - name: We Must Rebuild
    level: 4
    rowId: 66131
    questId: SubWil027_00595
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.6, 9.6)
      name: Momodi
    steps:
      - location: Central Thanalan
        coords: (23.0, 27.8)
        name: Speak with Papashan at the Ul'dah Dispatch Yard.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      gil: 127
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
            id: '32'
            name: Mole Brown
            color: '6378053'
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
  - name: Nothing to See Here
    level: 4
    rowId: 66207
    questId: SubWil025_00671
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (23.0, 27.8)
      name: Papashan
    steps:
      - location: Central Thanalan
        coords: (23.2, 30.0)
        name: Deliver twilight pretzels to the patrols.
      - location: Central Thanalan
        coords: (23.0, 27.8)
        name: Speak with Papashan.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      items:
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
          count: 5
      optional:
        - item:
            name: Bronze Bastard Sword
            id: '1602'
            icon: '30502'
            ilvl: '5'
            level: '5'
            category:
              id: '2'
              name: Gladiator's Arm
              icon: '60102'
          count: 1
        - item:
            name: Bone Hora
            id: '1681'
            icon: '31005'
            ilvl: '5'
            level: '5'
            category:
              id: '1'
              name: Pugilist's Arm
              icon: '60101'
          count: 1
        - item:
            name: Bone Staff
            id: '2106'
            icon: '33001'
            ilvl: '5'
            level: '5'
            category:
              id: '7'
              name: "Two\u2013handed Thaumaturge's Arm"
              icon: '60108'
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
    partQuestNo: 3
  - name: Underneath the Sultantree
    level: 4
    rowId: 66086
    questId: ManWil005_00550
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (23.0, 27.8)
      name: Papashan
    steps:
      - location: Central Thanalan
        coords: (25.5, 32.2)
        name: Search for Lilira near the Sultantree.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 8
      timeLimit: 30
      id: '37'
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      gil: 132
    partQuestNo: 4
  - name: Step Nine
    level: 4
    rowId: 65839
    questId: SubWil060_00303
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (23.1, 27.7)
      name: Cicidoa
    steps:
      - location: Central Thanalan
        coords: (22.7, 26.6)
        name: Present the receipt to Gagari.
      - location: Central Thanalan
        coords: (19.5, 20.6)
        name: Deliver the pumpkin to Roger.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      gil: 139
      items:
        - item:
            name: Marmot Steak
            id: '4639'
            icon: '24355'
            ilvl: '5'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 2
    partQuestNo: 5
  - name: Prudence at This Junction
    level: 4
    rowId: 69388
    questId: XxaWil063_03852
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (19.5, 20.6)
      name: Roger
    steps:
      - location: Central Thanalan
        coords: (20.8, 18.5)
        name: Speak with Warin.
      - location: Central Thanalan
        coords: (20.8, 18.5)
        name: Present yourself to Warin for inspection.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
            id: '35'
            name: Ul Brown
            color: '12034928'
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
  - name: Out of House and Home
    level: 4
    rowId: 65843
    questId: SubWil064_00307
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (20.8, 18.5)
      name: Warin
    steps:
      - location: Central Thanalan
        coords: (22.0, 22.4)
        name: Lure out and slay coblyns.
      - location: Central Thanalan
        coords: (20.8, 18.5)
        name: Report to Warin.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '4'
        avg: 1040
      optional:
        - item:
            name: Viking Sword
            id: '1603'
            icon: '30491'
            ilvl: '7'
            level: '7'
            category:
              id: '2'
              name: Gladiator's Arm
              icon: '60102'
          count: 1
        - item:
            name: Leather Himantes
            id: '1682'
            icon: '31008'
            ilvl: '8'
            level: '8'
            category:
              id: '1'
              name: Pugilist's Arm
              icon: '60101'
          count: 1
        - item:
            name: Ramhorn Staff
            id: '2107'
            icon: '33001'
            ilvl: '9'
            level: '9'
            category:
              id: '7'
              name: "Two\u2013handed Thaumaturge's Arm"
              icon: '60108'
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
  - name: Way Down in the Hole
    level: 9
    rowId: 65856
    questId: SubWil066_00320
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (20.7, 18.3)
      name: Zuzumeda
    steps:
      - location: Central Thanalan
        coords: (19.5, 20.6)
        name: Speak with Wystan.
      - location: Central Thanalan
        coords: (19.8, 20.7)
        name: Give ginger cookies to the children.
      - location: Central Thanalan
        coords: (19.5, 20.6)
        name: Speak with Wystan.
      - location: Central Thanalan
        coords: (16.9, 23.8)
        name: Follow Wystan to the Sil'dih ruins.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 13
      timeLimit: 30
      id: '18'
    rewards:
      xp:
        factor: 400
        paramGrowId: '9'
        avg: 3240
      gil: 179
      items:
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
          count: 5
    partQuestNo: 8
  - name: Takin' What They're Givin'
    level: 10
    rowId: 66159
    questId: SubWil026_00623
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.6, 9.6)
      name: Momodi
    steps:
      - location: Western Thanalan
        coords: (22.7, 17.3)
        name: Speak with Dadanen at Horizon.
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
            id: '17'
            name: Mesa Red
            color: '8206598'
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
            id: '30'
            name: Gobbiebag Brown
            color: '12166281'
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
    partQuestNo: 9
  - name: Supply and Demands
    level: 10
    rowId: 65864
    questId: SubWil080_00328
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (22.7, 17.3)
      name: Dadanen
    steps:
      - location: Western Thanalan
        coords: (26.3, 18.2)
        name: Deliver Dadanen's final notice to Drunken Stag.
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
            id: '17'
            name: Mesa Red
            color: '8206598'
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
            id: '33'
            name: Loam Brown
            color: '4141865'
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
  - name: Give It to Me Raw
    level: 10
    rowId: 66039
    questId: SubWil095_00503
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (26.3, 18.2)
      name: Drunken Stag
    steps:
      - location: Western Thanalan
        coords: (27.4, 17.6)
        name: Search for the raw Nashachite.
      - location: Western Thanalan
        coords: (26.3, 18.2)
        name: Return the raw Nashachite to Drunken Stag.
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
            id: '17'
            name: Mesa Red
            color: '8206598'
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
  - name: The Perfect Swarm
    level: 10
    rowId: 65865
    questId: SubWil081_00329
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (26.3, 18.2)
      name: Drunken Stag
    steps:
      - location: Western Thanalan
        coords: (25.2, 18.9)
        name: Slay sun midge swarms.
      - location: Western Thanalan
        coords: (22.6, 17.1)
        name: Report to Fufulupa at Horizon.
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
            id: '17'
            name: Mesa Red
            color: '8206598'
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
  - name: Last Letter to Lost Hope
    level: 10
    rowId: 65866
    questId: SubWil082_00330
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (22.6, 17.1)
      name: Fufulupa
    steps:
      - location: Central Thanalan
        coords: (16.3, 22.0)
        name: Search for Seseli in central Thanalan.
      - location: Central Thanalan
        coords: (23.3, 16.0)
        name: Deliver Fufulupa's letter to Leofric at Lost Hope.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 188
    partQuestNo: 13
  - name: Heir Today, Gone Tomorrow
    level: 10
    rowId: 69389
    questId: XxaWil083_03853
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (23.3, 16.0)
      name: Leofric
    steps:
      - location: Central Thanalan
        coords: (24.0, 21.1)
        name: Defeat Baron von Quiveron III Esquire.
      - location: Central Thanalan
        coords: (23.3, 16.0)
        name: Report to Leofric.
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
            id: '48'
            name: Olive Green
            color: '4936242'
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
            id: '12'
            name: Wine Red
            color: '4527377'
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
  - name: Passing the Blade
    level: 10
    rowId: 65868
    questId: SubWil084_00332
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Central Thanalan
      coords: (23.3, 16.0)
      name: Leofric
    steps:
      - location: Western Thanalan
        coords: (22.6, 17.1)
        name: Deliver the antique dagger to Fufulupa in Horizon.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 196
    partQuestNo: 15
  - name: Following Footfalls
    level: 10
    rowId: 65869
    questId: SubWil085_00333
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (22.6, 17.1)
      name: Fufulupa
    steps:
      - location: Western Thanalan
        coords: (17.9, 16.0)
        name: Speak with Totoruna.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 204
      optional:
        - item:
            name: Bronze Scutum
            id: '2230'
            icon: '30003'
            ilvl: '13'
            level: '13'
            category:
              id: '11'
              name: Shield
              icon: '60110'
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
          count: 6
    partQuestNo: 16
  - name: Storms on the Horizon
    level: 10
    rowId: 65870
    questId: SubWil086_00334
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (17.9, 16.0)
      name: Nunuzofu
    steps:
      - location: Western Thanalan
        coords: (15.8, 18.5)
        name: Speak with Raffe in Crescent Cove.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '10'
        avg: 3420
      gil: 195
      optional:
        - item:
            name: Bronze Spatha
            id: '1605'
            icon: '30401'
            ilvl: '13'
            level: '13'
            category:
              id: '2'
              name: Gladiator's Arm
              icon: '60102'
          count: 1
        - item:
            name: Hard Leather Himantes
            id: '1685'
            icon: '31008'
            ilvl: '14'
            level: '14'
            category:
              id: '1'
              name: Pugilist's Arm
              icon: '60101'
          count: 1
        - item:
            name: Decorated Bone Staff
            id: '2108'
            icon: '33002'
            ilvl: '12'
            level: '12'
            category:
              id: '7'
              name: "Two\u2013handed Thaumaturge's Arm"
              icon: '60108'
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
          count: 3
    partQuestNo: 17
  - name: Oh Captain, My Captain
    level: 14
    rowId: 65872
    questId: SubWil088_00336
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (14.9, 18.9)
      name: Merilda
    steps:
      - location: Western Thanalan
        coords: (16.7, 15.6)
        name: Speak with Captain Baldewyn.
      - location: Western Thanalan
        coords: (22.6, 17.1)
        name: Speak with Fufulupa in Horizon.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 18
      timeLimit: 30
      id: '39'
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 220
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
    partQuestNo: 18
  - name: Secrets and Lies
    level: 14
    rowId: 66164
    questId: ManWil006_00628
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Western Thanalan
      coords: (22.6, 17.1)
      name: Fufulupa
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Show the letter to Momodi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 220
    partQuestNo: 19
  - name: Duty, Honor, Country
    level: 14
    rowId: 66087
    questId: ManWil007_00551
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.6, 9.6)
      name: Momodi
    steps:
      - location: Heart of the Sworn
        coords: (6.1, 6.0)
        name: Deliver the letter to Owyne.
      - location: Central Thanalan
        coords: (26.4, 18.8)
        name: Rendezvous with Owyne at the Unholy Heir.
      - location: Central Thanalan
        coords: (26.4, 18.8)
        name: Speak with Papashan in the Heart of the Sworn.
      - location: Heart of the Sworn
        coords: (6.1, 6.0)
        name: Speak with Papashan in the Heart of the Sworn.
    expansion:
      id: '0'
      name: A Realm Reborn
    soloDuty:
      levelSync: 18
      timeLimit: 30
      id: '38'
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 220
      items:
        - item:
            name: Ul'dahn Ring
            id: '4429'
            icon: '54414'
            ilvl: '15'
            level: '15'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
    partQuestNo: 20
  - name: A Matter of Tradition
    level: 14
    rowId: 66177
    questId: ManWil008_00641
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Heart of the Sworn
      coords: (6.1, 6.0)
      name: Owyne
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Speak with Momodi at the Quicksand.
      - location: Ul'dah - Steps of Thal
        coords: (10.7, 13.4)
        name: Collect the earrings from Serendipity.
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Deliver the wooden lockbox to Momodi.
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
            name: Voice of the Just
            id: '4196'
            icon: '55213'
            ilvl: '1'
            level: '1'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
    partQuestNo: 21
  - name: A Royal Reception
    level: 14
    rowId: 66088
    questId: ManWil009_00552
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.6, 9.6)
      name: Momodi
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (10.7, 12.9)
        name: Put on the Voice of the Just and speak with Bartholomew.
      - location: Ul'dah - Steps of Nald
        coords: (8.4, 8.9)
        name: Speak with Raubahn in the Hall of Flames.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '14'
        avg: 5520
      gil: 319
    partQuestNo: 22
  - name: The Ul'dahn Envoy
    level: 14
    rowId: 66064
    questId: ManWil200_00528
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (8.4, 8.9)
      name: Raubahn
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Speak with Momodi.
      - location: Ul'dah - Steps of Nald
        coords: (10.7, 11.2)
        name: Speak with Elyenora at the airship landing.
      - location: Ul'dah - Steps of Nald
        coords: (10.3, 11.2)
        name: Board the airship.
      - location: Limsa Lominsa Upper Decks
        coords: (11.1, 10.9)
        name: Speak with the storm honor guard.
      - location: Limsa Lominsa Lower Decks
        coords: (11.4, 10.9)
        name: Present Raubahn's missive to Zanthael at Bulwark Hall.
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
        name: Present Raubahn's missive to the silent conjurer at Nophica's Altar.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: 312
        name: Out of Ul'dah
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
    partQuestNo: 23
  - name: Call of the Sea
    level: 14
    rowId: 66209
    questId: SubFst102_00673
    genre:
      id: '1'
      name: Seventh Umbral Era
    icon: '71000'
    issuer:
      location: Old Gridania
      coords: (8.1, 11.1)
      name: serpent officer
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Speak with Baderon at the Drowning Wench in Limsa Lominsa.
    expansion:
      id: '0'
      name: A Realm Reborn
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
            id: '12'
            name: Wine Red
            color: '4527377'
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
    partQuestNo: 24


---