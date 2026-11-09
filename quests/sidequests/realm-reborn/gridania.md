---
layout: quest-table
title: Gridanian Sidequests
permalink: /quests/sidequests/realm-reborn/gridania
nonsequential: true
brandLabel: Mognet
brandUrl: /quests/sidequests/realm-reborn
quests:
  - name: Coming to Gridania
    level: 1
    rowId: 65575
    questId: ManFst001_00039
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (13.5, 14.1)
      name: Bertennant
    steps:
      - location: New Gridania
        coords: (11.7, 13.5)
        name: Speak with Miounne.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '1'
        avg: 400
      gil: 103
  - name: A Good Adventurer Is Hard to Find
    level: 1
    rowId: 65537
    questId: SubFst010_00001
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (12.2, 12.2)
      name: Bernadette
    steps:
      - location: New Gridania
        coords: (15.2, 12.3)
        name: Speak with Chansteloup.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Coming to Gridania
        level: 1
        rowId: 65575
        questId: ManFst001_00039
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
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
          count: 2
  - name: Incense and Sensibility
    level: 1
    rowId: 65556
    questId: SubFst000_00020
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (8.4, 8.9)
      name: Mellaine
    steps:
      - location: Old Gridania
        coords: (6.3, 11.0)
        name: Speak with Braya.
      - location: Old Gridania
        coords: (5.9, 10.6)
        name: Pour the Azeyma rose oil into the censers.
      - location: Old Gridania
        coords: (6.3, 11.0)
        name: Report to Braya at the Conjurers' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 103
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
  - name: Coarse Correspondence
    level: 1
    rowId: 65560
    questId: SubFst001_00024
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (15.1, 12.0)
      name: F'mibhas
    steps:
      - location: Old Gridania
        coords: (14.6, 9.3)
        name: Deliver the sealed message to Parnell in the markets.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 103
  - name: Preserving the Past
    level: 1
    rowId: 65563
    questId: SubFst004_00027
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (10.9, 12.0)
      name: Idele
    steps:
      - location: New Gridania
        coords: (9.9, 12.5)
        name: Speak with Louhelic.
      - location: Old Gridania
        coords: (10.5, 8.9)
        name: Deliver the recruit's toolbox to Artor.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      items:
        - item:
            name: Grade 1 Dark Matter
            id: '5594'
            icon: '20401'
            ilvl: '1'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 10
  - name: I Am Millicent, Hear Me Roar
    level: 1
    rowId: 65585
    questId: SubFst019_00049
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (10.3, 8.5)
      name: Duimessand
    steps:
      - location: Old Gridania
        coords: (12.3, 8.6)
        name: Speak with Millicent.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
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
  - name: Parsemontrenomics
    level: 1
    rowId: 65574
    questId: SubFst012_00038
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (14.7, 9.4)
      name: Parsemontret
    steps:
      - location: Old Gridania
        coords: (14.2, 9.9)
        name: Obtain a bone spearhead from Gurthcid.
      - location: Old Gridania
        coords: (14.5, 10.0)
        name: Obtain a pot of beeswax oil from Admiranda.
      - location: Old Gridania
        coords: (14.3, 8.8)
        name: Obtain a length of brambleweed rope from Alaric.
      - location: Old Gridania
        coords: (14.1, 6.2)
        name: Deliver the requested items to Ceinguled.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 111
  - name: For Friendship
    level: 1
    rowId: 65576
    questId: SubFst013_00040
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (9.6, 12.3)
      name: Nicoliaux
    steps:
      - location: New Gridania
        coords: (9.6, 12.0)
        name: Greet Aunillie with a /bow.
      - location: New Gridania
        coords: (9.6, 12.3)
        name: Speak with Nicoliaux.
      - location: New Gridania
        coords: (9.6, 12.0)
        name: Express your /joy to Aunillie.
      - location: New Gridania
        coords: (9.6, 12.3)
        name: Speak with Nicoliaux.
      - location: New Gridania
        coords: (9.6, 12.0)
        name: /dance for Aunillie.
      - location: New Gridania
        coords: (9.6, 12.3)
        name: Speak with Nicoliaux.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 111
  - name: Covered in Roses
    level: 1
    rowId: 65577
    questId: SubFst014_00041
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (7.7, 8.0)
      name: Samiane
    steps:
      - location: Old Gridania
        coords: (6.8, 8.1)
        name: Gather Azeyma rose hips.
      - location: Old Gridania
        coords: (7.7, 8.0)
        name: Deliver the Azeyma rose hips to Samiane.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 111
  - name: Sylphic Gratitude
    level: 1
    rowId: 65578
    questId: SubFst015_00042
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (10.1, 8.8)
      name: Estaine
    steps:
      - location: Old Gridania
        coords: (10.2, 9.1)
        name: Gather the vegetable offerings.
      - location: Old Gridania
        coords: (10.1, 8.8)
        name: Speak with Estaine.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 110
  - name: Quarrels with Squirrels
    level: 1
    rowId: 65561
    questId: SubFst002_00025
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (14.0, 5.7)
      name: Boiselont
    steps:
      - location: Central Shroud
        coords: (23.7, 16.2)
        name: Slay ground squirrels.
      - location: Old Gridania
        coords: (14.0, 5.7)
        name: Report to Boiselont at the Lancers' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '1'
        avg: 100
  - name: Once Bitten, Twice Shy
    level: 1
    rowId: 65562
    questId: SubFst003_00026
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (6.5, 7.5)
      name: Ethelred
    steps:
      - location: Old Gridania
        coords: (7.9, 10.9)
        name: Deliver the Azeyma rose to Waldew.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 118
  - name: Essential Oil
    level: 1
    rowId: 65567
    questId: SubFst007_00031
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (6.3, 11.0)
      name: Braya
    steps:
      - location: Central Shroud
        coords: (22.9, 17.0)
        name: Obtain scarlet oil from little ladybugs.
      - location: Old Gridania
        coords: (6.3, 11.0)
        name: Deliver the scarlet oil to Braya.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '1'
        avg: 100
      optional:
        - item:
            name: Fingerless Leather Gloves
            id: '3530'
            icon: '44060'
            ilvl: '5'
            level: '5'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '74'
            name: Midnight Blue
            color: '1579319'
        - item:
            name: Leather Lightmitts
            id: '3531'
            icon: '44065'
            ilvl: '5'
            level: '5'
            category:
              id: '37'
              name: Hands
              icon: '60129'
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
          count: 1
  - name: A Hard Nut to Crack
    level: 3
    rowId: 65568
    questId: SubFst008_00032
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (12.0, 13.4)
      name: Tatasosa
    steps:
      - location: Old Gridania
        coords: (7.3, 9.2)
        name: Speak with Barnabontant.
      - location: North Shroud
        coords: (28.4, 28.3)
        name: Deliver the iron snaffle to Bodwine.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 65621
        questId: ManFst002_00085
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 65659
        questId: ManFst003_00123
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 65660
        questId: ManFst004_00124
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '3'
        avg: 240
      optional:
        - item:
            name: Hempen Tabard
            id: '2999'
            icon: '43042'
            ilvl: '5'
            level: '5'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '74'
            name: Midnight Blue
            color: '1579319'
        - item:
            name: Hempen Halfrobe
            id: '3010'
            icon: '42150'
            ilvl: '5'
            level: '5'
            category:
              id: '35'
              name: Body
              icon: '60126'
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
  - name: Derision of Labor
    level: 4
    rowId: 65570
    questId: SubFst009_00034
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (12.0, 13.5)
      name: Celestine
    steps:
      - location: Central Shroud
        coords: (23.6, 19.9)
        name: Deliver the provisions to Tsubh Khamazom.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 65621
        questId: ManFst002_00085
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 65659
        questId: ManFst003_00123
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 65660
        questId: ManFst004_00124
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 127
      optional:
        - item:
            name: Hempen Sarouel
            id: '3311'
            icon: '45064'
            ilvl: '5'
            level: '5'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '33'
            name: Loam Brown
            color: '4141865'
        - item:
            name: Hempen Tights
            id: '3312'
            icon: '45079'
            ilvl: '5'
            level: '5'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '33'
            name: Loam Brown
            color: '4141865'
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 3
  - name: Population Control
    level: 1
    rowId: 65573
    questId: SubFst011_00037
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (15.2, 12.3)
      name: Chansteloup
    steps:
      - location: Central Shroud
        coords: (24.2, 18.0)
        name: Slay forest funguars.
      - location: New Gridania
        coords: (15.2, 12.3)
        name: Report to Chansteloup.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Good Adventurer Is Hard to Find
        level: 1
        rowId: 65537
        questId: SubFst010_00001
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '1'
        avg: 100
      optional:
        - item:
            name: Leather Eyepatch
            id: '2653'
            icon: '40914'
            ilvl: '5'
            level: '5'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '74'
            name: Midnight Blue
            color: '1579319'
        - item:
            name: Hempen Hat
            id: '2655'
            icon: '41015'
            ilvl: '5'
            level: '5'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '32'
            name: Mole Brown
            color: '6378053'
        - item:
            name: Allagan Tin Piece
            id: '5823'
            icon: '26001'
            ilvl: '5'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 4
  - name: Jumping at Shadows
    level: 3
    rowId: 65706
    questId: SubFst026_00170
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (28.4, 28.3)
      name: Bodwine
    steps:
      - location: North Shroud
        coords: (26.6, 27.1)
        name: Slay mitelings.
      - location: North Shroud
        coords: (28.4, 28.3)
        name: Report to Bodwine.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '3'
        avg: 240
      gil: 135
  - name: The Nose Knows
    level: 3
    rowId: 65709
    questId: SubFst030_00173
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (28.0, 27.9)
      name: Vionne
    steps:
      - location: North Shroud
        coords: (27.7, 29.0)
        name: Speak with Gillian.
      - location: North Shroud
        coords: (27.9, 29.0)
        name: Retrieve the burlap sack.
      - location: North Shroud
        coords: (25.8, 28.2)
        name: Deliver the burlap sack to Nolanel.
      - location: North Shroud
        coords: (28.0, 27.9)
        name: Report to Vionne.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '3'
        avg: 240
      gil: 103
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
          count: 10
  - name: A Glim Harvest
    level: 4
    rowId: 65731
    questId: SubFst044_00195
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (29.2, 18.7)
      name: Linyeve
    steps:
      - location: North Shroud
        coords: (25.7, 23.0)
        name: Pick the brightest glimshroom.
      - location: North Shroud
        coords: (29.2, 18.7)
        name: Deliver the glimshroom to Linyeve at Hyrstmill.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 138
  - name: Idle Initiatives
    level: 4
    rowId: 65746
    questId: SubFst046_00210
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (23.6, 19.9)
      name: Tsubh Khamazom
    steps:
      - location: Central Shroud
        coords: (23.3, 19.6)
        name: Speak with the idle initiates.
      - location: Central Shroud
        coords: (23.6, 19.9)
        name: Report to Tsubh Khamazom at the Bannock.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 135
  - name: Death to the Bean Thieves
    level: 4
    rowId: 65639
    questId: SubFst025_00103
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (27.5, 27.9)
      name: Q'djawana
    steps:
      - location: North Shroud
        coords: (27.8, 24.8)
        name: "Slay opo-opos and recover Dametta's Mun\u2013Tuy beans."
      - location: North Shroud
        coords: (29.5, 19.4)
        name: "Deliver the bags of Mun\u2013Tuy beans to Dametta."
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Clear Sign
        level: 4
        rowId: 65735
        questId: SubFst043_00199
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 146
      items:
        - item:
            name: Chanterelle Saute
            id: '4689'
            icon: '24205'
            ilvl: '7'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 5
  - name: The Valued Vilekin
    level: 3
    rowId: 65707
    questId: SubFst028_00171
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (28.4, 28.3)
      name: Bodwine
    steps:
      - location: North Shroud
        coords: (25.5, 28.4)
        name: Search for aphids in the tangled undergrowth.
      - location: North Shroud
        coords: (25.5, 28.4)
        name: Gather aphids from the tangled undergrowth.
      - location: North Shroud
        coords: (28.6, 25.7)
        name: Deliver the aphids to Guithrit.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Jumping at Shadows
        level: 3
        rowId: 65706
        questId: SubFst026_00170
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '3'
        avg: 240
      gil: 147
  - name: A Clear Sign
    level: 4
    rowId: 65735
    questId: SubFst043_00199
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (28.6, 26.1)
      name: Paulemont
    steps:
      - location: North Shroud
        coords: (27.4, 27.4)
        name: Clean the dusty malmstones.
      - location: North Shroud
        coords: (27.5, 27.9)
        name: Report to Q'djawana at Treespeak Stables.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 146
  - name: Hematophagic Harassment
    level: 4
    rowId: 65631
    questId: SubFst021_00095
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (27.9, 19.9)
      name: Eadbert
    steps:
      - location: North Shroud
        coords: (27.5, 21.4)
        name: Slay midge swarms.
      - location: North Shroud
        coords: (27.9, 19.9)
        name: Report to Eadbert.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 128
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
          count: 7
  - name: More than a Flesh Wound
    level: 4
    rowId: 65708
    questId: SubFst029_00172
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (25.5, 19.5)
      name: Arold
    steps:
      - location: Central Shroud
        coords: (25.5, 19.5)
        name: Give a hi-potion to Arold.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Eggs over Queasy
        level: 4
        rowId: 69390
        questId: XxaFst034_03854
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 146
      optional:
        - item:
            name: Copper Gorget
            id: '4305'
            icon: '54801'
            ilvl: '8'
            level: '8'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Bone Necklace
            id: '4306'
            icon: '54830'
            ilvl: '8'
            level: '8'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
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
  - name: No Quarter Given
    level: 4
    rowId: 65710
    questId: SubFst037_00174
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (28.6, 25.7)
      name: Guithrit
    steps:
      - location: North Shroud
        coords: (26.1, 26.1)
        name: Slay Ixali dulltalons.
      - location: North Shroud
        coords: (26.1, 26.1)
        name: Slay Ixali lostwings.
      - location: North Shroud
        coords: (26.1, 26.1)
        name: Slay Ixali slowbeaks.
      - location: North Shroud
        coords: (28.6, 25.7)
        name: "Report to Guithrit outside E\u2013Tatt's Spire."
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Valued Vilekin
        level: 3
        rowId: 65707
        questId: SubFst028_00171
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 156
  - name: Splitting Shells
    level: 4
    rowId: 65733
    questId: SubFst041_00197
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (23.6, 20.0)
      name: Maurelin
    steps:
      - location: Central Shroud
        coords: (25.0, 23.7)
        name: Slay bog yarzons and obtain their shells.
      - location: Central Shroud
        coords: (24.2, 20.1)
        name: Deliver the bog yarzon shells to Mariustel at the Bannock.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      optional:
        - item:
            name: Braised Pipira
            id: '4657'
            icon: '24311'
            ilvl: '7'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Tree Toad Legs
            id: '4658'
            icon: '24313'
            ilvl: '7'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Allagan Tin Piece
            id: '5823'
            icon: '26001'
            ilvl: '5'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 3
  - name: Harriers of the Hedgetree
    level: 4
    rowId: 65633
    questId: SubFst022_00097
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (27.9, 19.9)
      name: Eadbert
    steps:
      - location: North Shroud
        coords: (29.5, 23.0)
        name: Investigate the Hedgetree.
      - location: North Shroud
        coords: (27.9, 19.9)
        name: Report to Eadbert.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Hematophagic Harassment
        level: 4
        rowId: 65631
        questId: SubFst021_00095
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      optional:
        - item:
            name: Leather Leggings
            id: '3765'
            icon: '46159'
            ilvl: '8'
            level: '8'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '5'
            name: Charcoal Grey
            color: '4736834'
        - item:
            name: Leather Boots
            id: '3766'
            icon: '46137'
            ilvl: '8'
            level: '8'
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
  - name: Drink Your Beans, Dear
    level: 4
    rowId: 65634
    questId: SubFst023_00098
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (29.5, 19.4)
      name: Dametta
    steps:
      - location: North Shroud
        coords: (27.0, 20.8)
        name: Slay microchus and gather leaflets from their remains.
      - location: North Shroud
        coords: (29.5, 19.4)
        name: Deliver the microchu leaflets to Dametta.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Death to the Bean Thieves
        level: 4
        rowId: 65639
        questId: SubFst025_00103
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      optional:
        - item:
            name: Hard Leather Pot Helm
            id: '2654'
            icon: '40015'
            ilvl: '8'
            level: '8'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '5'
            name: Charcoal Grey
            color: '4736834'
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
          count: 10
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
  - name: Parasite Cleave
    level: 4
    rowId: 65663
    questId: SubFst033_00127
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (27.2, 20.8)
      name: Gabineaux
    steps:
      - location: Central Shroud
        coords: (26.7, 21.5)
        name: Apply the amber unguent to the ailing trees and slay parasite funguars.
      - location: Central Shroud
        coords: (27.2, 20.8)
        name: Report to Gabineaux at Gabineaux's Bower.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Surveying the Damage
        level: 4
        rowId: 65711
        questId: SubFst038_00175
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      optional:
        - item:
            name: Leather Mitts
            id: '3534'
            icon: '44065'
            ilvl: '8'
            level: '8'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '5'
            name: Charcoal Grey
            color: '4736834'
        - item:
            name: Leather Ringbands
            id: '3535'
            icon: '48250'
            ilvl: '8'
            level: '8'
            category:
              id: '37'
              name: Hands
              icon: '60129'
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
          count: 1
  - name: Soil Despoilers
    level: 4
    rowId: 65666
    questId: SubFst036_00130
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (27.2, 20.8)
      name: Gabineaux
    steps:
      - location: Central Shroud
        coords: (28.7, 20.3)
        name: Slay eight microchus.
      - location: Central Shroud
        coords: (26.9, 21.3)
        name: Report to Ealdfrith at Gabineaux's Bower.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Parasite Cleave
        level: 4
        rowId: 65663
        questId: SubFst033_00127
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 122
  - name: The Kindness of Strangers
    level: 4
    rowId: 65635
    questId: SubFst024_00099
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (28.1, 20.1)
      name: Emeria
    steps:
      - location: North Shroud
        coords: (28.6, 21.5)
        name: Meet with Ailbert.
      - location: North Shroud
        coords: (28.1, 20.1)
        name: Deliver Ailbert's letter to Emeria.
      - location: New Gridania
        coords: (11.7, 13.5)
        name: Speak with Miounne in Gridania.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Harriers of the Hedgetree
        level: 4
        rowId: 65633
        questId: SubFst022_00097
        genre: Gridanian Sidequests
        icon: '71020'
      - name: Drink Your Beans, Dear
        level: 4
        rowId: 65634
        questId: SubFst023_00098
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      optional:
        - item:
            name: Hempen Kecks
            id: '3313'
            icon: '45062'
            ilvl: '8'
            level: '8'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '5'
            name: Charcoal Grey
            color: '4736834'
        - item:
            name: Hempen Gaskins
            id: '3314'
            icon: '45309'
            ilvl: '8'
            level: '8'
            category:
              id: '36'
              name: Legs
              icon: '60128'
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
          count: 1
  - name: He's Got a Ticket to Ride
    level: 9
    rowId: 66964
    questId: SubFst122_01428
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (12.0, 13.5)
      name: Spinning Blade
    steps:
      - location: New Gridania
        coords: (12.0, 12.9)
        name: Speak with Raimondaux.
      - location: New Gridania
        coords: (12.0, 12.9)
        name: "With the chat mode in **Say**, enter \u201CHail fellow well met!\u201D\
          \ to greet Raimondaux."
      - location: New Gridania
        coords: (12.0, 12.9)
        name: "With the chat mode in **Say**, enter the auto\u2013translate option\
          \ Hello! to greet Raimondaux again."
      - location: New Gridania
        coords: (12.0, 12.9)
        name: Speak with Raimondaux.
      - location: New Gridania
        coords: (12.0, 12.9)
        name: "With the chat mode in **Say**, enter \u201CGot everything?\u201D"
      - location: New Gridania
        coords: (12.0, 12.9)
        name: Give the airship ticket to Raimondaux.
      - location: New Gridania
        coords: (12.0, 12.9)
        name: "With the chat mode in **Say**, enter the auto\u2013translate option\
          \ Good-bye.."
      - location: New Gridania
        coords: (12.0, 13.5)
        name: Speak with Spinning Blade.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Spirithold Broken
        level: 9
        rowId: 65665
        questId: SubFst035_00129
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '9'
        avg: 810
  - name: Simply the Hest
    level: 10
    rowId: 65596
    questId: SubFst121_00060
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Central Shroud
      coords: (22.6, 22.3)
      name: Tierney
    steps:
      - location: Central Shroud
        coords: (22.5, 21.7)
        name: Speak with Battlewarden Ribald.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Leves of Bentbranch
        level: 10
        rowId: 65756
        questId: SubFst070_00220
        genre: Gridanian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
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
  - name: Leves of Bentbranch
    level: 10
    rowId: 65756
    questId: SubFst070_00220
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: New Gridania
      coords: (11.7, 13.4)
      name: Gontrant
    steps:
      - location: Central Shroud
        coords: (22.6, 22.3)
        name: Speak with Tierney at Bentbranch Meadows.
      - location: Central Shroud
        coords: (18.7, 19.2)
        name: Complete Tierney's trial guildleve.
      - location: Central Shroud
        coords: (22.6, 22.3)
        name: Report to Tierney at Bentbranch Meadows.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Spirithold Broken
        level: 9
        rowId: 65665
        questId: SubFst035_00129
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 215
  - name: Not a Material Girl
    level: 10
    rowId: 65911
    questId: SubFst048_00375
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (20.3, 22.3)
      name: Kukuvachi
    steps:
      - location: Central Shroud
        coords: (20.7, 22.7)
        name: Ask the locals about Keitha's wants and desires.
      - location: Central Shroud
        coords: (20.3, 22.3)
        name: Return to Kukuvachi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 173
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
  - name: Look, but Won't Touch
    level: 10
    rowId: 65914
    questId: SubFst057_00378
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (18.9, 20.6)
      name: Roseline
    steps:
      - location: Central Shroud
        coords: (17.8, 18.9)
        name: Destroy the diremite eggs.
      - location: Central Shroud
        coords: (18.9, 20.6)
        name: Report to Roseline.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: You Shall Not Trespass
        level: 10
        rowId: 65912
        questId: SubFst049_00376
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 220
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
  - name: Where the Heart Is (The Lavender Beds)
    level: 10
    rowId: 66748
    questId: SubCts803_01212
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Central Shroud
      coords: (21.7, 21.9)
      name: Margeria
    steps:
      - location: Central Shroud
        coords: (25.2, 28.0)
        name: Speak with Emblyn.
      - location: The Lavender Beds
        coords: (11.4, 15.2)
        name: Journey to the Lavender Beds.
      - location: The Lavender Beds
        coords: (11.2, 14.8)
        name: Speak with the serpent recruit.
      - location: Central Shroud
        coords: (21.7, 21.9)
        name: Report to Margeria.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '10'
        avg: 427
      gil: 167
  - name: Extending Fences
    level: 10
    rowId: 65693
    questId: SubFst051_00157
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (20.2, 21.6)
      name: Luquelot
    steps:
      - location: Central Shroud
        coords: (19.5, 19.3)
        name: Obtain six strands of diremite web.
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Deliver the strands of diremite web to Luquelot at Bentbranch Meadows.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Not a Material Girl
        level: 10
        rowId: 65911
        questId: SubFst048_00375
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 180
      optional:
        - item:
            name: Bone Armillae
            id: '4093'
            icon: '55632'
            ilvl: '10'
            level: '10'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Copper Ear Cuffs
            id: '4198'
            icon: '55201'
            ilvl: '11'
            level: '11'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
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
  - name: Walking the Planks
    level: 10
    rowId: 65922
    questId: SubFst072_00386
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (25.1, 27.9)
      name: Waltheof
    steps:
      - location: Central Shroud
        coords: (25.9, 27.9)
        name: Pick up the goods at the end of the pier.
      - location: Central Shroud
        coords: (25.1, 27.9)
        name: Deliver the goods.
      - location: Central Shroud
        coords: (25.1, 27.9)
        name: Report to Waltheof.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 178
      optional:
        - item:
            name: Copper Ring
            id: '4422'
            icon: '54401'
            ilvl: '9'
            level: '9'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Bone Ring
            id: '4421'
            icon: '54432'
            ilvl: '9'
            level: '9'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Allagan Tin Piece
            id: '5823'
            icon: '26001'
            ilvl: '5'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 3
  - name: Sting in a Bottle
    level: 10
    rowId: 65694
    questId: SubFst052_00158
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (25.1, 27.9)
      name: Waltheof
    steps:
      - location: Central Shroud
        coords: (24.7, 29.3)
        name: Slay hornet swarms and collect their husks.
      - location: Central Shroud
        coords: (25.1, 27.9)
        name: Deliver the hornet husks to Waltheof.
      - location: Central Shroud
        coords: (20.6, 20.8)
        name: Deliver the bottle of stingbrew to Margault at Bentbranch Meadows.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Walking the Planks
        level: 10
        rowId: 65922
        questId: SubFst072_00386
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 220
      optional:
        - item:
            name: Hard Leather Kecks
            id: '27636'
            icon: '45099'
            ilvl: '12'
            level: '12'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '41'
            name: Halatali Yellow
            color: '10847280'
        - item:
            name: Striped Cotton Slops
            id: '3320'
            icon: '45296'
            ilvl: '13'
            level: '13'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '31'
            name: Shale Brown
            color: '9601388'
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
  - name: If Ye Break Faith
    level: 10
    rowId: 65919
    questId: SubFst067_00383
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (22.4, 25.9)
      name: Finnea
    steps:
      - location: Central Shroud
        coords: (20.6, 28.2)
        name: Speak with Balarr.
      - location: Central Shroud
        coords: (19.5, 27.7)
        name: Lay the Nymeia lilies atop the barrows.
      - location: Central Shroud
        coords: (20.6, 28.2)
        name: Report to Balarr.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 211
      optional:
        - item:
            name: Hard Leather Thighboots
            id: '27637'
            icon: '46103'
            ilvl: '12'
            level: '12'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
        - item:
            name: Hard Leather Sandals
            id: '3773'
            icon: '49804'
            ilvl: '12'
            level: '12'
            category:
              id: '38'
              name: Feet
              icon: '60130'
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
          count: 2
  - name: Favor for the Fisherwoman
    level: 10
    rowId: 65921
    questId: SubFst069_00385
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (25.1, 27.9)
      name: Berthe
    steps:
      - location: Central Shroud
        coords: (28.9, 30.6)
        name: Retrieve the well-worn fishing rod.
      - location: Central Shroud
        coords: (25.1, 27.9)
        name: Deliver the well-worn fishing rod to Berthe at the Mirror Planks.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 188
      optional:
        - item:
            name: Hard Leather Harness
            id: '3017'
            icon: '43134'
            ilvl: '12'
            level: '12'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '41'
            name: Halatali Yellow
            color: '10847280'
        - item:
            name: Hempen Robe
            id: '3018'
            icon: '42044'
            ilvl: '12'
            level: '12'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '25'
            name: Aldgoat Brown
            color: '10651484'
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
  - name: Slimy Hollows
    level: 10
    rowId: 65696
    questId: SubFst054_00160
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (22.4, 25.9)
      name: Finnea
    steps:
      - location: Central Shroud
        coords: (20.3, 30.0)
        name: Sprinkle ale near the moist depressions and defeat the saprophagous
          slugs.
      - location: Central Shroud
        coords: (22.4, 25.9)
        name: Report to Finnea at Galvanth's Spire.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: If Ye Break Faith
        level: 10
        rowId: 65919
        questId: SubFst067_00383
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      optional:
        - item:
            name: Altered Cotton Bandana
            id: '27635'
            icon: '41540'
            ilvl: '12'
            level: '12'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '34'
            name: Bone White
            color: '15455136'
        - item:
            name: Brass Spectacles
            id: '2668'
            icon: '40879'
            ilvl: '13'
            level: '13'
            category:
              id: '34'
              name: Head
              icon: '60124'
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
          count: 2
  - name: Saw That One Coming
    level: 14
    rowId: 66961
    questId: SubFst159_01425
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (12.0, 13.1)
      name: Eral
    steps:
      - location: New Gridania
        coords: (9.4, 12.0)
        name: Speak with Yedythe.
      - location: New Gridania
        coords: (10.3, 12.3)
        name: Speak with Beatin.
      - location: Old Gridania
        coords: (8.3, 10.6)
        name: Give the toys to the children.
      - location: New Gridania
        coords: (9.4, 12.0)
        name: Report to Yedythe.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: '102'
        name: Harvest Dance
        type: emote
    requires:
      - name: A Royal Reception
        level: 14
        rowId: 66088
        questId: ManWil009_00552
        genre: Seventh Umbral Era
        icon: '71000'
      - name: A Mizzenmast Repast
        level: 14
        rowId: 66081
        questId: ManSea009_00545
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Renewing the Covenant
        level: 14
        rowId: 65985
        questId: ManFst009_00449
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 75
        paramGrowId: '14'
        avg: 1035
  - name: Leves of Hawthorne
    level: 15
    rowId: 65757
    questId: SubFst071_00221
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: East Shroud
      coords: (17.2, 27.2)
      name: Qina Lyehga
    steps:
      - location: East Shroud
        coords: (18.3, 27.5)
        name: Complete the trial guildleve assigned to you by Qina Lyehga.
      - location: East Shroud
        coords: (17.2, 27.2)
        name: Report to Qina Lyehga at the Hawthorne Hut.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Leves of Swiftperch
        level: 10
        rowId: 66229
        questId: SubSea901_00693
        genre: La Noscean Sidequests
        icon: '71140'
      - name: Leves of Bentbranch
        level: 10
        rowId: 65756
        questId: SubFst070_00220
        genre: Gridanian Sidequests
        icon: '71140'
      - name: Leves of Horizon
        level: 10
        rowId: 66223
        questId: SubWil150_00687
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      gil: 239
  - name: So You Think You Can Ride This Chocobo
    level: 15
    rowId: 66101
    questId: SubGsc105_00565
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Central Shroud
      coords: (20.4, 22.8)
      name: Katering
    steps:
      - location: Chocobo Square
        coords: (6.1, 4.7)
        name: Speak with the race chocobo registrar in the Gold Saucer.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: So You Want to Be a Jockey
        level: 15
        rowId: 65972
        questId: SubGsc101_00436
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
      gil: 539
  - name: An Ill-conceived Venture
    level: 17
    rowId: 66968
    questId: SubCts811_01432
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: New Gridania
      coords: (11.8, 12.3)
      name: troubled adventurer
    steps:
      - location: East Shroud
        coords: (20.4, 27.5)
        name: Search Nine Ivies for the missing retainer.
      - location: Old Gridania
        coords: (14.6, 9.3)
        name: Speak with Parnell in Old Gridania.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '17'
        avg: 1560
      gil: 418
      items:
        - item:
            name: Venture
            id: '21072'
            icon: '65049'
            ilvl: '1'
            level: '1'
            category:
              id: '100'
              name: Currency
              icon: '60179'
          count: 6
  - name: A Sight to Behold
    level: 20
    rowId: 65698
    questId: SubCts817_00162
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: New Gridania
      coords: (11.8, 13.4)
      name: Naoh Gamduhla
    steps:
      - location: New Gridania
        coords: (12.0, 13.1)
        name: Speak with Eral.
      - location: Old Gridania
        coords: (10.7, 5.9)
        name: Deliver the age-worn log to Millith Ironheart.
      - location: Old Gridania
        coords: (8.2, 10.6)
        name: "Seek out a place where \u201Cafore the Fane...\u201D and /lookout upon\
          \ your surroundings."
      - location: Old Gridania
        coords: (10.7, 5.9)
        name: Report to Millith Ironheart.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sylph-management
        level: 20
        rowId: 66049
        questId: ManFst304_00513
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 50
        paramGrowId: '20'
        avg: 870
      gil: 320
  - name: Leves of Quarrymill
    level: 20
    rowId: 65979
    questId: SubFst100_00443
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (25.5, 20.2)
      name: Nyell
    steps:
      - location: South Shroud
        coords: (23.9, 21.0)
        name: Complete the trial leve.
      - location: South Shroud
        coords: (25.5, 20.2)
        name: Report to Nyell at Quarrymill.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Leves of Swiftperch
        level: 10
        rowId: 66229
        questId: SubSea901_00693
        genre: La Noscean Sidequests
        icon: '71140'
      - name: Leves of Bentbranch
        level: 10
        rowId: 65756
        questId: SubFst070_00220
        genre: Gridanian Sidequests
        icon: '71140'
      - name: Leves of Horizon
        level: 10
        rowId: 66223
        questId: SubWil150_00687
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '20'
        avg: 1740
      items:
        - item:
            name: Glamour Prism
            id: '21800'
            icon: '26235'
            ilvl: '35'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 1
      optional:
        - item:
            name: Iron Cuirass
            id: '3045'
            icon: '48002'
            ilvl: '20'
            level: '20'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '60'
            name: Ice Blue
            color: '11715790'
        - item:
            name: Goatskin Jacket
            id: '3043'
            icon: '43030'
            ilvl: '20'
            level: '20'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '10'
            name: Dalamud Red
            color: '7871002'
        - item:
            name: Altered Cotton Dalmatica
            id: '27666'
            icon: '42657'
            ilvl: '18'
            level: '18'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '43'
            name: Mud Green
            color: '5788208'
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: My Little Chocobo (Twin Adder)
    level: 20
    rowId: 66236
    questId: SubFst120_00700
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: New Gridania
      coords: (9.7, 11.1)
      name: Vorsaile Heuloix
    steps:
      - location: New Gridania
        coords: (11.8, 12.6)
        name: Present a Serpent Chocobo Issuance to Cingur.
      - location: New Gridania
        coords: (11.9, 12.6)
        name: Name your chocobo.
      - location: New Gridania
        coords: (11.8, 12.6)
        name: Speak with Cingur.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '20'
        avg: 1740
      items:
        - item:
            name: Chocobo Whistle
            id: '6001'
            icon: '26012'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
  - name: The Replacement Culler
    level: 20
    rowId: 66247
    questId: GaiUsa005_00711
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (16.6, 27.2)
      name: Florimond
    steps:
      - location: East Shroud
        coords: (17.3, 26.4)
        name: Report to Aniud.
      - location: East Shroud
        coords: (17.7, 24.1)
        name: Cull black bats.
      - location: East Shroud
        coords: (17.3, 26.4)
        name: Report to Aniud.
      - location: East Shroud
        coords: (16.6, 27.2)
        name: Speak with Florimond.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '20'
        avg: 1740
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
      optional:
        - item:
            name: Echo Drops
            id: '4566'
            icon: '20643'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
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
  - name: Meat of the Matter
    level: 20
    rowId: 66248
    questId: GaiUsa006_00712
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (16.5, 27.1)
      name: Ysabel Hawthorne
    steps:
      - location: East Shroud
        coords: (17.3, 25.4)
        name: Lay traps in the Bramble Patch.
      - location: East Shroud
        coords: (16.5, 27.1)
        name: Report to Ysabel.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sylphic Studies
        level: 20
        rowId: 66245
        questId: GaiUsa003_00709
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '20'
        avg: 1740
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
      optional:
        - item:
            name: Iron Celata
            id: '2712'
            icon: '40002'
            ilvl: '20'
            level: '20'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Iron Sallet
            id: '2708'
            icon: '40022'
            ilvl: '20'
            level: '20'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Ash Mask (Lapis Lazuli)
            id: '2703'
            icon: '40415'
            ilvl: '20'
            level: '20'
            category:
              id: '34'
              name: Head
              icon: '60124'
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
  - name: Stand-in Sentry
    level: 20
    rowId: 66249
    questId: GaiUsa007_00713
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (17.4, 26.5)
      name: Piralnaut
    steps:
      - location: East Shroud
        coords: (15.1, 29.2)
        name: Stand guard at the Twin Adder standards.
      - location: East Shroud
        coords: (17.4, 26.5)
        name: Report to Piralnaut.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Swinophobia
        level: 20
        rowId: 66250
        questId: GaiUsa008_00714
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '20'
        avg: 1740
      items:
        - item:
            name: Glamour Prism
            id: '21800'
            icon: '26235'
            ilvl: '35'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 1
      optional:
        - item:
            name: Antelope Steak
            id: '4643'
            icon: '24360'
            ilvl: '20'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Dried Plums
            id: '4730'
            icon: '24058'
            ilvl: '21'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: Swinophobia
    level: 20
    rowId: 66250
    questId: GaiUsa008_00714
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (17.4, 26.5)
      name: Piralnaut
    steps:
      - location: East Shroud
        coords: (18.2, 24.6)
        name: Slay wild boars.
      - location: East Shroud
        coords: (17.4, 26.5)
        name: Report to Piralnaut.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '20'
        avg: 1740
      items:
        - item:
            name: Glamour Dispeller
            id: '7621'
            icon: '26228'
            ilvl: '30'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 1
      optional:
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
  - name: Roof Riders
    level: 21
    rowId: 66252
    questId: GaiUsa102_00716
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (17.3, 27.5)
      name: Blaisette
    steps:
      - location: East Shroud
        coords: (16.7, 27.4)
        name: Scour the roof for signs of a visitor.
      - location: East Shroud
        coords: (17.3, 27.5)
        name: Deliver the small cane to Blaisette.
      - location: East Shroud
        coords: (21.3, 26.8)
        name: Deliver the small cane to Dellexia.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: First Impressions
        level: 20
        rowId: 66246
        questId: GaiUsa004_00710
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '21'
        avg: 1800
      gil: 1109
      optional:
        - item:
            name: Iron Cuirass
            id: '3045'
            icon: '48002'
            ilvl: '20'
            level: '20'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
        - item:
            name: Cotton Halfrobe
            id: '3050'
            icon: '42154'
            ilvl: '21'
            level: '21'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '36'
            name: Desert Yellow
            color: '14398551'
        - item:
            name: Goatskin Jacket
            id: '3043'
            icon: '43030'
            ilvl: '20'
            level: '20'
            category:
              id: '35'
              name: Body
              icon: '60126'
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
          count: 2
  - name: Sylph Says
    level: 21
    rowId: 66256
    questId: GaiUsa106_00720
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (22.0, 25.6)
      name: Laxio
    steps:
      - location: East Shroud
        coords: (22.0, 25.6)
        name: /poke Laxio.
      - location: East Shroud
        coords: (22.0, 25.6)
        name: /examineself before Laxio.
      - location: East Shroud
        coords: (22.0, 25.6)
        name: /congratulate Laxio.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Dance Dance Diplomacy
        level: 21
        rowId: 69393
        questId: XxaUsa103_03857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '21'
        avg: 1800
      optional:
        - item:
            name: Iron Gauntlets
            id: '3563'
            icon: '48302'
            ilvl: '20'
            level: '20'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
        - item:
            name: Cotton Dress Gloves
            id: '3568'
            icon: '44076'
            ilvl: '21'
            level: '21'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
        - item:
            name: Goatskin Armguards
            id: '3559'
            icon: '48324'
            ilvl: '20'
            level: '20'
            category:
              id: '37'
              name: Hands
              icon: '60129'
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
  - name: Buzz Kill
    level: 21
    rowId: 66257
    questId: GaiUsa107_00721
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (22.0, 25.6)
      name: Laxio
    steps:
      - location: East Shroud
        coords: (19.9, 26.8)
        name: Defeat buzzing djiggas at the specified location.
      - location: East Shroud
        coords: (22.0, 25.6)
        name: Report to Laxio at Little Solace.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sylph Says
        level: 21
        rowId: 66256
        questId: GaiUsa106_00720
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '21'
        avg: 1800
      gil: 1285
      optional:
        - item:
            name: Antelope Steak
            id: '4643'
            icon: '24360'
            ilvl: '20'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Grape Juice
            id: '4746'
            icon: '24403'
            ilvl: '20'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: A Porcine Plight
    level: 21
    rowId: 66258
    questId: GaiUsa108_00722
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (21.4, 25.8)
      name: Ameexia
    steps:
      - location: East Shroud
        coords: (20.4, 28.0)
        name: Search the thicket and slay the wild boars.
      - location: East Shroud
        coords: (19.9, 25.3)
        name: Search the thicket and slay the tusked hog.
      - location: East Shroud
        coords: (21.4, 25.8)
        name: Report to Ameexia.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Dance Dance Diplomacy
        level: 21
        rowId: 69393
        questId: XxaUsa103_03857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '21'
        avg: 1800
      gil: 226
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
  - name: Threads Unraveled
    level: 21
    rowId: 66259
    questId: GaiUsa109_00723
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (21.4, 25.8)
      name: Ameexia
    steps:
      - location: East Shroud
        coords: (16.4, 23.6)
        name: Search for spindles of thread.
      - location: East Shroud
        coords: (21.4, 25.8)
        name: Deliver the cloud silk to Ameexia at Little Solace.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Porcine Plight
        level: 21
        rowId: 66258
        questId: GaiUsa108_00722
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '21'
        avg: 1800
      gil: 1109
  - name: Cloven-hoofed Horrors
    level: 22
    rowId: 66263
    questId: GaiUsa204_00727
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.1, 19.9)
      name: Ianna
    steps:
      - location: South Shroud
        coords: (18.5, 23.5)
        name: Use sparhawk egg soup on a scarred antelope and slay it.
      - location: South Shroud
        coords: (18.1, 19.9)
        name: Report to Ianna.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '22'
        avg: 1860
      gil: 1320
  - name: The Trees Have Eyes
    level: 22
    rowId: 66264
    questId: GaiUsa205_00728
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.1, 19.9)
      name: Ianna
    steps:
      - location: South Shroud
        coords: (17.8, 21.9)
        name: Gather piles of antelope umbles.
      - location: South Shroud
        coords: (20.0, 20.4)
        name: Gather kedtrap petals.
      - location: South Shroud
        coords: (22.3, 22.4)
        name: Place the antelope umbles before the withered treant.
      - location: South Shroud
        coords: (22.3, 22.4)
        name: Place the kedtrap petals before the withered treant.
      - location: South Shroud
        coords: (22.3, 22.4)
        name: /kneel in respect to the withered treant.
      - location: South Shroud
        coords: (18.1, 19.9)
        name: Speak with Ianna at Buscarron's Druthers.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Cloven-hoofed Horrors
        level: 22
        rowId: 66263
        questId: GaiUsa204_00727
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '22'
        avg: 1860
      gil: 1320
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
  - name: No Guts, No Glory
    level: 22
    rowId: 66265
    questId: GaiUsa206_00729
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.0, 19.8)
      name: Auphiliot
    steps:
      - location: South Shroud
        coords: (19.3, 20.5)
        name: Slay smallmouth orobon.
      - location: South Shroud
        coords: (18.0, 19.8)
        name: Report to Auphiliot.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '22'
        avg: 1860
      optional:
        - item:
            name: Iron Sabatons
            id: '3793'
            icon: '46806'
            ilvl: '20'
            level: '20'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
        - item:
            name: Cotton Dress Shoes
            id: '3800'
            icon: '46194'
            ilvl: '22'
            level: '22'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '75'
            name: Shadow Blue
            color: '3618631'
        - item:
            name: Goatskin Leg Guards
            id: '3791'
            icon: '46321'
            ilvl: '20'
            level: '20'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Occupational Hazards
    level: 22
    rowId: 66266
    questId: GaiUsa207_00730
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.2, 20.3)
      name: Yoenne
    steps:
      - location: South Shroud
        coords: (17.3, 22.2)
        name: Speak with Irielle.
      - location: South Shroud
        coords: (16.6, 22.2)
        name: Examine the strange shadow and slay chigoes.
      - location: South Shroud
        coords: (17.3, 22.2)
        name: Speak with Irielle.
      - location: South Shroud
        coords: (18.2, 20.3)
        name: Report to Yoenne.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: No Guts, No Glory
        level: 22
        rowId: 66265
        questId: GaiUsa206_00729
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '22'
        avg: 1860
      items:
        - item:
            name: Chigoe Larva
            id: '6176'
            icon: '59415'
            ilvl: '1'
            level: '1'
            category:
              id: '81'
              name: Minion
              icon: '60155'
          count: 1
  - name: Potsherds for Posterity
    level: 22
    rowId: 66267
    questId: GaiUsa208_00731
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (17.2, 22.2)
      name: Rolandaix
    steps:
      - location: South Shroud
        coords: (17.0, 22.2)
        name: Scour the area for possible relics.
      - location: South Shroud
        coords: (17.2, 22.2)
        name: Deliver the muddy potsherds to Rolandaix.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: No Guts, No Glory
        level: 22
        rowId: 66265
        questId: GaiUsa206_00729
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '22'
        avg: 1860
      items:
        - item:
            name: Glamour Dispeller
            id: '7621'
            icon: '26228'
            ilvl: '30'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 1
      optional:
        - item:
            name: Cotton Dress Shoes
            id: '3800'
            icon: '46194'
            ilvl: '22'
            level: '22'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '75'
            name: Shadow Blue
            color: '3618631'
        - item:
            name: Potion of Strength
            id: '4594'
            icon: '20665'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Potion of Dexterity
            id: '4595'
            icon: '20667'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Potion of Vitality
            id: '4596'
            icon: '20666'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
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
  - name: Stash Saboteur
    level: 22
    rowId: 66268
    questId: GaiUsa209_00732
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.0, 19.8)
      name: Auphiliot
    steps:
      - location: South Shroud
        coords: (15.6, 17.5)
        name: Use the firepots to destroy Qiqirn stashes.
      - location: South Shroud
        coords: (18.0, 19.8)
        name: Report to Auphiliot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: No Guts, No Glory
        level: 22
        rowId: 66265
        questId: GaiUsa206_00729
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '22'
        avg: 1860
      gil: 1140
  - name: Enemy Mine
    level: 23
    rowId: 66275
    questId: GaiUsa307_00739
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.0, 19.8)
      name: Auphiliot
    steps:
      - location: South Shroud
        coords: (18.4, 22.4)
        name: Speak with a Coeurlclaw poacher.
      - location: South Shroud
        coords: (16.8, 23.3)
        name: Speak with a flyer for the Redbelly Wasps.
      - location: South Shroud
        coords: (18.0, 19.8)
        name: Report to Auphiliot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sylphish Concerns
        level: 23
        rowId: 66274
        questId: GaiUsa306_00738
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '23'
        avg: 1920
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
      optional:
        - item:
            name: Iron Scale Fingers
            id: '3574'
            icon: '48377'
            ilvl: '23'
            level: '23'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '5'
            name: Charcoal Grey
            color: '4736834'
        - item:
            name: Cotton Bracers
            id: '3570'
            icon: '44051'
            ilvl: '23'
            level: '23'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '32'
            name: Mole Brown
            color: '6378053'
        - item:
            name: Goatskin Lightmitts
            id: '3572'
            icon: '44068'
            ilvl: '23'
            level: '23'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '31'
            name: Shale Brown
            color: '9601388'
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
  - name: Shadows of the Empire
    level: 24
    rowId: 66278
    questId: GaiUsa310_00742
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (18.0, 19.8)
      name: Auphiliot
    steps:
      - location: South Shroud
        coords: (19.4, 19.4)
        name: Investigate the specified locations and defeat Garleans.
      - location: South Shroud
        coords: (18.0, 19.8)
        name: Report to Auphiliot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Into the Beast's Maw
        level: 24
        rowId: 66050
        questId: ManFst306_00514
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      gil: 244
  - name: The Blood Price
    level: 24
    rowId: 66281
    questId: GaiUsa403_00745
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (21.9, 25.9)
      name: Knolexia
    steps:
      - location: East Shroud
        coords: (15.8, 20.9)
        name: Use the empty blood bottles on weakened djiggas.
      - location: East Shroud
        coords: (21.9, 25.9)
        name: Deliver the djigga blood to Knolexia.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Into the Beast's Maw
        level: 24
        rowId: 66050
        questId: ManFst306_00514
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      gil: 1399
      items:
        - item:
            name: Cotton Robe
            id: '3062'
            icon: '42053'
            ilvl: '24'
            level: '24'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '10'
            name: Dalamud Red
            color: '7871002'
  - name: Savage Snares
    level: 26
    rowId: 66302
    questId: GaiUsa604_00766
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (25.0, 20.6)
      name: Balan
    steps:
      - location: South Shroud
        coords: (23.7, 21.9)
        name: Disarm iron leg traps.
      - location: South Shroud
        coords: (25.0, 20.6)
        name: Report to Balan.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      gil: 1474
  - name: Forest Law
    level: 26
    rowId: 66303
    questId: GaiUsa605_00767
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (24.6, 20.5)
      name: Wlfric
    steps:
      - location: South Shroud
        coords: (25.2, 20.4)
        name: Ferret out the poacher hiding in Quarrymill.
      - location: South Shroud
        coords: (24.6, 20.5)
        name: Report to Wlfric.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      gil: 1263
  - name: An Apple a Day
    level: 26
    rowId: 66304
    questId: GaiUsa606_00768
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (24.6, 20.0)
      name: Deidra
    steps:
      - location: South Shroud
        coords: (25.7, 18.2)
        name: Speak with Fawkes at the orchards.
      - location: South Shroud
        coords: (25.6, 18.4)
        name: Slay pests and harvest sprite apples.
      - location: South Shroud
        coords: (25.7, 18.2)
        name: Deliver your harvest to Fawkes.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      gil: 1263
      optional:
        - item:
            name: Apple Tart
            id: '4709'
            icon: '24054'
            ilvl: '17'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Apple Juice
            id: '4747'
            icon: '24402'
            ilvl: '40'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: A Bumper Crop
    level: 26
    rowId: 66305
    questId: GaiUsa607_00769
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (25.7, 18.2)
      name: Fawkes
    steps:
      - location: South Shroud
        coords: (22.3, 22.4)
        name: Place a sprite apple in offering before the withered treant.
      - location: South Shroud
        coords: (24.5, 20.3)
        name: Deliver a sprite apple to Castellaint.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: An Apple a Day
        level: 26
        rowId: 66304
        questId: GaiUsa606_00768
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      gil: 1263
  - name: Wretched Hive of Villainy
    level: 26
    rowId: 66306
    questId: GaiUsa608_00770
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (24.5, 20.0)
      name: Faucertaux
    steps:
      - location: South Shroud
        coords: (23.7, 18.4)
        name: Slay a Redbelly lookout.
      - location: South Shroud
        coords: (23.7, 18.4)
        name: Slay a Redbelly sharpeye.
      - location: South Shroud
        coords: (23.7, 18.4)
        name: Slay a Redbelly larcener.
      - location: South Shroud
        coords: (24.5, 20.0)
        name: Report to Faucertaux.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
      optional:
        - item:
            name: Potion of Vitality
            id: '4596'
            icon: '20666'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Potion of Strength
            id: '4594'
            icon: '20665'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Potion of Dexterity
            id: '4595'
            icon: '20667'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
  - name: In Grandfather's Name
    level: 26
    rowId: 66307
    questId: GaiUsa609_00771
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (24.5, 20.0)
      name: Cuthbert
    steps:
      - location: South Shroud
        coords: (22.9, 19.4)
        name: Recover the Boughbury Axe near Redbelly Hive.
      - location: South Shroud
        coords: (24.5, 20.0)
        name: Deliver the Boughbury Axe to Cuthbert.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      gil: 1263
  - name: The Marvelous Mun-Tuy Bean
    level: 26
    rowId: 66308
    questId: GaiUsa610_00772
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (25.4, 21.0)
      name: Aedoc
    steps:
      - location: South Shroud
        coords: (27.0, 16.3)
        name: Speak with Erimmont.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: In Grandfather's Name
        level: 26
        rowId: 66307
        questId: GaiUsa609_00771
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      items:
        - item:
            name: Glamour Dispeller
            id: '7621'
            icon: '26228'
            ilvl: '30'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 1
      optional:
        - item:
            name: Silver Wristlets
            id: '4103'
            icon: '55603'
            ilvl: '26'
            level: '26'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Silver Gorget
            id: '4315'
            icon: '54803'
            ilvl: '26'
            level: '26'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Masher for a Day
    level: 26
    rowId: 66309
    questId: GaiUsa611_00773
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (27.0, 16.3)
      name: Erimmont
    steps:
      - location: South Shroud
        coords: (26.4, 16.8)
        name: Retrieve a perilla leaf.
      - location: South Shroud
        coords: (26.7, 16.4)
        name: Retrieve an onze of Shroud pepper.
      - location: South Shroud
        coords: (26.9, 16.3)
        name: Retrieve a dried dragon pepper.
      - location: South Shroud
        coords: (27.5, 16.5)
        name: Add the secret spices to the gyle-fat.
      - location: South Shroud
        coords: (27.5, 16.5)
        name: Speak with Geoffrey.
      - location: South Shroud
        coords: (25.4, 21.0)
        name: "Deliver the Mun\u2013Tuy sauce to Aedoc."
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Marvelous Mun-Tuy Bean
        level: 26
        rowId: 66308
        questId: GaiUsa610_00772
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '26'
        avg: 2275
      items:
        - item:
            name: Standard Spectrum Dye
            id: '52254'
            icon: '22811'
            ilvl: '1'
            level: '1'
            category:
              id: '55'
              name: Dye
              icon: '60147'
          count: 3
      optional:
        - item:
            name: Aldgoat Steak
            id: '4644'
            icon: '24360'
            ilvl: '27'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Crumpet
            id: '4732'
            icon: '24053'
            ilvl: '28'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: Potable Perils
    level: 28
    rowId: 66324
    questId: GaiUsa804_00788
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (21.5, 26.4)
      name: Somerhild
    steps:
      - location: North Shroud
        coords: (17.1, 26.5)
        name: Search for the missing key.
      - location: North Shroud
        coords: (20.9, 24.9)
        name: Return the key to Aeluuin.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      optional:
        - item:
            name: Velveteen Trousers
            id: '3365'
            icon: '45065'
            ilvl: '28'
            level: '28'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '1'
            name: Snow White
            color: '14999504'
        - item:
            name: Velveteen Tights
            id: '3355'
            icon: '45088'
            ilvl: '27'
            level: '27'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '33'
            name: Loam Brown
            color: '4141865'
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: No News Is Good News
    level: 28
    rowId: 66325
    questId: GaiUsa805_00789
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (20.8, 25.9)
      name: Godwin
    steps:
      - location: North Shroud
        coords: (15.4, 25.4)
        name: Deliver the Fallgourd report to Vortefaurt.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      optional:
        - item:
            name: Sunstone Choker
            id: '4320'
            icon: '54809'
            ilvl: '28'
            level: '28'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Malachite Choker
            id: '4324'
            icon: '54811'
            ilvl: '28'
            level: '28'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Sphene Choker
            id: '4326'
            icon: '54812'
            ilvl: '28'
            level: '28'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: Save the Trees
    level: 28
    rowId: 66326
    questId: GaiUsa806_00790
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (15.6, 25.5)
      name: Oriane
    steps:
      - location: North Shroud
        coords: (15.9, 26.9)
        name: Pour flat ale on the scarred trees and slay Shroud hares.
      - location: North Shroud
        coords: (15.6, 25.5)
        name: Report to Oriane.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      optional:
        - item:
            name: Fluorite Choker
            id: '4328'
            icon: '54814'
            ilvl: '28'
            level: '28'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Danburite Choker
            id: '4322'
            icon: '54813'
            ilvl: '28'
            level: '28'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Lapis Lazuli Choker
            id: '4330'
            icon: '54810'
            ilvl: '28'
            level: '28'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: Pumiceous Pursuits
    level: 28
    rowId: 66327
    questId: GaiUsa807_00791
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (15.6, 25.5)
      name: Oriane
    steps:
      - location: North Shroud
        coords: (15.8, 31.2)
        name: Use the sealing vessel on a weakened pumice golem.
      - location: North Shroud
        coords: (20.9, 25.0)
        name: Deliver the living soulstone to Yhom Epocan.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Save the Trees
        level: 28
        rowId: 66326
        questId: GaiUsa806_00790
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      gil: 1544
  - name: Cleaning House
    level: 28
    rowId: 66328
    questId: GaiUsa808_00792
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (20.9, 24.9)
      name: Aeluuin
    steps:
      - location: North Shroud
        coords: (20.7, 25.0)
        name: Use the chocobo duster on the paintings.
      - location: North Shroud
        coords: (20.9, 24.9)
        name: Report to Aeluuin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Potable Perils
        level: 28
        rowId: 66324
        questId: GaiUsa804_00788
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      gil: 1320
  - name: Trouble on the Road
    level: 28
    rowId: 66329
    questId: GaiUsa809_00793
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (20.9, 24.9)
      name: Aeluuin
    steps:
      - location: North Shroud
        coords: (19.3, 29.1)
        name: Save the well-equipped adventurer.
      - location: North Shroud
        coords: (19.3, 29.3)
        name: Speak with the well-equipped adventurer.
      - location: North Shroud
        coords: (20.9, 24.9)
        name: Report to Aeluuin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Cleaning House
        level: 28
        rowId: 66328
        questId: GaiUsa808_00792
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      optional:
        - item:
            name: Sphene Bracelet
            id: '4115'
            icon: '55612'
            ilvl: '28'
            level: '28'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Sunstone Bracelet
            id: '4109'
            icon: '55609'
            ilvl: '28'
            level: '28'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Malachite Bracelet
            id: '4113'
            icon: '55611'
            ilvl: '28'
            level: '28'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: A Welcome Overstayed
    level: 28
    rowId: 66330
    questId: GaiUsa810_00794
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (21.0, 25.0)
      name: Gogolata
    steps:
      - location: North Shroud
        coords: (20.3, 28.5)
        name: Deliver the envelope to the haughty houseboy.
      - location: North Shroud
        coords: (21.0, 25.0)
        name: Speak with Gogolata.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      optional:
        - item:
            name: Fluorite Bracelet
            id: '4117'
            icon: '55614'
            ilvl: '28'
            level: '28'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Danburite Bracelet
            id: '4111'
            icon: '55613'
            ilvl: '28'
            level: '28'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Lapis Lazuli Bracelet
            id: '4119'
            icon: '55610'
            ilvl: '28'
            level: '28'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: No Place Like Home
    level: 28
    rowId: 66331
    questId: GaiUsa811_00795
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (21.0, 25.0)
      name: Gogolata
    steps:
      - location: North Shroud
        coords: (21.8, 30.3)
        name: Retrieve Gogolata's goods.
      - location: North Shroud
        coords: (21.0, 25.0)
        name: Return the goods to Gogolata.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Welcome Overstayed
        level: 28
        rowId: 66330
        questId: GaiUsa810_00794
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      gil: 1320
  - name: Meals for Miners
    level: 28
    rowId: 66332
    questId: GaiUsa901_00796
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (20.9, 24.9)
      name: Aeluuin
    steps:
      - location: North Shroud
        coords: (16.4, 29.1)
        name: Deliver meals to the prospectors.
      - location: North Shroud
        coords: (20.9, 24.9)
        name: Report to Aeluuin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Trouble on the Road
        level: 28
        rowId: 66329
        questId: GaiUsa809_00793
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      gil: 1320
  - name: Digging in the Dark
    level: 28
    rowId: 66333
    questId: GaiUsa902_00797
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (16.5, 29.3)
      name: Ademar
    steps:
      - location: North Shroud
        coords: (17.1, 27.2)
        name: Weaken and then capture bright balloons with lamps.
      - location: North Shroud
        coords: (16.5, 29.3)
        name: Deliver the lamps to Ademar.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      gil: 1544
  - name: A Leg Up
    level: 28
    rowId: 66334
    questId: GaiUsa903_00798
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (16.5, 29.3)
      name: Ademar
    steps:
      - location: North Shroud
        coords: (17.2, 26.8)
        name: Place ladders as directed by Ademar.
      - location: North Shroud
        coords: (16.5, 29.3)
        name: Report to Ademar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Digging in the Dark
        level: 28
        rowId: 66333
        questId: GaiUsa902_00797
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '28'
        avg: 2775
      gil: 1320
  - name: Broadening Horizons
    level: 29
    rowId: 66338
    questId: GaiUsa907_00802
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: New Gridania
      coords: (12.1, 11.6)
      name: Tyoh Moui
    steps:
      - location: New Gridania
        coords: (8.9, 13.1)
        name: Speak with Franchemontiaux.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: '54'
        name: White Wolf Gate (Central Shroud)
        type: aethernet-shard
        location: Central Shroud
        coords: (15.4, 15.9)
    rewards:
      xp:
        factor: 100
        paramGrowId: '29'
        avg: 3040
      optional:
        - item:
            name: Sphene Earrings
            id: '4220'
            icon: '55211'
            ilvl: '29'
            level: '29'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Sunstone Earrings
            id: '4214'
            icon: '55208'
            ilvl: '29'
            level: '29'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Malachite Earrings
            id: '4218'
            icon: '55210'
            ilvl: '29'
            level: '29'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: Beneath the Planks
    level: 29
    rowId: 66339
    questId: GaiUsa908_00803
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: New Gridania
      coords: (8.9, 13.0)
      name: Roustebant
    steps:
      - location: Central Shroud
        coords: (17.0, 18.9)
        name: Speak with Thievenaix at Dunstan's Spire.
      - location: Central Shroud
        coords: (16.3, 18.3)
        name: Inspect the scaffolding and slay any Shroud hares that appear.
      - location: Central Shroud
        coords: (17.0, 18.9)
        name: Report to Thievenaix.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Broadening Horizons
        level: 29
        rowId: 66338
        questId: GaiUsa907_00802
        genre: Gridanian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '29'
        avg: 3040
      optional:
        - item:
            name: Fluorite Earrings
            id: '4222'
            icon: '55213'
            ilvl: '29'
            level: '29'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Danburite Earrings
            id: '4216'
            icon: '55212'
            ilvl: '29'
            level: '29'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Lapis Lazuli Earrings
            id: '4224'
            icon: '55209'
            ilvl: '29'
            level: '29'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: Fungal Frolic
    level: 29
    rowId: 66340
    questId: GaiUsa909_00804
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (16.6, 18.6)
      name: Marcette
    steps:
      - location: Central Shroud
        coords: (15.0, 17.5)
        name: Obtain toadstool caps from toadstools.
      - location: Central Shroud
        coords: (16.6, 18.6)
        name: Deliver the toadstool caps to Marcette.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '29'
        avg: 3040
      gil: 1580
  - name: Shocking Discoveries
    level: 29
    rowId: 66341
    questId: GaiUsa910_00805
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (16.6, 18.6)
      name: Marcette
    steps:
      - location: Central Shroud
        coords: (15.2, 18.1)
        name: Use the thick glass jar on a weakened lightning spark.
      - location: Central Shroud
        coords: (16.6, 18.6)
        name: Deliver the live lightning spark to Marcette.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Fungal Frolic
        level: 29
        rowId: 66340
        questId: GaiUsa909_00804
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '29'
        avg: 3040
      gil: 1580
  - name: In Too Deep
    level: 29
    rowId: 66342
    questId: GaiUsa911_00806
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (16.6, 18.6)
      name: Hobriaut
    steps:
      - location: Central Shroud
        coords: (13.3, 21.7)
        name: Obtain water samples from Hopeseed Pond.
      - location: Central Shroud
        coords: (16.6, 18.6)
        name: Deliver the bottles of water to Hobriaut.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Shocking Discoveries
        level: 29
        rowId: 66341
        questId: GaiUsa910_00805
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '29'
        avg: 3040
      optional:
        - item:
            name: Sphene Ring
            id: '4448'
            icon: '54410'
            ilvl: '29'
            level: '29'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Sunstone Ring
            id: '4442'
            icon: '54407'
            ilvl: '29'
            level: '29'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Malachite Ring
            id: '4446'
            icon: '54409'
            ilvl: '29'
            level: '29'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: Doing the Dirty Work
    level: 29
    rowId: 66343
    questId: GaiUsa912_00807
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Central Shroud
      coords: (16.6, 18.6)
      name: Marcette
    steps:
      - location: Central Shroud
        coords: (15.0, 21.3)
        name: Use Marcette's medicine and kill a halitostroper.
      - location: Central Shroud
        coords: (16.6, 18.6)
        name: Deliver the stomach to Marcette.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Shocking Discoveries
        level: 29
        rowId: 66341
        questId: GaiUsa910_00805
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '29'
        avg: 3040
      optional:
        - item:
            name: Fluorite Ring
            id: '4450'
            icon: '54412'
            ilvl: '29'
            level: '29'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Danburite Ring
            id: '4444'
            icon: '54411'
            ilvl: '29'
            level: '29'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Lapis Lazuli Ring
            id: '4452'
            icon: '54408'
            ilvl: '29'
            level: '29'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 2
  - name: Unicorn Power
    level: 30
    rowId: 65730
    questId: SubFst910_00194
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (6.3, 11.0)
      name: Braya
    steps:
      - location: North Shroud
        coords: (16.5, 31.0)
        name: Use Cure to heal the injured beast at Alder Springs.
      - location: Old Gridania
        coords: (6.3, 11.0)
        name: Report to Braya.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: In Nature's Embrace
        level: 30
        rowId: 65977
        questId: ClsCnj006_00441
        genre: Conjurer Quests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '30'
        avg: 3120
      items:
        - item:
            name: Unicorn Whistle
            id: '6269'
            icon: '26039'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
  - name: Leves of Camp Tranquil
    level: 30
    rowId: 65980
    questId: SubFst101_00444
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (16.7, 28.3)
      name: Merthelin
    steps:
      - location: South Shroud
        coords: (15.9, 28.8)
        name: Complete Merthelin's trial leve.
      - location: South Shroud
        coords: (16.7, 28.3)
        name: Report to Merthelin at Camp Tranquil.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Leves of Swiftperch
        level: 10
        rowId: 66229
        questId: SubSea901_00693
        genre: La Noscean Sidequests
        icon: '71140'
      - name: Leves of Bentbranch
        level: 10
        rowId: 65756
        questId: SubFst070_00220
        genre: Gridanian Sidequests
        icon: '71140'
      - name: Leves of Horizon
        level: 10
        rowId: 66223
        questId: SubWil150_00687
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '30'
        avg: 3120
      items:
        - item:
            name: Glamour Prism
            id: '21800'
            icon: '26235'
            ilvl: '35'
            level: '1'
            category:
              id: '60'
              name: Catalyst
              icon: '60152'
          count: 1
      optional:
        - item:
            name: Steel Cuirass
            id: '3102'
            icon: '48003'
            ilvl: '30'
            level: '30'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '60'
            name: Ice Blue
            color: '11715790'
        - item:
            name: Toadskin Jacket
            id: '3100'
            icon: '43085'
            ilvl: '30'
            level: '30'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '60'
            name: Ice Blue
            color: '11715790'
        - item:
            name: Velveteen Bliaud
            id: '27669'
            icon: '42663'
            ilvl: '31'
            level: '31'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '56'
            name: Deepwood Green
            color: '1976865'
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 4
  - name: We'll Always Have Ul'dah
    level: 30
    rowId: 66353
    questId: GaiUsb010_00817
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (16.8, 28.2)
      name: Detoh Moshroca
    steps:
      - location: South Shroud
        coords: (16.8, 34.3)
        name: Speak with the Ul'dahn trader.
      - location: South Shroud
        coords: (16.8, 28.2)
        name: Deliver the Ul'dahn incense to Detoh Moshroca.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Modest Proposal
        level: 30
        rowId: 66350
        questId: GaiUsb007_00814
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '30'
        avg: 3120
      gil: 1615
      optional:
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
  - name: A Burning Request
    level: 30
    rowId: 66354
    questId: GaiUsb011_00818
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (17.4, 28.8)
      name: Florent
    steps:
      - location: South Shroud
        coords: (17.6, 29.2)
        name: Gather the lengths of dropped lumber.
      - location: South Shroud
        coords: (17.4, 28.8)
        name: Return the lumber to Florent.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Modest Proposal
        level: 30
        rowId: 66350
        questId: GaiUsb007_00814
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '30'
        avg: 3120
      gil: 1377
      optional:
        - item:
            name: Aldgoat Steak
            id: '4644'
            icon: '24360'
            ilvl: '27'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Crumpet
            id: '4732'
            icon: '24053'
            ilvl: '28'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: My Feisty Little Chocobo
    level: 30
    rowId: 66698
    questId: SubFst911_01162
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (17.1, 28.2)
      name: Docette
    steps:
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Speak with Luquelot at Bentbranch Meadows.
      - location: Central Shroud
        coords: (20.4, 20.7)
        name: Obtain a fresh bunch of gysahl greens.
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Deliver gysahl greens to Luquelot.
      - location: Central Shroud
        coords: (16.1, 20.1)
        name: Dispatch brood ziz with your companion.
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Report to Luquelot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: My Little Chocobo (Twin Adder)
        level: 20
        rowId: 66236
        questId: SubFst120_00700
        genre: Gridanian Sidequests
        icon: '71140'
      - name: My Little Chocobo (Maelstrom)
        level: 20
        rowId: 66237
        questId: SubSea910_00701
        genre: La Noscean Sidequests
        icon: '71140'
      - name: My Little Chocobo (Immortal Flames)
        level: 20
        rowId: 66238
        questId: SubWil160_00702
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '30'
        avg: 3120
  - name: Bird in Hand
    level: 30
    rowId: 67096
    questId: SubCts821_01560
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Central Shroud
      coords: (20.2, 21.6)
      name: Luquelot
    steps:
      - location: Central Shroud
        coords: (20.3, 21.5)
        name: Collect vegetable scraps in the stables.
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Speak with Luquelot.
      - location: Central Shroud
        coords: (20.6, 20.8)
        name: Speak with Margault and acquire some feed.
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Show the gigantic krakka root to Luquelot.
      - location: Central Shroud
        coords: (20.3, 22.0)
        name: Speak with Keitha.
      - location: Central Shroud
        coords: (20.3, 22.0)
        name: Train Little Leia.
      - location: Central Shroud
        coords: (20.3, 22.0)
        name: Speak with Keitha.
      - location: Central Shroud
        coords: (20.2, 21.6)
        name: Report to Luquelot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: My Feisty Little Chocobo
        level: 30
        rowId: 66698
        questId: SubFst911_01162
        genre: Gridanian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 50
        paramGrowId: '30'
        avg: 1560
      items:
        - item:
            name: Krakka Root
            id: '8165'
            icon: '25207'
            ilvl: '70'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 5
  - name: Hunger Is the Best Sauce
    level: 36
    rowId: 66421
    questId: GaiUsb603_00885
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (15.5, 25.4)
      name: Idristan
    steps:
      - location: North Shroud
        coords: (15.8, 27.2)
        name: Use the dodo meat as bait and slay jackals.
      - location: North Shroud
        coords: (15.5, 25.4)
        name: 'Report to Idristan. '
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '36'
        avg: 4275
      optional:
        - item:
            name: Linen Trousers
            id: '3399'
            icon: '45184'
            ilvl: '36'
            level: '36'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '1'
            name: Snow White
            color: '14999504'
        - item:
            name: Altered Linen Chausses
            id: '27990'
            icon: '45280'
            ilvl: '36'
            level: '36'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
        - item:
            name: Allagan Silver Piece
            id: '5825'
            icon: '26001'
            ilvl: '25'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 4
  - name: Tit for Tat
    level: 37
    rowId: 66442
    questId: GaiUsb711_00906
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (20.8, 25.0)
      name: Isaudorel
    steps:
      - location: North Shroud
        coords: (22.5, 25.0)
        name: Lurk by the antelope carcass and slay the Ixali wildtalons.
      - location: North Shroud
        coords: (20.8, 25.0)
        name: Report to Isaudorel.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Stand and Quiver
        level: 37
        rowId: 66441
        questId: GaiUsb710_00905
        genre: Coerthan Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '37'
        avg: 4370
      gil: 5764
  - name: Inquire at the Spire
    level: 37
    rowId: 66443
    questId: GaiUsb712_00907
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (20.8, 25.0)
      name: Ireine
    steps:
      - location: North Shroud
        coords: (22.7, 24.3)
        name: Report to Miah Molkot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Tit for Tat
        level: 37
        rowId: 66442
        questId: GaiUsb711_00906
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '37'
        avg: 4370
      gil: 1478
  - name: Don't Shut Me Out
    level: 37
    rowId: 66444
    questId: GaiUsb713_00908
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (22.7, 24.3)
      name: Miah Molkot
    steps:
      - location: North Shroud
        coords: (22.2, 21.7)
        name: Use the bomb finger to destroy the Ixali blockade.
      - location: North Shroud
        coords: (22.7, 24.3)
        name: Report to Miah Molkot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Inquire at the Spire
        level: 37
        rowId: 66443
        questId: GaiUsb712_00907
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '37'
        avg: 4370
      gil: 1478
  - name: From Gridania, with Love
    level: 37
    rowId: 66445
    questId: GaiUsb714_00909
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: North Shroud
      coords: (22.7, 24.3)
      name: Miah Molkot
    steps:
      - location: Coerthas Central Highlands
        coords: (26.5, 16.2)
        name: Deliver the letter to Belmont at Camp Dragonhead.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Don't Shut Me Out
        level: 37
        rowId: 66444
        questId: GaiUsb713_00908
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '37'
        avg: 4370
      gil: 1478
  - name: Adventurer for Hire
    level: 43
    rowId: 66505
    questId: GaiUsc302_00969
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: Old Gridania
      coords: (8.4, 8.3)
      name: Selaine
    steps:
      - location: East Shroud
        coords: (21.6, 26.9)
        name: Deliver the perfume to Jeulerand at Little Solace.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '43'
        avg: 5720
      gil: 1624
  - name: Some Seedy Business
    level: 43
    rowId: 66506
    questId: GaiUsc303_00970
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (21.6, 26.9)
      name: Jeulerand
    steps:
      - location: East Shroud
        coords: (21.3, 26.8)
        name: Give the sweetrose perfume to Dellexia.
      - location: East Shroud
        coords: (26.1, 25.2)
        name: Obtain sylvan lily seeds while warding off attackers.
      - location: East Shroud
        coords: (18.0, 16.3)
        name: Give the seeds to Kain.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Adventurer for Hire
        level: 43
        rowId: 66505
        questId: GaiUsc302_00969
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '43'
        avg: 5720
      gil: 2500
  - name: This One's for the Lovers
    level: 43
    rowId: 66508
    questId: GaiUsc305_00972
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (18.0, 16.3)
      name: Kain
    steps:
      - location: East Shroud
        coords: (17.8, 18.6)
        name: Give the roses to the nervy nipper.
      - location: East Shroud
        coords: (18.0, 16.3)
        name: Report to Kain.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Some Seedy Business
        level: 43
        rowId: 66506
        questId: GaiUsc303_00970
        genre: Gridanian Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '43'
        avg: 5720
      gil: 1729
  - name: Windy Wedding
    level: 43
    rowId: 66509
    questId: GaiUsc306_00973
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: East Shroud
      coords: (16.7, 17.6)
      name: Elfleda
    steps:
      - location: East Shroud
        coords: (22.0, 21.3)
        name: Slay wind sprites for their cores.
      - location: East Shroud
        coords: (16.7, 17.6)
        name: Give the wind sprite cores to Elfleda.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '43'
        avg: 5720
      optional:
        - item:
            name: Mega-Potion
            id: '4553'
            icon: '20603'
            ilvl: '45'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Hi-Ether
            id: '4556'
            icon: '20622'
            ilvl: '35'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
  - name: Who Was That Man in Black
    level: 46
    rowId: 66544
    questId: GaiUsc608_01008
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Seat of the First Bow
      coords: (3.5, 3.4)
      name: Lewin
    steps:
      - location: New Gridania
        coords: (15.2, 12.3)
        name: Gather information from the residents of Gridania.
      - location: Seat of the First Bow
        coords: (3.5, 3.4)
        name: Report your findings to Lewin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Primal Fear
        level: 46
        rowId: 66543
        questId: GaiUsc607_01007
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '46'
        avg: 6325
      gil: 1694
  - name: The Dark Divinity
    level: 46
    rowId: 66545
    questId: GaiUsc609_01009
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Seat of the First Bow
      coords: (3.5, 3.4)
      name: Lewin
    steps:
      - location: South Shroud
        coords: (25.3, 20.3)
        name: "Speak with O\u2013App\u2013Pesi in Quarrymill."
      - location: South Shroud
        coords: (33.8, 23.2)
        name: Inspect Urth's Seal and use cleansing water to defeat evil spirits.
      - location: South Shroud
        coords: (33.8, 23.1)
        name: Obtain the sundered binding stone from Urth's Seal.
      - location: South Shroud
        coords: (25.3, 20.3)
        name: "Deliver the sundered binding stone to O\u2013App\u2013Pesi."
      - location: South Shroud
        coords: (25.6, 21.0)
        name: Report to Simmie.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Who Was That Man in Black
        level: 46
        rowId: 66544
        questId: GaiUsc608_01008
        genre: Gridanian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '46'
        avg: 6325
      optional:
        - item:
            name: Electrum Gorget
            id: '4361'
            icon: '54804'
            ilvl: '46'
            level: '46'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Electrum Wristlets
            id: '4150'
            icon: '55604'
            ilvl: '46'
            level: '46'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Allagan Gold Piece
            id: '5826'
            icon: '26001'
            ilvl: '35'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Slim Pickings
    level: 46
    rowId: 66546
    questId: GaiUsc610_01010
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (25.4, 19.7)
      name: Isarmoix
    steps:
      - location: South Shroud
        coords: (29.5, 24.4)
        name: Slay wild hogs and obtain their meat.
      - location: South Shroud
        coords: (25.4, 19.7)
        name: Deliver boar meat to Isarmoix.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '46'
        avg: 6325
      optional:
        - item:
            name: Tortoiseshell Scale Greaves
            id: '3886'
            icon: '46881'
            ilvl: '46'
            level: '46'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '68'
            name: Ink Blue
            color: '1711911'
        - item:
            name: Raptorskin Moccasins
            id: '27647'
            icon: '49070'
            ilvl: '46'
            level: '46'
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
            name: Allagan Gold Piece
            id: '5826'
            icon: '26001'
            ilvl: '35'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Serveth Thy Master
    level: 46
    rowId: 66547
    questId: GaiUsc611_01011
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71020'
    issuer:
      location: South Shroud
      coords: (25.1, 19.9)
      name: Kerrich
    steps:
      - location: South Shroud
        coords: (25.1, 19.9)
        name: Show deference and /kneel to Kerrich.
      - location: South Shroud
        coords: (32.0, 24.2)
        name: Defeat keds and obtain their wings.
      - location: South Shroud
        coords: (25.1, 19.9)
        name: Deliver the ked wings to Kerrich.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '46'
        avg: 6325
      optional:
        - item:
            name: Tortoiseshell Scale Fingers
            id: '3669'
            icon: '48387'
            ilvl: '46'
            level: '46'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '6'
            name: Soot Black
            color: '2828579'
        - item:
            name: Fingerless Raptorskin Gloves
            id: '3651'
            icon: '44103'
            ilvl: '45'
            level: '45'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '32'
            name: Mole Brown
            color: '6378053'
        - item:
            name: Boarskin Ringbands of Flames
            id: '3656'
            icon: '44135'
            ilvl: '46'
            level: '46'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '33'
            name: Loam Brown
            color: '4141865'
        - item:
            name: Allagan Gold Piece
            id: '5826'
            icon: '26001'
            ilvl: '35'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: All You Wanted to Know about Odin
    level: 46
    rowId: 66548
    questId: GaiUsc612_01012
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (25.6, 21.0)
      name: Simmie
    steps:
      - location: The Waking Sands
        coords: (6.0, 4.9)
        name: Deliver the Odin report to Urianger.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Dark Divinity
        level: 46
        rowId: 66545
        questId: GaiUsc609_01009
        genre: Gridanian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '46'
        avg: 6325
      gil: 1694
      optional:
        - item:
            name: Savage Aim Materia III
            id: '5671'
            icon: '20223'
            ilvl: '45'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Heavens' Eye Materia III
            id: '5666'
            icon: '20223'
            ilvl: '45'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Savage Might Materia III
            id: '5676'
            icon: '20223'
            ilvl: '45'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Quickarm Materia III
            id: '5716'
            icon: '20227'
            ilvl: '45'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Quicktongue Materia III
            id: '5721'
            icon: '20227'
            ilvl: '45'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
  - name: One Man's Trash
    level: 50
    rowId: 66676
    questId: JobRel005_01140
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: North Shroud
      coords: (29.6, 19.8)
      name: Ealdwine
    steps:
      - location: Mor Dhona
        coords: (22.0, 6.7)
        name: Deliver the map to Brangwine at Revenant's Toll.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Treasures and Tribulations
        level: 36
        rowId: 66747
        questId: SubCts802_01211
        genre: La Noscean Sidequests
        icon: '71140'
      - name: Celestial Radiance
        level: 50
        rowId: 66998
        questId: JobRel003_01462
        genre: Zodiac Weapons
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 517
  - name: One Night in Amdapor
    level: 50
    rowId: 66925
    questId: SubCts003_01389
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Old Gridania
      coords: (6.0, 10.7)
      name: E-Sumi-Yan
    steps:
      - location: South Shroud
        coords: (18.7, 27.1)
        name: "Speak with Raya\u2013O\u2013Senna at Camp Tranquil."
      - location: South Shroud
        coords: (14.2, 30.7)
        name: Speak with Alphene outside the Lost City of Amdapor.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Heart of the Forest
        level: 50
        rowId: 66620
        questId: JobWhm500_01084
        genre: White Mage Quests
        icon: '71140'
      - name: In Nature's Embrace
        level: 30
        rowId: 65977
        questId: ClsCnj006_00441
        genre: Conjurer Quests
        icon: '71140'
      - name: Seer Folly
        level: 30
        rowId: 66615
        questId: JobWhm300_01079
        genre: White Mage Quests
        icon: '71140'
      - name: The Ultimate Weapon
        level: 50
        rowId: 70058
        questId: XxcFst503_04522
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 939
  - name: Kettle to the Mettle
    level: 50
    rowId: 67206
    questId: SubFst980_01670
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: North Shroud
      coords: (29.6, 19.7)
      name: Jalzahn
    steps:
      - location: North Shroud
        coords: (30.3, 20.2)
        name: Speak with Gerolt.
      - location: North Shroud
        coords: (30.3, 20.2)
        name: Deliver the pieces of alexandrite to Gerolt.
      - location: North Shroud
        coords: (29.6, 19.7)
        name: Deliver the Thavnairian mist to Jalzahn.
      - location: Bowl of Embers
        coords: (6.1, 6.1)
        name: Obtain an Inferno fragment in the Bowl of Embers (Extreme).
      - location: The Howling Eye
        coords: (6.1, 6.1)
        name: Obtain a Vortex fragment in the Howling Eye (Extreme).
      - location: The Navel
        coords: (6.1, 6.1)
        name: Obtain a Crag fragment in the Navel (Extreme).
      - location: North Shroud
        coords: (30.3, 20.2)
        name: Deliver the materials to Gerolt.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - name: the Bowl of Embers (Extreme)
        type: trial
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 70
        ilevelSync: 0
      - name: the Howling Eye (Extreme)
        type: trial
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 65
        ilevelSync: 0
      - name: the Navel (Extreme)
        type: trial
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 67
        ilevelSync: 0
      - id: 1492
        name: A Watched Pot
        type: achievement
    requires:
      - name: The Vital Title
        level: 50
        rowId: 66097
        questId: JobRel017_00561
        genre: Zodiac Weapons
        icon: '71140'
      - name: The Vital Title
        level: 50
        rowId: 67823
        questId: JobRel099_02287
        genre: Zodiac Weapons
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 5800
      items:
        - item:
            name: Ultimate Kettle Nexus
            id: '13087'
            icon: '52211'
            ilvl: '1'
            level: '1'
            category:
              id: '76'
              name: Outdoor Furnishing
              icon: '60168'
          count: 1
  - name: One More Night in Amdapor
    level: 60
    rowId: 67818
    questId: HeaVny103_02282
    genre:
      id: '113'
      name: Gridanian Sidequests
    icon: '71140'
    issuer:
      location: Old Gridania
      coords: (6.0, 10.7)
      name: E-Sumi-Yan
    steps:
      - location: South Shroud
        coords: (18.7, 27.1)
        name: "Speak with Raya\u2013O\u2013Senna at Camp Tranquil."
      - location: South Shroud
        coords: (14.2, 30.7)
        name: Speak with Alphene outside the Lost City of Amdapor.
      - location: The Lost City of Amdapor
        coords: (12.3, 13.4)
        name: Enter the Lost City of Amdapor (Hard).
      - location: South Shroud
        coords: (18.7, 27.1)
        name: "Report to Raya\u2013O\u2013Senna at Camp Tranquil."
    expansion:
      id: '1'
      name: Heavensward
    unlocks:
      - name: the Lost City of Amdapor (Hard)
        type: dungeon
        levelRequired: 60
        levelSync: 60
        ilevelRequired: 180
        ilevelSync: 0
    requires:
      - name: One Night in Amdapor
        level: 50
        rowId: 66925
        questId: SubCts003_01389
        genre: Gridanian Sidequests
        icon: '71140'
      - name: Heavensward
        level: 60
        rowId: 67205
        questId: HeaVna707_01669
        genre: Heavensward
        icon: '71000'
    rewards:
      xp:
        factor: 0
        paramGrowId: '60'
        avg: 0
      gil: 3881
genre:
  genreId: '113'
  name: Gridanian Sidequests


---