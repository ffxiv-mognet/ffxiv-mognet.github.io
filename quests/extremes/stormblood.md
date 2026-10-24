---
layout: quests-with-shops-mounts
title: Stormblood Extreme Trials
permalink: /quests/extremes/stormblood
links:
  previous: /quests/trials/four-lords
brandLabel: Mognet
brandUrl: /quests
nonsequential: true
quests:
  - name: Songs in the Key of Kugane
    level: 1
    rowId: 68479
    questId: StmBdy201_02943
    icon: '71140'
    issuer:
      location: Kugane
      coords: (11.6, 12.6)
      name: wandering minstrel
    steps: []
    expansion:
      id: '2'
      name: Stormblood
    requires:
      - name: Stormblood
        link: /quests/msq/stormblood/part2
        level: 70
        rowId: 68089
        questId: StmBda706_02553
        genre: Stormblood
        icon: '71000'
    unlocks:
      - name: The Pool of Tribute (Extreme)
        type: trial
      - name: Emanation (Extreme)
        type: trial
      - name: "The Minstrel's Ballad: Shinryu's Domain"
        type: trial
      - name: The Jade Stoa (Extreme)
        type: trial
      - name: "The Minstrel's Ballad: Tsukuyomi's Pain"
        type: trial
      - name: "Hells' Kier (Extreme)"
        type: trial
      - name: The Wreath of Snakes (Extreme)
        type: trial
    partQuestNo: 1
  - name: A Lone Wolf No More
    level: 1
    rowId: 68736
    questId: SubCts825_03200
    genre:
      id: '128'
      name: Kugane Sidequests
    icon: '71020'
    issuer:
      location: Kugane
      coords: (11.6, 9.9)
      name: news hawker
    steps:
      - location: Yanxia
        coords: (30.6, 20.2)
        name: Speak with the mysterious client in Namai.
      - location: Yanxia
        coords: (25.1, 21.3)
        name: Play the Fife of Nine Tails at the specified location.
    expansion:
      id: '2'
      name: Stormblood
    unlocks:
      - id: 2161
        name: Flute of the Plume
        type: achievement
    requires:
      - name: Blissful Kamuy
      - name: Reveling Kamuy
      - name: Legendary Kamuy
      - name: Auspicious Kamuy
      - name: Lunar Kamuy
      - name: Euphonious Kamuy
      - name: Hallowed Kamuy
    rewards:
      xp:
        factor: 0
        paramGrowId: '1'
        avg: 0
      gil: 552
      items:
        - item:
            name: Fabled Kamuy Fife
            id: '24625'
            icon: '26039'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
    partQuestNo: 2

  - name: The Newer King on the Block
    level: 70
    rowId: 67091
    questId: StmBdy992_01555
    genre:
      id: '252'
      name: Collaboration Quests
    icon: '71140'
    issuer:
      location: Kugane
      coords: (9.7, 8.9)
      name: hearty hunter
    steps:
      - location: Kugane
        coords: (9.7, 8.9)
        name: Speak with the hearty hunter.
    expansion:
      id: '2'
      name: Stormblood
    unlocks:
      - name: the Great Hunt (Extreme)
        type: trial
        levelRequired: 70
        levelSync: 70
        ilevelRequired: 350
        ilevelSync: 0
    requires:
      - name: The New King on the Block
        level: 70
        rowId: 67090
        questId: StmBdy991_01554
        genre: Collaboration Quests
        icon: '71140'
    partQuestNo: 2



