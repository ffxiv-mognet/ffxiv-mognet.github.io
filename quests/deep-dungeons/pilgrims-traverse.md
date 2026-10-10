---
layout: quest-table
title: Pilgrim's Traverse Deep Dungeon
permalink: /quests/deep-dungeons/pilgrims-traverse
quests:
  - name: Pilgrimage of Light
    level: 91
    rowId: 70941
    questId: KinGdd101_05405
    genre:
      id: '106'
      name: Pilgrim's Traverse
    icon: '71140'
    issuer:
      location: The Crystarium
      coords: (10.3, 10.7)
      name: bright-eyed child
    steps:
      - location: The Crystarium
        coords: (8.9, 8.3)
        name: Search for Fuath.
      - location: Il Mheg
        coords: (29.6, 7.4)
        name: Speak with Aenc Daen in Wolekdorf.
      - location: Il Mheg
        coords: (32.3, 4.0)
        name: Speak with Ose Wyd.
      - location: Il Mheg
        coords: (29.8, 5.9)
        name: Speak with Aenc Daen.
      - location: Il Mheg
        coords: (29.9, 6.0)
        name: Speak with Vanthau.
    requires:
      - name: Floor 50 - Palace of the Dead
        link: /quests/deep-dungeons/palace-dead
        icon: deep-dungeon
      - name: Endwalker
        link: /quests/msq/endwalker/part2
        level: 90
        rowId: 70000
        questId: AktKmg115_04464
        genre: Endwalker
        icon: '71000'
    unlocks:
      - name: Pilgrim's Traverse
        type: deep-dungeon
    partQuestNo: 1
  - name: Faerie Tale
    level: 91
    rowId: 70942
    questId: KinGdd102_05406
    genre:
      id: '106'
      name: Pilgrim's Traverse
    icon: '71140'
    issuer:
      location: Il Mheg
      coords: (29.8, 5.8)
      name: Aenc Daen
    steps:
      - location: Il Mheg
        coords: (29.8, 5.8)
        name: Speak with Aenc Daen.
    requires:
        - name: Floor 30 - Pilgrim's Traverse
          icon: deep-dungeon
    partQuestNo: 2
  - name: A Branch and Their Sapling
    level: 91
    rowId: 70943
    questId: KinGdd103_05407
    genre:
      id: '106'
      name: Pilgrim's Traverse
    icon: '71140'
    issuer:
      location: Il Mheg
      coords: (29.8, 5.8)
      name: Aenc Daen
    steps:
      - location: Il Mheg
        coords: (32.3, 4.0)
        name: Wait at the designated location.
      - location: Il Mheg
        coords: (29.8, 5.8)
        name: Speak with Aenc Daen.
    unlocks:
        - name: The Final Verse (Quantum)
          type: deep-dungeon
    requires:
        - name: Floor 100 - Pilgrim's Traverse
          icon: deep-dungeon
    partQuestNo: 3
genre:
  genreId: '106'
  name: Pilgrim's Traverse


---
