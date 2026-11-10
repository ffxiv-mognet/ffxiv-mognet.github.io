---
layout: quests-with-shops
title: The Hunt - Dawntrail
permalink: /quests/the-hunt/dawntrail
brandLabel: Mognet
brandUrl: /quests
quests:
  - name: A New Dawn, a New Hunt
    level: 90
    rowId: 70545
    questId: KinGyr201_05009
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (11.8, 13.7)
      name: Wing of Protection scout
    steps:
      - location: Tuliyollal
        coords: (13.8, 13.7)
        name: Speak with Bol Ogaw.
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: Elite and Dangerous
        link: /quests/the-hunt/heavensward
        level: 60
        rowId: 67658
        questId: HeaVny813_02122
        genre: Ishgardian Sidequests
        icon: '71140'
      - name: The Rite of Succession
        link: /quests/msq/dawntrail/part1
        level: 90
        rowId: 70400
        questId: KinGma105_04864
        genre: Dawntrail
        icon: '71000'
    rewards:
      xp:
        factor: 150
        paramGrowId: '90'
        avg: 372960
      gil: 613
    unlocks:
      - name: Beginner Dawn mark bills
    partQuestNo: 1
  - name: Why We Hunt
    level: 94
    rowId: 70546
    questId: KinGyr202_05010
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (13.8, 13.7)
      name: Bol Ogaw
    steps:
      - location: Tuliyollal
        coords: (11.5, 15.2)
        name: Speak with Ty'at Qat.
      - location: Tuliyollal
        coords: (13.8, 13.7)
        name: Speak with Bol Ogaw.
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: The Leap to Yak T'el
        link: /quests/msq/dawntrail/part1
        level: 94
        rowId: 70433
        questId: KinGmc101_04897
        genre: Dawntrail
        icon: '71000'
    unlocks:
      - name: Intermediate Dawn mark bills
    rewards:
      xp:
        factor: 150
        paramGrowId: '94'
        avg: 393120
      gil: 613
    partQuestNo: 2
  - name: Hunting the Hunter
    level: 99
    rowId: 70547
    questId: KinGyr203_05011
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (13.8, 13.7)
      name: Bol Ogaw
    steps:
      - location: Heritage Found
        coords: (17.0, 9.4)
        name: Speak with Zomenike in Heritage Found.
      - location: Solution Nine
        coords: (11.0, 4.9)
        name: Speak with Filomena in Solution Nine.
      - location: Solution Nine
        coords: (4.3, 16.4)
        name: Speak with Napikwe.
      - location: Tuliyollal
        coords: (13.8, 13.7)
        name: Deliver Napikwe's notebook to Bol Ogaw in Tuliyollal.
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: Through the Gate of Gold
        link: /quests/msq/dawntrail/part2
        level: 99
        rowId: 70484
        questId: KinGmf103_04948
        genre: Dawntrail
        icon: '71000'
    unlocks:
      - name: Advanced Dawn mark bills
    rewards:
      xp:
        factor: 150
        paramGrowId: '99'
        avg: 418320
      gil: 872
    partQuestNo: 3
  - name: The Hunt Goes On
    level: 100
    rowId: 70548
    questId: KinGyr204_05012
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (13.8, 13.7)
      name: Bol Ogaw
    steps:
      - location: Solution Nine
        coords: (4.3, 16.4)
        name: Speak with Napikwe in Solution Nine.
      - location: Tuliyollal
        coords: (13.8, 13.7)
        name: Report back to Bol Ogaw in Tuliyollal.
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
      - name: Dawntrail Elite Marks
    rewards:
      xp:
        factor: 0
        paramGrowId: '100'
        avg: 0
      gil: 699
    partQuestNo: 4

