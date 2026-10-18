---
layout: quests-with-shops
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
      - name: Palace of the Dead Floors 1-50
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
      - name: Floor 50 - Palace of the Dead
        type: deep-dungeon
        icon: deep-dungeon
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
        type: deep-dungeon
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
      - name: Floor 100 - Palace of the Dead
        icon: deep-dungeon
shops:
  shops:
    - id: '1769675'
      name: Gelmorran Potsherd Exchange
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Wind-up Sasquatch
                id: '15446'
                category:
                  id: '81'
                  name: Minion
                  icon: '60155'
          costs:
            - quantity: '3'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Hecteye
                id: '15448'
                category:
                  id: '81'
                  name: Minion
                  icon: '60155'
          costs:
            - quantity: '3'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Disembodied Head Resonator
                id: '15933'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '10'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Piety Materia V
                id: '5633'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Heavens' Eye Materia V
                id: '5668'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Aim Materia V
                id: '5673'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Savage Might Materia V
                id: '5678'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Battledance Materia V
                id: '5683'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quickarm Materia V
                id: '5718'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Quicktongue Materia V
                id: '5723'
                category:
                  id: '58'
                  name: Materia
                  icon: '60150'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Firecrest Trophy
                id: '15986'
                category:
                  id: '76'
                  name: Outdoor Furnishing
                  icon: '60168'
          costs:
            - quantity: '1'
              currency:
                id: '16168'
                name: Firecrest
                plural: firecrests
                icon: '25988'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Glass Pumpkin Trophy
                id: '15987'
                category:
                  id: '76'
                  name: Outdoor Furnishing
                  icon: '60168'
          costs:
            - quantity: '1'
              currency:
                id: '16169'
                name: Glass Pumpkin
                plural: glass pumpkins
                icon: '25989'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Firecrest Earring
                id: '16166'
                category:
                  id: '41'
                  name: Earrings
                  icon: '60133'
          costs:
            - quantity: '1'
              currency:
                id: '16168'
                name: Firecrest
                plural: firecrests
                icon: '25988'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Glass Pumpkin Earring
                id: '16167'
                category:
                  id: '41'
                  name: Earrings
                  icon: '60133'
          costs:
            - quantity: '1'
              currency:
                id: '16169'
                name: Glass Pumpkin
                plural: glass pumpkins
                icon: '25989'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Fog of Phantom Orchestrion Roll
                id: '16813'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '5'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 102
          achievement:
            id: '1656'
            name: In Too Deep VII
            description: Clear the 150th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Blasphemous Experiment Orchestrion Roll
                id: '16814'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 102
          achievement:
            id: '1655'
            name: In Too Deep VI
            description: Clear the 100th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Notice of Death Orchestrion Roll
                id: '16815'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '10'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 102
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Firecrest Bracelet
                id: '20515'
                category:
                  id: '42'
                  name: Bracelets
                  icon: '60134'
          costs:
            - quantity: '1'
              currency:
                id: '16168'
                name: Firecrest
                plural: firecrests
                icon: '25988'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Firecrest Choker
                id: '20516'
                category:
                  id: '40'
                  name: Necklace
                  icon: '60132'
          costs:
            - quantity: '1'
              currency:
                id: '16168'
                name: Firecrest
                plural: firecrests
                icon: '25988'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Firecrest Ring
                id: '20517'
                category:
                  id: '43'
                  name: Ring
                  icon: '60135'
          costs:
            - quantity: '1'
              currency:
                id: '16168'
                name: Firecrest
                plural: firecrests
                icon: '25988'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Glass Pumpkin Bracelet
                id: '20518'
                category:
                  id: '42'
                  name: Bracelets
                  icon: '60134'
          costs:
            - quantity: '1'
              currency:
                id: '16169'
                name: Glass Pumpkin
                plural: glass pumpkins
                icon: '25989'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Glass Pumpkin Choker
                id: '20519'
                category:
                  id: '40'
                  name: Necklace
                  icon: '60132'
          costs:
            - quantity: '1'
              currency:
                id: '16169'
                name: Glass Pumpkin
                plural: glass pumpkins
                icon: '25989'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Glass Pumpkin Ring
                id: '20520'
                category:
                  id: '43'
                  name: Ring
                  icon: '60135'
          costs:
            - quantity: '1'
              currency:
                id: '16169'
                name: Glass Pumpkin
                plural: glass pumpkins
                icon: '25989'
          order: 110
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '20'
              item:
                name: Sustaining Potion
                id: '20309'
                category:
                  id: '44'
                  name: Medicine
                  icon: '60136'
          costs:
            - quantity: '1'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Firecrest
                id: '16168'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '2'
              currency:
                id: '16169'
                name: Glass Pumpkin
                plural: glass pumpkins
                icon: '25989'
          order: 120
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Glass Pumpkin
                id: '16169'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '2'
              currency:
                id: '16168'
                name: Firecrest
                plural: firecrests
                icon: '25988'
          order: 120
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Deadly Welcome Framer's Kit
                id: '48086'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '5'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 105
          achievement:
            id: '1580'
            name: In Too Deep V
            description: Clear the 50th floor of the Palace of the Dead.
        - items:
            - quantity: '1'
              item:
                name: Deadly Descent Framer's Kit
                id: '48087'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '10'
              currency:
                id: '15422'
                name: Gelmorran Potsherd
                plural: Gelmorran potsherds
                icon: '25975'
          order: 105
          achievement:
            id: '1657'
            name: In Too Deep VIII
            description: Clear the 200th floor of the Palace of the Dead.
      npcs:
        - name: E-Una-Kotor
          location: South Shroud
          coords: (25.1, 20.6)
  categories:
    - id: '81'
      name: Minion
      icon: '60155'
    - id: '63'
      name: Other
      icon: '60159'
    - id: '58'
      name: Materia
      icon: '60150'
    - id: '76'
      name: Outdoor Furnishing
      icon: '60168'
    - id: '41'
      name: Earrings
      icon: '60133'
    - id: '94'
      name: Orchestrion Roll
      icon: '60173'
    - id: '42'
      name: Bracelets
      icon: '60134'
    - id: '40'
      name: Necklace
      icon: '60132'
    - id: '43'
      name: Ring
      icon: '60135'
    - id: '44'
      name: Medicine
      icon: '60136'
    - id: '61'
      name: Miscellany
      icon: '60153'
  currencies:
    - id: '15422'
      name: Gelmorran Potsherd
      plural: Gelmorran potsherds
      icon: '25975'
    - id: '16168'
      name: Firecrest
      plural: firecrests
      icon: '25988'
    - id: '16169'
      name: Glass Pumpkin
      plural: glass pumpkins
      icon: '25989'

currencies:
  - name: Gelmorran potsherds
    sources:
      - "Guaranteed drop for clearing floor 50 / 100"
      - "Random drop from Bronze Chests in Palace of the Dead"
      - "Higher chance for Bronze Chest to contain potsherd on floor 101+"
  - name: Glass Pumpkin
    sources:
      - "Guaranteed either a Firecrest or a Glass Pumpkin for clearing floor 200"
  - name: Firecrest
    sources:
      - "Guaranteed either a Firecrest or a Glass Pumpkin for clearing floor 200"

---

