---
layout: quests-with-shops-mounts
title: Shadowbringers Extreme Trials
permalink: /quests/extremes/shadowbringers
links:
  previous: /quests/trials/sorrow-werlyt
nonsequential: true
quests:
  - name: Minstrel from Another Mother
    level: 1
    rowId: 69198
    questId: LucKyb006_03662
    genre:
      id: '0'
      name: ''
    icon: '71140'
    issuer:
      location: The Crystarium
      coords: (7.5, 12.5)
      name: minstreling wanderer
    steps: []
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: Shadowbringers
        link: /quests/msq/shadowbringers/part2
        level: 80
        rowId: 69190
        questId: LucKmf111_03654
        genre: Shadowbringers
        icon: '71000'
    unlocks:
      - name: The Dancing Plague (Extreme)
        type: trial
      - name: The Crown of the Immaculate (Extreme)
        type: trial
      - name: "The Minstrel's Ballad: Hades's Elegy"
        type: trial
      - name: "The Seat of Sacrifice (Extreme)"
        type: trial
    partQuestNo: 1
  - name: Weapon of Choice
    level: 80
    rowId: 69378
    questId: LucKyb007_03842
    icon: '71140'
    issuer:
      location: The Lochs
      coords: (11.5, 22.5)
      name: warmachina fanatic
    steps: []
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: Ruby Doomsday
        link: /quests/trials/sorrow-werlyt
        level: 80
        rowId: 69319
        questId: LucKyw101_03783
        genre: Garlemald's Machinations
        icon: '71140'
    unlocks:
      - name: Cinder Drift (Extreme)
        type: trial
    partQuestNo: 2
  - name: Weapon of Choice
    level: 80
    rowId: 69378
    questId: LucKyb007_03842
    icon: '71140'
    issuer:
      location: The Lochs
      coords: (11.5, 22.5)
      name: warmachina fanatic
    steps: []
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: Blood of Emerald
        link: /quests/trials/sorrow-werlyt
        level: 80
        rowId: 69516
        questId: LucKyw301_03980
        genre: Garlemald's Machinations
        icon: '71140'
    unlocks:
      - name: Castrum Marinum (Extreme)
        type: trial
    partQuestNo: 2
  - name: Weapon of Choice
    level: 80
    rowId: 69378
    questId: LucKyb007_03842
    icon: '71140'
    issuer:
      location: The Lochs
      coords: (11.5, 22.5)
      name: warmachina fanatic
    steps: []
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: Forever at Your Side
        link: /quests/trials/sorrow-werlyt
        level: 80
        rowId: 69568
        questId: LucKyw402_04032
        genre: "Garlemald's Machinations"
        icon: '71140'
    unlocks:
      - name: The Cloud Deck (Extreme)
        type: trial
    partQuestNo: 3

