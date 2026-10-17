---
layout: quests-with-shops
title: Sil'dihn Subterrane Variant Dungeon
permalink: /quests/variant/sildihn-subterrane
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
  - name: A Key to the Past
    level: 90
    rowId: 70182
    questId: AktKva101_04646
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.0, 13.4)
      name: Shallow Moor
    steps:
      - location: Ul'dah - Steps of Nald
        coords: (12.7, 8.4)
        name: Meet with Kokoshu in Ul'dah.
      - location: Central Thanalan
        coords: (16.8, 23.7)
        name: Speak with the Sil'dihn Subterrane foreman at the Sil'dih excavation
          site.
      - location: Central Thanalan
        coords: (16.8, 23.7)
        name: Enter the Sil'dihn Subterrane.
      - location: Central Thanalan
        coords: (16.8, 23.7)
        name: Speak with the Sil'dihn Subterrane foreman.
      - location: Ul'dah - Steps of Nald
        coords: (12.5, 8.3)
        name: Speak with Kokoshu in Ul'dah.
      - location: Old Sharlayan
        coords: (12.0, 13.4)
        name: Speak with Shallow Moor in Old Sharlayan.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - name: the Sil'dihn Subterrane
        type: variant-dungeon
        levelRequired: 90
        levelSync: 90
        ilevelRequired: 575
        ilevelSync: 635
    partQuestNo: 2
  - name: For Coin, Country, and Comrades
    level: 90
    rowId: 70185
    questId: AktKva110_04649
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71020'
    issuer:
      location: Ul'dah - Steps of Nald
      coords: (12.5, 8.3)
      name: Kokoshu
    steps:
      - location: Ul'dah - Steps of Thal
        coords: (10.8, 11.6)
        name: Speak with Kokoshu on the Hustings Strip.
      - location: Ul'dah - Steps of Thal
        coords: (10.8, 11.6)
        name: Speak with Kokoshu again.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - id: 3152
        name: Sultana's Favor
        type: achievement
    partQuestNo: 3
shops:
  shops:
    - id: '1770621'
      name: Sil'dihn Potsherd Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Ballroom Etiquette - Ample Appreciation
                id: '38570'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '9'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Noir Hat
                id: '38223'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '15'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Noir Longcoat
                id: '38224'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '27'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Noir Leather Gloves
                id: '38225'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '9'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Noir Slacks
                id: '38226'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '12'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Noir Shoes
                id: '38227'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '9'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Sil'dihn Earring
                id: '38559'
                category:
                  id: '41'
                  name: Earrings
                  icon: '60133'
          costs:
            - quantity: '3'
              currency:
                id: '38533'
                name: Sil'dihn Potsherd
                plural: Sil'dihn potsherds
                icon: '26631'
          order: 100
      requires:
        name: A Key to the Past
        level: 90
        rowId: 70182
        questId: AktKva101_04646
        genre: Variant Dungeons
        icon: '71140'
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
    - id: '1770622'
      name: Sil'dihn Silver Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Sil'dihn Throne
                id: '38461'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '100'
              currency:
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Desert Sun Orchestrion Roll
                id: '38632'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '8'
              currency:
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
          order: 1
        - items:
            - quantity: '1'
              item:
                name: Sil'dih Survey Framer's Kit
                id: '38465'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '8'
              currency:
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
                id: '38534'
                name: Sil'dihn Silver
                plural: Sil'dihn silvers
                icon: '65098'
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
    - id: '41'
      name: Earrings
      icon: '60133'
    - id: '63'
      name: Other
      icon: '60159'
    - id: '94'
      name: Orchestrion Roll
      icon: '60173'
    - id: '58'
      name: Materia
      icon: '60150'
  currencies:
    - id: '38533'
      name: Sil'dihn Potsherd
      plural: Sil'dihn potsherds
      icon: '26631'
    - id: '38534'
      name: Sil'dihn Silver
      plural: Sil'dihn silvers
      icon: '65098'




---
