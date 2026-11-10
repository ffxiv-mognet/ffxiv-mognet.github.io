---
layout: quests-with-shops-mounts
title: Dawntrail Extreme Trials
permalink: /quests/extremes/dawntrail
links:
  previous: /quests/extremes/endwalker
nonsequential: true
quests:
  - name: How the West Was Sung
    level: 1
    rowId: 70540
    questId: KinGyr102_05004
    genre:
      id: '0'
      name: ''
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (11.1, 14.6)
      name: wandering minstrel
    steps: []
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: Dawntrail
        link: /quests/msq/dawntrail/part2
        level: 100
        rowId: 70495
        questId: KinGmf114_04959
        genre: Dawntrail
        icon: '71000'
    unlocks:
      - name: Worqor Lar Dor (Extreme)
        type: trial
      - name: Everkeep (Extreme)
        type: trial
      - name: "The Minstrel's Ballad: Sphene's Burden"
        type: trial
      - name: Recollection (Extreme)
        type: trial
      - name: "The Minstrel's Ballad: Necron's Embrace"
        type: trial
      - name: Hell on Rails (Extreme)
        type: trial
      - name: The Unmaking (Extreme)
        type: trial
    rewards:
      xp:
        factor: 0
        paramGrowId: '1'
        avg: 0
    partQuestNo: 1
  - name: The Wing Spirit Cometh
    level: 1
    rowId: 71005
    questId: SubCts830_05469
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71020'
    issuer:
      location: Tuliyollal
      coords: (15.3, 7.5)
      name: Tonawawtan boy
    steps:
      - location: Kozama'uka
        coords: (19.4, 20.2)
        name: Head to Kozama'uka and play the flute of wings at the designated location.
    expansion:
      id: '5'
      name: Dawntrail
    unlocks:
      - id: 3944
        name: On the Wing
        type: achievement
    requires:
      - name: A Grave Presentiment
        link: /quests/msq/dawntrail/part4
        level: 100
        rowId: 71008
        questId: KinGmk103_05472
        genre: Winter's Prelude
        icon: '71000'
      - name: Wings of Ruin
      - name: Wings of Resolve
      - name: Wings of Eternity
      - name: Wings of the Knighthood
      - name: Wings of Death
      - name: Wings of Mist
      - name: Wings of Nihility
    rewards:
      xp:
        factor: 0
        paramGrowId: '1'
        avg: 0
      gil: 106
      items:
        - item:
            name: Wings of Legacy
            id: '52259'
            icon: '26089'
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
    - id: '1770885'
      name: Sublime Curiosities
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Wings of Ruin
                id: '43593'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '43539'
                name: Skyruin Totem
                plural: Skyruin totems
                icon: '26662'
          order: 140
        - items:
            - quantity: '1'
              item:
                name: Wings of Resolve
                id: '43594'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '43540'
                name: Resilient Totem
                plural: Resilient totems
                icon: '26663'
          order: 150
        - items:
            - quantity: '1'
              item:
                name: Wings of Eternity
                id: '44499'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '44718'
                name: Totem Eternal
                plural: totems eternal
                icon: '26671'
          order: 160
        - items:
            - quantity: '1'
              item:
                name: Wings of the Knighthood
                id: '47976'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '46720'
                name: Knight Totem
                plural: knight totems
                icon: '26680'
          order: 170
        - items:
            - quantity: '1'
              item:
                name: Wings of Death
                id: '46826'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '46982'
                name: Grave Totem
                plural: grave totems
                icon: '26682'
          order: 180
        - items:
            - quantity: '1'
              item:
                name: Wings of Mist
                id: '50444'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '49748'
                name: Runaway Totem
                plural: runaway totems
                icon: '26684'
          order: 190
        - items:
            - quantity: '1'
              item:
                name: Wings of Nihility
                id: '52270'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '50892'
                name: Totem of Naught
                plural: totems of naught
                icon: '26696'
          order: 195

      npcs:
        - name: Uah'shepya
          location: Solution Nine
          coords: (X:8.6, Y:13.5)
  categories:
    - id: '34'
      name: Head
      icon: '60124'
    - id: '35'
      name: Body
      icon: '60126'
    - id: '63'
      name: Other
      icon: '60159'
    - id: '61'
      name: Miscellany
      icon: '60153'
    - id: '94'
      name: Orchestrion Roll
      icon: '60173'
  currencies:
    - id: '43539'
      name: Skyruin Totem
      plural: Skyruin totems
      icon: '26662'
    - id: '43540'
      name: Resilient Totem
      plural: Resilient totems
      icon: '26663'
    - id: '44718'
      name: Totem Eternal
      plural: totems eternal
      icon: '26671'
    - id: '46720'
      name: Knight Totem
      plural: knight totems
      icon: '26680'
    - id: '46982'
      name: Grave Totem
      plural: grave totems
      icon: '26682'
    - id: '49748'
      name: Runaway Totem
      plural: runaway totems
      icon: '26684'
    - id: '50892'
      name: Totem of Naught
      plural: totems of naught
      icon: '26696'


totems:
  - totem:
      id: '43539'
      name: Skyruin Totem
      plural: Skyruin totems
      icon: '26662'
    trial:
      name: Worqor Lar Dor (Extreme)
    item:
      name: Wings of Ruin
      id: '43593'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '43540'
      name: Resilient Totem
      plural: Resilient totems
      icon: '26663'
    trial:
      name: Everkeep (Extreme)
    item:
      name: Wings of Resolve
      id: '43594'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '44718'
      name: Totem Eternal
      plural: totems eternal
      icon: '26671'
    trial:
      name: "The Minstrel's Ballad: Sphene's Burden"
    item:
      name: Wings of Eternity
      id: '44499'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '46720'
      name: Knight Totem
      plural: knight totems
      icon: '26680'
    trial:
      name: Recollection (Extreme)
    item:
      name: Wings of the Knighthood
      id: '47976'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '46982'
      name: Grave Totem
      plural: grave totems
      icon: '26682'
    trial:
      name: "The Minstrel's Ballad: Necron's Embrace"
    item:
      name: Wings of Death
      id: '46826'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '49748'
      name: Runaway Totem
      plural: runaway totems
      icon: '26684'
    trial:
      name: Hell on Rails (Extreme)
    item:
      name: Wings of Mist
      id: '50444'
      category:
        id: '63'
        name: Other
        icon: '60159'
  - totem:
      id: '50892'
      name: Totem of Naught
      plural: totems of naught
      icon: '26696'
    trial: 
      name: The Unmaking (Extreme)
    item:
      name: Wings of Nihility
      id: '52270'
      category:
        id: '63'
        name: Other
        icon: '60159'



---