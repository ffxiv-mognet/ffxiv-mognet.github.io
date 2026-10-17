---
layout: quests-with-shops
title: Mount Rokkon Variant Dungeon
permalink: /quests/variant/mount-rokkon
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
  - name: Mononoke Aware
    level: 90
    rowId: 70269
    questId: AktKva201_04733
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.0, 13.4)
      name: Shallow Moor
    steps:
      - location: Kugane
        coords: (9.4, 7.7)
        name: Wait for Hancock by the Bokairo Inn.
      - location: Kugane
        coords: (8.9, 8.8)
        name: Speak with Tsubaki.
      - location: Kugane
        coords: (8.9, 8.8)
        name: Enter Mount Rokkon.
      - location: Kugane
        coords: (8.9, 8.8)
        name: Speak with Tsubaki.
      - location: Old Sharlayan
        coords: (12.0, 13.4)
        name: Speak with Shallow Moor.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - name: Mount Rokkon
        type: variant-dungeon
        levelRequired: 90
        levelSync: 90
        ilevelRequired: 605
        ilevelSync: 665
    partQuestNo: 2
  - name: Of Price and Ruin
    level: 90
    rowId: 70270
    questId: AktKva210_04734
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71020'
    issuer:
      location: Kugane
      coords: (8.9, 8.8)
      name: Tsubaki
    steps:
      - location: Kugane
        coords: (11.9, 14.3)
        name: Wait at the specified location.
      - location: Kugane
        coords: (8.9, 8.8)
        name: Speak with Tsubaki.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - id: 3336
        name: A Tale of Two Orphans
        type: achievement
    partQuestNo: 3
shops:
  shops:
    - id: '1770663'
      name: Rokkon Potsherd Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Modern Aesthetics - Ambitious Ends
                id: '40601'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '6'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Ballroom Etiquette - Scrupulous Citations
                id: '40363'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Shishu Bujin Eboshi
                id: '40441'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Shishu Bujin Hitatare
                id: '40442'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '18'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Shishu Bujin Kiribakama
                id: '40443'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Shishu Obutozori
                id: '40444'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 90
        - items:
            - quantity: '1'
              item:
                name: Shishu Gozen Kanzashi
                id: '40445'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 95
        - items:
            - quantity: '1'
              item:
                name: Shishu Gozen Kochiki
                id: '40446'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '18'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 95
        - items:
            - quantity: '1'
              item:
                name: Shishu Gozen Hakama
                id: '40447'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 95
        - items:
            - quantity: '1'
              item:
                name: The Faces We Wear - Rose-colored Spectacles
                id: '44262'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '3'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Looping in the Deepest Fringes Orchestrion Roll
                id: '40713'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '9'
              currency:
                id: '39884'
                name: Rokkon Potsherd
                plural: Rokkon potsherds
                icon: '26641'
          order: 100
      requires:
        name: Mononoke Aware
        level: 90
        rowId: 70269
        questId: AktKva201_04733
        genre: Variant Dungeons
        icon: '71140'
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
    - id: '1770664'
      name: Shishu Coin Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Shishioji Flute
                id: '40388'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '100'
              currency:
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Mount Rokkon Framer's Kit
                id: '40509'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '8'
              currency:
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Crimson Rise Orchestrion Roll
                id: '40707'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '8'
              currency:
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
                id: '39885'
                name: Shishu Coin
                plural: Shishu coins
                icon: '65102'
          order: 110
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
  currencies:
    - id: '39884'
      name: Rokkon Potsherd
      plural: Rokkon potsherds
      icon: '26641'
    - id: '39885'
      name: Shishu Coin
      plural: Shishu coins
      icon: '65102'


---