shops:
  shops:
    - id: '1770015'
      name: Glorious Gewgaws
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Fae Gwiber Trumpet
                id: '26778'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '27391'
                name: King Totem
                plural: King totems
                icon: '26555'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Innocent Gwiber Trumpet
                id: '26783'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '27392'
                name: Immaculate Totem
                plural: Immaculate totems
                icon: '26556'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Shadow Gwiber Trumpet
                id: '28121'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '28708'
                name: Hades Totem
                plural: Hades totems
                icon: '26587'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Gwiber of Light Trumpet
                id: '30863'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '30596'
                name: Totem of Light
                plural: totems of Light
                icon: '26606'
          order: 120
          questId: '69314'
          quest:
            name: Hope's Confluence
            link: /quests/msq/shadowbringers/part3
            level: 80
            rowId: 69314
            questId: LucKmi108_03778
            genre: The Voyage Home
            icon: '71000'
      npcs:
        - name: Fathard
          location: Eulmore
          coords: (10.1, 11.7)
    - id: '1770312'
      name: Bombastic Bric-a-brac
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Ruby Gwiber Trumpet
                id: '30105'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '29001'
                name: Ruby Totem
                plural: Ruby totems
                icon: '26601'
          order: 100
          questId: 69319
          quest:
            name: Ruby Doomsday
            link: /quests/trials/sorrow-werlyt
            level: 80
            rowId: 69319
            questId: LucKyw101_03783
            genre: Garlemald's Machinations
            icon: '71140'
        - items:
            - quantity: '1'
              item:
                name: G-Warrior Card
                id: '33338'
                category:
                  id: '86'
                  name: Triple Triad Card
                  icon: '60156'
          costs:
            - quantity: '1'
              currency:
                id: '29001'
                name: Ruby Totem
                plural: Ruby totems
                icon: '26601'
            - quantity: '1'
              currency:
                id: '32132'
                name: Emerald Totem
                plural: Emerald totems
                icon: '26611'
            - quantity: '1'
              currency:
                id: '33480'
                name: Diamond Totem
                plural: Diamond totems
                icon: '26614'
          order: 110
          questId: '69568'
          quest:
            name: Forever at Your Side
            link: /quests/trials/sorrow-werlyt
            level: 80
            rowId: 69568
            questId: LucKyw402_04032
            genre: Garlemald's Machinations
            icon: '71140'
        - items:
            - quantity: '1'
              item:
                name: Emerald Gwiber Trumpet
                id: '32843'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '32132'
                name: Emerald Totem
                plural: Emerald totems
                icon: '26611'
          order: 100
          questId: '69516'
          quest:
            name: Blood of Emerald
            link: /quests/trials/sorrow-werlyt
            level: 80
            rowId: 69516
            questId: LucKyw301_03980
            genre: Garlemald's Machinations
            icon: '71140'
        - items:
            - quantity: '1'
              item:
                name: Diamond Gwiber Trumpet
                id: '33685'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '33480'
                name: Diamond Totem
                plural: Diamond totems
                icon: '26614'
          order: 100
          questId: '69567'
          quest:
            name: Duty in the Sky with Diamond
            link: /quests/trials/sorrow-werlyt
            level: 80
            rowId: 69567
            questId: LucKyw401_04031
            genre: Garlemald's Machinations
            icon: '71140'
      npcs:
        - name: C'intana
          location: Mor Dhona
          coords: (22.8, 6.6)
  categories:
    - id: '63'
      name: Other
      icon: '60159'
    - id: '86'
      name: Triple Triad Card
      icon: '60156'
  currencies:
    - id: '27391'
      name: King Totem
      plural: King totems
      icon: '26555'
    - id: '27392'
      name: Immaculate Totem
      plural: Immaculate totems
      icon: '26556'
    - id: '28708'
      name: Hades Totem
      plural: Hades totems
      icon: '26587'
    - id: '30596'
      name: Totem of Light
      plural: totems of Light
      icon: '26606'
    - id: '29001'
      name: Ruby Totem
      plural: Ruby totems
      icon: '26601'
    - id: '32132'
      name: Emerald Totem
      plural: Emerald totems
      icon: '26611'
    - id: '33480'
      name: Diamond Totem
      plural: Diamond totems
      icon: '26614'

totems:
  - totem:
      id: '27391'
      name: King Totem
      plural: King totems
      icon: '26555'
    trial:
      name: The Dancing Plague (Extreme)
    item:
        name: Fae Gwiber Trumpet
        id: '26778'
        category:
          id: '63'
          name: Other
          icon: '60159'
  - totem:
      id: '27392'
      name: Immaculate Totem
      plural: Immaculate totems
      icon: '26556'
    trial:
      name: The Crown of the Immaculate (Extreme)
    item:
        name: Innocent Gwiber Trumpet
        id: '26783'
        category:
          id: '63'
          name: Other
          icon: '60159'
  - totem:
      id: '28708'
      name: Hades Totem
      plural: Hades totems
      icon: '26587'
    trial:
      name: "The Minstrel's Ballad: Hades's Elegy"
    item:
      name: Shadow Gwiber Trumpet
      id: '28121'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '30596'
      name: Totem of Light
      plural: totems of Light
      icon: '26606'
    trial:
      name: The Seat of Sacrifice (Extreme)
    item:
      name: Gwiber of Light Trumpet
      id: '30863'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '29001'
      name: Ruby Totem
      plural: Ruby totems
      icon: '26601'
    trial:
      name: Cinder Drift (Extreme)
    item:
      name: Ruby Gwiber Trumpet
      id: '30105'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '32132'
      name: Emerald Totem
      plural: Emerald totems
      icon: '26611'
    trial:
      name: Castrum Marinum (Extreme)
    item:
      name: Emerald Gwiber Trumpet
      id: '32843'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '33480'
      name: Diamond Totem
      plural: Diamond totems
      icon: '26614'
    trial:
      name: The Cloud Deck (Extreme)
    item:
      name: Diamond Gwiber Trumpet
      id: '33685'
      category:
        id: '63'
        name: Other
        icon: '60159'

---