shops:
  shops:
    shops:
  shops:
    - id: '1769872'
      name: ''
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Rathalos Helm [M]
                id: '23384'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '4'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Mail [M]
                id: '23385'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '8'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Vambraces [M]
                id: '23386'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '4'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Coil [M]
                id: '23387'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '8'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Greaves [M]
                id: '23388'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '4'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Helm [F]
                id: '23389'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '4'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Mail [F]
                id: '23390'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '8'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Vambraces [F]
                id: '23391'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '4'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Coil [F]
                id: '23392'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '8'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Rathalos Greaves [F]
                id: '23393'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '4'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Cornerstone of the New World - Astera Orchestrion Roll
                id: '22603'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '10'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 110
        - items:
            - quantity: '1'
              item:
                name: Savage of the Ancient Forest Orchestrion Roll
                id: '22604'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '10'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 110
        - items:
            - quantity: '1'
              item:
                name: Indoor BBQ Spit
                id: '22571'
                category:
                  id: '78'
                  name: Tabletop
                  icon: '60163'
          costs:
            - quantity: '10'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 110
        - items:
            - quantity: '1'
              item:
                name: BBQ Spit
                id: '22583'
                category:
                  id: '76'
                  name: Outdoor Furnishing
                  icon: '60168'
          costs:
            - quantity: '10'
              currency:
                id: '22599'
                name: Rathalos Scale
                plural: Rathalos scales
                icon: '22217'
          order: 110
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Helm [M]
                id: '22606'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '1'
              currency:
                id: '23384'
                name: Rathalos Helm [M]
                plural: Rathalos helms [M]
                icon: '40804'
            - quantity: '2'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Mail [M]
                id: '22607'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '1'
              currency:
                id: '23385'
                name: Rathalos Mail [M]
                plural: suits of Rathalos mail [M]
                icon: '43408'
            - quantity: '4'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Vambraces [M]
                id: '22608'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '1'
              currency:
                id: '23386'
                name: Rathalos Vambraces [M]
                plural: pairs of Rathalos vambraces [M]
                icon: '48715'
            - quantity: '2'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Coil [M]
                id: '22609'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '1'
              currency:
                id: '23387'
                name: Rathalos Coil [M]
                plural: Rathalos coils [M]
                icon: '47415'
            - quantity: '4'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Greaves [M]
                id: '22610'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '1'
              currency:
                id: '23388'
                name: Rathalos Greaves [M]
                plural: pairs of Rathalos greaves [M]
                icon: '47145'
            - quantity: '2'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Helm [F]
                id: '22611'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '1'
              currency:
                id: '23389'
                name: Rathalos Helm [F]
                plural: Rathalos helms [F]
                icon: '40804'
            - quantity: '2'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Mail [F]
                id: '22612'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '1'
              currency:
                id: '23390'
                name: Rathalos Mail [F]
                plural: suits of Rathalos mail [F]
                icon: '43407'
            - quantity: '4'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Vambraces [F]
                id: '22613'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '1'
              currency:
                id: '23391'
                name: Rathalos Vambraces [F]
                plural: pairs of Rathalos vambraces [F]
                icon: '48715'
            - quantity: '2'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Coil [F]
                id: '22614'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '1'
              currency:
                id: '23392'
                name: Rathalos Coil [F]
                plural: Rathalos coils [F]
                icon: '47414'
            - quantity: '4'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Augmented Rathalos Greaves [F]
                id: '22615'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '1'
              currency:
                id: '23393'
                name: Rathalos Greaves [F]
                plural: pairs of Rathalos greaves [F]
                icon: '47145'
            - quantity: '2'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: 'Proof of a Hero - Monster Hunter: World Version Orchestrion
                  Roll'
                id: '22605'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '5'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 130
        - items:
            - quantity: '1'
              item:
                name: Poogie
                id: '22602'
                category:
                  id: '81'
                  name: Minion
                  icon: '60155'
          costs:
            - quantity: '5'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 130
        - items:
            - quantity: '1'
              item:
                name: Rathalos Whistle
                id: '22600'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '50'
              currency:
                id: '23383'
                name: Rathalos Scale+
                plural: Rathalos scales+
                icon: '22218'
          order: 130
      npcs:
        - name: smithy
          location: Kugane
          coords: (9.7, 8.9)
    - id: '1769807'
      name: Wondrous Sundries
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Blissful Kamuy Fife
                id: '20549'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '19110'
                name: Bliss Totem
                plural: Bliss totems
                icon: '26511'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Reveling Kamuy Fife
                id: '20550'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '19109'
                name: Revel Totem
                plural: Revel totems
                icon: '26510'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Legendary Kamuy Fife
                id: '21047'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '21196'
                name: Shinryu Totem
                plural: Shinryu totems
                icon: '26521'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Auspicious Kamuy Fife
                id: '21903'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '21773'
                name: Byakko Totem
                plural: Byakko totems
                icon: '26529'
          order: 120
          questId: '68551'
          quest:
            name: An Auspicious Encounter
            link: /quests/trials/four-lords
            level: 70
            rowId: 68551
            questId: StmBdy301_03015
            genre: The Four Lords
            icon: '71140'
        - items:
            - quantity: '1'
              item:
                name: Lunar Kamuy Fife
                id: '23020'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '23043'
                name: Lunar Totem
                plural: lunar totems
                icon: '26533'
          order: 120
          questId: '68610'
          quest:
            name: The Primary Agreement
            link: /quests/msq/stormblood/part3
            level: 70
            rowId: 68610
            questId: StmBdd105_03074
            genre: Post-Ala Mhigan Liberation
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Euphonious Kamuy Fife
                id: '23984'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '23962'
                name: Suzaku Totem
                plural: Suzaku totems
                icon: '26541'
          order: 120
          questId: '68688'
          quest:
            name: The Fire-bird Down Below
            link: /quests/trials/four-lords
            level: 70
            rowId: 68688
            questId: StmBdy321_03152
            genre: The Four Lords
            icon: '71140'
        - items:
            - quantity: '1'
              item:
                name: Hallowed Kamuy Fife
                id: '24623'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '24797'
                name: Seiryu Totem
                plural: Seiryu totems
                icon: '26545'
          order: 120
          questId: '68701'
          quest:
            name: Surpassing the Samurai
            link: /quests/trials/four-lords
            level: 70
            rowId: 68701
            questId: StmBdy331_03165
            genre: The Four Lords
            icon: '71140'
      npcs:
        - name: Eschina
          location: Rhalgr's Reach
          coords: (13.9, 11.8)
  categories:
    - id: '34'
      name: Head
      icon: '60124'
    - id: '35'
      name: Body
      icon: '60126'
    - id: '37'
      name: Hands
      icon: '60129'
    - id: '36'
      name: Legs
      icon: '60128'
    - id: '38'
      name: Feet
      icon: '60130'
    - id: '94'
      name: Orchestrion Roll
      icon: '60173'
    - id: '78'
      name: Tabletop
      icon: '60163'
    - id: '76'
      name: Outdoor Furnishing
      icon: '60168'
    - id: '81'
      name: Minion
      icon: '60155'
    - id: '63'
      name: Other
      icon: '60159'
  currencies:
    - id: '19110'
      name: Bliss Totem
      plural: Bliss totems
      icon: '26511'
    - id: '19109'
      name: Revel Totem
      plural: Revel totems
      icon: '26510'
    - id: '21196'
      name: Shinryu Totem
      plural: Shinryu totems
      icon: '26521'
    - id: '21773'
      name: Byakko Totem
      plural: Byakko totems
      icon: '26529'
    - id: '23043'
      name: Lunar Totem
      plural: lunar totems
      icon: '26533'
    - id: '23962'
      name: Suzaku Totem
      plural: Suzaku totems
      icon: '26541'
    - id: '24797'
      name: Seiryu Totem
      plural: Seiryu totems
      icon: '26545'
    - id: '22599'
      name: Rathalos Scale
      plural: Rathalos scales
      icon: '22217'
    - id: '23384'
      name: Rathalos Helm [M]
      plural: Rathalos helms [M]
      icon: '40804'
    - id: '23383'
      name: Rathalos Scale+
      plural: Rathalos scales+
      icon: '22218'
    - id: '23385'
      name: Rathalos Mail [M]
      plural: suits of Rathalos mail [M]
      icon: '43408'
    - id: '23386'
      name: Rathalos Vambraces [M]
      plural: pairs of Rathalos vambraces [M]
      icon: '48715'
    - id: '23387'
      name: Rathalos Coil [M]
      plural: Rathalos coils [M]
      icon: '47415'
    - id: '23388'
      name: Rathalos Greaves [M]
      plural: pairs of Rathalos greaves [M]
      icon: '47145'
    - id: '23389'
      name: Rathalos Helm [F]
      plural: Rathalos helms [F]
      icon: '40804'
    - id: '23390'
      name: Rathalos Mail [F]
      plural: suits of Rathalos mail [F]
      icon: '43407'
    - id: '23391'
      name: Rathalos Vambraces [F]
      plural: pairs of Rathalos vambraces [F]
      icon: '48715'
    - id: '23392'
      name: Rathalos Coil [F]
      plural: Rathalos coils [F]
      icon: '47414'
    - id: '23393'
      name: Rathalos Greaves [F]
      plural: pairs of Rathalos greaves [F]
      icon: '47145'



