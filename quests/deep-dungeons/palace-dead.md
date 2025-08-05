---
layout: quest-table
title: Palace of the Dead Deep Dungeon
permalink: /quests/deep-dungeons/palace-dead
quests:
  - name: The House That Death Built
    level: 17
    rowId: 67092
    questId: SubCts701_01556
    genre: Palace of the Dead
    icon: '71140'
    issuer:
      location: New Gridania
      coords: (12.1, 13.1)
      name: Nojiro Marujiro
    steps:
      - location: South Shroud
        coords: (17.5, 22.1)
        name: Speak with the Wood Wailer expeditionary at Issom-Har in the South Shroud.
      - location: South Shroud
        coords: (25.2, 20.7)
        name: Speak with the Wood Wailer expeditionary captain at Quarrymill.
    unlocks:
      - name: Palace of the Dead
        type: deep-dungeon
    requires:
      - name: Into a Copper Hell
        level: 17
        rowId: 66196
        questId: ManFst205_00660
        genre: Seventh Umbral Era
        icon: '71000'
        link: /quests/msq/realm-reborn/part2
    partQuestNo: 1
  - name: The Nightmare's End
    level: 50
    rowId: 67093
    questId: SubCts702_01557
    genre: Palace of the Dead
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (25.0, 20.6)
      name: Balan
    steps:
      - location: South Shroud
        coords: (18.0, 20.0)
        name: Search for the drunken Lalafell at Buscarron's Druthers.
      - location: South Shroud
        coords: (19.0, 20.3)
        name: Speak with Paiyo Reiyo.
      - location: South Shroud
        coords: (19.4, 20.7)
        name: Retrieve Avere's ring from the rusted gauntlets.
      - location: South Shroud
        coords: (19.2, 20.1)
        name: Show Avere's ring to Paiyo Reiyo.
      - location: Middle La Noscea
        coords: (16.5, 18.1)
        name: Speak with Paiyo Reiyo at Summerford.
    unlocks:
      - id: 1575
        name: I'll Sleep When I'm Dead
        type: achievement
    requires:
      - name: Corpse Groom
        level: 50
        rowId: 67060
        questId: SubCts105_01524
        genre: Ul'dahn Sidequests
        icon: '71140'
        link: /quests/dungeons/realm-reborn
      - name: Palace of the Dead Floor 50
        type: deepdungeon
    partQuestNo: 2
  - name: What Lies Beneath
    level: 17
    rowId: 67923
    questId: SubCts711_02387
    genre: ''
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (25.2, 20.7)
      name: Wood Wailer expeditionary captain
    steps:
      - name: Speak with Wood Wailer Expeditionary Captain
        location: South Shroud
        coords: (25.2, 20.7)
    unlocks:
      - name: Palace of the Dead Floors 51-100
        type: deepdungeon
    partQuestNo: 3
  - name: Dead but Not Gone
    level: 60
    rowId: 67924
    questId: SubCts712_02388
    genre: Palace of the Dead
    icon: '71140'
    issuer:
      location: South Shroud
      coords: (25.0, 20.5)
      name: Wood Wailer expeditionary
    steps:
      - location: South Shroud
        coords: (17.5, 22.0)
        name: Speak with the expeditionary.
    unlocks:
      - id: 1680
        name: Dead Tired
        type: achievement
    partQuestNo: 4
    requires:
      - name: Palace of the Dead Floor 100
        type: deepdungeon

---