shops:
  shops:
    - id: '1770761'
      name: Sacks of Nuts Exchange
      inventory:
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '150'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
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
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 150
        - items:
            - quantity: '1'
              item:
                name: Bluecoat Cat
                id: '43580'
                category:
                  id: '81'
                  name: Minion
                  icon: '60155'
          costs:
            - quantity: '800'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 95
        - items:
            - quantity: '1'
              item:
                name: Wild Ride Barding
                id: '43604'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '640'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 95
        - items:
            - quantity: '1'
              item:
                name: Automatoise Identification Key
                id: '44245'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '3200'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 90
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Everkeep Striking Dummy
                id: '41831'
                category:
                  id: '76'
                  name: Outdoor Furnishing
                  icon: '60168'
          costs:
            - quantity: '300'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 100
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Blade's Exaltation Orchestrion Roll
                id: '44321'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '300'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 95
        - items:
            - quantity: '1'
              item:
                name: Surgelight Twine
                id: '43554'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '50'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 110
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Surgelight Glaze
                id: '43555'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '25'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 110
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Brachiosaur Horn
                id: '45071'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '3200'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 90
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Evercharged Twine
                id: '46730'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '600'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 115
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Evercharged Glaze
                id: '46731'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '400'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 115
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Surgelight Solvent
                id: '43553'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '60'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 105
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Thundersteeped Twine
                id: '49758'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '3000'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 120
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
        - items:
            - quantity: '1'
              item:
                name: Thundersteeping Glaze
                id: '49759'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '2000'
              currency:
                id: '26533'
                name: Sack of Nuts
                plural: sacks of Nuts
                icon: '65068'
          order: 120
          questId: '70495'
          quest:
            name: Dawntrail
            level: 100
            rowId: 70495
            questId: KinGmf114_04959
            genre: Dawntrail
            icon: '71000'
      npcs:
        - name: Ryubool Ja
          location: Tuliyollal
          coords: (13.9, 13.4)
    - id: '1770885'
      name: Sublime Curiosities
      inventory:
        - items:
            - quantity: '1'
              item:
                name: Mica Head
                id: '43469'
                category:
                  id: '34'
                  name: Head
                  icon: '60124'
          costs:
            - quantity: '4'
              currency:
                id: '41804'
                name: Mica Magicog
                plural: Mica magicogs
                icon: '26273'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Mica Suit
                id: '43470'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '6'
              currency:
                id: '41804'
                name: Mica Magicog
                plural: Mica magicogs
                icon: '26273'
          order: 100
        - items:
            - quantity: '1'
              item:
                name: Mehwapyarra Whistle
                id: '43596'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '12'
              currency:
                id: '41803'
                name: Ttokrrone Scale
                plural: Ttokrrone scales
                icon: '22252'
          order: 110
        - items:
            - quantity: '1'
              item:
                name: Qeziigural Horn
                id: '43600'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '3'
              currency:
                id: '41805'
                name: Twilight Gemstone
                plural: twilight gemstones
                icon: '21333'
          order: 120
        - items:
            - quantity: '1'
              item:
                name: Shroud of Darkness
                id: '44501'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '99'
              currency:
                id: '44868'
                name: Clouddark Demimateria I
                plural: clouddark demimateria I
                icon: '20261'
          order: 130
        - items:
            - quantity: '1'
              item:
                name: Dais of Darkness
                id: '44500'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '75'
              currency:
                id: '44869'
                name: Clouddark Demimateria II
                plural: clouddark demimateria II
                icon: '20264'
          order: 131
        - items:
            - quantity: '1'
              item:
                name: Modern Aesthetics - A Half Times Two
                id: '44507'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '49'
              currency:
                id: '44869'
                name: Clouddark Demimateria II
                plural: clouddark demimateria II
                icon: '20264'
          order: 132
        - items:
            - quantity: '1'
              item:
                name: Surgelight Twine
                id: '43554'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Surgelight Glaze
                id: '43555'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Faerie Battle Orchestrion Roll
                id: '45015'
                category:
                  id: '94'
                  name: Orchestrion Roll
                  icon: '60173'
          costs:
            - quantity: '2'
              currency:
                id: '41804'
                name: Mica Magicog
                plural: Mica magicogs
                icon: '26273'
          order: 101
        - items:
            - quantity: '1'
              item:
                name: Clouddark Demimateria II
                id: '44869'
                category:
                  id: '61'
                  name: Miscellany
                  icon: '60153'
          costs:
            - quantity: '5'
              currency:
                id: '44868'
                name: Clouddark Demimateria I
                plural: clouddark demimateria I
                icon: '20261'
          order: 133
        - items:
            - quantity: '1'
              item:
                name: Surgelight Solvent
                id: '43553'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Evercharged Twine
                id: '46730'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
            - quantity: '1'
              currency:
                id: '46978'
                name: Montiont Coin
                plural: Montiont coins
                icon: '26345'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Evercharged Glaze
                id: '46731'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
            - quantity: '1'
              currency:
                id: '46978'
                name: Montiont Coin
                plural: Montiont coins
                icon: '26345'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Mica Neotunic
                id: '48998'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '2'
              currency:
                id: '41804'
                name: Mica Magicog
                plural: Mica magicogs
                icon: '26273'
          order: 101
        - items:
            - quantity: '1'
              item:
                name: Oversized Mica Neotunic
                id: '49003'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '2'
              currency:
                id: '41804'
                name: Mica Magicog
                plural: Mica magicogs
                icon: '26273'
          order: 101
        - items:
            - quantity: '1'
              item:
                name: Form-fitting Mica Neotunic
                id: '49008'
                category:
                  id: '35'
                  name: Body
                  icon: '60126'
          costs:
            - quantity: '2'
              currency:
                id: '41804'
                name: Mica Magicog
                plural: Mica magicogs
                icon: '26273'
          order: 101
        - items:
            - quantity: '1'
              item:
                name: Evercharged Ester
                id: '46729'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
            - quantity: '1'
              currency:
                id: '46978'
                name: Montiont Coin
                plural: Montiont coins
                icon: '26345'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Thundersteeped Twine
                id: '49758'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
            - quantity: '1'
              currency:
                id: '46978'
                name: Montiont Coin
                plural: Montiont coins
                icon: '26345'
            - quantity: '1'
              currency:
                id: '50888'
                name: Ranperre Coin
                plural: Ranperre coins
                icon: '26349'
          order: 200
        - items:
            - quantity: '1'
              item:
                name: Thundersteeping Glaze
                id: '49759'
                category:
                  id: '63'
                  name: Other
                  icon: '60159'
          costs:
            - quantity: '1'
              currency:
                id: '44549'
                name: Ordelle Coin
                plural: Ordelle coins
                icon: '26342'
            - quantity: '1'
              currency:
                id: '46978'
                name: Montiont Coin
                plural: Montiont coins
                icon: '26345'
            - quantity: '1'
              currency:
                id: '50888'
                name: Ranperre Coin
                plural: Ranperre coins
                icon: '26349'
          order: 200
      npcs:
        - name: Uah'shepya
          location: Solution Nine
          coords: (X:8.6, Y:13.5)
  categories:
    - id: '58'
      name: Materia
      icon: '60150'
    - id: '81'
      name: Minion
      icon: '60155'
    - id: '63'
      name: Other
      icon: '60159'
    - id: '76'
      name: Outdoor Furnishing
      icon: '60168'
    - id: '94'
      name: Orchestrion Roll
      icon: '60173'
    - id: '34'
      name: Head
      icon: '60124'
    - id: '35'
      name: Body
      icon: '60126'
    - id: '61'
      name: Miscellany
      icon: '60153'
  currencies:
    - id: '26533'
      name: Sack of Nuts
      plural: sacks of Nuts
      icon: '65068'
    - id: '41804'
      name: Mica Magicog
      plural: Mica magicogs
      icon: '26273'
    - id: '41803'
      name: Ttokrrone Scale
      plural: Ttokrrone scales
      icon: '22252'
    - id: '41805'
      name: Twilight Gemstone
      plural: twilight gemstones
      icon: '21333'
    - id: '44868'
      name: Clouddark Demimateria I
      plural: clouddark demimateria I
      icon: '20261'
    - id: '44869'
      name: Clouddark Demimateria II
      plural: clouddark demimateria II
      icon: '20264'
    - id: '44549'
      name: Ordelle Coin
      plural: Ordelle coins
      icon: '26342'
    - id: '46978'
      name: Montiont Coin
      plural: Montiont coins
      icon: '26345'
    - id: '50888'
      name: Ranperre Coin
      plural: Ranperre coins
      icon: '26349'


currencies:
  - name: Chi Bolts
    sources:
      - "FATE: The Serpentlord Seethes"
---