totems:
  - totem:
      id: '19110'
      name: Bliss Totem
      plural: Bliss totems
      icon: '26511'
    trial:
      name: Emanation (Extreme)
    item:
      name: Blissful Kamuy Fife
      id: '20549'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '19109'
      name: Revel Totem
      plural: Revel totems
      icon: '26510'
    trial:
      name: The Pool of Tribute (Extreme)
    item:
      name: Reveling Kamuy Fife
      id: '20550'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '21196'
      name: Shinryu Totem
      plural: Shinryu totems
      icon: '26521'
    trial:
      name: "The Minstrel's Ballad: Shinryu's Domain"
    item:
      name: Legendary Kamuy Fife
      id: '21047'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '21773'
      name: Byakko Totem
      plural: Byakko totems
      icon: '26529'
    trial:
      name: The Jade Stoa (Extreme)
    item:
      name: Auspicious Kamuy Fife
      id: '21903'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '23043'
      name: Lunar Totem
      plural: lunar totems
      icon: '26533'
    trial:
      name: "The Minstrel's Ballad: Tsukuyomi's Pain"
    item:
      name: Lunar Kamuy Fife
      id: '23020'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '23962'
      name: Suzaku Totem
      plural: Suzaku totems
      icon: '26541'
    trial:
      name: Hells' Kier (Extreme)
    item:
      name: Euphonious Kamuy Fife
      id: '23984'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '24797'
      name: Seiryu Totem
      plural: Seiryu totems
      icon: '26545'
    trial:
      name: The Wreath of Snakes (Extreme)
    item:
      name: Hallowed Kamuy Fife
      id: '24623'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '23383'
      name: Rathalos Scale+
      plural: Rathalos scales+
      icon: '22218'
    trial:
      name: The Great Hunt (Extreme)
    item:
      name: Rathalos Whistle
      id: '22600'
      category:
        id: '63'
        name: Other
        icon: '60159'



---
