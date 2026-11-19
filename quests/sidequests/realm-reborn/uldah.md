---
layout: quest-table
title: Ul'Dahn Sidequests
permalink: /quests/sidequests/realm-reborn/uldah
nonsequential: true
brandLabel: Mognet
brandUrl: /quests/sidequests/realm-reborn
quests:
  - name: Coming to Ul'dah
    level: 1
    rowId: 66130
    questId: ManWil001_00594
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.9, 8.2)
      name: Wymond
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Speak with Momodi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 400
        paramGrowId: '1'
        avg: 400
      gil: 103
  - name: Due Diligence
    level: 1
    rowId: 65685
    questId: SubWil000_00149
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (9.8, 8.7)
      name: Wymond
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (9.4, 10.1)
        name: Deliver the unsigned envelope to Josias.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 103
  - name: Motivational Speaking
    level: 1
    rowId: 65686
    questId: SubWil001_00150
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (9.6, 10.2)
      name: Gelther
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (8.2, 11.5)
        name: Threaten Didilata.
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
          count: 2
  - name: Gil for Gold
    level: 1
    rowId: 65687
    questId: SubWil002_00151
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (8.2, 11.5)
      name: Didilata
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (7.0, 12.6)
        name: Take the ring to Mamane for appraisal.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Motivational Speaking
        level: 1
        rowId: 65686
        questId: SubWil001_00150
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
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
  - name: Unholy Matrimony
    level: 1
    rowId: 65689
    questId: SubWil004_00153
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (7.9, 12.0)
      name: Hihito
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (8.7, 11.2)
        name: Speak with Bobonima.
      - location: Ul'dah - Steps of Thal
        coords: (9.5, 11.6)
        name: Post the flyers inside the Coliseum.
      - location: Ul'dah - Steps of Thal
        coords: (9.3, 11.6)
        name: Speak with Wolkan.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Gil for Gold
        level: 1
        rowId: 65687
        questId: SubWil002_00151
        genre: Ul'dahn Sidequests
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
          count: 5
  - name: The Great Gladiator
    level: 1
    rowId: 65701
    questId: SubWil006_00165
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (9.4, 11.8)
      name: Zazarikku
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (10.5, 13.1)
        name: Present the receipt of purchase to Jemime.
      - location: Ul'dah - Steps of Thal
        coords: (10.8, 14.3)
        name: Speak with Crooked Haft.
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
  - name: With Open Arms
    level: 1
    rowId: 65703
    questId: SubWil007_00167
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (14.1, 13.0)
      name: Juliana
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (14.1, 13.0)
        name: Show Juliana your best /welcome.
      - location: Ul'dah - Steps of Thal
        coords: (13.2, 12.3)
        name: Seek out any would-be weavers and give them a warm /welcome.
      - location: Ul'dah - Steps of Thal
        coords: (14.1, 13.0)
        name: Report back to Juliana at the Weavers' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 102
  - name: No Lady Is an Island
    level: 1
    rowId: 65932
    questId: SubWil018_00396
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (9.4, 11.4)
      name: Genevieve
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (9.4, 11.4)
        name: Gather the dropped gil.
      - location: Ul'dah - Steps of Thal
        coords: (9.4, 11.4)
        name: Return the gil to Genevieve.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 102
  - name: The Greatest Story Never Told
    level: 1
    rowId: 66973
    questId: SubFst999_01437
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (18.3, 17.4)
      name: Valiant Hart
    steps: []
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: 1005
        name: The Rest of the Story
        type: achievement
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
        paramGrowId: '1'
        avg: 0
      gil: 10
  - name: Decisions, Decisions
    level: 1
    rowId: 65928
    questId: SubWil019_00392
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (11.8, 13.2)
      name: Bitter Snow
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (14.0, 13.3)
        name: Speak with Yellow Moon in the Weavers' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 111
      items:
        - item:
            name: Lavender
            id: '5539'
            icon: '25002'
            ilvl: '11'
            level: '1'
            category:
              id: '54'
              name: Reagent
              icon: '60145'
          count: 1
  - name: Vox Populi
    level: 1
    rowId: 65929
    questId: SubWil020_00393
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (14.1, 13.1)
      name: Aethelwine
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (12.6, 10.4)
        name: Find the most popular color on the Hustings Strip.
      - location: Ul'dah - Steps of Thal
        coords: (12.6, 11.9)
        name: Find the most popular color on the Steps of Thal.
      - location: Ul'dah - Steps of Thal
        coords: (9.1, 13.8)
        name: Report to Leucu at the Alchemists' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 55
        paramGrowId: '1'
        avg: 55
      gil: 109
  - name: A Luxury Long Lost
    level: 1
    rowId: 65930
    questId: SubWil021_00394
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (9.2, 13.9)
      name: Alewyn
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (13.1, 10.5)
        name: Offer Alewyn's tonic to Landebert.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 111
  - name: The Wealth of Nations
    level: 1
    rowId: 65931
    questId: SubWil022_00395
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (13.1, 10.5)
      name: Landebert
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (14.0, 10.0)
        name: Find a merchant who will appraise the vase.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Luxury Long Lost
        level: 1
        rowId: 65930
        questId: SubWil021_00394
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 50
        paramGrowId: '1'
        avg: 50
      gil: 111
  - name: Tougher than Leather
    level: 1
    rowId: 65699
    questId: SubWil015_00163
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (9.0, 9.7)
      name: Jajakuta
    steps:
      - location: Central Thanalan
        coords: (22.1, 26.9)
        name: Collect shrew pelts from snapping shrews in central Thanalan.
      - location: Ul'dah - Steps of Nald
        coords: (9.0, 9.7)
        name: Report to Jajakuta outside the Pugilists' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 35
        paramGrowId: '1'
        avg: 35
      gil: 127
  - name: Beet Red Beetles Beat Red
    level: 1
    rowId: 66107
    questId: SubWil013_00571
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (9.3, 11.6)
      name: Wolkan
    steps:
      - location: Western Thanalan
        coords: (28.4, 24.9)
        name: Slay ladybugs in western Thanalan.
      - location: Ul'dah - Steps of Thal
        coords: (9.3, 11.6)
        name: Report to Wolkan at the Gladiators' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 35
        paramGrowId: '1'
        avg: 35
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
  - name: In the Name of Science
    level: 1
    rowId: 66108
    questId: SubWil014_00572
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (7.3, 12.4)
      name: Erasmus
    steps:
      - location: Western Thanalan
        coords: (29.4, 24.4)
        name: Collect bottles of marmot blood.
      - location: Ul'dah - Steps of Nald
        coords: (7.3, 12.4)
        name: Report back to Erasmus at the Thaumaturges' Guild.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 35
        paramGrowId: '1'
        avg: 35
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
            id: '20'
            name: Russet Brown
            color: '5188895'
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
            id: '11'
            name: Rust Red
            color: '6431239'
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
  - name: Bottled Fantasy
    level: 1
    rowId: 70723
    questId: KinGyr301_05187
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (13.4, 9.2)
      name: medicine merchant
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (10.3, 9.2)
        name: Deliver the phial of mysterious liquid to the diminutive gladiator on
          the Steps of Nald.
      - location: Ul'dah - Steps of Thal
        coords: (13.4, 9.2)
        name: Deliver the leather sack of coin to the medicine merchant.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Scions of the Seventh Dawn
        level: 17
        rowId: 66045
        questId: ManFst206_00509
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 0
        paramGrowId: '1'
        avg: 0
      gil: 105
      items:
        - item:
            name: Fantasia
            id: '6221'
            icon: '20629'
            ilvl: '1'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 1
  - name: Nor Rain nor Heat nor Gloom of Night
    level: 4
    rowId: 65758
    questId: SubWil030_00222
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (25.9, 24.3)
      name: Oswell
    steps:
      - location: Western Thanalan
        coords: (25.8, 24.3)
        name: Locate the missing cargo crates.
      - location: Western Thanalan
        coords: (25.9, 24.3)
        name: Deliver the crates to Oswell.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 125
  - name: Fantastic Voyage
    level: 4
    rowId: 65925
    questId: SubWil028_00389
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.6, 9.0)
      name: Kekezani
    steps:
      - location: Central Thanalan
        coords: (23.2, 27.9)
        name: Deliver the timetable to Giginasu at the Ul'dah Dispatch Yard.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 66104
        questId: ManWil002_00568
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 66105
        questId: ManWil003_00569
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 66106
        questId: ManWil004_00570
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
            id: '32'
            name: Mole Brown
            color: '6378053'
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
  - name: Catch Your Breath
    level: 4
    rowId: 65926
    questId: SubWil029_00390
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.5, 9.1)
      name: Botulf
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (7.7, 11.0)
        name: Speak with Mimishu.
      - location: Western Thanalan
        coords: (25.9, 24.3)
        name: Deliver to Oswell the package to Horizon.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Close to Home
        level: 1
        rowId: 66104
        questId: ManWil002_00568
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 66105
        questId: ManWil003_00569
        genre: Seventh Umbral Era
        icon: '71000'
      - name: Close to Home
        level: 1
        rowId: 66106
        questId: ManWil004_00570
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
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
            id: '35'
            name: Ul Brown
            color: '12034928'
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
  - name: A Dab'll Do Ya
    level: 4
    rowId: 65759
    questId: SubWil031_00223
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (25.9, 24.3)
      name: Guntram
    steps:
      - location: Western Thanalan
        coords: (27.4, 24.5)
        name: Slay cactuars and gather bottles of cactuar blood.
      - location: Western Thanalan
        coords: (25.9, 24.3)
        name: Deliver the bottles of cactuar blood to Guntram.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 132
  - name: Ticked Off
    level: 4
    rowId: 65767
    questId: SubWil039_00231
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (26.0, 24.1)
      name: Imme
    steps:
      - location: Western Thanalan
        coords: (26.1, 24.2)
        name: Examine Slugger and slay any parasites you find.
      - location: Western Thanalan
        coords: (26.1, 24.2)
        name: Speak with Slugger.
      - location: Western Thanalan
        coords: (26.0, 24.1)
        name: Speak with Imme.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 132
  - name: Where the Heart Is (The Goblet)
    level: 5
    rowId: 66749
    questId: SubCts804_01213
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (26.0, 24.1)
      name: Imme
    steps:
      - location: Western Thanalan
        coords: (27.9, 26.1)
        name: Speak with Momoraji.
      - location: The Goblet
        coords: (11.1, 7.4)
        name: Journey to the Goblet.
      - location: The Goblet
        coords: (11.3, 7.4)
        name: Speak with the flame recruit.
      - location: Western Thanalan
        coords: (26.0, 24.1)
        name: Report to Imme.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '5'
        avg: 175
      gil: 132
  - name: I Believe You Can Fly
    level: 4
    rowId: 65760
    questId: SubWil032_00224
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (25.9, 24.3)
      name: Oswell
    steps:
      - location: Western Thanalan
        coords: (22.7, 25.4)
        name: Gather tailfeathers from hammer beaks.
      - location: Western Thanalan
        coords: (16.4, 29.5)
        name: Deliver the tailfeathers and Oswell's letter to Kikipu at the Silver
          Bazaar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Nor Rain nor Heat nor Gloom of Night
        level: 4
        rowId: 65758
        questId: SubWil030_00222
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 139
  - name: Reasonable /Doubt
    level: 4
    rowId: 65762
    questId: SubWil034_00226
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (16.4, 29.5)
      name: Kikipu
    steps:
      - location: Western Thanalan
        coords: (15.5, 28.7)
        name: Use the power of /doubt to make the workers leave.
      - location: Western Thanalan
        coords: (16.4, 29.5)
        name: Report back to Kikipu.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: I Believe You Can Fly
        level: 4
        rowId: 65760
        questId: SubWil032_00224
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 60
        paramGrowId: '4'
        avg: 156
      gil: 139
  - name: The Slaying of the Shrews
    level: 4
    rowId: 65857
    questId: SubWil067_00321
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (22.8, 26.6)
      name: Hihiyaja
    steps:
      - location: Central Thanalan
        coords: (22.7, 26.3)
        name: Slay the snipping shrews.
      - location: Central Thanalan
        coords: (22.8, 26.6)
        name: Report to Hihiyaja.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Underneath the Sultantree
        level: 4
        rowId: 66086
        questId: ManWil005_00550
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 139
  - name: Greasing the Cogs
    level: 4
    rowId: 65763
    questId: SubWil035_00227
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (16.3, 29.6)
      name: Fafafono
    steps:
      - location: Western Thanalan
        coords: (21.4, 26.9)
        name: Collect four bottles of coblyn grease from rusty coblyns.
      - location: Western Thanalan
        coords: (20.3, 27.9)
        name: Deliver the coblyn grease to Adelard at the Hammers.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 146
  - name: Getting Your Bearings
    level: 4
    rowId: 65764
    questId: SubWil036_00228
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (15.5, 28.1)
      name: Danyell
    steps:
      - location: Western Thanalan
        coords: (18.2, 27.7)
        name: Find chunks of magnetite.
      - location: Western Thanalan
        coords: (16.4, 29.7)
        name: Deliver the magnetite to Galfridus at the Silver Bazaar.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 141
  - name: The Tasting of the Shrews
    level: 4
    rowId: 65840
    questId: SubWil061_00304
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (19.5, 20.5)
      name: Wowobaru
    steps:
      - location: Central Thanalan
        coords: (21.8, 20.3)
        name: Slay the captured shrews.
      - location: Central Thanalan
        coords: (19.5, 20.5)
        name: Deliver the shrew meat to Wowobaru.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Listen to Your Fish
        level: 4
        rowId: 65858
        questId: SubWil068_00322
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 141
  - name: Listen to Your Fish
    level: 4
    rowId: 65858
    questId: SubWil068_00322
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (22.8, 26.6)
      name: Hihiyaja
    steps:
      - location: Central Thanalan
        coords: (21.1, 24.6)
        name: Obtain slices of fatty orobon.
      - location: Central Thanalan
        coords: (19.5, 20.5)
        name: Offer the fatty orobon to Wowobaru.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Slaying of the Shrews
        level: 4
        rowId: 65857
        questId: SubWil067_00321
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 141
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
  - name: So Close yet So Far
    level: 4
    rowId: 65761
    questId: SubWil033_00225
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (16.3, 29.6)
      name: Fafafono
    steps:
      - location: Western Thanalan
        coords: (17.3, 28.7)
        name: Gather pieces of Fafafono's baggage.
      - location: Western Thanalan
        coords: (16.3, 29.6)
        name: Deliver the baggage to Fafafono.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Greasing the Cogs
        level: 4
        rowId: 65763
        questId: SubWil035_00227
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 70
        paramGrowId: '4'
        avg: 182
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
  - name: Tackle the Problem
    level: 4
    rowId: 65765
    questId: SubWil037_00229
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (16.4, 29.7)
      name: Galfridus
    steps:
      - location: Western Thanalan
        coords: (18.8, 25.9)
        name: Obtain copper lures from goblin muggers.
      - location: Western Thanalan
        coords: (16.4, 29.7)
        name: Return the copper lures to Galfridus at the Silver Bazaar.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Getting Your Bearings
        level: 4
        rowId: 65764
        questId: SubWil036_00228
        genre: Ul'dahn Sidequests
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
  - name: Bloodied and Bowed
    level: 4
    rowId: 65924
    questId: SubWil074_00388
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (20.8, 18.5)
      name: Aethelgyth
    steps:
      - location: Central Thanalan
        coords: (21.2, 17.8)
        name: Offer a hi-potion to Osbert.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Prudence at This Junction
        level: 4
        rowId: 69388
        questId: XxaWil063_03852
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 70
        paramGrowId: '4'
        avg: 182
      gil: 122
  - name: Search and Seizure
    level: 4
    rowId: 65766
    questId: SubWil038_00230
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (16.4, 29.5)
      name: Kikipu
    steps:
      - location: Western Thanalan
        coords: (16.5, 29.1)
        name: Tear down the writs of seizure.
      - location: Western Thanalan
        coords: (17.1, 28.8)
        name: Return the writs to Kenrick.
      - location: Western Thanalan
        coords: (16.4, 29.5)
        name: Speak with Kikipu.
      - location: Ul'dah - Steps of Nald
        coords: (11.6, 9.6)
        name: Deliver Kikipu's letter to Momodi at the Quicksand.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Getting Your Bearings
        level: 4
        rowId: 65764
        questId: SubWil036_00228
        genre: Ul'dahn Sidequests
        icon: '71020'
      - name: Tackle the Problem
        level: 4
        rowId: 65765
        questId: SubWil037_00229
        genre: Ul'dahn Sidequests
        icon: '71020'
      - name: Reasonable /Doubt
        level: 4
        rowId: 65762
        questId: SubWil034_00226
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '4'
        avg: 260
      gil: 132
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
  - name: In the Court of the Rat King
    level: 4
    rowId: 65844
    questId: SubWil065_00308
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (20.6, 18.4)
      name: Zezeda
    steps:
      - location: Central Thanalan
        coords: (16.1, 20.1)
        name: Recover the stolen coffers.
      - location: Central Thanalan
        coords: (20.6, 18.4)
        name: Return the coffers to Zezeda.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Sometimes the Old Ways Are Best
        level: 4
        rowId: 65862
        questId: SubWil072_00326
        genre: Ul'dahn Sidequests
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
  - name: Sometimes the Old Ways Are Best
    level: 4
    rowId: 65862
    questId: SubWil072_00326
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (20.6, 18.4)
      name: Zezeda
    steps:
      - location: Central Thanalan
        coords: (18.8, 20.3)
        name: Slay hammer beaks and obtain their ribs.
      - location: Central Thanalan
        coords: (20.6, 17.4)
        name: Deliver the hammer beak ribs to Beringaer.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Out of House and Home
        level: 4
        rowId: 65843
        questId: SubWil064_00307
        genre: Seventh Umbral Era
        icon: '71000'
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
            id: '6'
            name: Soot Black
            color: '2828579'
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
  - name: Lend Me Your Ears Already
    level: 9
    rowId: 66965
    questId: SubWil101_01429
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (11.5, 9.5)
      name: Memenaru
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (11.5, 9.1)
        name: Speak with Botulf.
      - location: Ul'dah - Steps of Nald
        coords: (11.5, 9.1)
        name: "With the chat mode in **Say**, enter \u201CWell met!\u201D to greet\
          \ Botulf."
      - location: Ul'dah - Steps of Nald
        coords: (11.5, 9.1)
        name: "With the chat mode in **Say**, enter the auto\u2013translate option\
          \ Hello! and greet Botulf once again."
      - location: Ul'dah - Steps of Nald
        coords: (11.5, 9.1)
        name: Speak with Botulf.
      - location: Ul'dah - Steps of Nald
        coords: (11.5, 9.1)
        name: "With the chat mode in **Say**, enter \u201CYou misunderstand.\u201D\
          \ to allay Botulf's concern. "
      - location: Ul'dah - Steps of Nald
        coords: (11.5, 9.1)
        name: "With the chat mode in **Say**, enter the auto\u2013translate option\
          \ Good-bye."
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Way Down in the Hole
        level: 9
        rowId: 65856
        questId: SubWil066_00320
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
    rowId: 65594
    questId: SubWil154_00058
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (23.2, 16.5)
      name: Totonowa
    steps:
      - location: Western Thanalan
        coords: (23.2, 16.7)
        name: Speak with Battlewarden Lost Rabbit.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Leves of Horizon
        level: 10
        rowId: 66223
        questId: SubWil150_00687
        genre: Ul'dahn Sidequests
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
  - name: By the Toe
    level: 10
    rowId: 65873
    questId: SubWil089_00337
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (22.6, 17.1)
      name: Fufulupa
    steps:
      - location: Western Thanalan
        coords: (23.5, 18.0)
        name: Set the iron leg traps.
      - location: Western Thanalan
        coords: (23.1, 17.2)
        name: Report to Chechezan.
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
  - name: For Their Eyes Only
    level: 10
    rowId: 65875
    questId: SubWil090_00339
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (22.6, 17.3)
      name: Zuzutyro
    steps:
      - location: Western Thanalan
        coords: (25.2, 20.1)
        name: Slay desert peistes and obtain Eyes of the Serpent.
      - location: Western Thanalan
        coords: (22.6, 17.3)
        name: Deliver the Eyes of the Serpent to Zuzutyro.
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
          count: 2
  - name: Leves of Horizon
    level: 10
    rowId: 66223
    questId: SubWil150_00687
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (12.0, 9.0)
      name: Eustace
    steps:
      - location: Western Thanalan
        coords: (23.2, 16.5)
        name: Speak with Totonowa at Horizon.
      - location: Western Thanalan
        coords: (18.4, 16.4)
        name: Complete Totonowa's trial guildleve.
      - location: Western Thanalan
        coords: (23.2, 16.5)
        name: Report to Totonowa.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Way Down in the Hole
        level: 9
        rowId: 65856
        questId: SubWil066_00320
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 215
  - name: The Scent of a Mongrel
    level: 10
    rowId: 65877
    questId: SubWil092_00341
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (23.1, 17.2)
      name: Chechezan
    steps:
      - location: Western Thanalan
        coords: (22.4, 21.9)
        name: Collect bottles of mongrel blood.
      - location: Western Thanalan
        coords: (26.7, 21.3)
        name: Deliver the mongrel blood to Nononzo.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Perfect Swarm
        level: 10
        rowId: 65865
        questId: SubWil081_00329
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 196
  - name: No Tool Gets Left Behind
    level: 10
    rowId: 66040
    questId: SubWil096_00504
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (26.3, 18.3)
      name: Torrid Whisper
    steps:
      - location: Western Thanalan
        coords: (27.5, 16.9)
        name: Find the sharpened pickaxe.
      - location: Western Thanalan
        coords: (27.5, 16.9)
        name: Find the old hammer.
      - location: Western Thanalan
        coords: (27.5, 16.9)
        name: Find the heavy sledgehammer.
      - location: Western Thanalan
        coords: (26.3, 18.3)
        name: Return the mining tools to Torrid Whisper.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Supply and Demands
        level: 10
        rowId: 65864
        questId: SubWil080_00328
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 173
      items:
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
  - name: Need Not Apply in Person
    level: 10
    rowId: 66067
    questId: SubWil099_00531
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (23.3, 16.3)
      name: Hamund
    steps:
      - location: Central Thanalan
        coords: (20.6, 17.4)
        name: Deliver Hamund's application to Beringaer at Black Brush Station.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Last Letter to Lost Hope
        level: 10
        rowId: 65866
        questId: SubWil082_00330
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 188
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
  - name: This Fishwife's Life
    level: 10
    rowId: 66042
    questId: SubWil094_00506
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (15.6, 18.1)
      name: Edalene
    steps:
      - location: Western Thanalan
        coords: (15.7, 18.1)
        name: Remove debris from the trawling nets.
      - location: Western Thanalan
        coords: (15.6, 18.1)
        name: Speak with Edalene.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Passing the Blade
        level: 10
        rowId: 65868
        questId: SubWil084_00332
        genre: Seventh Umbral Era
        icon: '71000'
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
            id: '48'
            name: Olive Green
            color: '4936242'
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
  - name: Alternative Medicine
    level: 10
    rowId: 66066
    questId: SubWil098_00530
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (23.4, 16.0)
      name: Blayves
    steps:
      - location: Central Thanalan
        coords: (27.5, 19.3)
        name: Obtain gigantoad secretions from toxic toads.
      - location: Central Thanalan
        coords: (23.4, 16.0)
        name: Deliver the gigantoad secretions to Blayves at Lost Hope.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Last Letter to Lost Hope
        level: 10
        rowId: 65866
        questId: SubWil082_00330
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
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
            id: '32'
            name: Mole Brown
            color: '6378053'
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
  - name: Fringe Benefits
    level: 10
    rowId: 66109
    questId: SubWil100_00573
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Central Thanalan
      coords: (23.3, 16.0)
      name: Amalberga
    steps:
      - location: Central Thanalan
        coords: (24.0, 21.0)
        name: Steal the raw Nashachite.
      - location: Central Thanalan
        coords: (23.3, 16.0)
        name: Deliver the Nashachite to Amalberga.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Last Letter to Lost Hope
        level: 10
        rowId: 65866
        questId: SubWil082_00330
        genre: Seventh Umbral Era
        icon: '71000'
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
  - name: Lominsan Rubbish
    level: 10
    rowId: 65878
    questId: SubWil093_00342
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (15.8, 18.5)
      name: Osment
    steps:
      - location: Western Thanalan
        coords: (15.8, 18.4)
        name: Clean up the rubbish on the docks.
      - location: Western Thanalan
        coords: (15.8, 18.5)
        name: Speak with Osment.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Passing the Blade
        level: 10
        rowId: 65868
        questId: SubWil084_00332
        genre: Seventh Umbral Era
        icon: '71000'
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
            id: '34'
            name: Bone White
            color: '15455136'
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
  - name: Angling Ankle-biters
    level: 10
    rowId: 66041
    questId: SubWil097_00505
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (17.9, 16.0)
      name: Totoruna
    steps:
      - location: Western Thanalan
        coords: (18.4, 16.3)
        name: Slay orobon.
      - location: Western Thanalan
        coords: (17.9, 16.0)
        name: Report to Totoruna.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Passing the Blade
        level: 10
        rowId: 65868
        questId: SubWil084_00332
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '10'
        avg: 855
      gil: 212
  - name: Help Me, Lord of the Dance
    level: 14
    rowId: 66963
    questId: SubWil159_01427
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (10.8, 9.8)
      name: P'molminn
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (11.2, 11.1)
        name: Ask about Guillaunaux on the Steps of Thal.
      - location: Ul'dah - Steps of Thal
        coords: (10.9, 10.2)
        name: Speak with Guillaunaux.
      - location: Ul'dah - Steps of Thal
        coords: (10.9, 10.2)
        name: /dance for Guillaunaux.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - id: '103'
        name: Ball Dance
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
  - name: It Could Happen to You
    level: 15
    rowId: 65970
    questId: SubGsc001_00434
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (9.6, 9.0)
      name: well-heeled youth
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (10.7, 11.2)
        name: Present the golden airship ticket to Elyenora at the airship landing.
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
      - name: The Ul'dahn Envoy
        level: 14
        rowId: 66064
        questId: ManWil200_00528
        genre: Seventh Umbral Era
        icon: '71000'
      - name: The Lominsan Envoy
        level: 14
        rowId: 66082
        questId: ManSea200_00546
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
      gil: 239
  - name: World of Wonders
    level: 15
    rowId: 65971
    questId: SubGsc002_00435
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: The Gold Saucer
      coords: (5.3, 8.0)
      name: airship ticketer
    steps:
      - location: The Gold Saucer
        coords: (5.0, 6.7)
        name: Speak with the Gold Saucer attendant at the main counter.
      - location: The Gold Saucer
        coords: (4.9, 6.6)
        name: Speak with the other Gold Saucer attendant at the main counter.
      - location: The Gold Saucer
        coords: (4.1, 7.4)
        name: Speak with the Triple Triad trader at Card Square.
      - location: The Gold Saucer
        coords: (6.5, 6.9)
        name: Speak with the GATE Keeper at Wonder Square.
      - location: The Gold Saucer
        coords: (8.6, 5.8)
        name: Speak with Veleda at the Cactpot Board.
      - location: The Gold Saucer
        coords: (5.8, 4.6)
        name: Speak with the GATE Keeper at Round Square.
      - location: The Gold Saucer
        coords: (5.0, 6.7)
        name: Speak with the Gold Saucer attendant at the main counter.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: It Could Happen to You
        level: 15
        rowId: 65970
        questId: SubGsc001_00434
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
      items:
        - item:
            name: Gold Saucer Ticket
            id: '10085'
            icon: '26173'
            ilvl: '1'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 5
  - name: So You Want to Be a Jockey
    level: 15
    rowId: 65972
    questId: SubGsc101_00436
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Chocobo Square
      coords: (6.1, 4.7)
      name: race chocobo registrar
    steps:
      - location: Central Shroud
        coords: (20.4, 22.8)
        name: Speak with Katering at Bentbranch Meadows.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: It Could Happen to You
        level: 15
        rowId: 65970
        questId: SubGsc001_00434
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
      optional:
        - item:
            name: Fledgling Chocobo Registration G1-M
            id: '9561'
            icon: '27651'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
        - item:
            name: Fledgling Chocobo Registration G1-F
            id: '9570'
            icon: '27652'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
  - name: Like Sire Like Fledgling
    level: 15
    rowId: 66112
    questId: SubGsc106_00576
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Chocobo Square
      coords: (6.2, 4.7)
      name: chocobokeep
    steps:
      - location: Central Shroud
        coords: (20.4, 22.8)
        name: Speak with Katering at Bentbranch Meadows.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: So You Think You Can Ride This Chocobo
        level: 15
        rowId: 66101
        questId: SubGsc105_00565
        genre: Gridanian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
      optional:
        - item:
            name: Grade 2 Feed - Special Speed Blend
            id: '10147'
            icon: '27562'
            ilvl: '70'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
        - item:
            name: Grade 2 Feed - Special Acceleration Blend
            id: '10148'
            icon: '27559'
            ilvl: '70'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
        - item:
            name: Grade 2 Feed - Special Balance Blend
            id: '10149'
            icon: '27561'
            ilvl: '70'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
        - item:
            name: Grade 2 Feed - Special Endurance Blend
            id: '10150'
            icon: '27558'
            ilvl: '70'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
        - item:
            name: Grade 2 Feed - Special Stamina Blend
            id: '10151'
            icon: '27560'
            ilvl: '70'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Leves of Camp Drybone
    level: 15
    rowId: 66224
    questId: SubWil151_00688
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Eastern Thanalan
      coords: (13.9, 24.0)
      name: Poponagu
    steps:
      - location: Eastern Thanalan
        coords: (13.1, 24.7)
        name: Complete Poponagu's trial guildleve.
      - location: Eastern Thanalan
        coords: (13.9, 24.0)
        name: Report to Poponagu.
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
  - name: Color Your World
    level: 15
    rowId: 66235
    questId: SubSea921_00699
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.6, 14.3)
      name: Swyrgeim
    steps:
      - location: Western Thanalan
        coords: (12.6, 14.3)
        name: Deliver a bottle of orange juice to Swyrgeim.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
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
          count: 9
  - name: If I Had a Glamour
    level: 15
    rowId: 68553
    questId: SubCts896_03017
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.6, 14.3)
      name: Swyrgeim
    steps:
      - location: Western Thanalan
        coords: (12.5, 15.0)
        name: Speak with Folclind.
      - location: Western Thanalan
        coords: (12.6, 14.3)
        name: Deliver the blood orange juice to Swyrgeim.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
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
          count: 12
        - item:
            name: Green Beret
            id: '13258'
            icon: '41292'
            ilvl: '1'
            level: '1'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
  - name: Absolutely Glamourous
    level: 15
    rowId: 68554
    questId: SubCts897_03018
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.6, 14.3)
      name: Swyrgeim
    steps:
      - location: Western Thanalan
        coords: (12.5, 15.0)
        name: Speak with Folclind.
      - location: Western Thanalan
        coords: (12.6, 14.3)
        name: Deliver the Othardian orange juice to Swyrgeim.
      - location: Western Thanalan
        coords: (12.2, 15.0)
        name: Present the letter to Goberin.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: If I Had a Glamour
        level: 15
        rowId: 68553
        questId: SubCts896_03017
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '15'
        avg: 0
      items:
        - item:
            name: Clear Prism
            id: '7671'
            icon: '26226'
            ilvl: '35'
            level: '1'
            category:
              id: '48'
              name: Stone
              icon: '60139'
          count: 1
  - name: A Dying Wish
    level: 17
    rowId: 66160
    questId: SubWil115_00624
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (13.8, 23.4)
      name: Tutusi
    steps:
      - location: Eastern Thanalan
        coords: (17.7, 21.8)
        name: Obtain sirloins from myotragus nannies.
      - location: Eastern Thanalan
        coords: (12.5, 23.1)
        name: Deliver the myotragus sirloins to Sister Zozoru.
      - location: Eastern Thanalan
        coords: (13.8, 23.4)
        name: Report to Tutusi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '17'
        avg: 1560
      gil: 257
  - name: The Circle of Life
    level: 17
    rowId: 66166
    questId: SubWil120_00630
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (13.8, 23.4)
      name: Tutusi
    steps:
      - location: Eastern Thanalan
        coords: (19.9, 24.3)
        name: Gather sprigs of Althyk lavender.
      - location: Eastern Thanalan
        coords: (13.8, 23.4)
        name: Deliver the Althyk lavender to Tutusi.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Dying Wish
        level: 17
        rowId: 66160
        questId: SubWil115_00624
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '17'
        avg: 1560
      gil: 235
  - name: Green Thumb
    level: 17
    rowId: 66173
    questId: SubWil127_00637
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (19.8, 24.7)
      name: Jospaire
    steps:
      - location: Eastern Thanalan
        coords: (17.2, 24.8)
        name: Obtain a pot of muddy spring water.
      - location: Eastern Thanalan
        coords: (19.8, 24.7)
        name: Deliver muddy spring water to Jospaire.
      - location: Eastern Thanalan
        coords: (19.8, 24.8)
        name: Remove vilekin eggs from the plants.
      - location: Eastern Thanalan
        coords: (19.8, 24.7)
        name: Speak with Jospaire.
      - location: Eastern Thanalan
        coords: (19.9, 24.4)
        name: Pour stingbrew on thick bramble patches and slay syrphid clouds.
      - location: Eastern Thanalan
        coords: (19.8, 24.7)
        name: Speak with Jospaire.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Dying Wish
        level: 17
        rowId: 66160
        questId: SubWil115_00624
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '17'
        avg: 1560
      gil: 214
  - name: Seeds of Change
    level: 17
    rowId: 66960
    questId: SubCts809_01424
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Western Thanalan
      coords: (12.0, 15.0)
      name: Tatafu
    steps:
      - location: Western Thanalan
        coords: (15.5, 17.9)
        name: Deliver the two sacks to Nanalai.
      - location: Western Thanalan
        coords: (12.0, 15.0)
        name: Deliver Nanalai's payment to Tatafu.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 50
        paramGrowId: '17'
        avg: 780
      items:
        - item:
            name: La Noscean Orange Seeds
            id: '7725'
            icon: '27457'
            ilvl: '7'
            level: '1'
            category:
              id: '82'
              name: Gardening
              icon: '60153'
          count: 1
        - item:
            name: Lowland Grape Seeds
            id: '7726'
            icon: '27457'
            ilvl: '11'
            level: '1'
            category:
              id: '82'
              name: Gardening
              icon: '60153'
          count: 1
  - name: An Ill-conceived Venture
    level: 17
    rowId: 66970
    questId: SubCts813_01434
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (9.3, 8.7)
      name: troubled adventurer
    steps:
      - location: Eastern Thanalan
        coords: (16.6, 23.6)
        name: Search Drybone for the missing retainer.
      - location: Ul'dah - Steps of Thal
        coords: (13.3, 9.8)
        name: Speak with Chachabi in Ul'dah.
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
  - name: All Dogs Go to Hell
    level: 18
    rowId: 66161
    questId: SubWil116_00625
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (13.6, 23.3)
      name: Caitlyn
    steps:
      - location: Eastern Thanalan
        coords: (16.8, 26.0)
        name: Slay dusty mongrels.
      - location: Eastern Thanalan
        coords: (13.6, 23.3)
        name: Report to Caitlyn.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '18'
        avg: 1620
      gil: 243
  - name: Buzzing at Church
    level: 18
    rowId: 66162
    questId: SubWil117_00626
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.1, 21.3)
      name: Esmour
    steps:
      - location: Eastern Thanalan
        coords: (11.6, 22.7)
        name: Slay blowfly swarms.
      - location: Eastern Thanalan
        coords: (11.1, 21.3)
        name: Report to Esmour.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '18'
        avg: 1620
      gil: 220
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
  - name: Lichyard Lilies
    level: 18
    rowId: 66163
    questId: SubWil118_00627
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.1, 21.4)
      name: Airell
    steps:
      - location: Eastern Thanalan
        coords: (11.8, 21.4)
        name: Place Nymeia lilies at the simple graves.
      - location: Eastern Thanalan
        coords: (11.1, 21.4)
        name: Report to Sister Airell.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Dead Bodies Everywhere
        level: 18
        rowId: 66178
        questId: SubWil128_00642
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '18'
        avg: 1620
      gil: 220
  - name: Honoring the Dead
    level: 18
    rowId: 66165
    questId: SubWil119_00629
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.1, 21.5)
      name: Eaduuard
    steps:
      - location: Eastern Thanalan
        coords: (13.7, 20.6)
        name: Obtain a slab of cloud marble.
      - location: Eastern Thanalan
        coords: (11.1, 21.3)
        name: Deliver the cloud marble to Brother Esmour.
      - location: Eastern Thanalan
        coords: (11.1, 21.5)
        name: Report to Eaduuard.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Buzzing at Church
        level: 18
        rowId: 66162
        questId: SubWil117_00626
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '18'
        avg: 1620
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
            name: Hi-Potion
            id: '4552'
            icon: '20602'
            ilvl: '25'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 10
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
  - name: Dead Bodies Everywhere
    level: 18
    rowId: 66178
    questId: SubWil128_00642
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.1, 21.4)
      name: Airell
    steps:
      - location: Eastern Thanalan
        coords: (11.4, 22.3)
        name: Gather old offerings.
      - location: Eastern Thanalan
        coords: (11.1, 21.4)
        name: Deliver the old offerings to Sister Airell.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '18'
        avg: 1620
      gil: 243
  - name: Steaking Claims
    level: 19
    rowId: 66167
    questId: SubWil121_00631
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (13.6, 23.3)
      name: Caitlyn
    steps:
      - location: Eastern Thanalan
        coords: (12.3, 19.1)
        name: Obtain chunks of tuco-tuco meat.
      - location: Eastern Thanalan
        coords: (10.6, 16.6)
        name: Deliver the tuco-tuco meat to Beneger.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: A Proper Burial
        level: 18
        rowId: 66156
        questId: SubWil112_00620
        genre: Seventh Umbral Era
        icon: '71000'
      - name: All Dogs Go to Hell
        level: 18
        rowId: 66161
        questId: SubWil116_00625
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
      gil: 250
      optional:
        - item:
            name: Coral Armillae
            id: '4100'
            icon: '55632'
            ilvl: '19'
            level: '19'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Brass Ring
            id: '4430'
            icon: '54402'
            ilvl: '18'
            level: '18'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Coral Ring
            id: '4433'
            icon: '54432'
            ilvl: '19'
            level: '19'
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
          count: 2
  - name: Now Hiring
    level: 19
    rowId: 66168
    questId: SubWil122_00632
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (10.6, 16.6)
      name: Beneger
    steps:
      - location: Eastern Thanalan
        coords: (10.4, 17.7)
        name: Post hiring notices in prime locations.
      - location: Eastern Thanalan
        coords: (10.6, 16.6)
        name: Speak with Beneger.
      - location: Eastern Thanalan
        coords: (10.8, 16.9)
        name: Distribute hiring notices.
      - location: Eastern Thanalan
        coords: (10.6, 16.6)
        name: Report to Beneger.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Steaking Claims
        level: 19
        rowId: 66167
        questId: SubWil121_00631
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
      gil: 215
  - name: Impish Implications
    level: 19
    rowId: 66169
    questId: SubWil123_00633
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (10.6, 16.6)
      name: Lululo
    steps:
      - location: Eastern Thanalan
        coords: (14.1, 17.4)
        name: Slay vandalous imps.
      - location: Eastern Thanalan
        coords: (10.6, 16.6)
        name: Report to Lululo.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
      gil: 210
  - name: There's Mythril in Them Thar Hills
    level: 19
    rowId: 66170
    questId: SubWil124_00634
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (10.6, 16.6)
      name: Beneger
    steps:
      - location: Eastern Thanalan
        coords: (14.7, 16.7)
        name: Obtain slabs of cloud marble.
      - location: Eastern Thanalan
        coords: (10.6, 16.6)
        name: Deliver the cloud marble to Beneger.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Now Hiring
        level: 19
        rowId: 66168
        questId: SubWil122_00632
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
      gil: 210
  - name: Purging the Earth
    level: 19
    rowId: 66171
    questId: SubWil125_00635
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (10.6, 16.6)
      name: Lululo
    steps:
      - location: Eastern Thanalan
        coords: (18.2, 20.3)
        name: Slay earth sprites.
      - location: Eastern Thanalan
        coords: (13.4, 23.7)
        name: Speak with Reremaki.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Impish Implications
        level: 19
        rowId: 66169
        questId: SubWil123_00633
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
      gil: 210
  - name: Forging the Spirit
    level: 19
    rowId: 66174
    questId: SubWil500_00638
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Central Thanalan
      coords: (23.9, 13.7)
      name: Swynbroes
    steps:
      - location: Central Thanalan
        coords: (23.9, 13.7)
        name: Speak with Swynbroes.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
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
          count: 3
  - name: Waking the Spirit
    level: 19
    rowId: 66175
    questId: SubWil501_00639
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Central Thanalan
      coords: (23.5, 13.9)
      name: F'hobhas
    steps:
      - location: Central Thanalan
        coords: (23.5, 13.9)
        name: Speak with F'hobhas.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Forging the Spirit
        level: 19
        rowId: 66174
        questId: SubWil500_00638
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
  - name: Marvelously Mutable Materia
    level: 19
    rowId: 66999
    questId: SubCts814_01463
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Central Thanalan
      coords: (23.8, 14.3)
      name: Kokosamu
    steps:
      - location: Central Thanalan
        coords: (23.8, 13.6)
        name: Speak with Mutamix.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Life, Materia and Everything
        level: 19
        rowId: 65808
        questId: ManFst208_00272
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 50
        paramGrowId: '19'
        avg: 840
      gil: 227
  - name: Hallo Halatali
    level: 19
    rowId: 66233
    questId: SubWil140_00697
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.0, 14.3)
      name: Nedrick Ironheart
    steps:
      - location: Eastern Thanalan
        coords: (14.8, 30.2)
        name: Speak with Fafajoni at Halatali.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Dressed to Deceive
        level: 19
        rowId: 66110
        questId: SubWil129_00574
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '19'
        avg: 1680
      gil: 258
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
  - name: My Little Chocobo (Immortal Flames)
    level: 20
    rowId: 66238
    questId: SubWil160_00702
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (8.4, 8.9)
      name: Swift
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (12.3, 8.3)
        name: Present a Flame Chocobo Issuance to Mimigun.
      - location: Ul'dah - Steps of Nald
        coords: (12.2, 8.4)
        name: Name your chocobo.
      - location: Ul'dah - Steps of Nald
        coords: (12.3, 8.3)
        name: Speak with Mimigun.
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
  - name: Strawman Defense
    level: 24
    rowId: 66285
    questId: GaiUsa407_00749
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (20.1, 20.4)
      name: Claudian
    steps:
      - location: Eastern Thanalan
        coords: (21.4, 20.6)
        name: Set handmade scarecrows at the specified locations.
      - location: Eastern Thanalan
        coords: (20.1, 20.4)
        name: Report to Claudian.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      optional:
        - item:
            name: Iron Scale Greaves
            id: '3804'
            icon: '46869'
            ilvl: '23'
            level: '23'
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
            name: Iron-plated Jackboots
            id: '3802'
            icon: '46833'
            ilvl: '23'
            level: '23'
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
            name: Goatskin Duckbills
            id: '3806'
            icon: '46117'
            ilvl: '24'
            level: '24'
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
  - name: Buzz Off, Birds
    level: 24
    rowId: 66286
    questId: GaiUsa408_00750
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (19.6, 20.2)
      name: Gogoshu
    steps:
      - location: Eastern Thanalan
        coords: (22.2, 19.7)
        name: Slay chasm buzzards.
      - location: Eastern Thanalan
        coords: (19.6, 20.2)
        name: Report to Gogoshu.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      optional:
        - item:
            name: Iron Scale Mail
            id: '3057'
            icon: '43063'
            ilvl: '23'
            level: '23'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '5'
            name: Charcoal Grey
            color: '4736834'
        - item:
            name: Cotton Trapper's Tunic
            id: '3060'
            icon: '42091'
            ilvl: '23'
            level: '23'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '49'
            name: Marsh Green
            color: '3290657'
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
          count: 1
  - name: Hair Club for Hyur
    level: 24
    rowId: 66287
    questId: GaiUsa409_00751
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (20.1, 21.4)
      name: Helmhart
    steps:
      - location: Eastern Thanalan
        coords: (23.4, 22.1)
        name: Slay phurbles to obtain their blood.
      - location: Eastern Thanalan
        coords: (20.1, 21.4)
        name: Deliver the bottles of phurble blood to Helmhart.
      - location: Eastern Thanalan
        coords: (20.1, 21.4)
        name: Apply the hair tonic to Helmhart's head.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      gil: 1399
      optional:
        - item:
            name: Weak Poisoning Potion
            id: '4574'
            icon: '20681'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 2
        - item:
            name: Weak Blinding Potion
            id: '4575'
            icon: '20685'
            ilvl: '20'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 2
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
  - name: Melding Materia Muchly
    level: 25
    rowId: 66176
    questId: SubWil502_00640
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Central Thanalan
      coords: (23.8, 13.6)
      name: Mutamix Bubblypots
    steps:
      - location: Central Thanalan
        coords: (23.9, 13.6)
        name: Meld materia before Mutamix.
      - location: Central Thanalan
        coords: (23.8, 13.6)
        name: Speak with Mutamix.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Waking the Spirit
        level: 19
        rowId: 66175
        questId: SubWil501_00639
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '25'
        avg: 2040
      gil: 5157
  - name: Leves of Little Ala Mhigo
    level: 25
    rowId: 66228
    questId: SubWil152_00692
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Southern Thanalan
      coords: (18.1, 13.5)
      name: Esmond
    steps:
      - location: Southern Thanalan
        coords: (19.7, 12.2)
        name: Complete Esmond's trial guildleve.
      - location: Southern Thanalan
        coords: (18.1, 13.5)
        name: Report to Esmond.
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
        paramGrowId: '25'
        avg: 2040
      gil: 2112
  - name: Scholarly Funds
    level: 24
    rowId: 66289
    questId: GaiUsa501_00753
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (20.1, 20.4)
      name: Claudian
    steps:
      - location: Eastern Thanalan
        coords: (26.3, 16.0)
        name: Deliver the Highbridge report to Kyokyozo.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Strawman Defense
        level: 24
        rowId: 66285
        questId: GaiUsa407_00749
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      gil: 1232
  - name: The Perils of Pilgrimage
    level: 24
    rowId: 66290
    questId: GaiUsa502_00754
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (26.3, 16.0)
      name: Kyokyozo
    steps:
      - location: Eastern Thanalan
        coords: (26.6, 17.7)
        name: Slay axe beaks.
      - location: Eastern Thanalan
        coords: (26.3, 16.0)
        name: Report to Kyokyozo.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Buzz Off, Birds
        level: 24
        rowId: 66286
        questId: GaiUsa408_00750
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      gil: 1232
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
  - name: Friendlier Skies
    level: 24
    rowId: 66291
    questId: GaiUsa503_00755
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (26.3, 16.0)
      name: Kyokyozo
    steps:
      - location: Eastern Thanalan
        coords: (20.2, 21.3)
        name: Deliver the signed petition to Hihibaru.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Perils of Pilgrimage
        level: 24
        rowId: 66290
        questId: GaiUsa502_00754
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '24'
        avg: 1980
      gil: 1232
  - name: Bad Blood
    level: 25
    rowId: 66294
    questId: GaiUsa506_00758
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (17.1, 14.2)
      name: Hihira
    steps:
      - location: Southern Thanalan
        coords: (16.7, 14.0)
        name: Deliver Hihira's medicine to the suffering refugees.
      - location: Southern Thanalan
        coords: (17.1, 14.2)
        name: Report to Hihira.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: On to Little Ala Mhigo
        level: 25
        rowId: 66293
        questId: GaiUsa505_00757
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '25'
        avg: 2040
      gil: 1232
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
  - name: Prickly Patients
    level: 25
    rowId: 66295
    questId: GaiUsa507_00759
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (17.1, 14.2)
      name: Hihira
    steps:
      - location: Southern Thanalan
        coords: (18.2, 12.7)
        name: Speak with Alfan.
      - location: Southern Thanalan
        coords: (15.0, 15.2)
        name: Slay sabotenders and obtain their fruits.
      - location: Southern Thanalan
        coords: (17.1, 14.2)
        name: Deliver the sabotender fruits to Hihira.
      - location: Southern Thanalan
        coords: (16.7, 14.0)
        name: Deliver the cactus tea to the suffering refugees.
      - location: Southern Thanalan
        coords: (17.1, 14.2)
        name: Report to Hihira.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Bad Blood
        level: 25
        rowId: 66294
        questId: GaiUsa506_00758
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '25'
        avg: 2040
      gil: 1232
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
  - name: Blast from the Past
    level: 25
    rowId: 66296
    questId: GaiUsa508_00760
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (18.7, 12.9)
      name: Annabel
    steps:
      - location: Southern Thanalan
        coords: (19.5, 17.4)
        name: Use blessed water and slay a tempered sword.
      - location: Southern Thanalan
        coords: (19.5, 17.4)
        name: Use blessed water and slay a tempered brand.
      - location: Southern Thanalan
        coords: (18.7, 12.9)
        name: Report to Annabel.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '25'
        avg: 2040
      gil: 1232
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
  - name: Corpse Confrontation
    level: 27
    rowId: 66315
    questId: GaiUsa706_00779
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (16.9, 14.3)
      name: Hremfing
    steps:
      - location: Southern Thanalan
        coords: (21.8, 8.1)
        name: Slay Corpse Brigade bandits.
      - location: Southern Thanalan
        coords: (16.9, 14.3)
        name: Report to Hremfing.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Wilred Wants You
        level: 27
        rowId: 66314
        questId: GaiUsa705_00778
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '27'
        avg: 2520
      optional:
        - item:
            name: Goatskin Wristbands
            id: '4106'
            icon: '55640'
            ilvl: '27'
            level: '27'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Horn Necklace
            id: '4317'
            icon: '54831'
            ilvl: '27'
            level: '27'
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
  - name: What's Your Poison
    level: 27
    rowId: 66316
    questId: GaiUsa707_00780
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (17.1, 14.4)
      name: Amelot
    steps:
      - location: Southern Thanalan
        coords: (17.0, 12.2)
        name: Use the leoformic acid and slay a rockskin peiste.
      - location: Southern Thanalan
        coords: (17.1, 14.4)
        name: Deliver the peiste poison to Amelot.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '27'
        avg: 2520
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
            name: Poisoning Potion
            id: '4579'
            icon: '20681'
            ilvl: '35'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Blinding Potion
            id: '4580'
            icon: '20685'
            ilvl: '35'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
        - item:
            name: Silencing Potion
            id: '4581'
            icon: '20684'
            ilvl: '35'
            level: '1'
            category:
              id: '44'
              name: Medicine
              icon: '60136'
          count: 3
  - name: Death from Above
    level: 27
    rowId: 66317
    questId: GaiUsa708_00781
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (17.1, 14.4)
      name: Amelot
    steps:
      - location: Southern Thanalan
        coords: (15.4, 13.6)
        name: Use cactus piss on the peiste carcass and slay insects.
      - location: Southern Thanalan
        coords: (16.8, 16.5)
        name: Use cactus piss on the angler carcass and slay insects.
      - location: Southern Thanalan
        coords: (20.7, 10.2)
        name: Slay potter wasp swarms.
      - location: Southern Thanalan
        coords: (17.1, 14.4)
        name: Report to Amelot.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: What's Your Poison
        level: 27
        rowId: 66316
        questId: GaiUsa707_00780
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '27'
        avg: 2520
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
            name: Fried Egg
            id: '4653'
            icon: '24257'
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
  - name: Gone to Pieces
    level: 30
    rowId: 65688
    questId: SubCts815_00152
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (14.0, 10.0)
      name: Syntgoht
    steps:
      - location: Central Thanalan
        coords: (23.4, 14.4)
        name: Speak with Nesting Heron at the Bonfire.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Life, Materia and Everything
        level: 19
        rowId: 65808
        questId: ManFst208_00272
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 50
        paramGrowId: '30'
        avg: 1560
  - name: Fetch the Freshman
    level: 31
    rowId: 66359
    questId: GaiUsb104_00823
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.4, 29.8)
      name: U'tykha Tia
    steps:
      - location: Southern Thanalan
        coords: (12.4, 33.0)
        name: Render assistance to U'kahzuna.
      - location: Southern Thanalan
        coords: (14.4, 29.8)
        name: Report to U'tykha Tia.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1404
  - name: Survey Says
    level: 31
    rowId: 66360
    questId: GaiUsb105_00824
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.2, 30.0)
      name: U'khuba Tia
    steps:
      - location: Southern Thanalan
        coords: (14.5, 26.8)
        name: Speak with the people of Forgotten Springs.
      - location: Southern Thanalan
        coords: (14.2, 30.0)
        name: Report your findings to U'khuba Tia.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1404
  - name: Tools of Office
    level: 31
    rowId: 66361
    questId: GaiUsb106_00825
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.2, 30.0)
      name: U'khuba Tia
    steps:
      - location: Southern Thanalan
        coords: (13.3, 32.0)
        name: Slay russet yarzons and acquire barbs.
      - location: Southern Thanalan
        coords: (14.2, 30.0)
        name: Give the yarzon barbs to U'khuba Tia.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Survey Says
        level: 31
        rowId: 66360
        questId: GaiUsb105_00824
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1650
  - name: Minority Rapport
    level: 31
    rowId: 66362
    questId: GaiUsb107_00826
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.5, 26.8)
      name: Riridesu
    steps:
      - location: Southern Thanalan
        coords: (19.2, 35.9)
        name: Deliver the bundle of wrapped merchandise to Odinel.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1404
  - name: Heat of the Moment
    level: 31
    rowId: 66363
    questId: GaiUsb108_00827
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (19.2, 35.9)
      name: Mumugoi
    steps:
      - location: Southern Thanalan
        coords: (19.4, 36.1)
        name: Remove the sand dunes and dispatch smoke bombs.
      - location: Southern Thanalan
        coords: (19.2, 35.9)
        name: Speak with Mumugoi.
      - location: Southern Thanalan
        coords: (18.5, 36.5)
        name: Slay smoke bombs.
      - location: Southern Thanalan
        coords: (19.2, 35.9)
        name: Report to Mumugoi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1404
  - name: The Eyes Have It
    level: 31
    rowId: 66364
    questId: GaiUsb109_00828
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (16.0, 30.9)
      name: U'rahtalo
    steps:
      - location: Southern Thanalan
        coords: (16.2, 31.0)
        name: Confront the oglers with a /furious anger.
      - location: Southern Thanalan
        coords: (16.0, 30.9)
        name: Report to U'rahtalo.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Tools of Office
        level: 31
        rowId: 66361
        questId: GaiUsb106_00825
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1404
  - name: Mind Games
    level: 31
    rowId: 66365
    questId: GaiUsb110_00829
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.4, 29.8)
      name: U'tykha Tia
    steps:
      - location: Southern Thanalan
        coords: (26.3, 34.4)
        name: Defeat Amalj'aa in the eastern Sagolii Desert.
      - location: Southern Thanalan
        coords: (27.5, 34.5)
        name: Find U'kahzuna and /psych her up.
      - location: Southern Thanalan
        coords: (14.4, 29.8)
        name: Report to U'tykha Tia.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Fetch the Freshman
        level: 31
        rowId: 66359
        questId: GaiUsb104_00823
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1650
  - name: U Don't Know Me
    level: 31
    rowId: 66366
    questId: GaiUsb111_00830
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.2, 30.0)
      name: U'khuba Tia
    steps:
      - location: Southern Thanalan
        coords: (14.4, 29.8)
        name: 'Speak with U''tykha Tia. '
      - location: Southern Thanalan
        coords: (14.8, 27.0)
        name: Speak with U'kahzuna.
      - location: Southern Thanalan
        coords: (18.5, 30.8)
        name: Use empty sacks on weakened dune anglers.
      - location: Southern Thanalan
        coords: (14.8, 27.0)
        name: Deliver the angler-filled sacks to U'kahzuna.
      - location: Southern Thanalan
        coords: (14.4, 29.8)
        name: Report to U'tykha Tia.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Mind Games
        level: 31
        rowId: 66365
        questId: GaiUsb110_00829
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '31'
        avg: 3200
      gil: 1650
  - name: Braving New Depths
    level: 32
    rowId: 66300
    questId: GaiUsa602_00764
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.0, 14.3)
      name: Nedrick Ironheart
    steps:
      - location: Southern Thanalan
        coords: (25.2, 12.6)
        name: Speak with Bibimu at the Sunken Temple of Qarn.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - name: the Sunken Temple of Qarn
        type: dungeon
        levelRequired: 35
        levelSync: 37
        ilevelRequired: 0
        ilevelSync: 0
    rewards:
      xp:
        factor: 100
        paramGrowId: '32'
        avg: 3485
      gil: 1518
  - name: Plagued by Indecision
    level: 35
    rowId: 66409
    questId: GaiUsb504_00873
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.2, 21.3)
      name: Iliud
    steps:
      - location: Central Thanalan
        coords: (25.0, 15.1)
        name: Show Zazawaka the sticks of vilekin repellent.
      - location: Central Thanalan
        coords: (25.5, 15.2)
        name: Sprinkle the repellent at the destinations.
      - location: Central Thanalan
        coords: (25.0, 15.1)
        name: Speak with Zazawaka.
      - location: Eastern Thanalan
        coords: (11.2, 21.3)
        name: Return to the church and report to Iliud.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: All Good Things
        level: 34
        rowId: 66053
        questId: ManFst313_00517
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '35'
        avg: 3960
      gil: 1518
  - name: The Voyage of the Goobbue
    level: 35
    rowId: 66410
    questId: GaiUsb505_00874
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.5, 21.4)
      name: Barryn
    steps:
      - location: Eastern Thanalan
        coords: (19.8, 24.5)
        name: Investigate the spot and slay the foes.
      - location: Eastern Thanalan
        coords: (11.5, 21.4)
        name: Report to Barryn.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: All Good Things
        level: 34
        rowId: 66053
        questId: ManFst313_00517
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '35'
        avg: 3960
      gil: 1518
  - name: Scent of Cinnamon
    level: 35
    rowId: 66411
    questId: GaiUsb506_00875
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.5, 21.4)
      name: Barryn
    steps:
      - location: Eastern Thanalan
        coords: (11.1, 21.3)
        name: Collect a sack of gil from Esmour.
      - location: Eastern Thanalan
        coords: (12.5, 23.1)
        name: Collect a sack of gil from Zozoru.
      - location: Eastern Thanalan
        coords: (13.1, 23.4)
        name: Give the collected gil to Ermegarde at Camp Drybone.
      - location: Eastern Thanalan
        coords: (11.2, 21.3)
        name: Give the cinnamon cookies to Iliud.
      - location: Eastern Thanalan
        coords: (11.5, 21.4)
        name: Report to Barryn.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Voyage of the Goobbue
        level: 35
        rowId: 66410
        questId: GaiUsb505_00874
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '35'
        avg: 3960
      gil: 1518
  - name: Mr. Slipshod and Ms. Uptight
    level: 35
    rowId: 66415
    questId: GaiUsb510_00879
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.2, 21.9)
      name: Fuandrec
    steps:
      - location: Eastern Thanalan
        coords: (12.3, 27.7)
        name: Find a slipshod wayfarer.
      - location: Eastern Thanalan
        coords: (11.2, 21.9)
        name: Report to Fuandrec.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: All Good Things
        level: 34
        rowId: 66053
        questId: ManFst313_00517
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '35'
        avg: 3960
      gil: 1518
  - name: Out of Whole Cloth
    level: 35
    rowId: 66416
    questId: GaiUsb511_00880
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (11.4, 21.5)
      name: Dedeju
    steps:
      - location: Central Thanalan
        coords: (21.4, 18.4)
        name: Collect a square of tattered linen from a scrupulous shopkeep at Black
          Brush Station.
      - location: Eastern Thanalan
        coords: (11.4, 21.5)
        name: Give the linen to Dedeju.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: All Good Things
        level: 34
        rowId: 66053
        questId: ManFst313_00517
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '35'
        avg: 3960
      gil: 1518
  - name: Hold for Customer Support
    level: 38
    rowId: 66455
    questId: GaiUsb810_00919
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (14.0, 10.0)
      name: Syntgoht
    steps:
      - location: Northern Thanalan
        coords: (20.9, 31.1)
        name: Speak with Papawazu at Camp Bluefog.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Where's My Juice
        level: 38
        rowId: 66454
        questId: GaiUsb809_00918
        genre: Coerthan Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '38'
        avg: 4700
      optional:
        - item:
            name: Amethyst Bracelet
            id: '4141'
            icon: '55622'
            ilvl: '38'
            level: '38'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Peridot Bracelet
            id: '4137'
            icon: '55619'
            ilvl: '38'
            level: '38'
            category:
              id: '42'
              name: Bracelets
              icon: '60134'
          count: 1
        - item:
            name: Goshenite Bracelet
            id: '4135'
            icon: '55621'
            ilvl: '38'
            level: '38'
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
  - name: Thieves and Robbers
    level: 38
    rowId: 66456
    questId: GaiUsb811_00920
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (20.9, 31.1)
      name: Papawazu
    steps:
      - location: Northern Thanalan
        coords: (20.6, 30.0)
        name: Question the spirited porter with much /doubt.
      - location: Northern Thanalan
        coords: (20.6, 29.8)
        name: Investigate the processed ceruleum.
      - location: Northern Thanalan
        coords: (20.6, 30.0)
        name: Speak with the porter.
      - location: Northern Thanalan
        coords: (20.9, 31.1)
        name: Report to Papawazu.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Hold for Customer Support
        level: 38
        rowId: 66455
        questId: GaiUsb810_00919
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '38'
        avg: 4700
      optional:
        - item:
            name: Amethyst Choker
            id: '4347'
            icon: '54820'
            ilvl: '38'
            level: '38'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Peridot Choker
            id: '4343'
            icon: '54817'
            ilvl: '38'
            level: '38'
            category:
              id: '40'
              name: Necklace
              icon: '60132'
          count: 1
        - item:
            name: Goshenite Choker
            id: '4341'
            icon: '54819'
            ilvl: '38'
            level: '38'
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
          count: 1
  - name: Dishonor Before Death
    level: 35
    rowId: 66457
    questId: GaiUsb812_00921
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (14.0, 10.1)
      name: Sibold
    steps:
      - location: Central Thanalan
        coords: (15.9, 14.1)
        name: Place the lilies on the burial mound at Cutter's Cry.
      - location: Central Thanalan
        coords: (15.8, 14.0)
        name: Speak with Norman.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - name: Cutter's Cry
        type: dungeon
        levelRequired: 38
        levelSync: 40
        ilevelRequired: 0
        ilevelSync: 0
    rewards:
      xp:
        factor: 100
        paramGrowId: '35'
        avg: 3960
      gil: 4352
      optional:
        - item:
            name: Altered Mythril Elmo
            id: '27656'
            icon: '40341'
            ilvl: '38'
            level: '38'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Altered Boarskin Pot Helm
            id: '27641'
            icon: '40351'
            ilvl: '37'
            level: '37'
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
            name: Mythril Circlet (Rubellite)
            id: '2790'
            icon: '40606'
            ilvl: '38'
            level: '38'
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
          count: 8
  - name: The Ceruleum Must Flow
    level: 38
    rowId: 66458
    questId: GaiUsb813_00922
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (20.9, 31.1)
      name: Papawazu
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (14.0, 10.0)
        name: Speak with Syntgoht at the Sapphire Avenue Exchange.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Thieves and Robbers
        level: 38
        rowId: 66456
        questId: GaiUsb811_00920
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '38'
        avg: 4700
      gil: 1500
  - name: A Tale of Three Cities
    level: 38
    rowId: 66459
    questId: GaiUsb814_00923
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Thal
      coords: (14.0, 10.0)
      name: Syntgoht
    steps:
      - location: Coerthas Central Highlands
        coords: (26.8, 16.4)
        name: Deliver the cherry brandewine to Edwyn.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Ceruleum Must Flow
        level: 38
        rowId: 66458
        questId: GaiUsb813_00922
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '38'
        avg: 4700
      gil: 1500
  - name: Leves of Camp Bluefog
    level: 40
    rowId: 65551
    questId: SubWil153_00015
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Northern Thanalan
      coords: (22.1, 29.4)
      name: Rurubana
    steps:
      - location: Northern Thanalan
        coords: (21.6, 26.9)
        name: Complete Rurubana's trial guildleve.
      - location: Northern Thanalan
        coords: (22.1, 29.4)
        name: Report to Rurubana.
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
        paramGrowId: '40'
        avg: 5390
      gil: 1958
  - name: Tresses in Distress
    level: 41
    rowId: 66493
    questId: GaiUsc106_00957
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (20.1, 21.4)
      name: Helmhart
    steps:
      - location: Eastern Thanalan
        coords: (29.2, 24.6)
        name: Slay golden fleeces and obtain snurble blood.
      - location: Eastern Thanalan
        coords: (20.1, 21.4)
        name: Give the blood to Helmhart.
      - location: Eastern Thanalan
        coords: (20.1, 21.4)
        name: Apply the snurble tonic to Helmhart's head.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Hair Club for Hyur
        level: 24
        rowId: 66287
        questId: GaiUsa409_00751
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '41'
        avg: 5500
      gil: 1993
  - name: D Is for Dead
    level: 41
    rowId: 66494
    questId: GaiUsc107_00958
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Eastern Thanalan
      coords: (28.0, 22.2)
      name: Floating Stone
    steps:
      - location: Eastern Thanalan
        coords: (28.2, 26.1)
        name: Slay quartz doblyns and obtain clear quartz.
      - location: Eastern Thanalan
        coords: (28.0, 22.2)
        name: Deliver the clear quartz to Floating Stone.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 100
        paramGrowId: '41'
        avg: 5500
      gil: 1993
  - name: Primal Fear
    level: 46
    rowId: 66543
    questId: GaiUsc607_01007
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: The Waking Sands
      coords: (6.0, 4.9)
      name: Urianger
    steps:
      - location: Seat of the First Bow
        coords: (3.5, 3.4)
        name: Speak with Lewin at the Seat of the First Bow.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Black Wolf's Ultimatum
        level: 46
        rowId: 66058
        questId: ManFst408_00522
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '46'
        avg: 6325
      gil: 1694
  - name: Going for Gold
    level: 44
    rowId: 66550
    questId: GaiUsc702_01014
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.0, 14.3)
      name: Nedrick Ironheart
    steps:
      - location: Coerthas Central Highlands
        coords: (14.4, 35.3)
        name: Speak with Willielmus at the Aurum Vale.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - name: the Aurum Vale
        type: dungeon
        levelRequired: 47
        levelSync: 49
        ilevelRequired: 0
        ilevelSync: 0
    rewards:
      xp:
        factor: 100
        paramGrowId: '44'
        avg: 5830
      gil: 5126
      optional:
        - item:
            name: Electrum Ring
            id: '4497'
            icon: '54404'
            ilvl: '47'
            level: '47'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Red Coral Necklace
            id: '4363'
            icon: '54832'
            ilvl: '47'
            level: '47'
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
          count: 1
  - name: A Kobold Initiative
    level: 47
    rowId: 66551
    questId: GaiUsc703_01015
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: The Waking Sands
      coords: (6.1, 5.8)
      name: Slafswys
    steps:
      - location: Outer La Noscea
        coords: (18.6, 17.2)
        name: Speak with Bloeidin at Camp Overlook.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Black Wolf's Ultimatum
        level: 46
        rowId: 66058
        questId: ManFst408_00522
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
  - name: What's It to U
    level: 47
    rowId: 66557
    questId: GaiUsc709_01021
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.3, 29.9)
      name: U'odh Nunh
    steps:
      - location: Southern Thanalan
        coords: (15.8, 28.9)
        name: Speak with the U tribeswomen.
      - location: Southern Thanalan
        coords: (14.3, 29.9)
        name: Report to U'odh Nunh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Can't Do It without U
        level: 47
        rowId: 66552
        questId: GaiUsc704_01016
        genre: ''
        icon: '71020'
      - name: Can't Do It without U
        level: 47
        rowId: 67089
        questId: GaiUsx704_01553
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      optional:
        - item:
            name: Altered Cobalt Elmo
            id: '27659'
            icon: '40342'
            ilvl: '46'
            level: '46'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
          stain:
            id: '6'
            name: Soot Black
            color: '2828579'
        - item:
            name: Raptorskin Pot Helm
            id: '2862'
            icon: '40049'
            ilvl: '47'
            level: '47'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Felt Hat
            id: '2852'
            icon: '41030'
            ilvl: '46'
            level: '46'
            category:
              id: '34'
              name: Head
              icon: '60124'
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
  - name: Zombies Are People Too
    level: 47
    rowId: 66558
    questId: GaiUsc710_01022
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (24.8, 40.9)
      name: Hab
    steps:
      - location: Central Shroud
        coords: (17.9, 22.4)
        name: Seek out Sabotendrick in the Central Shroud.
      - location: Southern Thanalan
        coords: (24.8, 40.9)
        name: Report to Hab.
      - location: Outer La Noscea
        coords: (15.8, 10.0)
        name: Seek out Sabotendred in outer La Noscea.
      - location: Southern Thanalan
        coords: (24.8, 40.9)
        name: Report to Hab.
      - location: Southern Thanalan
        coords: (17.9, 24.3)
        name: Blow up the odd pot with firesand.
      - location: Southern Thanalan
        coords: (17.6, 24.0)
        name: Speak to Sabotendale.
      - location: Southern Thanalan
        coords: (24.8, 40.9)
        name: Report to Hab.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Can't Do It without U
        level: 47
        rowId: 66552
        questId: GaiUsc704_01016
        genre: ''
        icon: '71020'
      - name: Can't Do It without U
        level: 47
        rowId: 67089
        questId: GaiUsx704_01553
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      items:
        - item:
            name: Cactuar Cutting
            id: '6194'
            icon: '59429'
            ilvl: '1'
            level: '1'
            category:
              id: '81'
              name: Minion
              icon: '60155'
          count: 1
  - name: U! Ow! That Stings
    level: 47
    rowId: 66559
    questId: GaiUsc711_01023
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.3, 29.9)
      name: U'odh Nunh
    steps:
      - location: Southern Thanalan
        coords: (17.8, 24.5)
        name: Use the battle ointment on the U tribeswomen.
      - location: Southern Thanalan
        coords: (14.3, 29.9)
        name: Report to U'odh Nunh.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: What's It to U
        level: 47
        rowId: 66557
        questId: GaiUsc709_01021
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      optional:
        - item:
            name: Tortoiseshell Scale Mail
            id: '3183'
            icon: '43084'
            ilvl: '46'
            level: '46'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
        - item:
            name: Raptorskin Harness
            id: '3191'
            icon: '43081'
            ilvl: '47'
            level: '47'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
        - item:
            name: Altered Woolen Cowl
            id: '27677'
            icon: '43906'
            ilvl: '47'
            level: '47'
            category:
              id: '35'
              name: Body
              icon: '60126'
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
  - name: True U
    level: 47
    rowId: 66560
    questId: GaiUsc712_01024
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (14.3, 29.9)
      name: U'odh Nunh
    steps:
      - location: Southern Thanalan
        coords: (14.6, 29.9)
        name: Speak with the U tribeswomen.
      - location: Southern Thanalan
        coords: (14.3, 29.9)
        name: Speak with U'odh Nunh.
      - location: The Waking Sands
        coords: (6.3, 5.0)
        name: Report to Wigstan at the Waking Sands.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: U! Ow! That Stings
        level: 47
        rowId: 66559
        questId: GaiUsc711_01023
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
      gil: 1716
  - name: Can't Do It without U
    level: 47
    rowId: 67089
    questId: GaiUsx704_01553
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: The Waking Sands
      coords: (6.3, 5.0)
      name: Wigstan
    steps:
      - location: Southern Thanalan
        coords: (14.3, 29.9)
        name: Speak with U'odh Nunh at Forgotten Springs.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Black Wolf's Ultimatum
        level: 46
        rowId: 66058
        questId: ManFst408_00522
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '47'
        avg: 6440
  - name: Into the Valley of the Skull
    level: 48
    rowId: 66561
    questId: GaiUsc801_01025
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: The Waking Sands
      coords: (6.1, 5.5)
      name: Radolf
    steps:
      - location: Western La Noscea
        coords: (22.8, 22.7)
        name: Speak with Falkbryda at Camp Skull Valley.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Black Wolf's Ultimatum
        level: 46
        rowId: 66058
        questId: ManFst408_00522
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '48'
        avg: 6840
      gil: 1857
  - name: High Standards
    level: 49
    rowId: 66574
    questId: GaiUsc903_01038
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (22.2, 29.9)
      name: Rafold
    steps:
      - location: Northern Thanalan
        coords: (21.2, 27.5)
        name: Stand watch at  and defeat enemies.
      - location: Northern Thanalan
        coords: (22.2, 29.9)
        name: Report to Rafold.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Operation Archon
        level: 49
        rowId: 70057
        questId: XxcUsc901_04521
        genre: Seventh Umbral Era
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '49'
        avg: 6960
      optional:
        - item:
            name: Cobalt Mask
            id: '27660'
            icon: '40350'
            ilvl: '49'
            level: '49'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Woolen Bandana
            id: '27648'
            icon: '41775'
            ilvl: '49'
            level: '49'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Altered Felt Hat
            id: '27678'
            icon: '41468'
            ilvl: '49'
            level: '49'
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
          count: 6
  - name: Crate Expectations
    level: 49
    rowId: 66576
    questId: GaiUsc905_01040
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (22.6, 29.9)
      name: Spiraling Path
    steps:
      - location: Northern Thanalan
        coords: (22.4, 26.1)
        name: Deliver the Immortal Flames scimitars to Dodoroba.
      - location: Northern Thanalan
        coords: (22.6, 29.9)
        name: Report to Spiraling Path.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Ladle in the Darkness
        level: 49
        rowId: 66575
        questId: GaiUsc904_01039
        genre: ''
        icon: '71000'
    rewards:
      xp:
        factor: 100
        paramGrowId: '49'
        avg: 6960
      gil: 1879
      optional:
        - item:
            name: Altered Cobalt Gauntlets
            id: '27662'
            icon: '48799'
            ilvl: '49'
            level: '49'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
        - item:
            name: Raptorskin Gloves
            id: '27650'
            icon: '44736'
            ilvl: '49'
            level: '49'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
        - item:
            name: Felt Gloves
            id: '27680'
            icon: '44737'
            ilvl: '49'
            level: '49'
            category:
              id: '37'
              name: Hands
              icon: '60129'
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
          count: 8
  - name: Jumping on a Grenade
    level: 49
    rowId: 66577
    questId: GaiUsc906_01041
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (22.2, 29.9)
      name: Rafold
    steps:
      - location: Northern Thanalan
        coords: (24.2, 21.9)
        name: Lurk at the specified location and slay a grenade for its claw.
      - location: Northern Thanalan
        coords: (21.9, 21.1)
        name: Deliver the grenade claw to Memezofu.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: High Standards
        level: 49
        rowId: 66574
        questId: GaiUsc903_01038
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '49'
        avg: 6960
      optional:
        - item:
            name: Altered Cobalt Sabatons
            id: '27664'
            icon: '47210'
            ilvl: '49'
            level: '49'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
        - item:
            name: Raptorskin Boots
            id: '27652'
            icon: '47209'
            ilvl: '49'
            level: '49'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
        - item:
            name: Raptorskin Crakows
            id: '27682'
            icon: '49076'
            ilvl: '49'
            level: '49'
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
          count: 8
  - name: The Life of the Party
    level: 49
    rowId: 66580
    questId: GaiUsc909_01044
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (21.9, 21.1)
      name: Memezofu
    steps:
      - location: Northern Thanalan
        coords: (17.9, 20.0)
        name: Administer potion cocktails to the wounded.
      - location: Northern Thanalan
        coords: (21.9, 21.1)
        name: Report to Memezofu.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: Jumping on a Grenade
        level: 49
        rowId: 66577
        questId: GaiUsc906_01041
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '49'
        avg: 6960
      optional:
        - item:
            name: Woolen Trousers of Fending
            id: '27663'
            icon: '47612'
            ilvl: '49'
            level: '49'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
        - item:
            name: Raptorskin Skirt
            id: '27651'
            icon: '47611'
            ilvl: '49'
            level: '49'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
        - item:
            name: Felt Breeches
            id: '27681'
            icon: '47613'
            ilvl: '49'
            level: '49'
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
          count: 8
  - name: An Eye for Elixirs
    level: 49
    rowId: 66581
    questId: GaiUsc910_01045
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Northern Thanalan
      coords: (21.9, 21.1)
      name: Memezofu
    steps:
      - location: Northern Thanalan
        coords: (24.9, 21.2)
        name: Slay ahrimans and obtain their corneas.
      - location: Northern Thanalan
        coords: (21.9, 21.1)
        name: Deliver the ahriman corneas to Memezofu.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: The Life of the Party
        level: 49
        rowId: 66580
        questId: GaiUsc909_01044
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 100
        paramGrowId: '49'
        avg: 6960
      gil: 372
  - name: The Weaponsmith of Legend
    level: 50
    rowId: 66241
    questId: SubWil142_00705
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.0, 14.3)
      name: Nedrick Ironheart
    steps:
      - location: Mor Dhona
        coords: (22.0, 4.9)
        name: Speak with Rowena at Revenant's Toll.
      - location: North Shroud
        coords: (30.3, 20.2)
        name: Show the promise of payment to Gerolt.
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
      gil: 1659
  - name: Trauma Queen
    level: 47
    rowId: 66406
    questId: GaiUsb501_00870
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (11.5, 13.9)
      name: Allene
    steps:
      - location: Upper La Noscea
        coords: (25.6, 23.0)
        name: Speak with Abazi Charazi.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 0
        paramGrowId: '47'
        avg: 0
      gil: 5368
      optional:
        - item:
            name: Amber Ring
            id: '4508'
            icon: '54424'
            ilvl: '49'
            level: '49'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Rubellite Ring
            id: '4502'
            icon: '54421'
            ilvl: '49'
            level: '49'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Tourmaline Ring
            id: '4506'
            icon: '54423'
            ilvl: '49'
            level: '49'
            category:
              id: '43'
              name: Ring
              icon: '60135'
          count: 1
        - item:
            name: Black Pearl Ring
            id: '4514'
            icon: '54429'
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
  - name: Ghosts of Amdapor
    level: 50
    rowId: 66671
    questId: SubFst900_01135
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Western Thanalan
      coords: (12.0, 14.3)
      name: Nedrick Ironheart
    steps:
      - location: South Shroud
        coords: (24.7, 25.0)
        name: Speak with Maxinne at Amdapor Keep.
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - name: Amdapor Keep
        type: dungeon
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 45
        ilevelSync: 110
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
      gil: 5368
  - name: Corpse Groom
    level: 50
    rowId: 67060
    questId: SubCts105_01524
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (12.3, 8.1)
      name: Paiyo Reiyo
    steps:
      - location: Eastern Thanalan
        coords: (13.3, 22.2)
        name: Examine Liavinne's grave at the Church of Saint Adama Landama.
      - location: Central Shroud
        coords: (19.2, 28.2)
        name: "Speak with Huguemont at the Tam\u2013Tara Deepcroft."
      - location: The Tam-Tara Deepcroft
        coords: (6.8, 7.5)
        name: "Enter the Tam\u2013Tara Deepcroft (Hard)."
      - location: Central Shroud
        coords: (19.6, 27.9)
        name: "Speak with Paiyo Reiyo at the Tam\u2013Tara Deepcroft."
    expansion:
      id: '0'
      name: A Realm Reborn
    unlocks:
      - name: "the Tam\u2013Tara Deepcroft (Hard)"
        type: dungeon
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 70
        ilevelSync: 110
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
      gil: 2064
  - name: For Wilred
    level: 70
    rowId: 68422
    questId: StmBdz992_02886
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (16.9, 14.4)
      name: Gundobald
    steps:
      - location: Southern Thanalan
        coords: (19.4, 13.9)
        name: Present Wilred's sword to Bertliana.
      - location: Southern Thanalan
        coords: (16.9, 14.4)
        name: Speak with Gundobald.
      - location: Southern Thanalan
        coords: (19.8, 14.4)
        name: Speak with those who wish to return to Ala Mhigo.
      - location: Southern Thanalan
        coords: (16.9, 14.4)
        name: Report to Gundobald.
    expansion:
      id: '2'
      name: Stormblood
    requires:
      - name: Stormblood
        level: 70
        rowId: 68089
        questId: StmBda706_02553
        genre: Stormblood
        icon: '71000'
      - name: Dreaming of Home
        level: 70
        rowId: 68421
        questId: StmBdz991_02885
        genre: Rhalgr's Reach Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 0
        paramGrowId: '70'
        avg: 0
      gil: 1500
  - name: Journey's Beginning
    level: 70
    rowId: 68423
    questId: StmBdz993_02887
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: Southern Thanalan
      coords: (16.9, 14.5)
      name: Bertliana
    steps:
      - location: The Fringes
        coords: (7.9, 11.3)
        name: Speak with Bertliana near Castrum Oriens.
      - location: The Fringes
        coords: (32.6, 28.5)
        name: Find Bertliana and slay any enemies that appear.
      - location: The Fringes
        coords: (32.8, 28.6)
        name: Speak with Bertliana.
      - location: The Peaks
        coords: (28.1, 29.4)
        name: Speak with Bertliana in Radiata.
    expansion:
      id: '2'
      name: Stormblood
    requires:
      - name: Stormblood
        level: 70
        rowId: 68089
        questId: StmBda706_02553
        genre: Stormblood
        icon: '71000'
      - name: For Wilred
        level: 70
        rowId: 68422
        questId: StmBdz992_02886
        genre: Ul'dahn Sidequests
        icon: '71020'
    rewards:
      xp:
        factor: 0
        paramGrowId: '70'
        avg: 0
      gil: 1500
  - name: Passion for Fashion
    level: 15
    rowId: 68617
    questId: SubCts691_03081
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: The Gold Saucer
      coords: (4.8, 6.1)
      name: Lewena
    steps:
      - location: The Gold Saucer
        coords: (7.2, 7.4)
        name: Speak with Masked Rose.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: It Could Happen to You
        level: 15
        rowId: 65970
        questId: SubGsc001_00434
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      gil: 104
  - name: Every Little Thing She Does Is Mahjong
    level: 15
    rowId: 68737
    questId: SubGsc107_03201
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71140'
    issuer:
      location: The Gold Saucer
      coords: (4.8, 6.1)
      name: Lewena
    steps:
      - location: The Gold Saucer
        coords: (7.2, 7.7)
        name: Speak with the mahjong tutor.
    expansion:
      id: '0'
      name: A Realm Reborn
    requires:
      - name: It Could Happen to You
        level: 15
        rowId: 65970
        questId: SubGsc001_00434
        genre: Ul'dahn Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '15'
        avg: 1440
      gil: 210
  - name: The Adventurer with All the Cards
    level: 1
    rowId: 69617
    questId: SubGsc109_04081
    genre:
      id: '114'
      name: Ul'dahn Sidequests
    icon: '71020'
    issuer:
      location: The Gold Saucer
      coords: (5.0, 6.7)
      name: Gold Saucer attendant
    steps:
      - location: The Gold Saucer
        coords: (4.5, 6.9)
        name: Wait by the entrance to Card Square.
    expansion:
      id: '0'
      name: A Realm Reborn
    rewards:
      xp:
        factor: 0
        paramGrowId: '1'
        avg: 0
      items:
        - item:
            name: Magicked Card
            id: '33689'
            icon: '27672'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
genre:
  genreId: '114'
  name: Ul'dahn Sidequests


---