---
layout: quests-with-shops-mounts
title: Endwalker Extreme Trials
permalink: /quests/extremes/endwalker
links:
  next: /quests/extremes/dawntrail
  previous: /quests/extremes/shadowbringers
nonsequential: true
quests:
  - name: I Wandered Sharlayan as a Minstrel
    level: 1
    rowId: 69707
    questId: AktKyr102_04171
    genre:
      id: '0'
      name: ''
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.7, 14.2)
      name: wandering minstrel
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
    unlocks:
      - name: "The Minstrel's Ballad: Zodiark's Fall"
        type: trial
      - name: "The Minstrel's Ballad: Hydaelyn's Call"
        type: trial
      - name: "The Minstrel's Ballad: Endsinger's Aria"
        type: trial
      - name: Storm's Crown (Extreme) 
        type: trial
      - name: Mount Ordeals (Extreme)
        type: trial
      - name: The Voidcast Dais (Extreme)
        type: trial
      - name: The Abyssal Fracture (Extreme)
        type: trial
    partQuestNo: 1

  - name: Wings of Hope
    level: 1
    rowId: 70331
    questId: SubCts829_04795
    genre:
      id: '140'
      name: Old Sharlayan Sidequests
    icon: '71020'
    issuer:
      location: Old Sharlayan
      coords: (11.5, 10.3)
      name: Singingway
    steps:
      - location: Mare Lamentorum
        coords: (11.9, 30.5)
        name: Speak with Singingway in Sinus Lacrimarum.
      - location: Mare Lamentorum
        coords: (35.3, 26.8)
        name: Use the curiously carrot-shaped amplifier to find the source of the
          signal in Sinus Tormenti.
      - location: Mare Lamentorum
        coords: (34.4, 24.2)
        name: Speak with Singingway.
      - location: Mare Lamentorum
        coords: (19.9, 25.3)
        name: Blow the apocryphal horn at the designated location.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - id: 3412
        name: Dragon-sitting
        type: achievement
    requires:
      - name: Down in the Dark
        link: /quests/msq/endwalker/part4
        level: 90
        rowId: 70284
        questId: AktKml105_04748
        genre: Newfound Adventure
        icon: '71000'
      - name: Lynx of Eternal Darkness
      - name: Lynx of Divine Light
      - name: Bluefeather Lynx
      - name: Lynx of Imperious Wind
      - name: Lynx of Righteous Fire
      - name: Lynx of Fallen Shadow
      - name: Lynx of Abyssal Grief 
    rewards:
      xp:
        factor: 0
        paramGrowId: '1'
        avg: 0
      gil: 1770
      items:
        - item:
            name: Apocryphal Bahamut Horn
            id: '41489'
            icon: '26038'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
    partQuestNo: 2



