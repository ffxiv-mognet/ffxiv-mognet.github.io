---
layout: quests-with-shops-mounts
title: Stormblood Extreme Trials
permalink: /quests/extremes/stormblood
links:
  previous: /quests/trials/four-lords
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

shops:
  shops:
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
---
