---
layout: quests-with-shops
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
        - name: Stone 30 - Pilgrim's Traverse
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
        - name: Stone 100 - Pilgrim's Traverse
          icon: deep-dungeon
    partQuestNo: 3
genre:
  genreId: '106'
  name: Pilgrim's Traverse

shops:
  shops:
    - id: '1770968'
      name: ''
      inventory:
        - items:
            - quantity: '20'
              item:
                name: Pilgrim's Potion
                id: '47102'
                category:
                  id: '44'
                  name: Medicine
                  icon: '60136'
          costs:
            - quantity: '1'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 60
        - items:
            - quantity: '1'
              item:
                name: Piety Materia XI
                id: '41757'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Heavens' Eye Materia XI
                id: '41758'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Aim Materia XI
                id: '41759'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Might Materia XI
                id: '41760'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Battledance Materia XI
                id: '41761'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quickarm Materia XI
                id: '41768'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quicktongue Materia XI
                id: '41769'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '3'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Piety Materia XII
                id: '41770'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Heavens' Eye Materia XII
                id: '41771'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Aim Materia XII
                id: '41772'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Might Materia XII
                id: '41773'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Battledance Materia XII
                id: '41774'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quickarm Materia XII
                id: '41781'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quicktongue Materia XII
                id: '41782'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '6'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Pilgrim's Traverse Framer's Kit
                id: '46769'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '10'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 40
          achievement:
            id: '3809'
            name: Pilgrim's Progress III
            description: Clear the area marked by stone 30 of Pilgrim's Traverse.
        - items:
            - quantity: '1'
              item:
                name: Ballroom Etiquette - The Ceremony of Tea
                id: '46793'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '50'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 50
        - items:
            - quantity: '1'
              item:
                name: Fuath Plumed Hat
                id: '47207'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '10'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Fuath Swallowtail
                id: '47208'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '10'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Fuath Dress Gloves
                id: '47209'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '10'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Fuath Pantaloons
                id: '47210'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '10'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Fuath Dress Shoes
                id: '47211'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '10'
              currency:
                id: '46186'
                name: Illumed Aetherpool Glass
                plural: fragments of illumed aetherpool glass
                icon: '26683'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Blue Pixie Parasol
                id: '46847'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '30'
              currency:
                id: '46263'
                name: First Light Relic
                plural: First Light relics
                icon: '21282'
          order: 20
        - items:
            - quantity: '1'
              item:
                name: Pilgrim's Protector Horn
                id: '47334'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '46263'
                name: First Light Relic
                plural: First Light relics
                icon: '21282'
          order: 10
        - items:
            - quantity: '1'
              item:
                name: Forgiven Mimicry Resonator
                id: '46831'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '46263'
                name: First Light Relic
                plural: First Light relics
                icon: '21282'
          order: 10
        - items:
            - quantity: '1'
              item:
                name: Modern Aesthetics - Simple and Clean
                id: '46798'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '99'
              currency:
                id: '47342'
                name: Luminous Oil
                plural: phials of luminous oil
                icon: '22654'
          order: 30
        - items:
            - quantity: '1'
              item:
                name: Sin Beaver
                id: '46245'
                category:
                  id: '81'
                  name: Minion
                  icon: '60155'
          costs:
            - quantity: '25'
              currency:
                id: '47342'
                name: Luminous Oil
                plural: phials of luminous oil
                icon: '22654'
          order: 35
      npcs:
        - name: Ose Wyd
          location: Il Mheg
          coords: (29.9, 5.9)
    - id: '1770969'
      name: ''
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Earrings of the First Light
                id: '47297'
                category:
                  id: '41'
                  name: Earrings
                  icon: '60133'
          costs:
            - quantity: '2'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 100
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
        - items:
            - quantity: '1'
              item:
                name: Necklace of the First Light
                id: '47298'
                category:
                  id: '40'
                  name: Necklace
                  icon: '60132'
          costs:
            - quantity: '2'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 100
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
        - items:
            - quantity: '1'
              item:
                name: Bangles of the First Light
                id: '47299'
                category:
                  id: '42'
                  name: Bracelets
                  icon: '60134'
          costs:
            - quantity: '2'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 100
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
        - items:
            - quantity: '1'
              item:
                name: Ring of the First Light
                id: '47300'
                category:
                  id: '43'
                  name: Ring
                  icon: '60135'
          costs:
            - quantity: '2'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 100
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
        - items:
            - quantity: '1'
              item:
                name: Traverse Clocktower
                id: '46169'
                category:
                  id: '76'
                  name: Outdoor Furnishing
                  icon: '60168'
          costs:
            - quantity: '2'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 90
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
        - items:
            - quantity: '1'
              item:
                name: Distant Sanctums Framer's Kit
                id: '46770'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '2'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 80
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
        - items:
            - quantity: '2'
              item:
                name: Luminous Oil
                id: '47342'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '46187'
                name: Illumed Invocations
                plural: copies of *Illumed Invocations*
                icon: '26448'
          order: 95
          achievement:
            id: '3811'
            name: Pilgrim's Progress VI
            description: Clear the area marked by stone 100 of Pilgrim's Traverse.
      npcs:
        - name: Ose Wyd
          location: Il Mheg
          coords: (29.9, 5.9)
    - id: "pilgrims-traverse-mount"
      name: ''
      inventory:
        - items:
            - quantity: 1
              item: 
                name: Chandeleir of First Light
                id: '46832'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                name: Bangles of the First Light
                plural: Bangles of the First Light
                id: '47299'
                icon: '60134'
            - quantity: '1'
              currency:
                name: Earrings of the First Light
                plural: Earrings of the First Light
                id: '47297'
                icon: '60133'
            - quantity: '1'
              currency:
                name: Necklace of the First Light
                plural: Necklace of the First Light
                id: '47298'
                icon: '60132'
            - quantity: '1'
              currency:
                name: Ring of the First Light
                plural: Ring of the First Light
                id: '47300'
                icon: '60135'
      npcs:
        - name: Aenc Daen
          location: Il Mheg
          coords: (29.8, 5.9)
  categories:
    - id: '44'
      name: Medicine
      icon: '60136'
    - id: '58'
      name: Materia
      icon: '60150'
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
    - id: '63'
      name: Other
      icon: '60159'
    - id: '81'
      name: Minion
      icon: '60155'
    - id: '41'
      name: Earrings
      icon: '60133'
    - id: '40'
      name: Necklace
      icon: '60132'
    - id: '42'
      name: Bracelets
      icon: '60134'
    - id: '43'
      name: Ring
      icon: '60135'
    - id: '76'
      name: Outdoor Furnishing
      icon: '60168'
  currencies:
    - id: '46186'
      name: Illumed Aetherpool Glass
      plural: fragments of illumed aetherpool glass
      icon: '26683'
    - id: '46263'
      name: First Light Relic
      plural: First Light relics
      icon: '21282'
    - id: '47342'
      name: Luminous Oil
      plural: phials of luminous oil
      icon: '22654'
    - id: '46187'
      name: Illumed Invocations
      plural: copies of *Illumed Invocations*
      icon: '26448'

currencies:
  - name: Illumed Aetherpool Glass
    sources:
      - "Guaranteed drop from Stone 30/50/70"
      - "Random drop from Bronze Coffers"
  - name: Illumed Invocation
    sources:
      - "Guaranteed drop from Stone 100"
  - name: First Light Relic
    sources:
      - "Guaranteed drop from The Final Verse (Quantum)"
      - "Random drop from The Final Verse"
  - name: Luminous Oil
    sources:
      - "Trade 1x Illumed Invocation"
      - "Challenge Log: 7x for Clear Stone 20"
      - "Challenge Log: 8x for Clear Stone 50"
      - "Challenge Log: 10x for Clear Stone 100"
---