shops:
  shops:
    - id: '1770456'
      name: Out-of-this-world Oddities
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Lynx of Eternal Darkness Flute
                id: '36000'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '35815'
                name: Astral Totem
                plural: astral totems
                icon: '26619'
          order: 115
        - items:
            - quantity: '1'
              item:
                name: Lynx of Divine Light Flute
                id: '36001'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '35816'
                name: Umbral Totem
                plural: umbral totems
                icon: '26620'
          order: 115
        - items:
            - quantity: '1'
              item:
                name: Bluefeather Lynx Flute
                id: '36912'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '36809'
                name: Ultimatum Totem
                plural: Ultimatum totems
                icon: '26626'
          order: 115
        - items:
            - quantity: '1'
              item:
                name: Lynx of Imperious Wind Flute
                id: '38464'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '38374'
                name: Windswept Archfiend Totem
                plural: windswept archfiend totems
                icon: '26629'
          order: 115
          questId: '70133'
          quest:
            name: The Wind Rises
            link: /quests/msq/endwalker/part3
            level: 90
            rowId: 70133
            questId: AktKmi106_04597
            genre: Newfound Adventure
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Lynx of Righteous Fire Flute
                id: '39492'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '38949'
                name: Flamecloaked Archfiend Totem
                plural: flamecloaked archfiend totems
                icon: '26638'
          order: 115
          questId: '70213'
          quest:
            name: Desires Untold
            link: /quests/msq/endwalker/part3
            level: 90
            rowId: 70213
            questId: AktKmj108_04677
            genre: Newfound Adventure
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Lynx of Fallen Shadow Flute
                id: '40391'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '40295'
                name: Voidcast Archfiend Totem
                plural: voidcast archfiend totems
                icon: '26644'
          order: 115
          questId: '70278'
          quest:
            name: Abyssal Dark
            link: /quests/msq/endwalker/part4
            level: 90
            rowId: 70278
            questId: AktKmk108_04742
            genre: Newfound Adventure
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Lynx of Abyssal Grief Flute
                id: '41493'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '41053'
                name: Voidvessel Totem
                plural: voidvessel totems
                icon: '26646'
          order: 115
          questId: '70284'
          quest:
            name: Down in the Dark
            link: /quests/msq/endwalker/part4
            level: 90
            rowId: 70284
            questId: AktKml105_04748
            genre: Newfound Adventure
            icon: '71000'
      npcs:
        - name: Nesvaaz
          location: Radz-at-Han 
          coords: (X:10.6, Y:10.0)
        - name: Agora Merchant
          location: Old Sharlayan
          coords: (X:11.6, Y:11.2)
  categories:
    - id: '63'
      name: Other
      icon: '60159'
  currencies:
    - id: '35815'
      name: Astral Totem
      plural: astral totems
      icon: '26619'
    - id: '35816'
      name: Umbral Totem
      plural: umbral totems
      icon: '26620'
    - id: '36809'
      name: Ultimatum Totem
      plural: Ultimatum totems
      icon: '26626'
    - id: '38374'
      name: Windswept Archfiend Totem
      plural: windswept archfiend totems
      icon: '26629'
    - id: '38949'
      name: Flamecloaked Archfiend Totem
      plural: flamecloaked archfiend totems
      icon: '26638'
    - id: '40295'
      name: Voidcast Archfiend Totem
      plural: voidcast archfiend totems
      icon: '26644'
    - id: '41053'
      name: Voidvessel Totem
      plural: voidvessel totems
      icon: '26646'

totems:
  - totem:
      id: '35815'
      name: Astral Totem
      plural: astral totems
      icon: '26619'
    trial:
      name: "The Minstrel's Ballad: Zodiark's Fall"
    item:
      name: Lynx of Eternal Darkness Flute
      id: '36000'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '35816'
      name: Umbral Totem
      plural: umbral totems
      icon: '26620'
    trial:
      name: "The Minstrel's Ballad: Hydaelyn's Call"
    item:
      name: Lynx of Divine Light Flute
      id: '36001'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '36809'
      name: Ultimatum Totem
      plural: Ultimatum totems
      icon: '26626'
    trial:
      name: "The Minstrel's Ballad: Endsinger's Aria"
    item:
      name: Bluefeather Lynx Flute
      id: '36912'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '38374'
      name: Windswept Archfiend Totem
      plural: windswept archfiend totems
      icon: '26629'
    trial:
      name: Storm's Crown (Extreme)
    item:
      name: Lynx of Imperious Wind Flute
      id: '38464'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '38949'
      name: Flamecloaked Archfiend Totem
      plural: flamecloaked archfiend totems
      icon: '26638'
    trial:
      name: Mount Ordeals (Extreme)
    item:
      name: Lynx of Righteous Fire Flute
      id: '39492'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '40295'
      name: Voidcast Archfiend Totem
      plural: voidcast archfiend totems
      icon: '26644'
    trial:
      name: The Voidcast Dais (Extreme)
    item:
      name: Lynx of Fallen Shadow Flute
      id: '40391'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '41053'
      name: Voidvessel Totem
      plural: voidvessel totems
      icon: '26646'
    trial:
      name: The Abyssal Fracture (Extreme)
    item:
      name: Lynx of Abyssal Grief Flute
      id: '41493'
      category:
        id: '63'
        name: Other
        icon: '60159'


---