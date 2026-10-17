---
layout: quests-with-shops
title: The Merchant's Tale Variant Dungeon
permalink: /quests/variant/merchants-tale
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
  - name: A Spellbinding Read
    level: 90
    rowId: 70977
    questId: KinGva101_05441
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.0, 13.4)
      name: Shallow Moor
    steps:
      - location: Old Sharlayan
        coords: (14.7, 11.1)
        name: Speak with Y'nazqha.
      - location: The Maiden's Home
        coords: (6.1, 6.1)
        name: Speak with Y'nazqha.
      - location: The Maiden's Home
        coords: (6.0, 6.0)
        name: Speak with Y'nazqha in the maiden's home.
      - location: The Maiden's Home
        coords: (6.0, 5.9)
        name: Enter *The Merchant's Tale*.
      - location: Old Sharlayan
        coords: (14.7, 11.1)
        name: Speak with Y'nazqha in Old Sharlayan.
      - location: Old Sharlayan
        coords: (12.0, 13.4)
        name: Speak with Shallow Moor.
    expansion:
      id: '5'
      name: Dawntrail
    unlocks:
      - name: '*The Merchant''s Tale*'
        type: variant-dungeon
        levelRequired: 90
        levelSync: 100
        ilevelRequired: 0
        ilevelSync: 765
    partQuestNo: 2
  - name: Starting a New Chapter
    level: 90
    rowId: 70978
    questId: KinGva110_05442
    genre:
      id: '108'
      name: Variant Dungeons
    icon: '71020'
    issuer:
      location: Old Sharlayan
      coords: (14.7, 11.1)
      name: Fyrgeim
    steps:
      - location: Old Sharlayan
        coords: (11.1, 8.4)
        name: Wait at the designated location.
      - location: Old Sharlayan
        coords: (14.7, 11.1)
        name: Speak with Fyrgeim.
    expansion:
      id: '5'
      name: Dawntrail
    unlocks:
      - id: 3896
        name: A Timeless Tale
        type: achievement
    partQuestNo: 3
shops:
  shops:
    - id: '1771003'
      name: Corvosi Potsherd Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Story-lover's Bandana
                id: '50291'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '9'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-lover's Top
                id: '50292'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '12'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-lover's Armlets
                id: '50293'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '6'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-lover's Sarouel
                id: '50294'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '9'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-lover's Sandals
                id: '50295'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '6'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-spinner's Headdress
                id: '50296'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '9'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-spinner's Chestwrap
                id: '50297'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '12'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-spinner's Chaplets
                id: '50298'
                category:
                  id: '37'
                  name: Hands
                  icon: '60129'
          costs:
            - quantity: '6'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-spinner's Sarouel
                id: '50299'
                category:
                  id: '36'
                  name: Legs
                  icon: '60128'
          costs:
            - quantity: '9'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Story-spinner's Sandals
                id: '50300'
                category:
                  id: '38'
                  name: Feet
                  icon: '60130'
          costs:
            - quantity: '6'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Ballroom Etiquette - Saving Face
                id: '50337'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '9'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 110
        - items:
            - quantity: '1'
              item:
                name: Worthy Pursuits Orchestrion Roll
                id: '50804'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '9'
              currency:
                id: '50434'
                name: Corvosi Potsherd
                plural: Corvosi potsherds
                icon: '25919'
          order: 120
      requires:
        name: A Spellbinding Read
        level: 90
        rowId: 70977
        questId: KinGva101_05441
        genre: Variant Dungeons
        icon: '71140'
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
    - id: '1771004'
      name: Corvosi Brass Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Royal Magicked Carpet
                id: '50447'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '100'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 110
          achievement:
            id: '3898'
            name: Stranger than Fiction
            description: Complete *The Merchant's Tale* (Advanced).
        - items:
            - quantity: '1'
              item:
                name: Soothing Sea-beast
                id: '50824'
                category:
                  id: '81'
                  name: Minion
                  icon: '60155'
          costs:
            - quantity: '12'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Modern Aesthetics - Shadowhunter Chic
                id: '50327'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '20'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 140
          achievement:
            id: '3898'
            name: Stranger than Fiction
            description: Complete *The Merchant's Tale* (Advanced).
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
            - quantity: '40'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 180
          achievement:
            id: '3898'
            name: Stranger than Fiction
            description: Complete *The Merchant's Tale* (Advanced).
        - items:
            - quantity: '1'
              item:
                name: The Faces We Wear - Dark Glasses
                id: '50459'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '12'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 130
        - items:
            - quantity: '1'
              item:
                name: Earrings of the Sea-folk
                id: '50430'
                category:
                  id: '41'
                  name: Earrings
                  icon: '60133'
          costs:
            - quantity: '12'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 50
        - items:
            - quantity: '1'
              item:
                name: Collar of the Sea-folk
                id: '50431'
                category:
                  id: '40'
                  name: Necklace
                  icon: '60132'
          costs:
            - quantity: '12'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 50
        - items:
            - quantity: '1'
              item:
                name: Bracelets of the Sea-folk
                id: '50432'
                category:
                  id: '42'
                  name: Bracelets
                  icon: '60134'
          costs:
            - quantity: '12'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 50
        - items:
            - quantity: '1'
              item:
                name: Ring of the Sea-folk
                id: '50433'
                category:
                  id: '43'
                  name: Ring
                  icon: '60135'
          costs:
            - quantity: '12'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 50
        - items:
            - quantity: '1'
              item:
                name: Corvosi Screen
                id: '50419'
                category:
                  id: '57'
                  name: Furnishing
                  icon: '60164'
          costs:
            - quantity: '8'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 150
        - items:
            - quantity: '10'
              item:
                name: Magicked Prism (Ribbons)
                id: '48157'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '1'
              currency:
                id: '50847'
                name: Corvosi Brass
                plural: pieces of Corvosi brass
                icon: '26348'
          order: 200
      npcs:
        - name: Trisassant
          location: Old Sharlayan
          coords: (12.0, 13.3)
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
    - id: '61'
      name: Miscellany
      icon: '60153'
    - id: '94'
      name: Orchestrion Roll
      icon: '60173'
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
    - id: '57'
      name: Furnishing
      icon: '60164'
  currencies:
    - id: '50434'
      name: Corvosi Potsherd
      plural: Corvosi potsherds
      icon: '25919'
    - id: '50847'
      name: Corvosi Brass
      plural: pieces of Corvosi brass
      icon: '26348'



---