---
layout: quest-table
title: La Noscean Sidequests
permalink: /quests/sidequests/realm-reborn/la-noscean
nonsequential: true
brandLabel: Mognet
brandUrl: /quests/sidequests/realm-reborn
quests:
  - name: It's Time to Duel
    level: 1
    rowId: 67929
    questId: HeaVny816_02393
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Wolves' Den Pier
      coords: (5.8, 5.8)
      name: faint-hearted fighter
    steps:
      - location: Wolves' Den Pier
        coords: (6.8, 5.7)
        name: Speak with the Maelstrom drill sergeant.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 231
  - name: Earning Your Wings
    level: 30
    rowId: 68543
    questId: ComAll002_03007
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Wolves' Den Pier
      coords: (5.7, 5.4)
      name: Softknox
    steps: []
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Pup No Longer (Maelstrom)
        level: 30
        rowId: 66640
        questId: ComLim001_01104
        genre: Maelstrom Quests
        icon: '71140'
      - name: A Pup No Longer (Twin Adder)
        level: 30
        rowId: 66641
        questId: ComGrd001_01105
        genre: Order of the Twin Adder Quests
        icon: '71140'
      - name: A Pup No Longer (Immortal Flames)
        level: 30
        rowId: 66642
        questId: ComUld001_01106
        genre: Immortal Flames Quests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '30'
        avg: 0
  - name: The Crystal (Line's) Call
    level: 30
    rowId: 70121
    questId: ComAll003_04585
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Wolves' Den Pier
      coords: (4.9, 6.4)
      name: Gungi Zelungi
    steps: []
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Pup No Longer (Maelstrom)
        level: 30
        rowId: 66640
        questId: ComLim001_01104
        genre: Maelstrom Quests
        icon: '71140'
      - name: A Pup No Longer (Twin Adder)
        level: 30
        rowId: 66641
        questId: ComGrd001_01105
        genre: Order of the Twin Adder Quests
        icon: '71140'
      - name: A Pup No Longer (Immortal Flames)
        level: 30
        rowId: 66642
        questId: ComUld001_01106
        genre: Immortal Flames Quests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '30'
        avg: 0
  - name: Coming to Limsa Lominsa
    level: 1
    rowId: 65643
    questId: ManSea001_00107
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa
      coords: (10.4, 11.1)
      name: Ryssfloh
    steps:
      - location: Limsa Lominsa
        coords: (11.4, 11.5)
        name: Speak with Grehfarr at the Crow's Lift.
      - location: Limsa Lominsa
        coords: (11.6, 11.1)
        name: Speak with Baderon at the Drowning Wench.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '1'
        avg: 400
      gil: 103
  - name: Making a Name
    level: 1
    rowId: 65647
    questId: SubSea001_00111
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa
      coords: (11.4, 11.3)
      name: Niniya
    steps:
      - location: Limsa Lominsa
        coords: (11.4, 11.5)
        name: Speak with Skaenrael.
      - location: Limsa Lominsa Lower Decks
        coords: (11.3, 11.4)
        name: Gather the peculiar herbs.
      - location: Limsa Lominsa Lower Decks
        coords: (10.0, 11.1)
        name: Deliver the peculiar herbs to Ahldskyf.
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
  - name: Suspiciously Sober
    level: 1
    rowId: 65648
    questId: SubSea002_00112
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (10.0, 11.1)
      name: Ahldskyf
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (9.0, 11.5)
        name: Speak with Glazrael.
      - location: Limsa Lominsa Lower Decks
        coords: (8.3, 11.5)
        name: Speak with Frydwyb.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Making a Name
        level: 1
        rowId: 65647
        questId: SubSea001_00111
        genre: La Noscean Sidequests
        icon: '71020'
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
  - name: Proper Procedure
    level: 1
    rowId: 65649
    questId: SubSea003_00113
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (9.1, 11.5)
      name: Sweetnix Rosycheeks
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (4.3, 11.3)
        name: Deliver the letter to P'tahjha.
      - location: Limsa Lominsa Lower Decks
        coords: (9.1, 11.5)
        name: Report to Sweetnix.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 103
  - name: The Right Price
    level: 1
    rowId: 65650
    questId: SubSea004_00114
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (8.4, 11.5)
      name: Swozblaet
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 11.6)
        name: Speak with Iron Thunder.
      - location: Limsa Lominsa Lower Decks
        coords: (6.6, 12.2)
        name: Speak with Kyokyoroon.
      - location: Limsa Lominsa Lower Decks
        coords: (6.3, 11.9)
        name: Speak with Syneyhil.
      - location: Limsa Lominsa Lower Decks
        coords: (5.9, 12.2)
        name: Deliver the price list to Baensyng.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
  - name: Duty Calls
    level: 1
    rowId: 65651
    questId: SubSea005_00115
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (4.3, 11.3)
      name: P'tahjha
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (9.6, 10.7)
        name: Deliver a log assessor's ledger to Sundhimal.
      - location: Limsa Lominsa Upper Decks
        coords: (10.0, 7.9)
        name: Deliver a log assessor's ledger to Latisha.
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
          count: 5
  - name: Edelweiss, Edelweiss
    level: 1
    rowId: 65859
    questId: SubSea016_00323
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (10.0, 11.3)
      name: J'nasshym
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 16.1)
        name: Deliver the package for the Dutiful Sisters to Lonwoerd.
      - location: Limsa Lominsa Lower Decks
        coords: (10.0, 11.3)
        name: Return to J'nasshym.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 95
  - name: All the Fish in the Sea
    level: 1
    rowId: 69379
    questId: SubCts826_03843
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (7.8, 14.5)
      name: Fhilsnoe
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (2.9, 12.7)
        name: Speak with Foerzagyl at the ferry docks.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: My First Fishing Rod
        level: 1
        rowId: 66644
        questId: ClsFsh021_01108
        genre: Fisher Quests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '1'
        avg: 100
      items:
        - item:
            name: Versatile Lure
            id: '29717'
            icon: '27051'
            ilvl: '1'
            level: '1'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 10
  - name: A Thousand Words
    level: 1
    rowId: 65653
    questId: SubSea007_00117
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (10.0, 7.9)
      name: Latisha
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (10.2, 8.3)
        name: Receive R'sushmo's artist's rendition.
      - location: Limsa Lominsa Upper Decks
        coords: (11.0, 6.2)
        name: Deliver the artist's rendition to Godebert at the Coral Tower.
      - location: Limsa Lominsa Upper Decks
        coords: (10.2, 8.3)
        name: Speak with R'sushmo.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 110
  - name: Licensed to Reave
    level: 1
    rowId: 65654
    questId: SubSea008_00118
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.2, 7.9)
      name: Mordyn
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 8.0)
        name: Speak with Carvallain.
      - location: Limsa Lominsa Upper Decks
        coords: (11.1, 6.4)
        name: Deliver a Seventh Sage sampler to Ginnade at the Coral Tower.
      - location: Limsa Lominsa Upper Decks
        coords: (10.1, 8.2)
        name: Deliver a Seventh Sage sampler to Lyngsath at the Bismarck.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 8.0)
        name: Speak with Carvallain.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 110
  - name: Lost and Found
    level: 1
    rowId: 65655
    questId: SubSea009_00119
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.1, 6.4)
      name: Ginnade
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (11.1, 11.2)
        name: Deliver the missing persons list to N'delika in Bulwark Hall.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 110
  - name: I Stay the Streetlight
    level: 1
    rowId: 65656
    questId: SubSea010_00120
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (11.1, 11.2)
      name: N'tanmo
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (9.9, 11.6)
        name: Refill guttering streetlamps with streetlamp oil.
      - location: Limsa Lominsa Lower Decks
        coords: (7.9, 14.5)
        name: Speak with Sisipu at the Fishermen's Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Lost and Found
        level: 1
        rowId: 65655
        questId: SubSea009_00119
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 110
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
  - name: A Sheepish Request
    level: 1
    rowId: 65652
    questId: SubSea006_00116
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (9.9, 8.4)
      name: H'lahono
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (11.6, 11.3)
        name: Speak with Abylfarr.
      - location: Middle La Noscea
        coords: (22.9, 25.2)
        name: Obtain slices of fresh lamb from lost lambs.
      - location: Limsa Lominsa Upper Decks
        coords: (9.9, 8.4)
        name: Deliver the slices of fresh lamb to H'lahono.
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
  - name: Back in the Water
    level: 1
    rowId: 65657
    questId: SubSea011_00121
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (7.9, 14.5)
      name: Sisipu
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (10.6, 15.4)
        name: Speak with H'naanza at the Armorers' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 115
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
          count: 5
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
          count: 5
  - name: The Rats in the Wharf
    level: 1
    rowId: 66197
    questId: SubSea013_00661
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (10.6, 15.4)
      name: H'naanza
    steps:
      - location: Lower La Noscea
        coords: (21.7, 23.7)
        name: Slay wharf rats.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Report to Baderon.
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
            id: '75'
            name: Shadow Blue
            color: '3618631'
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
  - name: Glory Days
    level: 1
    rowId: 65658
    questId: SubSea012_00122
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.1, 11.0)
      name: S'dhodjbi
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.8, 14.7)
        name: Speak with Klindrael.
      - location: Lower La Noscea
        coords: (25.3, 22.5)
        name: Slay aureliae.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Deliver the aurelia umbrellas to Baderon.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 65644
        questId: ManSea002_00108
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 65645
        questId: ManSea003_00109
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '1'
        avg: 100
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
          count: 1
  - name: Soothing the Savage Siren
    level: 1
    rowId: 66198
    questId: SubSea014_00662
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (12.1, 13.9)
      name: O'kalkaya
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (12.9, 13.8)
        name: /kneel before Rhoswen.
      - location: Limsa Lominsa Upper Decks
        coords: (12.9, 13.8)
        name: Show Rhoswen that you are /disappointed.
      - location: Limsa Lominsa Upper Decks
        coords: (12.9, 13.8)
        name: /rally Rhoswen's spirits.
      - location: Limsa Lominsa Upper Decks
        coords: (12.1, 13.9)
        name: Speak with O'kalkaya.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 122
  - name: Fool Me Once
    level: 4
    rowId: 66199
    questId: SubSea015_00663
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.4, 11.3)
      name: Niniya
    steps:
      - location: Lower La Noscea
        coords: (27.0, 22.1)
        name: Speak with Ancreta at the Eyes.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 65644
        questId: ManSea002_00108
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 65645
        questId: ManSea003_00109
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
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
            id: '32'
            name: Mole Brown
            color: '6378053'
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
            id: '20'
            name: Russet Brown
            color: '5188895'
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
  - name: Rocks in a Hard Place
    level: 4
    rowId: 66007
    questId: SubSea059_00471
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (26.1, 16.6)
      name: Grynewyda
    steps:
      - location: Middle La Noscea
        coords: (25.9, 16.6)
        name: Obtain the tiller's shovel.
      - location: Middle La Noscea
        coords: (24.2, 18.0)
        name: Remove rocks from the frontier with the shovel.
      - location: Middle La Noscea
        coords: (24.2, 18.0)
        name: Pick up debris from the frontier.
      - location: Middle La Noscea
        coords: (26.1, 16.6)
        name: Report to Grynewyda.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 128
  - name: Cry Me a Liver
    level: 4
    rowId: 66011
    questId: SubSea063_00475
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (27.0, 22.1)
      name: Ancreta
    steps:
      - location: Lower La Noscea
        coords: (24.5, 22.7)
        name: Slay rivertoads and collect three rivertoad livers.
      - location: Lower La Noscea
        coords: (27.0, 22.1)
        name: Report to Ancreta.
      - location: Lower La Noscea
        coords: (32.4, 20.0)
        name: Deliver the rivertoad livers to Anaoc at the Red Rooster Stead.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Fool Me Once
        level: 4
        rowId: 66199
        questId: SubSea015_00663
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 128
  - name: Moegramm Had a Little Lamb
    level: 4
    rowId: 66017
    questId: SubSea069_00481
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.3, 20.0)
      name: Moegramm
    steps:
      - location: Lower La Noscea
        coords: (31.2, 19.3)
        name: Speak with Chartain.
      - location: Lower La Noscea
        coords: (31.0, 19.5)
        name: Use the lice comb on the shaggy sheep.
      - location: Lower La Noscea
        coords: (32.3, 20.0)
        name: Report to Moegramm.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 128
  - name: Where the Heart Is (Mist)
    level: 5
    rowId: 66750
    questId: SubCts805_01214
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Lower La Noscea
      coords: (31.6, 20.2)
      name: Ahctkoen
    steps:
      - location: Lower La Noscea
        coords: (33.3, 19.2)
        name: Speak with Roeganlona.
      - location: Mist
        coords: (11.0, 8.8)
        name: Journey to Mist.
      - location: Mist
        coords: (10.8, 8.9)
        name: Speak with the storm recruit.
      - location: Lower La Noscea
        coords: (31.6, 20.2)
        name: Report to Ahctkoen.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '5'
        avg: 175
      gil: 132
  - name: The Time Is Ripe
    level: 4
    rowId: 66008
    questId: SubSea060_00472
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (25.4, 16.9)
      name: Bhirdraeg
    steps:
      - location: Middle La Noscea
        coords: (23.0, 17.1)
        name: Harvest the La Noscean oranges.
      - location: Middle La Noscea
        coords: (25.4, 16.9)
        name: Deliver the oranges to Bhirdraeg.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: On to Summerford
        level: 4
        rowId: 65998
        questId: SubSea050_00462
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 135
      items:
        - item:
            name: Orange Juice
            id: '4745'
            icon: '24401'
            ilvl: '6'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 10
  - name: Wool's Errand
    level: 4
    rowId: 66012
    questId: SubSea064_00476
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.4, 20.0)
      name: Anaoc
    steps:
      - location: Lower La Noscea
        coords: (31.0, 19.9)
        name: Obtain the sack of fleece.
      - location: Lower La Noscea
        coords: (35.6, 15.3)
        name: Deliver the sack of fleece to Weitzaren at the Grey Fleet.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Cry Me a Liver
        level: 4
        rowId: 66011
        questId: SubSea063_00475
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 135
      items:
        - item:
            name: Flatbread
            id: '4696'
            icon: '24006'
            ilvl: '5'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 10
  - name: Much Ado About Dodos
    level: 4
    rowId: 66016
    questId: SubSea068_00480
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.3, 20.0)
      name: Moegramm
    steps:
      - location: Lower La Noscea
        coords: (32.3, 21.3)
        name: Speak with X'payan.
      - location: Lower La Noscea
        coords: (32.8, 20.4)
        name: Capture the bolting dodos with the dodo-sized sacks.
      - location: Lower La Noscea
        coords: (32.3, 20.0)
        name: Deliver the filled dodo-sized sacks to Moegramm.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Moegramm Had a Little Lamb
        level: 4
        rowId: 66017
        questId: SubSea069_00481
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 135
  - name: Yarzon, Yarzoff
    level: 5
    rowId: 66006
    questId: SubSea058_00470
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (25.2, 27.3)
      name: Ostfyr
    steps:
      - location: Middle La Noscea
        coords: (24.1, 22.1)
        name: Jostle the yarzons out of their nests and slay them.
      - location: Middle La Noscea
        coords: (25.2, 27.3)
        name: Report to Ostfyr.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Further Afield
        level: 5
        rowId: 66000
        questId: SubSea052_00464
        genre: ''
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '5'
        avg: 350
      gil: 128
  - name: Orange Crush
    level: 4
    rowId: 66009
    questId: SubSea061_00473
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (25.4, 16.9)
      name: Bhirdraeg
    steps:
      - location: Middle La Noscea
        coords: (23.3, 20.4)
        name: Slay puk hatchlings.
      - location: Middle La Noscea
        coords: (25.4, 16.9)
        name: Report to Bhirdraeg.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Time Is Ripe
        level: 4
        rowId: 66008
        questId: SubSea060_00472
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
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
  - name: Whack-a-Mole
    level: 4
    rowId: 66018
    questId: SubSea070_00482
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.1, 20.0)
      name: Arenlona
    steps:
      - location: Lower La Noscea
        coords: (30.7, 17.9)
        name: Visit the pumpkin patch and slay clever hedgemoles.
      - location: Lower La Noscea
        coords: (32.1, 20.0)
        name: Report to Arenlona.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 141
  - name: What Goes Around
    level: 4
    rowId: 66020
    questId: SubSea072_00484
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (35.6, 15.3)
      name: Loetrswys
    steps:
      - location: Lower La Noscea
        coords: (33.5, 15.3)
        name: Speak to Eshushu, Waentzirn, and R'jumani.
      - location: Lower La Noscea
        coords: (35.6, 15.3)
        name: Report to Weitzaren.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 141
      items:
        - item:
            name: Mutton Stew
            id: '4673'
            icon: '24107'
            ilvl: '9'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 5
  - name: A Pound of Cure
    level: 5
    rowId: 66010
    questId: SubSea062_00474
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (24.9, 17.1)
      name: Khanmhar
    steps:
      - location: Middle La Noscea
        coords: (21.5, 15.6)
        name: Deliver a hi-potion to Wydaloef at Tiller's Rest.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Double Dealing
        level: 5
        rowId: 66002
        questId: SubSea054_00466
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 50
        paramGrowId: '5'
        avg: 175
      gil: 128
  - name: Flour Power
    level: 4
    rowId: 66013
    questId: SubSea065_00477
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (35.6, 15.3)
      name: Weitzaren
    steps:
      - location: Lower La Noscea
        coords: (29.8, 14.4)
        name: Defeat the galagos and recover the sacks of flour.
      - location: Lower La Noscea
        coords: (32.8, 19.5)
        name: Deliver the sacks of flour to Skarnmhar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Wool's Errand
        level: 4
        rowId: 66012
        questId: SubSea064_00476
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      items:
        - item:
            name: Frumenty
            id: '4716'
            icon: '24102'
            ilvl: '4'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 5
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
            id: '27'
            name: Acorn Brown
            color: '9328667'
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
  - name: Beetle Juice
    level: 4
    rowId: 66019
    questId: SubSea071_00483
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.1, 20.0)
      name: Arenlona
    steps:
      - location: Lower La Noscea
        coords: (30.3, 17.9)
        name: Sprinkle aphid nectar upon Althyk lavender and obtain three phials of
          ladybug viscera.
      - location: Lower La Noscea
        coords: (32.1, 20.0)
        name: Deliver the ladybug viscera to Arenlona.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Whack-a-Mole
        level: 4
        rowId: 66018
        questId: SubSea070_00482
        genre: La Noscean Sidequests
        icon: '71020'
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
            id: '27'
            name: Acorn Brown
            color: '9328667'
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
  - name: Fire and Brimstone
    level: 4
    rowId: 66021
    questId: SubSea073_00485
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (27.7, 15.3)
      name: Broenruht
    steps:
      - location: Lower La Noscea
        coords: (27.0, 15.3)
        name: Use clear earth crystals on the gas plumes.
      - location: Lower La Noscea
        coords: (27.7, 15.3)
        name: Report to Broenruht.
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
            id: '27'
            name: Acorn Brown
            color: '9328667'
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
          count: 2
  - name: Kobolds Ahoy
    level: 4
    rowId: 66022
    questId: SubSea074_00486
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (35.6, 15.3)
      name: Loetrswys
    steps:
      - location: Lower La Noscea
        coords: (32.3, 20.0)
        name: Speak to Moegramm.
      - location: Lower La Noscea
        coords: (27.7, 15.3)
        name: Speak to Broenruht.
      - location: Middle La Noscea
        coords: (25.2, 27.3)
        name: Deliver the report on kobolds to Ostfyr.
      - location: Middle La Noscea
        coords: (25.6, 17.0)
        name: Speak to Staelwyrn.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Wool's Errand
        level: 4
        rowId: 66012
        questId: SubSea064_00476
        genre: La Noscean Sidequests
        icon: '71020'
      - name: What Goes Around
        level: 4
        rowId: 66020
        questId: SubSea072_00484
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 50
        paramGrowId: '4'
        avg: 130
      gil: 174
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
            id: '27'
            name: Acorn Brown
            color: '9328667'
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
  - name: Kobolds and Indigents
    level: 4
    rowId: 66014
    questId: SubSea066_00478
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.8, 19.5)
      name: Skarnmhar
    steps:
      - location: Lower La Noscea
        coords: (27.7, 15.0)
        name: Speak with Wahoy Mahoy.
      - location: Lower La Noscea
        coords: (26.5, 15.0)
        name: Slay the kobolds and recover the bundles of raiments.
      - location: Lower La Noscea
        coords: (27.7, 15.0)
        name: Speak with Wahoy Mahoy.
      - location: Lower La Noscea
        coords: (32.8, 19.5)
        name: Deliver the bundles of raiments to Skarnmhar.
      - location: Lower La Noscea
        coords: (32.4, 20.0)
        name: Report to Anaoc.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Flour Power
        level: 4
        rowId: 66013
        questId: SubSea065_00477
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 206
      items:
        - item:
            name: Amateur's Kurta
            id: '3014'
            icon: '42233'
            ilvl: '9'
            level: '9'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '36'
            name: Desert Yellow
            color: '14398551'
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
  - name: Bait and Swat
    level: 4
    rowId: 66015
    questId: SubSea067_00479
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (32.4, 20.0)
      name: Anaoc
    steps:
      - location: Lower La Noscea
        coords: (32.1, 20.0)
        name: Speak with Arenlona.
      - location: Lower La Noscea
        coords: (32.4, 20.0)
        name: Speak with Anaoc.
      - location: Lower La Noscea
        coords: (32.8, 19.5)
        name: Acquire the meat from Skarnmhar.
      - location: Lower La Noscea
        coords: (27.1, 17.3)
        name: Speak with K'wabati at Blind Iron Mines.
      - location: Lower La Noscea
        coords: (25.9, 15.8)
        name: Set the crate of meat in the mines.
      - location: Lower La Noscea
        coords: (26.4, 15.3)
        name: Take cover and ambush the kobolds that appear.
      - location: Lower La Noscea
        coords: (32.4, 20.0)
        name: Speak with Anaoc.
      - location: Limsa Lominsa Upper Decks
        coords: (11.6, 11.1)
        name: Speak with Baderon at the Drowning Wench.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Kobolds and Indigents
        level: 4
        rowId: 66014
        questId: SubSea066_00478
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 179
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
  - name: Meet, Greet, and Deceit
    level: 9
    rowId: 66023
    questId: SubSea075_00487
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.1, 11.3)
      name: Gregory
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.4, 11.3)
        name: Speak with Niniya.
      - location: Limsa Lominsa Upper Decks
        coords: (11.4, 11.3)
        name: "With the chat mode in **Say**, enter \u201CI come in peace.\u201D to\
          \ greet Niniya."
      - location: Limsa Lominsa Upper Decks
        coords: (11.4, 11.3)
        name: "With the chat mode in **Say**, enter the auto\u2013translate option\
          \ Hello!."
      - location: Limsa Lominsa Upper Decks
        coords: (11.3, 11.1)
        name: Speak with Singing Stormcloud.
      - location: Limsa Lominsa Upper Decks
        coords: (11.3, 11.1)
        name: "With the chat mode in **Say**, enter \u201CGreetings and salutations!\u201D\
          \ to greet Singing Stormcloud."
      - location: Limsa Lominsa Upper Decks
        coords: (11.3, 11.1)
        name: "With the chat mode in **Say**, enter the auto\u2013translate option\
          \ Thank you.."
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Just Deserts
        level: 9
        rowId: 66005
        questId: SubSea057_00469
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '9'
        avg: 810
      gil: 183
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
  - name: Simply the Hest
    level: 10
    rowId: 65595
    questId: SubSea906_00059
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Western La Noscea
      coords: (34.8, 31.7)
      name: Swygskyf
    steps:
      - location: Western La Noscea
        coords: (34.4, 31.2)
        name: Speak with Battlewarden Tiroro.
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
  - name: Out to Dry
    level: 10
    rowId: 65935
    questId: SubSea102_00399
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (15.6, 16.9)
      name: W'dhovaka
    steps:
      - location: Middle La Noscea
        coords: (15.3, 14.2)
        name: Slay megalocrabs.
      - location: Middle La Noscea
        coords: (15.6, 16.9)
        name: Report to W'dhovaka at the Skylift.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 173
  - name: Keeping It Fresh
    level: 10
    rowId: 65936
    questId: SubSea103_00400
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (15.8, 16.7)
      name: Kazai Buoyzai
    steps:
      - location: Middle La Noscea
        coords: (16.9, 14.7)
        name: Defeat water sprites and collect their cores.
      - location: Middle La Noscea
        coords: (15.8, 16.7)
        name: Deliver the water sprite cores to Kazai Buoyzai at the Skylift.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sky-high
        level: 10
        rowId: 65933
        questId: SubSea100_00397
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 173
  - name: Baiting Buzzards
    level: 10
    rowId: 65937
    questId: SubSea104_00401
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Middle La Noscea
      coords: (15.8, 16.7)
      name: Kazai Buoyzai
    steps:
      - location: Middle La Noscea
        coords: (17.0, 13.2)
        name: Empty the sack of rat meat in the buzzards' nest and slay the buzzards
          that appear.
      - location: Middle La Noscea
        coords: (15.8, 16.7)
        name: Report to Kazai Buoyzai at the Skylift.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Keeping It Fresh
        level: 10
        rowId: 65936
        questId: SubSea103_00400
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 175
  - name: Leves of Swiftperch
    level: 10
    rowId: 66229
    questId: SubSea901_00693
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.0, 11.0)
      name: T'mokkri
    steps:
      - location: Western La Noscea
        coords: (34.8, 31.7)
        name: Speak with Swygskyf at Swiftperch.
      - location: Western La Noscea
        coords: (33.7, 31.1)
        name: Complete Swygskyf's trial guildleve.
      - location: Western La Noscea
        coords: (34.8, 31.7)
        name: Report to Swygskyf.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Just Deserts
        level: 9
        rowId: 66005
        questId: SubSea057_00469
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 215
  - name: A Bridge Too Full
    level: 10
    rowId: 65943
    questId: SubSea110_00407
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (23.5, 28.0)
      name: Doesrael
    steps:
      - location: Lower La Noscea
        coords: (23.7, 29.0)
        name: Speak with Wyrstmaga.
      - location: Lower La Noscea
        coords: (22.3, 29.3)
        name: /soothe the irate coachmen.
      - location: Lower La Noscea
        coords: (23.7, 29.0)
        name: Speak with Wyrstmaga.
      - location: Lower La Noscea
        coords: (23.5, 28.0)
        name: Speak with Doesrael.
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
  - name: Need to Breed
    level: 10
    rowId: 65941
    questId: SubSea108_00405
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (34.5, 32.0)
      name: Lyulf
    steps:
      - location: Western La Noscea
        coords: (32.1, 28.1)
        name: Gather fertilized eggs from dodo nests.
      - location: Western La Noscea
        coords: (34.5, 32.0)
        name: Deliver the dodo eggs to Lyulf at Swiftperch.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Farmer of Fortune
        level: 10
        rowId: 65940
        questId: SubSea107_00404
        genre: ''
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 188
  - name: What Counts
    level: 10
    rowId: 65944
    questId: SubSea111_00408
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (25.1, 33.7)
      name: Yulgi Honalgi
    steps:
      - location: Lower La Noscea
        coords: (25.1, 33.2)
        name: Speak with Razyn Mylzyn.
      - location: Lower La Noscea
        coords: (26.2, 33.3)
        name: Speak with Ruimo Falaimo.
      - location: Lower La Noscea
        coords: (25.7, 33.3)
        name: Count the remaining forecastle planks.
      - location: Lower La Noscea
        coords: (24.9, 33.3)
        name: Count the remaining quarterdeck logs.
      - location: Lower La Noscea
        coords: (25.1, 33.7)
        name: Return to Yulgi Honalgi with the results.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Failure to Lunch
        level: 10
        rowId: 65945
        questId: SubSea112_00409
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
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
            id: '10'
            name: Dalamud Red
            color: '7871002'
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
          count: 3
  - name: Failure to Lunch
    level: 10
    rowId: 65945
    questId: SubSea112_00409
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (26.0, 33.9)
      name: Wafufu
    steps:
      - location: Lower La Noscea
        coords: (28.2, 34.4)
        name: Find Wafufu's missing lunches.
      - location: Lower La Noscea
        coords: (26.0, 33.9)
        name: Return the lunches to Wafufu.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 196
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
          stain:
            id: '18'
            name: Bark Brown
            color: '6966071'
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
          stain:
            id: '21'
            name: Kobold Brown
            color: '3154203'
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
  - name: Nailed It
    level: 10
    rowId: 65946
    questId: SubSea113_00410
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (27.2, 33.8)
      name: Hezzkhezl
    steps:
      - location: Lower La Noscea
        coords: (20.5, 32.1)
        name: Slay lightning sprites and obtain their cores.
      - location: Lower La Noscea
        coords: (27.2, 33.8)
        name: Deliver the elemental cores to Hezzkhezl.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Failure to Lunch
        level: 10
        rowId: 65945
        questId: SubSea112_00409
        genre: La Noscean Sidequests
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
            id: '10'
            name: Dalamud Red
            color: '7871002'
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
  - name: Constant Carvings
    level: 10
    rowId: 65947
    questId: SubSea114_00411
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (25.2, 35.0)
      name: Mimidoa
    steps:
      - location: Lower La Noscea
        coords: (21.6, 34.9)
        name: Slay wild jackals to obtain curved jackal fangs.
      - location: Lower La Noscea
        coords: (24.2, 40.2)
        name: Deliver the jackal fangs to Rostnzeh.
      - location: Lower La Noscea
        coords: (25.2, 35.0)
        name: Return to Mimidoa.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 220
  - name: Forbidden Island
    level: 10
    rowId: 65952
    questId: SubSea119_00416
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (20.8, 38.4)
      name: A'zumyn
    steps:
      - location: Lower La Noscea
        coords: (23.4, 36.9)
        name: Place fetid dodo flesh on a suspicious mound and slay the creatures
          that emerge.
      - location: Lower La Noscea
        coords: (20.8, 38.4)
        name: Report to A'zumyn at Candlekeep Quay.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 234
  - name: Say It with Flowers
    level: 10
    rowId: 65953
    questId: SubSea120_00417
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Lower La Noscea
      coords: (24.2, 40.2)
      name: Rostnzeh
    steps:
      - location: Lower La Noscea
        coords: (22.2, 35.8)
        name: Search Empty Heart for a La Noscean lilybell.
      - location: Lower La Noscea
        coords: (24.8, 35.1)
        name: Deliver the lilybell to Ghimthota at the Moraby Drydocks.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
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
            id: '31'
            name: Shale Brown
            color: '9601388'
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
          count: 2
  - name: Good for What Ales You
    level: 14
    rowId: 66962
    questId: SubSea159_01426
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (7.5, 12.3)
      name: Dodozan
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (7.3, 15.0)
        name: Speak with people around Fisherman's Bottom.
      - location: Limsa Lominsa Lower Decks
        coords: (6.0, 15.1)
        name: Speak with the young Executioner on the *Astalicia*.
      - location: Limsa Lominsa Lower Decks
        coords: (7.5, 12.3)
        name: Deliver the payment to Dodozan.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: '101'
        name: Step Dance
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
  - name: Leves of Aleport
    level: 15
    rowId: 66230
    questId: SubSea902_00694
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Western La Noscea
      coords: (27.7, 27.1)
      name: Orwen
    steps:
      - location: Western La Noscea
        coords: (27.7, 25.5)
        name: Complete Orwen's trial guildleve.
      - location: Western La Noscea
        coords: (27.7, 27.1)
        name: Report to Orwen.
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
  - name: Keep Your Day Job
    level: 15
    rowId: 66678
    questId: SubSea151_01142
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.7, 25.5)
      name: S'nairoh
    steps:
      - location: Western La Noscea
        coords: (27.6, 24.7)
        name: Slay puk hatchlings.
      - location: Western La Noscea
        coords: (26.7, 25.5)
        name: Report to Private S'nairoh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Call of the Sea
        level: 14
        rowId: 66210
        questId: SubWil141_00674
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Call of the Sea
        level: 14
        rowId: 66209
        questId: SubFst102_00673
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      optional:
        - item:
            name: Bronze Celata
            id: '2673'
            icon: '40001'
            ilvl: '15'
            level: '15'
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
            name: Hard Leather Eyepatch
            id: '2669'
            icon: '40891'
            ilvl: '14'
            level: '14'
            category:
              id: '34'
              name: Head
              icon: '60124'
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
          count: 3
  - name: Mountains out of Molehills
    level: 15
    rowId: 66679
    questId: SubSea152_01143
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.7, 25.5)
      name: S'nairoh
    steps:
      - location: Western La Noscea
        coords: (26.6, 23.5)
        name: Dispatch hedgemoles.
      - location: Western La Noscea
        coords: (26.7, 25.5)
        name: Report to S'nairoh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Keep Your Day Job
        level: 15
        rowId: 66678
        questId: SubSea151_01142
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      gil: 239
      optional:
        - item:
            name: Padded Hempen Trousers
            id: '3325'
            icon: '45015'
            ilvl: '15'
            level: '15'
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
            name: Cotton Sarouel
            id: '3321'
            icon: '45107'
            ilvl: '14'
            level: '14'
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
            name: Cotton Tights
            id: '3327'
            icon: '45083'
            ilvl: '15'
            level: '15'
            category:
              id: '36'
              name: Legs
              icon: '60128'
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
          count: 3
  - name: Walk of Shame
    level: 15
    rowId: 66680
    questId: SubSea153_01144
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.7, 25.5)
      name: S'nairoh
    steps:
      - location: Western La Noscea
        coords: (22.8, 22.7)
        name: Deliver the report to Commander Falkbryda.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Mountains out of Molehills
        level: 15
        rowId: 66679
        questId: SubSea152_01143
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      gil: 200
  - name: On a Wing and a Prayer
    level: 15
    rowId: 66681
    questId: SubSea154_01145
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (27.6, 28.5)
      name: Ahldfoet
    steps:
      - location: Western La Noscea
        coords: (24.9, 23.3)
        name: Harvest wings from dusk bats.
      - location: Western La Noscea
        coords: (27.6, 28.5)
        name: Give the dusk bat wings to Ahldfoet.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Call of the Sea
        level: 14
        rowId: 66210
        questId: SubWil141_00674
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Call of the Sea
        level: 14
        rowId: 66209
        questId: SubFst102_00673
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      optional:
        - item:
            name: Bronze Gauntlets
            id: '3544'
            icon: '48301'
            ilvl: '15'
            level: '15'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '11'
            name: Rust Red
            color: '6431239'
        - item:
            name: Hard Leather Lightmitts
            id: '3542'
            icon: '44067'
            ilvl: '14'
            level: '14'
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
            name: Fingerless Hard Leather Gloves
            id: '3546'
            icon: '44061'
            ilvl: '15'
            level: '15'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '23'
            name: Qiqirn Brown
            color: '10055231'
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
  - name: Mummy Dearest
    level: 15
    rowId: 66682
    questId: SubSea155_01146
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (27.6, 28.5)
      name: Ahldfoet
    steps:
      - location: Western La Noscea
        coords: (23.2, 22.2)
        name: Deliver the letter to Wiltswys.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: On a Wing and a Prayer
        level: 15
        rowId: 66681
        questId: SubSea154_01145
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      optional:
        - item:
            name: Bronze Sabatons
            id: '3775'
            icon: '46801'
            ilvl: '15'
            level: '15'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '11'
            name: Rust Red
            color: '6431239'
        - item:
            name: Hard Leather Crakows
            id: '3780'
            icon: '46155'
            ilvl: '15'
            level: '15'
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
            name: Hard Leather Boots
            id: '3777'
            icon: '46139'
            ilvl: '15'
            level: '15'
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
          count: 3
  - name: Beauty Is Only Scalp Deep
    level: 15
    rowId: 66746
    questId: SubCts801_01210
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.1, 11.0)
      name: S'dhodjbi
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (10.3, 12.5)
        name: Speak to the disgruntled madam.
      - location: Limsa Lominsa Upper Decks
        coords: (10.3, 12.4)
        name: Express /doubt as to the flustered man's intentions.
      - location: Limsa Lominsa Upper Decks
        coords: (10.6, 15.4)
        name: Speak with H'naanza at the Armorers' and Blacksmiths' Guild in Limsa
          Lominsa.
      - location: New Gridania
        coords: (10.3, 12.3)
        name: Speak with Beatin at the Carpenters' Guild in Gridania.
      - location: Ul'dah - Steps of Thal
        coords: (9.2, 13.6)
        name: Speak with Severian at the Alchemists' Guild in Ul'dah.
      - location: Limsa Lominsa Upper Decks
        coords: (10.3, 12.4)
        name: Deliver the supplies to Jandelaine in Limsa Lominsa.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Call of the Sea
        level: 14
        rowId: 66209
        questId: SubFst102_00673
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Call of the Sea
        level: 14
        rowId: 66210
        questId: SubWil141_00674
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      items:
        - item:
            name: Jandelaine's Token
            id: '7005'
            icon: '25918'
            ilvl: '1'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Like Cats and Dogs
    level: 15
    rowId: 66825
    questId: SubSea156_01289
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.4, 26.4)
      name: Skribyld
    steps:
      - location: Western La Noscea
        coords: (25.7, 25.9)
        name: Speak with R'kontai.
      - location: Western La Noscea
        coords: (25.8, 27.9)
        name: Pursue R'kontai.
      - location: Western La Noscea
        coords: (25.9, 27.9)
        name: Speak with R'kontai.
      - location: Western La Noscea
        coords: (26.4, 26.4)
        name: Report to Skribyld.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 75
        paramGrowId: '15'
        avg: 1080
      gil: 382
  - name: Man's Best Fiend
    level: 15
    rowId: 66826
    questId: SubSea157_01290
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.4, 26.4)
      name: Skribyld
    steps:
      - location: Western La Noscea
        coords: (25.7, 25.9)
        name: Speak with R'kontai.
      - location: Western La Noscea
        coords: (32.3, 27.8)
        name: Give the succulent bone to the starved pup.
      - location: Western La Noscea
        coords: (31.9, 27.3)
        name: /soothe the starved pup.
      - location: Western La Noscea
        coords: (26.4, 26.4)
        name: Report to Skribyld.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Like Cats and Dogs
        level: 15
        rowId: 66825
        questId: SubSea156_01289
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 75
        paramGrowId: '15'
        avg: 1080
      items:
        - item:
            name: Wolf Pup
            id: '6196'
            icon: '59450'
            ilvl: '1'
            level: '1'
            category:
              id: '81'
              name: Minion
              icon: '60155'
          count: 1
  - name: Curiosity Killed the Coeurl
    level: 15
    rowId: 66827
    questId: SubSea158_01291
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.4, 26.4)
      name: Skribyld
    steps:
      - location: Western La Noscea
        coords: (25.6, 23.7)
        name: Search for coeurls in Skull Valley.
      - location: Western La Noscea
        coords: (25.6, 23.7)
        name: Rescue the baby coeurl.
      - location: Western La Noscea
        coords: (26.4, 26.4)
        name: Report to Skribyld.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Like Cats and Dogs
        level: 15
        rowId: 66825
        questId: SubSea156_01289
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 75
        paramGrowId: '15'
        avg: 1080
      items:
        - item:
            name: Coeurl Kitten
            id: '6180'
            icon: '59452'
            ilvl: '1'
            level: '1'
            category:
              id: '81'
              name: Minion
              icon: '60155'
          count: 1
  - name: Rising to the Challenge
    level: 15
    rowId: 66967
    questId: SubCts810_01431
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.5, 10.9)
      name: I'tolwann
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (11.0, 11.4)
        name: Speak with Quentenain.
      - location: Limsa Lominsa Lower Decks
        coords: (7.5, 15.4)
        name: Deliver the well-worn journal to Wastlleid at the Lominsan ferry docks.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Call of the Sea
        level: 14
        rowId: 66209
        questId: SubFst102_00673
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Call of the Sea
        level: 14
        rowId: 66210
        questId: SubWil141_00674
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 50
        paramGrowId: '15'
        avg: 720
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
          count: 2
  - name: Nest We Forget
    level: 16
    rowId: 66683
    questId: SubSea161_01147
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.8, 22.7)
      name: Falkbryda
    steps:
      - location: Western La Noscea
        coords: (22.5, 22.3)
        name: Remove the dodo's nest and dispatch dodos.
      - location: Western La Noscea
        coords: (22.8, 22.7)
        name: Report to Falkbryda.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Walk of Shame
        level: 15
        rowId: 66680
        questId: SubSea153_01144
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '16'
        avg: 1500
      gil: 248
      optional:
        - item:
            name: Brass Gorget
            id: '4309'
            icon: '54802'
            ilvl: '16'
            level: '16'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Brass Wristlets
            id: '4094'
            icon: '55602'
            ilvl: '16'
            level: '16'
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
          count: 2
  - name: Toxic Avenger
    level: 16
    rowId: 66684
    questId: SubSea162_01148
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (23.2, 22.2)
      name: Wiltswys
    steps:
      - location: Western La Noscea
        coords: (23.5, 23.7)
        name: Collect poison from Rothlyt pelicans.
      - location: Western La Noscea
        coords: (23.2, 22.2)
        name: Deliver the vials of pelican poison to Wiltswys.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Mummy Dearest
        level: 15
        rowId: 66682
        questId: SubSea155_01146
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '16'
        avg: 1500
      gil: 197
  - name: My Brother's Not a Keeper
    level: 16
    rowId: 66685
    questId: SubSea163_01149
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (23.2, 22.2)
      name: Wiltswys
    steps:
      - location: Western La Noscea
        coords: (19.5, 22.8)
        name: Deliver wine to Captain Sthalrhet.
      - location: Western La Noscea
        coords: (23.2, 22.2)
        name: Report to Sergeant Wiltswys.
      - location: Western La Noscea
        coords: (22.0, 19.8)
        name: Deliver wine to Captain Nortmoen.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Toxic Avenger
        level: 16
        rowId: 66684
        questId: SubSea162_01148
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '16'
        avg: 1500
      gil: 207
  - name: Flowers for Aerghaemr
    level: 16
    rowId: 66686
    questId: SubSea164_01150
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.4, 20.0)
      name: Alyrloef
    steps:
      - location: Western La Noscea
        coords: (23.1, 20.3)
        name: Speak with Sergeant Roehanth.
      - location: Western La Noscea
        coords: (23.1, 20.3)
        name: Place the flowers on the Founder's Crypt.
      - location: Western La Noscea
        coords: (23.1, 20.3)
        name: Speak with Sergeant Roehanth.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Toxic Avenger
        level: 16
        rowId: 66684
        questId: SubSea162_01148
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '16'
        avg: 1500
      gil: 207
  - name: Scythe Extra Large
    level: 16
    rowId: 66687
    questId: SubSea165_01151
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (23.1, 20.3)
      name: Roehanth
    steps:
      - location: Western La Noscea
        coords: (22.8, 20.7)
        name: Slay the killer mantises.
      - location: Western La Noscea
        coords: (23.1, 20.3)
        name: Report to Roehanth.
      - location: Western La Noscea
        coords: (22.8, 22.7)
        name: Report to Falkbryda.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Flowers for Aerghaemr
        level: 16
        rowId: 66686
        questId: SubSea164_01150
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '16'
        avg: 1500
      gil: 248
  - name: I Hereby Relieve You
    level: 16
    rowId: 66688
    questId: SubSea166_01152
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.8, 22.7)
      name: Falkbryda
    steps:
      - location: Western La Noscea
        coords: (28.4, 22.9)
        name: Speak with Sergeant Catguistl.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Scythe Extra Large
        level: 16
        rowId: 66687
        questId: SubSea165_01151
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '16'
        avg: 1500
      gil: 207
  - name: An Ill-conceived Venture
    level: 17
    rowId: 66969
    questId: SubCts812_01433
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (9.0, 11.2)
      name: troubled adventurer
    steps:
      - location: Western La Noscea
        coords: (26.6, 23.5)
        name: Search Skull Valley for the missing retainer.
      - location: Limsa Lominsa Lower Decks
        coords: (8.3, 11.5)
        name: Speak with Frydwyb in Limsa Lominsa.
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
  - name: Leves of Moraby
    level: 20
    rowId: 66231
    questId: SubSea903_00695
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Lower La Noscea
      coords: (23.9, 33.0)
      name: Ourawann
    steps:
      - location: Lower La Noscea
        coords: (22.9, 34.5)
        name: Complete Ourawann's trial guildleve.
      - location: Lower La Noscea
        coords: (23.9, 33.0)
        name: Report to Ourawann.
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
      gil: 1795
  - name: My Little Chocobo (Maelstrom)
    level: 20
    rowId: 66237
    questId: SubSea910_00701
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (13.2, 12.8)
      name: R'ashaht Rhiki
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (12.1, 11.0)
        name: Present a Storm Chocobo Issuance to Fraegeim.
      - location: Limsa Lominsa Lower Decks
        coords: (12.2, 11.1)
        name: Name your chocobo.
      - location: Limsa Lominsa Lower Decks
        coords: (12.1, 11.0)
        name: Speak with Fraegeim.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: 590
        name: My Little Chocobo
        type: achievement
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
  - name: The Hottest of Box Lunches
    level: 23
    rowId: 66271
    questId: GaiUsa303_00735
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Upper La Noscea
      coords: (14.8, 24.3)
      name: Gegeroon
    steps:
      - location: Upper La Noscea
        coords: (12.4, 22.9)
        name: 'Deliver the hot box lunch to Tanga Tonga. '
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '23'
        avg: 1920
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
            name: Goatskin Breeches
            id: '3347'
            icon: '45304'
            ilvl: '23'
            level: '23'
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
            name: Cotton Kecks
            id: '3345'
            icon: '45099'
            ilvl: '23'
            level: '23'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
        - item:
            name: Cotton Gaskins
            id: '3343'
            icon: '45283'
            ilvl: '22'
            level: '22'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '75'
            name: Shadow Blue
            color: '3618631'
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
  - name: Buried Truth
    level: 23
    rowId: 66272
    questId: GaiUsa304_00736
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Upper La Noscea
      coords: (12.4, 22.9)
      name: Tanga Tonga
    steps:
      - location: Upper La Noscea
        coords: (13.8, 22.5)
        name: Search for a round fossil.
      - location: Upper La Noscea
        coords: (13.3, 21.4)
        name: Search for oblong fossils.
      - location: Upper La Noscea
        coords: (12.4, 22.9)
        name: Deliver the fossils to Tanga Tonga.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Hottest of Box Lunches
        level: 23
        rowId: 66271
        questId: GaiUsa303_00735
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '23'
        avg: 1920
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
            name: Iron Headgear
            id: '27653'
            icon: '40544'
            ilvl: '23'
            level: '23'
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
            name: Reinforced Iron Sallet
            id: '2725'
            icon: '40022'
            ilvl: '23'
            level: '23'
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
            name: Cotton Sugarloaf Hat
            id: '2719'
            icon: '41130'
            ilvl: '22'
            level: '22'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '36'
            name: Desert Yellow
            color: '14398551'
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
  - name: Leves of Costa del Sol
    level: 30
    rowId: 66232
    questId: SubSea904_00696
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Eastern La Noscea
      coords: (30.5, 30.9)
      name: Nahctahr
    steps:
      - location: Eastern La Noscea
        coords: (31.9, 28.7)
        name: Complete Nahctahr's trial guildleve.
      - location: Eastern La Noscea
        coords: (30.5, 30.9)
        name: Report to Nahctahr.
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
      gil: 2416
  - name: Costa Beach Party
    level: 30
    rowId: 66349
    questId: GaiUsb006_00813
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.8, 30.6)
      name: Gegeruju
    steps:
      - location: Eastern La Noscea
        coords: (30.0, 29.7)
        name: Speak with the carriage driver.
      - location: Eastern La Noscea
        coords: (32.4, 28.3)
        name: Find the dancing girls.
      - location: Eastern La Noscea
        coords: (33.8, 30.6)
        name: Report to Gegeruju.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '30'
        avg: 3120
      gil: 1377
  - name: A Faerie Tale Come True
    level: 30
    rowId: 70300
    questId: SubCts828_04764
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (4.7, 11.4)
      name: Thubyrgeim
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (4.5, 11.5)
        name: Wait at the designated location.
      - location: Limsa Lominsa Lower Decks
        coords: (4.7, 11.4)
        name: Speak with Thubyrgeim.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Forgotten but Not Gone
        level: 30
        rowId: 66633
        questId: JobSch300_01097
        genre: Scholar Quests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '30'
        avg: 0
      gil: 367
  - name: Who Moved My Headcheese
    level: 32
    rowId: 66369
    questId: GaiUsb202_00833
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.5, 30.6)
      name: Kuzai Tazai
    steps:
      - location: Eastern La Noscea
        coords: (32.4, 29.3)
        name: Place bloodstained sacks at the specified locations.
      - location: Eastern La Noscea
        coords: (32.8, 29.9)
        name: Lie in wait and defeat the kobolds.
      - location: Eastern La Noscea
        coords: (33.5, 30.6)
        name: Report to Kuzai Tazai.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Things We Do for Cheese
        level: 32
        rowId: 66368
        questId: GaiUsb201_00832
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      gil: 1690
  - name: Get a Grip
    level: 32
    rowId: 66370
    questId: GaiUsb203_00834
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.5, 30.6)
      name: Kuzai Tazai
    steps:
      - location: Eastern La Noscea
        coords: (31.1, 34.6)
        name: Slay snippers.
      - location: Eastern La Noscea
        coords: (30.9, 36.3)
        name: Lie in wait and defeat the gripper with the alchemic concoction.
      - location: Eastern La Noscea
        coords: (33.5, 30.6)
        name: Report to Kuzai Tazai.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Who Moved My Headcheese
        level: 32
        rowId: 66369
        questId: GaiUsb202_00833
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      gil: 1690
  - name: Unrefined Methods
    level: 32
    rowId: 66371
    questId: GaiUsb204_00835
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.5, 30.6)
      name: Fyrilsunn
    steps:
      - location: Eastern La Noscea
        coords: (29.0, 29.0)
        name: Throw makeshift bombs at the refiners and slay all foes.
      - location: Eastern La Noscea
        coords: (33.5, 30.6)
        name: Report to Fyrilsunn.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Things We Do for Cheese
        level: 32
        rowId: 66368
        questId: GaiUsb201_00832
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      optional:
        - item:
            name: Steel Scale Mail
            id: '3118'
            icon: '43175'
            ilvl: '32'
            level: '32'
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
  - name: Buffaloed All the Way
    level: 32
    rowId: 66372
    questId: GaiUsb205_00836
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.8, 30.6)
      name: P'ebaloh
    steps:
      - location: Eastern La Noscea
        coords: (27.8, 30.2)
        name: Slay large buffaloes.
      - location: Eastern La Noscea
        coords: (33.8, 30.6)
        name: Report to P'ebaloh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Things We Do for Cheese
        level: 32
        rowId: 66368
        questId: GaiUsb201_00832
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      optional:
        - item:
            name: Steel Scale Fingers
            id: '3605'
            icon: '48378'
            ilvl: '32'
            level: '32'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
          stain:
            id: '11'
            name: Rust Red
            color: '6431239'
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
  - name: Pests in the Pillars
    level: 32
    rowId: 66373
    questId: GaiUsb206_00837
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.8, 30.6)
      name: P'ebaloh
    steps:
      - location: Eastern La Noscea
        coords: (32.7, 30.5)
        name: Use steel spatulas on sturdy pillars and slay uragnites.
      - location: Eastern La Noscea
        coords: (33.8, 30.6)
        name: Report to P'ebaloh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Buffaloed All the Way
        level: 32
        rowId: 66372
        questId: GaiUsb205_00836
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
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
        - item:
            name: Quickarm Materia II
            id: '5715'
            icon: '20226'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Quicktongue Materia II
            id: '5720'
            icon: '20226'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
  - name: To You from Failing Hands We Throw
    level: 32
    rowId: 66374
    questId: GaiUsb207_00838
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.5, 30.6)
      name: Fyrilsunn
    steps:
      - location: Eastern La Noscea
        coords: (29.6, 33.9)
        name: Stand /lookout at the top of Gullperch Tower.
      - location: Eastern La Noscea
        coords: (29.2, 34.3)
        name: Locate the lion medals.
      - location: Eastern La Noscea
        coords: (33.5, 30.6)
        name: Return the lion medals to Fyrilsunn.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Unrefined Methods
        level: 32
        rowId: 66371
        questId: GaiUsb204_00835
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      gil: 1351
  - name: Raptor 'round Your Little Finger
    level: 32
    rowId: 66377
    questId: GaiUsb210_00841
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (21.0, 20.7)
      name: Etgar
    steps:
      - location: Eastern La Noscea
        coords: (23.7, 20.3)
        name: Slay grass raptors.
      - location: Eastern La Noscea
        coords: (21.0, 20.7)
        name: Report to Etgar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Things We Do for Cheese
        level: 32
        rowId: 66368
        questId: GaiUsb201_00832
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      optional:
        - item:
            name: Toadskin Breeches
            id: '3377'
            icon: '45307'
            ilvl: '32'
            level: '32'
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
  - name: Put a Cork in It
    level: 32
    rowId: 66378
    questId: GaiUsb211_00842
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (20.9, 20.7)
      name: Byrglaent
    steps:
      - location: Eastern La Noscea
        coords: (19.1, 25.2)
        name: Gather impeccable cork from cork bulbs.
      - location: Eastern La Noscea
        coords: (20.9, 20.7)
        name: Give the cork to Byrglaent.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Things We Do for Cheese
        level: 32
        rowId: 66368
        questId: GaiUsb201_00832
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      optional:
        - item:
            name: Steel Scale Greaves
            id: '3835'
            icon: '46870'
            ilvl: '32'
            level: '32'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '11'
            name: Rust Red
            color: '6431239'
        - item:
            name: Steel-plated Jackboots
            id: '3833'
            icon: '46836'
            ilvl: '32'
            level: '32'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
          stain:
            id: '19'
            name: Chocolate Brown
            color: '7224612'
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
  - name: Mona Lisa Smile
    level: 32
    rowId: 66380
    questId: GaiUsb303_00844
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (21.0, 20.7)
      name: Etgar
    steps:
      - location: Eastern La Noscea
        coords: (21.2, 25.6)
        name: Speak with the Ul'dahn artist.
      - location: Eastern La Noscea
        coords: (21.0, 20.7)
        name: Report to Etgar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Raptor 'round Your Little Finger
        level: 32
        rowId: 66377
        questId: GaiUsb210_00841
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      gil: 1461
  - name: Anise, Chocolate, and a Hint of Toad
    level: 33
    rowId: 66385
    questId: GaiUsb308_00849
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (21.0, 20.7)
      name: Etgar
    steps:
      - location: Eastern La Noscea
        coords: (19.6, 25.9)
        name: Slay gigantoads.
      - location: Eastern La Noscea
        coords: (21.0, 20.7)
        name: Report to Etgar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Mona Lisa Smile
        level: 32
        rowId: 66380
        questId: GaiUsb303_00844
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '33'
        avg: 3570
      gil: 1690
      optional:
        - item:
            name: Acorn Cookie
            id: '4701'
            icon: '24007'
            ilvl: '33'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 4
        - item:
            name: Scrambled Eggs
            id: '4654'
            icon: '24256'
            ilvl: '33'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 4
  - name: The Wind, It Passes
    level: 33
    rowId: 66387
    questId: GaiUsb310_00851
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.8, 30.6)
      name: Gegeruju
    steps:
      - location: Eastern La Noscea
        coords: (31.7, 32.4)
        name: Collect cores from wind sprites.
      - location: Eastern La Noscea
        coords: (32.6, 32.5)
        name: Place the wind sprite cores at the tip of the cliffs.
      - location: Eastern La Noscea
        coords: (33.8, 30.6)
        name: Report to Master Gegeruju.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Costa Beach Party
        level: 30
        rowId: 66349
        questId: GaiUsb006_00813
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '33'
        avg: 3570
      gil: 1725
  - name: Bird's-eye View
    level: 33
    rowId: 66388
    questId: GaiUsb311_00852
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.8, 30.6)
      name: Gegeruju
    steps:
      - location: Eastern La Noscea
        coords: (30.8, 24.6)
        name: Speak with the pitiless poacher.
      - location: Eastern La Noscea
        coords: (30.6, 25.8)
        name: Place bouquets of Oschon roselles along the specified trail.
      - location: Eastern La Noscea
        coords: (30.8, 24.6)
        name: Speak with the pitiless poacher.
      - location: Eastern La Noscea
        coords: (33.8, 30.6)
        name: Report to Master Gegeruju.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Wind, It Passes
        level: 33
        rowId: 66387
        questId: GaiUsb310_00851
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '33'
        avg: 3570
      optional:
        - item:
            name: Steel Headgear
            id: '27654'
            icon: '40543'
            ilvl: '32'
            level: '32'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Skull Eyepatch
            id: '2767'
            icon: '40892'
            ilvl: '33'
            level: '33'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Silver Monocle
            id: '27668'
            icon: '40906'
            ilvl: '32'
            level: '32'
            category:
              id: '34'
              name: Head
              icon: '60124'
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
  - name: The Stench of Danger
    level: 33
    rowId: 66389
    questId: GaiUsb312_00853
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Eastern La Noscea
      coords: (33.8, 30.6)
      name: P'ebaloh
    steps:
      - location: Eastern La Noscea
        coords: (34.8, 31.3)
        name: Slay the pugils.
      - location: Eastern La Noscea
        coords: (34.8, 31.3)
        name: Remove the carcass.
      - location: Eastern La Noscea
        coords: (33.8, 30.6)
        name: Report to P'ebaloh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Pests in the Pillars
        level: 32
        rowId: 66373
        questId: GaiUsb206_00837
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '33'
        avg: 3570
      gil: 1377
  - name: One Swallow Does Not a Victory Make
    level: 34
    rowId: 66394
    questId: GaiUsb402_00858
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Upper La Noscea
      coords: (30.4, 23.0)
      name: Blaugybal
    steps:
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Hand the plea to Bloeidin at Camp Overlook.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Lord of Crags
        level: 34
        rowId: 66393
        questId: GaiUsb401_00857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1492
  - name: Never Trout That I Love
    level: 34
    rowId: 66395
    questId: GaiUsb403_00859
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Outer La Noscea
        coords: (18.6, 17.1)
        name: Grill the trout at the nearby campfire.
      - location: Outer La Noscea
        coords: (18.6, 17.1)
        name: Take the grilled trout off the fire.
      - location: Outer La Noscea
        coords: (19.6, 16.7)
        name: Give the grilled trout to the soldiers.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Report to Bloeidin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: One Swallow Does Not a Victory Make
        level: 34
        rowId: 66394
        questId: GaiUsb402_00858
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1492
      items:
        - item:
            name: Mugwort Carp
            id: '4663'
            icon: '24314'
            ilvl: '38'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: Dead or Sumfin' Like It
    level: 34
    rowId: 66396
    questId: GaiUsb404_00860
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (19.4, 18.3)
      name: Augustine
    steps:
      - location: Outer La Noscea
        coords: (16.9, 16.4)
        name: Slay highland condors.
      - location: Outer La Noscea
        coords: (19.4, 18.3)
        name: Report to Augustine.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Lord of Crags
        level: 34
        rowId: 66393
        questId: GaiUsb401_00857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1580
      optional:
        - item:
            name: Savage Aim Materia II
            id: '5670'
            icon: '20222'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Heavens' Eye Materia II
            id: '5665'
            icon: '20222'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Savage Might Materia II
            id: '5675'
            icon: '20222'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Battledance Materia II
            id: '5680'
            icon: '20214'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
        - item:
            name: Piety Materia II
            id: '5630'
            icon: '20214'
            ilvl: '30'
            level: '1'
            category:
              id: '58'
              name: Materia
              icon: '60150'
          count: 1
  - name: Return to Your Dust
    level: 34
    rowId: 66397
    questId: GaiUsb405_00861
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Outer La Noscea
        coords: (14.5, 16.4)
        name: Wrest a soulstone from a basalt golem.
      - location: Outer La Noscea
        coords: (13.0, 15.9)
        name: Place the soulstone in the specified spot.
      - location: Outer La Noscea
        coords: (13.3, 16.3)
        name: Use the water in the glass bottles to defeat the Unbreakable kobold.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Report to Bloeidin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Never Trout That I Love
        level: 34
        rowId: 66395
        questId: GaiUsb403_00859
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 4580
  - name: Deduce, Reuse, Recycle
    level: 34
    rowId: 66398
    questId: GaiUsb406_00862
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Swygrael
    steps:
      - location: Outer La Noscea
        coords: (18.7, 15.5)
        name: Collect velociraptor claws.
      - location: Outer La Noscea
        coords: (18.5, 15.3)
        name: Collect serrated arrowheads.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Give Swygrael the claws and the arrowheads.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Lord of Crags
        level: 34
        rowId: 66393
        questId: GaiUsb401_00857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1492
  - name: Don't Let the Cat out of the Bag
    level: 34
    rowId: 66399
    questId: GaiUsb407_00863
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Swygrael
    steps:
      - location: Outer La Noscea
        coords: (16.0, 15.3)
        name: Weaken a young coeurl and capture it with a sack.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Give the bagged coeurl to Swygrael.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Deduce, Reuse, Recycle
        level: 34
        rowId: 66398
        questId: GaiUsb406_00862
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1580
      items:
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
            name: Spine Drops
            id: '4568'
            icon: '20645'
            ilvl: '30'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
  - name: Looking for Trouble
    level: 34
    rowId: 66400
    questId: GaiUsb408_00864
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Outer La Noscea
        coords: (18.0, 16.3)
        name: 'Search the specified locations and slay kobolds. '
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Report to Bloeidin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Return to Your Dust
        level: 34
        rowId: 66397
        questId: GaiUsb405_00861
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1580
  - name: Helm Me You Love Me
    level: 34
    rowId: 66401
    questId: GaiUsb409_00865
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Outer La Noscea
        coords: (15.9, 17.2)
        name: Detonate kobold bombs with smoldering coal.
      - location: Outer La Noscea
        coords: (15.6, 17.3)
        name: Lurk at the specified spot and defeat the kobold priest.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Show the kobold priest's helm to Bloeidin.
      - location: Upper La Noscea
        coords: (30.4, 23.0)
        name: Give the kobold priest's helm to Blaugybal at Camp Bronze Lake.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Looking for Trouble
        level: 34
        rowId: 66400
        questId: GaiUsb408_00864
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1580
  - name: The Monster of Bronze Lake
    level: 34
    rowId: 66402
    questId: GaiUsb410_00866
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Upper La Noscea
      coords: (30.0, 21.9)
      name: Rukusa Farusa
    steps:
      - location: Upper La Noscea
        coords: (27.4, 22.6)
        name: Slay salamanders and obtain salamander oil.
      - location: Upper La Noscea
        coords: (31.4, 22.7)
        name: Show the salamander oil to Godbert.
      - location: Upper La Noscea
        coords: (31.4, 22.7)
        name: Use the salamander oil on Godbert.
      - location: Upper La Noscea
        coords: (31.4, 22.7)
        name: Use the salamander oil on Godbert again.
      - location: Upper La Noscea
        coords: (31.4, 22.7)
        name: Massage the oil into Godbert's weary flesh.
      - location: Upper La Noscea
        coords: (31.4, 22.7)
        name: Continue massaging Godbert's tense muscles.
      - location: Upper La Noscea
        coords: (30.0, 21.9)
        name: Report to Rukusa Farusa.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Lord of Crags
        level: 34
        rowId: 66393
        questId: GaiUsb401_00857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1760
  - name: Red, Red Wine
    level: 34
    rowId: 66403
    questId: GaiUsb411_00867
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Upper La Noscea
      coords: (30.0, 21.8)
      name: A'rhunlika
    steps:
      - location: Upper La Noscea
        coords: (30.8, 23.6)
        name: Submerge the mulled wine in the hot spring.
      - location: Upper La Noscea
        coords: (30.8, 23.6)
        name: Take the bottles of warmwine from the hot spring.
      - location: Upper La Noscea
        coords: (29.6, 22.4)
        name: Give the warmwine to the convalescing soldiers.
      - location: Upper La Noscea
        coords: (30.0, 21.8)
        name: Report to A'rhunlika.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Lord of Crags
        level: 34
        rowId: 66393
        questId: GaiUsb401_00857
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1492
  - name: The Adventure of the Fainting Goldsmith
    level: 34
    rowId: 66404
    questId: GaiUsb412_00868
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Upper La Noscea
      coords: (30.0, 21.9)
      name: Rukusa Farusa
    steps:
      - location: Upper La Noscea
        coords: (31.6, 22.6)
        name: Give Godbert a firm /poke.
      - location: Upper La Noscea
        coords: (31.6, 22.6)
        name: Dump the freezing lake water on Godbert.
      - location: Upper La Noscea
        coords: (31.6, 22.6)
        name: Dump the freezing lake water on Godbert again.
      - location: Upper La Noscea
        coords: (31.6, 22.6)
        name: Dump the freezing lake water on Godbert yet again.
      - location: Upper La Noscea
        coords: (30.0, 21.9)
        name: Report to Rukusa Farusa.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Monster of Bronze Lake
        level: 34
        rowId: 66402
        questId: GaiUsb410_00866
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '34'
        avg: 3655
      gil: 1311
      items:
        - item:
            name: Meteor Survivor Ring
            id: '6138'
            icon: '54510'
            ilvl: '36'
            level: '34'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
  - name: Leves of Wineport
    level: 35
    rowId: 65550
    questId: SubSea905_00014
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Eastern La Noscea
      coords: (21.6, 21.5)
      name: Aileen
    steps:
      - location: Eastern La Noscea
        coords: (23.4, 21.9)
        name: Complete Aileen's trial guildleve.
      - location: Eastern La Noscea
        coords: (21.6, 21.5)
        name: Report to Aileen.
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
        paramGrowId: '35'
        avg: 3960
      gil: 1791
  - name: Treasures and Tribulations
    level: 36
    rowId: 66747
    questId: SubCts802_01211
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Eastern La Noscea
      coords: (21.1, 21.1)
      name: H'loonh
    steps:
      - location: Eastern La Noscea
        coords: (20.1, 25.0)
        name: Speak with the diligent digger.
      - location: Upper La Noscea
        coords: (33.9, 24.8)
        name: Speak with Ealdwine in upper La Noscea.
      - location: Upper La Noscea
        coords: (33.5, 24.9)
        name: Open the casket and deal with any disturbances.
      - location: Upper La Noscea
        coords: (33.5, 24.9)
        name: Obtain the treasure from the casket.
      - location: Upper La Noscea
        coords: (33.9, 24.8)
        name: Deliver the tattered coinpurse and shattered bottle to Ealdwine.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '36'
        avg: 4275
  - name: Grave Happenings
    level: 42
    rowId: 66500
    questId: GaiUsc205_00964
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (16.4, 31.2)
      name: Otan Yaratan
    steps:
      - location: Western La Noscea
        coords: (15.3, 35.3)
        name: Slay dead man's moans.
      - location: Western La Noscea
        coords: (16.4, 31.2)
        name: Report to Oran Yaratan.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '42'
        avg: 5610
      gil: 1703
  - name: Pickled and Brined
    level: 42
    rowId: 66501
    questId: GaiUsc206_00965
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (17.4, 31.5)
      name: Ahlduwil
    steps:
      - location: Western La Noscea
        coords: (11.4, 36.0)
        name: Fill the bottle with wine from the wine tun.
      - location: Western La Noscea
        coords: (17.4, 31.5)
        name: Give the bottle of wine to Ahlduwil.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '42'
        avg: 5610
      gil: 1703
  - name: Too Many Cooks
    level: 42
    rowId: 66502
    questId: GaiUsc207_00966
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (17.5, 31.5)
      name: Erapi Taropi
    steps:
      - location: Western La Noscea
        coords: (17.1, 36.4)
        name: Collect Far Eastern spices from the spice box.
      - location: Western La Noscea
        coords: (17.5, 31.5)
        name: Give the spices to Erapi Taropi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '42'
        avg: 5610
      gil: 1703
  - name: A Pirate's Life for Me
    level: 47
    rowId: 66553
    questId: GaiUsc705_01017
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Outer La Noscea
        coords: (19.4, 18.3)
        name: Speak with Bloeidin's crew.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Report to Bloeidin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Kobold Initiative
        level: 47
        rowId: 66551
        questId: GaiUsc703_01015
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      gil: 1716
  - name: Honor the Fallen
    level: 47
    rowId: 66554
    questId: GaiUsc706_01018
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (19.2, 16.7)
      name: F'majha
    steps:
      - location: Outer La Noscea
        coords: (21.2, 15.3)
        name: Retrieve marks from the fallen.
      - location: Outer La Noscea
        coords: (19.2, 16.7)
        name: Deliver marks to F'majha.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Kobold Initiative
        level: 47
        rowId: 66551
        questId: GaiUsc703_01015
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      gil: 1716
  - name: Operation Crucible Down
    level: 47
    rowId: 66555
    questId: GaiUsc707_01019
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Outer La Noscea
        coords: (21.8, 14.1)
        name: Use makeshift bombs to blow up kobold supplies.
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Report to Bloeidin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Pirate's Life for Me
        level: 47
        rowId: 66553
        questId: GaiUsc705_01017
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      optional:
        - item:
            name: Raptorskin Breeches
            id: '3443'
            icon: '45355'
            ilvl: '46'
            level: '46'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
          stain:
            id: '6'
            name: Soot Black
            color: '2828579'
        - item:
            name: Raptorskin Subligar
            id: '3447'
            icon: '45175'
            ilvl: '47'
            level: '47'
            category:
              id: '36'
              name: Legs
              icon: '60128'
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
  - name: Claiming the Booty
    level: 47
    rowId: 66556
    questId: GaiUsc708_01020
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Outer La Noscea
      coords: (18.6, 17.2)
      name: Bloeidin
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (13.2, 12.8)
        name: Deliver the report to R'ashaht Rhiki.
      - location: The Waking Sands
        coords: (6.1, 5.8)
        name: Report to Slafswys at the Waking Sands.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Operation Crucible Down
        level: 47
        rowId: 66555
        questId: GaiUsc707_01019
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      gil: 1716
  - name: Pier Review
    level: 48
    rowId: 66562
    questId: GaiUsc802_01026
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.8, 22.7)
      name: Falkbryda
    steps:
      - location: Western La Noscea
        coords: (26.5, 25.5)
        name: Speak with Ururu Kogururu at Aleport.
      - location: Western La Noscea
        coords: (27.9, 29.0)
        name: Speak with Dawson.
      - location: Western La Noscea
        coords: (27.4, 28.3)
        name: Obtain a supply box.
      - location: Western La Noscea
        coords: (27.9, 28.8)
        name: Take the supply box to the pier.
      - location: Western La Noscea
        coords: (27.4, 28.3)
        name: Obtain a supply box.
      - location: Western La Noscea
        coords: (27.9, 28.9)
        name: Take the supply box to the pier.
      - location: Western La Noscea
        coords: (27.4, 28.3)
        name: Obtain a supply box.
      - location: Western La Noscea
        coords: (27.9, 28.9)
        name: Take the supply box to the pier.
      - location: Western La Noscea
        coords: (27.9, 29.0)
        name: Speak with Dawson.
      - location: Western La Noscea
        coords: (26.5, 25.5)
        name: Report to Ururu Kogururu.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Into the Valley of the Skull
        level: 48
        rowId: 66561
        questId: GaiUsc801_01025
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      gil: 1857
  - name: Long Walk off a Short Pier
    level: 48
    rowId: 66563
    questId: GaiUsc803_01027
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (26.5, 25.5)
      name: Ururu Kogururu
    steps:
      - location: Western La Noscea
        coords: (27.9, 29.0)
        name: Speak with Dawson.
      - location: Western La Noscea
        coords: (28.1, 25.1)
        name: Examine the dropped cargo and slay the Serpent Reavers.
      - location: Western La Noscea
        coords: (27.9, 29.0)
        name: Speak with Dawson.
      - location: Western La Noscea
        coords: (22.8, 22.7)
        name: Report to Falkbryda.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Pier Review
        level: 48
        rowId: 66562
        questId: GaiUsc802_01026
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      gil: 2218
  - name: To Catch a Cutthroat
    level: 48
    rowId: 66564
    questId: GaiUsc804_01028
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.6, 22.5)
      name: U'jughal
    steps:
      - location: Western La Noscea
        coords: (13.2, 16.7)
        name: Slay Drysnagl in the Serpent's Tongue.
      - location: Western La Noscea
        coords: (22.6, 22.5)
        name: Report to U'jughal.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Long Walk off a Short Pier
        level: 48
        rowId: 66563
        questId: GaiUsc803_01027
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      optional:
        - item:
            name: Amber Choker
            id: '4371'
            icon: '54824'
            ilvl: '48'
            level: '48'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Rubellite Choker
            id: '4365'
            icon: '54821'
            ilvl: '48'
            level: '48'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Tourmaline Choker
            id: '4369'
            icon: '54823'
            ilvl: '48'
            level: '48'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
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
          count: 2
  - name: Serpent's Tongue-lashing
    level: 48
    rowId: 66565
    questId: GaiUsc805_01029
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.9, 22.5)
      name: Ahtzatrach
    steps:
      - location: Western La Noscea
        coords: (13.3, 16.8)
        name: Slay Serpent Reavers.
      - location: Western La Noscea
        coords: (22.9, 22.5)
        name: Report to Ahtzatrach.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Long Walk off a Short Pier
        level: 48
        rowId: 66563
        questId: GaiUsc803_01027
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      optional:
        - item:
            name: Spinel Choker
            id: '4373'
            icon: '54826'
            ilvl: '48'
            level: '48'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Zircon Choker
            id: '4367'
            icon: '54825'
            ilvl: '48'
            level: '48'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Turquoise Choker
            id: '4375'
            icon: '54822'
            ilvl: '48'
            level: '48'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
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
          count: 2
  - name: Culling the Horde
    level: 48
    rowId: 66566
    questId: GaiUsc806_01030
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.7, 22.4)
      name: Eilis
    steps:
      - location: Western La Noscea
        coords: (18.5, 21.4)
        name: Slay Sahagin invaders.
      - location: Western La Noscea
        coords: (22.7, 22.4)
        name: Report to Eilis.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Long Walk off a Short Pier
        level: 48
        rowId: 66563
        questId: GaiUsc803_01027
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      optional:
        - item:
            name: Spinel Earrings
            id: '4266'
            icon: '55227'
            ilvl: '49'
            level: '49'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Turquoise Earrings
            id: '4268'
            icon: '55223'
            ilvl: '49'
            level: '49'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Zircon Earrings
            id: '4260'
            icon: '55226'
            ilvl: '49'
            level: '49'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
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
          count: 2
  - name: Sibling Rivalry
    level: 48
    rowId: 66567
    questId: GaiUsc807_01031
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.7, 22.4)
      name: Eilis
    steps:
      - location: Western La Noscea
        coords: (22.0, 19.8)
        name: Deliver Maelstrom rations to Nortmoen.
      - location: Western La Noscea
        coords: (19.5, 22.8)
        name: Deliver Maelstrom rations to Sthalrhet.
      - location: Western La Noscea
        coords: (22.7, 22.4)
        name: Report to Eilis.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Serpent's Tongue-lashing
        level: 48
        rowId: 66565
        questId: GaiUsc805_01029
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      gil: 1857
  - name: Wag the Sea Dogs
    level: 48
    rowId: 66568
    questId: GaiUsc808_01032
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.7, 22.4)
      name: Eilis
    steps:
      - location: Western La Noscea
        coords: (22.0, 19.8)
        name: Speak with Nortmoen.
      - location: Western La Noscea
        coords: (19.9, 19.9)
        name: Slay trenchtooth Sahagin.
      - location: Western La Noscea
        coords: (22.7, 22.4)
        name: Report to Eilis.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sibling Rivalry
        level: 48
        rowId: 66567
        questId: GaiUsc807_01031
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      optional:
        - item:
            name: Spinel Ring
            id: '4510'
            icon: '54426'
            ilvl: '49'
            level: '49'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Turquoise Ring
            id: '4512'
            icon: '54422'
            ilvl: '49'
            level: '49'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Zircon Ring
            id: '4504'
            icon: '54425'
            ilvl: '49'
            level: '49'
            category:
              id: '43'
              name: Ring
              icon: '60135'
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
          count: 2
  - name: Sea Wasp Run
    level: 48
    rowId: 66569
    questId: GaiUsc809_01033
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.0, 19.8)
      name: Nortmoen
    steps:
      - location: Western La Noscea
        coords: (13.9, 17.4)
        name: Slay sea wasps and obtain their umbrellas.
      - location: Western La Noscea
        coords: (22.0, 19.8)
        name: Deliver the sea wasp umbrellas to Nortmoen.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      optional:
        - item:
            name: Amber Bracelet
            id: '4162'
            icon: '55626'
            ilvl: '48'
            level: '48'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Rubellite Bracelet
            id: '4156'
            icon: '55623'
            ilvl: '48'
            level: '48'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Tourmaline Bracelet
            id: '4160'
            icon: '55625'
            ilvl: '48'
            level: '48'
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
          count: 2
  - name: No Sea Wasp for You
    level: 48
    rowId: 66570
    questId: GaiUsc810_01034
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (19.5, 22.8)
      name: Sthalrhet
    steps:
      - location: Western La Noscea
        coords: (14.2, 17.0)
        name: Slay sea wasps and obtain their rotting umbrellas.
      - location: Western La Noscea
        coords: (19.5, 22.8)
        name: Deliver the rotting umbrellas to Sthalrhet.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      optional:
        - item:
            name: Spinel Bracelet
            id: '4164'
            icon: '55628'
            ilvl: '48'
            level: '48'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Turquoise Bracelet
            id: '4166'
            icon: '55624'
            ilvl: '48'
            level: '48'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Zircon Bracelet
            id: '4158'
            icon: '55627'
            ilvl: '48'
            level: '48'
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
          count: 2
  - name: The Way the Crystals Crumble
    level: 48
    rowId: 66571
    questId: GaiUsc811_01035
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Western La Noscea
      coords: (22.8, 22.7)
      name: Falkbryda
    steps:
      - location: Western La Noscea
        coords: (13.1, 16.7)
        name: Use the makeshift bombs to destroy the boxes of crystals.
      - location: Western La Noscea
        coords: (22.8, 22.7)
        name: Report to Falkbryda.
      - location: The Waking Sands
        coords: (6.1, 5.5)
        name: Report to Radolf.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Long Walk off a Short Pier
        level: 48
        rowId: 66563
        questId: GaiUsc803_01027
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      gil: 1857
      optional:
        - item:
            name: Amber Earrings
            id: '4264'
            icon: '55225'
            ilvl: '49'
            level: '49'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Rubellite Earrings
            id: '4258'
            icon: '55222'
            ilvl: '49'
            level: '49'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
          count: 1
        - item:
            name: Tourmaline Earrings
            id: '4262'
            icon: '55224'
            ilvl: '49'
            level: '49'
            category:
              id: '41'
              name: Earrings
              icon: '60133'
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
          count: 2
  - name: Sirius Business
    level: 50
    rowId: 66744
    questId: SubCts001_01208
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Western La Noscea
      coords: (26.5, 26.7)
      name: Diamanda
    steps:
      - location: Western La Noscea
        coords: (27.4, 29.1)
        name: Speak with Mimidoa.
      - location: Western La Noscea
        coords: (16.1, 30.7)
        name: Speak with Davyd at Pharos Sirius.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
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
  - name: Why So Sirius
    level: 50
    rowId: 66745
    questId: SubCts002_01209
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Western La Noscea
      coords: (26.5, 26.7)
      name: Diamanda
    steps:
      - location: Western La Noscea
        coords: (27.4, 29.1)
        name: Speak with Mimidoa.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sirius Business
        level: 50
        rowId: 66744
        questId: SubCts001_01208
        genre: La Noscean Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 658
  - name: The Beast of Brewer's Beacon
    level: 50
    rowId: 66966
    questId: SubSea922_01430
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (7.9, 14.5)
      name: Sisipu
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 15.3)
        name: Speak with Wawalago.
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 15.3)
        name: Deliver a titanic sawfish to Wawalago.
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 15.3)
        name: Deliver a Navigator's brand to Wawalago.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: 902
        name: I Like Big Fish and I Cannot Lie
        type: achievement
    requires:
      - name: So Long, and Thanks for All the Fish
        level: 50
        rowId: 66654
        questId: ClsFsh501_01118
        genre: Fisher Quests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 1220
      items:
        - item:
            name: Tomato Pie
            id: '4714'
            icon: '24156'
            ilvl: '55'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
      optional:
        - item:
            name: Pill Bug
            id: '2587'
            icon: '27005'
            ilvl: '5'
            level: '5'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 99
        - item:
            name: Crayfish Ball
            id: '2588'
            icon: '27008'
            ilvl: '5'
            level: '5'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 99
        - item:
            name: Butterworm
            id: '2594'
            icon: '27019'
            ilvl: '20'
            level: '20'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 99
        - item:
            name: Crow Fly
            id: '2614'
            icon: '27057'
            ilvl: '20'
            level: '20'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 15
  - name: Feast of Famine
    level: 50
    rowId: 65782
    questId: SubSea923_00246
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71020'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (8.1, 15.3)
      name: Wawalago
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 15.3)
        name: Deliver living legends fished in La Noscea, the Black Shroud, and Thanalan
          to Wawalago.
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 15.3)
        name: Deliver living legends fished in Coerthas and Mor Dhona to Wawalago.
      - location: Eastern La Noscea
        coords: (33.6, 29.3)
        name: Speak with the steersman at Costa del Sol.
      - location: Eastern La Noscea
        coords: (39.2, 24.1)
        name: Catch the Nepto Dragon from the privateer, and deliver it to the saltworn
          captain.
      - location: Limsa Lominsa Lower Decks
        coords: (8.1, 15.3)
        name: Speak with Wawalago at Fisherman's Bottom.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: 1031
        name: Imagine Dragon
        type: achievement
    requires:
      - name: The Beast of Brewer's Beacon
        level: 50
        rowId: 66966
        questId: SubSea922_01430
        genre: La Noscean Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 50000
      items:
        - item:
            name: Aetheryte Ticket
            id: '7569'
            icon: '25918'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 99
      optional:
        - item:
            name: Yumizuno
            id: '2628'
            icon: '27068'
            ilvl: '48'
            level: '48'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 50
        - item:
            name: Streamer
            id: '2627'
            icon: '27060'
            ilvl: '48'
            level: '48'
            category:
              id: '33'
              name: Fishing Tackle
              icon: '60123'
          count: 50
  - name: An Egi by Any Other Name
    level: 50
    rowId: 67896
    questId: SubCts823_02360
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Lower Decks
      coords: (4.7, 11.4)
      name: Thubyrgeim
    steps:
      - location: Limsa Lominsa Lower Decks
        coords: (4.5, 11.4)
        name: Wait for Thubyrgeim in the guild's practice area.
      - location: Limsa Lominsa Lower Decks
        coords: (4.7, 11.4)
        name: Speak with Thubyrgeim.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Primal Burdens
        level: 50
        rowId: 66632
        questId: JobSmn500_01096
        genre: Summoner Quests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '50'
        avg: 0
      gil: 461
  - name: Things Are Getting Sirius
    level: 60
    rowId: 67737
    questId: HeaVny101_02201
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (12.7, 12.8)
      name: Trachraet
    steps:
      - location: Limsa Lominsa Upper Decks
        coords: (10.7, 11.0)
        name: Speak with the storm flyer at the airship landing.
      - location: Pharos Sirius
        coords: (9.6, 7.8)
        name: Enter Pharos Sirius (Hard).
      - location: Western La Noscea
        coords: (16.1, 30.3)
        name: Report to the storm flyer at the entrance of Pharos Sirius.
      - location: Western La Noscea
        coords: (26.3, 26.3)
        name: Give the blunt whittle to Trachraet in Aleport.
    expansion:
      id: '1'
      name: Heavensward
    unlocks:
      - name: Pharos Sirius (Hard)
        type: dungeon
        levelRequired: 60
        levelSync: 60
        ilevelRequired: 170
        ilevelSync: 240
    requires:
      - name: Heavensward
        level: 60
        rowId: 67205
        questId: HeaVna707_01669
        genre: Heavensward
        icon: '71000'
      - name: Why So Sirius
        level: 50
        rowId: 66745
        questId: SubCts002_01209
        genre: La Noscean Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '60'
        avg: 0
      gil: 5000
  - name: Storming the Hull
    level: 60
    rowId: 67784
    questId: HeaVny102_02248
    genre:
      id: '112'
      name: La Noscean Sidequests
    icon: '71140'
    issuer:
      location: Limsa Lominsa Upper Decks
      coords: (11.0, 10.4)
      name: Denston
    steps:
      - location: Lower La Noscea
        coords: (27.0, 36.0)
        name: Speak with Denston at the Moraby Drydocks.
      - location: Hullbreaker Isle
        coords: (4.1, 12.4)
        name: Enter Hullbreaker Isle (Hard).
      - location: Limsa Lominsa Upper Decks
        coords: (11.0, 10.4)
        name: Speak with Denston in Limsa Lominsa.
    expansion:
      id: '1'
      name: Heavensward
    unlocks:
      - name: Hullbreaker Isle (Hard)
        type: dungeon
        levelRequired: 60
        levelSync: 60
        ilevelRequired: 200
        ilevelSync: 0
      - name: Copperbell Mines (Hard)
        type: dungeon
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 48
        ilevelSync: 110
    requires:
      - name: Heavensward
        level: 60
        rowId: 67205
        questId: HeaVna707_01669
        genre: Heavensward
        icon: '71000'
      - name: King of the Hull
        level: 50
        rowId: 67062
        questId: SubCts004_01526
        genre: Mor Dhonan Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '60'
        avg: 0
      gil: 5000
genre:
  genreId: '112'
  name: La Noscean Sidequests


---