---
layout: quests-with-shops
title: Aloalo Island Variant Dungeon
permalink: /quests/variant/aloalo-island
quests:
  - name: An Odd Job
    level: 90
    rowId: 70187
    questId: AktKva001_04651
    genre:
      id: '0'
      name: ''
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.0, 13.3)
      name: Osmon
    steps: []
    expansion:
      id: '4'
      name: Endwalker
    requires:
      - name: Endwalker
        link: /quests/msq/endwalker/part2
        level: 90
        rowId: 70000
        questId: AktKmg115_04464
        genre: Endwalker
        icon: '71000'
    partQuestNo: 1
  - name: Stranger from Paradise
    level: 90
    rowId: 70325
    questId: AktKva301_04789
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.0, 13.4)
      name: Shallow Moor
    steps:
      - location: Thavnair
        coords: (10.4, 23.8)
        name: Speak with Pasasun at the Great Work.
      - location: Thavnair
        coords: (24.6, 37.1)
        name: Speak with Pasasun at Yedlihmad.
      - location: Thavnair
        coords: (24.7, 37.1)
        name: Enter Aloalo Island.
      - location: Thavnair
        coords: (24.6, 37.1)
        name: Speak with Pasasun.
      - location: Old Sharlayan
        coords: (12.0, 13.4)
        name: Speak with Shallow Moor at Old Sharlayan.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - name: Aloalo Island
        type: variant-dungeon
        levelRequired: 90
        levelSync: 90
        ilevelRequired: 605
        ilevelSync: 665
    requires:
      - name: A Satrap's Duty
        level: 90
        rowId: 70071
        questId: AktKmh110_04535
        genre: Newfound Adventure
        icon: '71000'
    partQuestNo: 2
  - name: A Fish a Day
    level: 90
    rowId: 70326
    questId: AktKva310_04790
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71020'
    issuer:
      location: Thavnair
      coords: (24.6, 37.1)
      name: Kalika
    steps:
      - location: Thavnair
        coords: (28.9, 16.5)
        name: Wait at the designated location.
      - location: Thavnair
        coords: (24.6, 37.1)
        name: Speak with Kalika.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - id: 3346
        name: Aloalo's Greatest Gift
        type: achievement
    partQuestNo: 3
shops:
  shops:
    - id: '1770725'
      name: Aloalo Potsherd Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Ballroom Etiquette - Humble Triumph
                id: '41462'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '9'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Free Spirit's Hat
                id: '41587'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '15'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Free Spirit's Jacket
                id: '41588'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '27'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Free Spirit's Ringbands
                id: '41589'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '9'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Free Spirit's Cropped Slops
                id: '41590'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '12'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Free Spirit's Backless Loafers
                id: '41591'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '9'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Statice's Wings
                id: '41466'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '3'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: O Speaker, Slumber Orchestrion Roll
                id: '41662'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '9'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Modern Aesthetics - The Bold and the Braid
                id: '41465'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '6'
              currency:
                id: '41078'
                name: Aloalo Potsherd
                plural: Aloalo potsherds
                icon: '26648'
          order: 100
      requires:
        name: Stranger from Paradise
        level: 90
        rowId: 70325
        questId: AktKva301_04789
        genre: Variant Dungeons
        icon: '71140'
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
    - id: '1770726'
      name: Aloalo Coin Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Quaqua Horn
                id: '41499'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '100'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Aloalo Island Framer's Kit
                id: '41376'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '8'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: O Hunter, Rejoice Orchestrion Roll
                id: '41663'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '8'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Piety Materia IX
                id: '33917'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Heavens' Eye Materia IX
                id: '33918'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Aim Materia IX
                id: '33919'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Might Materia IX
                id: '33920'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Battledance Materia IX
                id: '33921'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quickarm Materia IX
                id: '33928'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quicktongue Materia IX
                id: '33929'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '2'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Piety Materia X
                id: '33930'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Heavens' Eye Materia X
                id: '33931'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Aim Materia X
                id: '33932'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Might Materia X
                id: '33933'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Battledance Materia X
                id: '33934'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quickarm Materia X
                id: '33941'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quicktongue Materia X
                id: '33942'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '4'
              currency:
                id: '41079'
                name: Aloalo Coin
                plural: Aloalo coins
                icon: '65105'
          order: 100
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
    - id: '1770727'
      name: Aloalo Manuscript Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Forgotten Figure
                id: '41431'
                category:
                  id: '78'
                  name: Tabletop
                  icon: '60163'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Elevated Ester
                id: '41699'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 2
        - items:
            - quantity: '1'
              item:
                name: Piety Materia X
                id: '33930'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Heavens' Eye Materia X
                id: '33931'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Aim Materia X
                id: '33932'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Might Materia X
                id: '33933'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Battledance Materia X
                id: '33934'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quickarm Materia X
                id: '33941'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quicktongue Materia X
                id: '33942'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '41080'
                name: Aloalo Manuscript
                plural: Aloalo manuscripts
                icon: '26456'
          order: 100
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
  categories:
    - id: '61'
      name: Miscellany
      icon: '60153'
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
    - id: '63'
      name: Other
      icon: '60159'
    - id: '58'
      name: Materia
      icon: '60150'
    - id: '78'
      name: Tabletop
      icon: '60163'
  currencies:
    - id: '41078'
      name: Aloalo Potsherd
      plural: Aloalo potsherds
      icon: '26648'
    - id: '41079'
      name: Aloalo Coin
      plural: Aloalo coins
      icon: '65105'
    - id: '41080'
      name: Aloalo Manuscript
      plural: Aloalo manuscripts
      icon: '26456'


---