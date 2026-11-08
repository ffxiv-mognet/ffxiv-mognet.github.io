---
layout: quest-table
title: Custom Deliveries
permalink: /quests/lifestyle/custom-deliveries
nonsequential: true
quests:
  - name: Arms Wide Open
    level: 60
    rowId: 67087
    questId: SubCts600_01551
    genre:
      id: '122'
      name: Idyllshire Sidequests
    icon: '71140'
    issuer:
      location: Idyllshire
      coords: (5.7, 6.9)
      name: Geimlona
    steps:
      - location: Idyllshire
        coords: (4.6, 6.7)
        name: Speak with Zhloe Aliapoh at the Hard Place.
    expansion:
      id: '1'
      name: Heavensward
    unlocks:
      - type: satisfaction-npc
        id: '1'
        name: Zhloe Aliapoh
        npcId: '1019615'
        location: Idyllshire
        coords: (4.6, 6.7)
    requires:
      - name: Go West, Craftsman
        level: 60
        rowId: 67634
        questId: HeaVny804_02098
        genre: Mor Dhonan Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 0
        paramGrowId: '60'
        avg: 0
      gil: 518
      items:
        - item:
            name: Bouillabaisse
            id: '4721'
            icon: '24111'
            ilvl: '55'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Landtrap Salad
            id: '4688'
            icon: '24151'
            ilvl: '55'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: None Forgotten, None Forsaken
    level: 60
    rowId: 68541
    questId: SubCts610_03005
    genre:
      id: '124'
      name: Rhalgr's Reach Sidequests
    icon: '71140'
    issuer:
      location: Rhalgr's Reach
      coords: (9.8, 12.5)
      name: Galiena
    steps:
      - location: Rhalgr's Reach
        coords: (14.6, 9.4)
        name: Speak with M'naago.
    expansion:
      id: '2'
      name: Stormblood
    unlocks:
      - type: satisfaction-npc
        id: '2'
        name: M'naago
        npcId: '1020337'
        location: Rhalgr's Reach
        coords: (14.6, 9.4)
    requires:
      - name: Return of the Bull
        level: 70
        rowId: 68508
        questId: StmBdb111_02972
        genre: Post-Ala Mhigan Liberation
        icon: '71000'
      - name: Reach Long and Prosper
        level: 60
        rowId: 68477
        questId: StmBdy110_02941
        genre: ''
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '60'
        avg: 25000
      items:
        - item:
            name: Baked Onion Soup
            id: '12861'
            icon: '24116'
            ilvl: '125'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Stuffed Cabbage Rolls
            id: '12866'
            icon: '24206'
            ilvl: '125'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: Not While Their Names Are Still Spoken
    level: 60
    rowId: 68542
    questId: SubCts611_03006
    genre:
      id: '124'
      name: Rhalgr's Reach Sidequests
    icon: '71140'
    issuer:
      location: Rhalgr's Reach
      coords: (14.6, 9.4)
      name: M'naago
    steps:
      - location: The Peaks
        coords: (15.4, 36.9)
        name: Speak with M'naago in Ala Ghiri.
      - location: The Lochs
        coords: (34.8, 32.1)
        name: Speak with M'naago in the Ala Mhigan Quarter.
      - location: The Fringes
        coords: (30.3, 25.7)
        name: Speak with M'rahz Nunh in the Peering Stones.
      - location: Rhalgr's Reach
        coords: (14.6, 9.4)
        name: Speak with M'naago in Rhalgr's Reach.
    expansion:
      id: '2'
      name: Stormblood
    requires:
      - name: None Forgotten, None Forsaken
        level: 60
        rowId: 68541
        questId: SubCts610_03005
        genre: Rhalgr's Reach Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 4
        name: M'naago satisfaction level:4
        id: '2'
        location: Rhalgr's Reach
        coords: (14.6, 9.4)
    rewards:
      xp:
        factor: 100
        paramGrowId: '60'
        avg: 25000
      items:
        - item:
            name: Emerald Soup
            id: '12863'
            icon: '24101'
            ilvl: '139'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Dhalmel Gratin
            id: '12867'
            icon: '24112'
            ilvl: '133'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: The Seaweed Is Always Greener
    level: 62
    rowId: 68675
    questId: SubCts620_03139
    genre:
      id: '128'
      name: Kugane Sidequests
    icon: '71140'
    issuer:
      location: Kugane
      coords: (10.2, 9.9)
      name: Kojin hireling
    steps:
      - location: The Ruby Sea
        coords: (28.3, 15.3)
        name: Speak with the lady-in-waiting in Tamamizu.
    expansion:
      id: '2'
      name: Stormblood
    unlocks:
      - type: satisfaction-npc
        id: '3'
        name: Kurenai
        npcId: '1025878'
        location: The Ruby Sea
        coords: (28.3, 15.3)
    requires:
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
      - name: "The Two Princesses of Sui\u2013no\u2013Sato"
        level: 63
        rowId: 68243
        questId: StmBdz311_02707
        genre: Ruby Sea Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '62'
        avg: 25500
      items:
        - item:
            name: Beet Soup
            id: '12862'
            icon: '24103'
            ilvl: '133'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Dhalmel Gratin
            id: '12867'
            icon: '24112'
            ilvl: '133'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: Up Where They Trade All Day in the Sun
    level: 62
    rowId: 68676
    questId: SubCts621_03140
    genre:
      id: '129'
      name: Ruby Sea Sidequests
    icon: '71140'
    issuer:
      location: The Ruby Sea
      coords: (28.3, 15.3)
      name: Kurenai
    steps:
      - location: The Ruby Sea
        coords: (21.2, 19.5)
        name: "Speak with Jikkan in Sui\u2013no\u2013Sato."
      - location: The Ruby Sea
        coords: (38.6, 39.0)
        name: Wait at the Ruby Price.
      - location: Kugane
        coords: (11.9, 8.3)
        name: Speak with Kurenai at the Rakuza District.
      - location: The Ruby Sea
        coords: (28.3, 15.3)
        name: Speak with Kurenai in Tamamizu.
    expansion:
      id: '2'
      name: Stormblood
    requires:
      - name: The Seaweed Is Always Greener
        level: 62
        rowId: 68675
        questId: SubCts620_03139
        genre: Kugane Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 4
        name: Kurenai satisfaction level:4
        id: '3'
        location: The Ruby Sea
        coords: (28.3, 15.3)
    rewards:
      xp:
        factor: 100
        paramGrowId: '62'
        avg: 25500
      items:
        - item:
            name: Clam Chowder
            id: '12864'
            icon: '24114'
            ilvl: '150'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Stuffed Chysahl
            id: '12868'
            icon: '24159'
            ilvl: '150'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: Between a Rock and the Hard Place
    level: 66
    rowId: 68713
    questId: SubCts630_03177
    genre:
      id: '122'
      name: Idyllshire Sidequests
    icon: '71140'
    issuer:
      location: Idyllshire
      coords: (5.7, 6.9)
      name: Geimlona
    steps:
      - location: Idyllshire
        coords: (4.9, 6.6)
        name: Speak with Adkiragh at the Hard Place.
    expansion:
      id: '2'
      name: Stormblood
    unlocks:
      - type: satisfaction-npc
        id: '4'
        name: Adkiragh
        npcId: '1018393'
        location: Idyllshire
        coords: (4.9, 6.6)
    requires:
      - name: Stormblood
        level: 70
        rowId: 68089
        questId: StmBda706_02553
        genre: Stormblood
        icon: '71000'
      - name: Arms Wide Open
        level: 60
        rowId: 67087
        questId: SubCts600_01551
        genre: Idyllshire Sidequests
        icon: '71140'
      - name: Purbol Rain
        level: 65
        rowId: 68294
        questId: StmBdz507_02758
        genre: Azim Steppe Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '66'
        avg: 26500
      gil: 620
      items:
        - item:
            name: Clam Chowder
            id: '12864'
            icon: '24114'
            ilvl: '150'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Stuffed Chysahl
            id: '12868'
            icon: '24159'
            ilvl: '150'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: He Ain't Piggy, He's My Brother
    level: 66
    rowId: 68714
    questId: SubCts631_03178
    genre:
      id: '122'
      name: Idyllshire Sidequests
    icon: '71140'
    issuer:
      location: Idyllshire
      coords: (5.0, 6.4)
      name: Melodie
    steps:
      - location: Idyllshire
        coords: (7.3, 6.5)
        name: Speak with Bulugan.
      - location: Idyllshire
        coords: (4.8, 6.4)
        name: Speak with Bulugan.
    expansion:
      id: '2'
      name: Stormblood
    requires:
      - name: Between a Rock and the Hard Place
        level: 66
        rowId: 68713
        questId: SubCts630_03177
        genre: Idyllshire Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 4
        name: Adkiragh satisfaction level:4
        id: '4'
        location: Idyllshire
        coords: (4.9, 6.6)
    rewards:
      xp:
        factor: 100
        paramGrowId: '66'
        avg: 26500
      gil: 760
      items:
        - item:
            name: Tempura Platter
            id: '19826'
            icon: '24323'
            ilvl: '279'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Nomad Meat Pie
            id: '19839'
            icon: '24354'
            ilvl: '279'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: Oh, Beehive Yourself
    level: 70
    rowId: 69265
    questId: SubCts640_03729
    genre:
      id: '133'
      name: Eulmore Sidequests
    icon: '71140'
    issuer:
      location: Eulmore
      coords: (11.7, 11.7)
      name: Kai-Shirr
    steps:
      - location: Eulmore
        coords: (11.7, 10.3)
        name: Wait outside the Beehive.
      - location: Eulmore
        coords: (12.3, 9.9)
        name: Speak with Kai-Shirr.
    expansion:
      id: '3'
      name: Shadowbringers
    unlocks:
      - type: satisfaction-npc
        id: '5'
        name: Kai-Shirr
        npcId: '1031801'
        location: Eulmore
        coords: (12.3, 9.9)
    requires:
      - name: Moving Forward
        level: 80
        rowId: 69217
        questId: LucKmg109_03681
        genre: The Voyage Home
        icon: '71000'
      - name: The Boutique Always Wins
        level: 70
        rowId: 69139
        questId: LucKyr002_03603
        genre: ''
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      items:
        - item:
            name: Blood Tomato Salad
            id: '27864'
            icon: '24151'
            ilvl: '406'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Mushroom Saute
            id: '27865'
            icon: '24202'
            ilvl: '406'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: Commercially Flyable
    level: 70
    rowId: 69266
    questId: SubCts641_03730
    genre:
      id: '133'
      name: Eulmore Sidequests
    icon: '71140'
    issuer:
      location: Eulmore
      coords: (12.2, 10.1)
      name: Bosta-Zia
    steps:
      - location: Eulmore
        coords: (12.3, 9.9)
        name: Speak with Kai-Shirr.
      - location: Eulmore
        coords: (11.0, 11.5)
        name: Speak with Colden.
      - location: Eulmore
        coords: (12.3, 9.9)
        name: Speak with Kai-Shirr.
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: Oh, Beehive Yourself
        level: 70
        rowId: 69265
        questId: SubCts640_03729
        genre: Eulmore Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 4
        name: Kai-Shirr satisfaction level:4
        id: '5'
        location: Eulmore
        coords: (12.3, 9.9)
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      items:
        - item:
            name: Blood Bouillabaisse
            id: '27876'
            icon: '24111'
            ilvl: '418'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
        - item:
            name: Coffee Biscuit
            id: '27878'
            icon: '24007'
            ilvl: '418'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 1
  - name: A Ship on His Shoulder
    level: 70
    rowId: 69267
    questId: SubCts642_03731
    genre:
      id: '133'
      name: Eulmore Sidequests
    icon: '71140'
    issuer:
      location: Eulmore
      coords: (12.2, 9.7)
      name: Anfrigg
    steps:
      - location: Eulmore
        coords: (11.2, 9.5)
        name: Speak with Lereberd.
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: Commercially Flyable
        level: 70
        rowId: 69266
        questId: SubCts641_03730
        genre: Eulmore Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Kai-Shirr satisfaction level:5
        id: '5'
        location: Eulmore
        coords: (12.3, 9.9)
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      gil: 533
  - name: O Crafter, My Crafter
    level: 70
    rowId: 69425
    questId: SubCts650_03889
    genre:
      id: '101'
      name: Ishgardian Restoration Sidequests
    icon: '71140'
    issuer:
      location: The Firmament
      coords: (13.5, 11.2)
      name: Ehll Tou
    steps:
      - location: The Firmament
        coords: (12.3, 12.2)
        name: Speak with crafters in the Firmament.
      - location: The Firmament
        coords: (13.5, 11.2)
        name: Speak with Ehll Tou.
      - location: The Firmament
        coords: (14.3, 12.6)
        name: Speak with Arvide.
      - location: The Firmament
        coords: (13.5, 11.2)
        name: Speak with Ehll Tou.
    expansion:
      id: '3'
      name: Shadowbringers
    unlocks:
      - type: satisfaction-npc
        id: '6'
        name: Ehll Tou
        npcId: '1033543'
        location: The Firmament
        coords: (13.5, 11.2)
    requires:
      - name: If Songs Had Wings
        level: 60
        rowId: 69373
        questId: LucKhz001_03837
        genre: Ishgardian Restoration Sidequests
        icon: '71140'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      items:
        - item:
            name: Mejillones al Ajillo
            id: '28720'
            icon: '24326'
            ilvl: '460'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 5
        - item:
            name: Arros Negre
            id: '28721'
            icon: '24032'
            ilvl: '460'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 5
  - name: An Ode to Unity
    level: 70
    rowId: 69426
    questId: SubCts651_03890
    genre:
      id: '101'
      name: Ishgardian Restoration Sidequests
    icon: '71140'
    issuer:
      location: The Firmament
      coords: (13.5, 11.2)
      name: Ehll Tou
    steps:
      - location: The Firmament
        coords: (14.3, 12.6)
        name: Speak with Arvide.
      - location: The Churning Mists
        coords: (8.3, 26.9)
        name: Search for Ehll Tou at Zenith.
      - location: The Churning Mists
        coords: (8.5, 27.1)
        name: Deliver Ehll Tou's hammer to the endearing dragonet.
      - location: The Firmament
        coords: (13.5, 11.2)
        name: Speak with Ehll Tou at Saint Roelle's Dais.
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: O Crafter, My Crafter
        level: 70
        rowId: 69425
        questId: SubCts650_03889
        genre: Ishgardian Restoration Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Ehll Tou satisfaction level:5
        id: '6'
        location: The Firmament
        coords: (13.5, 11.2)
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      items:
        - item:
            name: Crab Cakes
            id: '30481'
            icon: '24329'
            ilvl: '490'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Chili Crab
            id: '30482'
            icon: '24328'
            ilvl: '490'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: On Ehll Tou's Wings
    level: 70
    rowId: 69427
    questId: SubCts652_03891
    genre:
      id: '101'
      name: Ishgardian Restoration Sidequests
    icon: '71140'
    issuer:
      location: The Firmament
      coords: (13.5, 11.2)
      name: Hautdilong
    steps:
      - location: The Firmament
        coords: (14.3, 12.6)
        name: Speak with Arvide.
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: An Ode to Unity
        level: 70
        rowId: 69426
        questId: SubCts651_03890
        genre: Ishgardian Restoration Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Ehll Tou satisfaction level:5
        id: '6'
        location: The Firmament
        coords: (13.5, 11.2)
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      items:
        - item:
            name: Ehll Tou Whistle
            id: '30866'
            icon: '26039'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
  - name: You Can Count on It
    level: 70
    rowId: 69615
    questId: SubCts660_04079
    genre:
      id: '101'
      name: Ishgardian Restoration Sidequests
    icon: '71140'
    issuer:
      location: The Firmament
      coords: (11.1, 14.5)
      name: Francel
    steps:
      - location: The Firmament
        coords: (9.5, 8.4)
        name: Find the suspiciously familiar man.
      - location: The Firmament
        coords: (8.9, 8.5)
        name: Speak with Maurilette.
      - location: The Firmament
        coords: (14.0, 14.4)
        name: Speak with Maelie.
      - location: The Firmament
        coords: (8.9, 8.5)
        name: Speak with Maelie again.
    expansion:
      id: '3'
      name: Shadowbringers
    unlocks:
      - type: satisfaction-npc
        id: '7'
        name: Charlemend
        npcId: '1035211'
        location: The Firmament
        coords: (8.9, 8.5)
    requires:
      - name: Smiles Cross the Sky
        level: 60
        rowId: 69538
        questId: LucKha304_04002
        genre: Ishgardian Restoration Main Quests
        icon: '71140'
      - name: The Brume Lifts
        level: 60
        rowId: 69496
        questId: LucKhz003_03960
        genre: Ishgardian Restoration Sidequests
        icon: '71140'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      optional:
        - item:
            name: Baked Onion Soup
            id: '12861'
            icon: '24116'
            ilvl: '125'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Stuffed Cabbage Rolls
            id: '12866'
            icon: '24206'
            ilvl: '125'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: Those Who Serve
    level: 70
    rowId: 69616
    questId: SubCts661_04080
    genre:
      id: '101'
      name: Ishgardian Restoration Sidequests
    icon: '71140'
    issuer:
      location: The Firmament
      coords: (8.9, 8.5)
      name: Maurilette
    steps:
      - location: The Firmament
        coords: (9.9, 10.7)
        name: Find Maelie.
      - location: The Firmament
        coords: (9.2, 8.6)
        name: Speak with Charlemend.
    expansion:
      id: '3'
      name: Shadowbringers
    requires:
      - name: You Can Count on It
        level: 70
        rowId: 69615
        questId: SubCts660_04079
        genre: Ishgardian Restoration Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 4
        name: Charlemend satisfaction level:4
        id: '7'
        location: The Firmament
        coords: (8.9, 8.5)
    rewards:
      xp:
        factor: 100
        paramGrowId: '70'
        avg: 54000
      optional:
        - item:
            name: Crab Cakes
            id: '30481'
            icon: '24329'
            ilvl: '490'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Chili Crab
            id: '30482'
            icon: '24328'
            ilvl: '490'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: Of Mothers and Merchants
    level: 80
    rowId: 70059
    questId: SubCts670_04523
    genre:
      id: '140'
      name: Old Sharlayan Sidequests
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (12.7, 9.7)
      name: well-dressed attendant
    steps:
      - location: Old Sharlayan
        coords: (9.5, 14.0)
        name: Wait near the table reserved by House Leveilleur.
      - location: Old Sharlayan
        coords: (9.5, 14.0)
        name: Speak with Ameliance.
      - location: Old Sharlayan
        coords: (15.7, 7.2)
        name: Speak with Ameliance again.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - type: satisfaction-npc
        id: '8'
        name: Ameliance
        npcId: '1042241'
        location: Old Sharlayan
        coords: (15.7, 7.2)
    requires:
      - name: Endwalker
        level: 90
        rowId: 70000
        questId: AktKmg115_04464
        genre: Endwalker
        icon: '71000'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 895
      items:
        - item:
            name: Giant Haddock Dip
            id: '36053'
            icon: '24258'
            ilvl: '540'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Yakow Moussaka
            id: '36054'
            icon: '24112'
            ilvl: '540'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: A Mother's Love
    level: 80
    rowId: 70060
    questId: SubCts671_04524
    genre:
      id: '140'
      name: Old Sharlayan Sidequests
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (15.7, 7.2)
      name: Ameliance
    steps:
      - location: Old Sharlayan
        coords: (5.7, 9.8)
        name: Speak with Ameliance and have her accompany you.
      - location: Old Sharlayan
        coords: (5.7, 9.8)
        name: Accompany Ameliance to the designated location and then speak with her.
      - location: Old Sharlayan
        coords: (5.0, 8.1)
        name: Speak with the contemplative student while accompanied by Ameliance.
      - location: Old Sharlayan
        coords: (5.7, 9.8)
        name: Accompany Ameliance to the designated location and then speak with her.
      - location: Old Sharlayan
        coords: (15.7, 7.2)
        name: Speak with Ameliance.
    expansion:
      id: '4'
      name: Endwalker
    requires:
      - name: Of Mothers and Merchants
        level: 80
        rowId: 70059
        questId: SubCts670_04523
        genre: Old Sharlayan Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 4
        name: Ameliance satisfaction level:4
        id: '8'
        location: Old Sharlayan
        coords: (15.7, 7.2)
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 975
      items:
        - item:
            name: Tsai tou Vounou
            id: '36060'
            icon: '24417'
            ilvl: '554'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Sideritis Cookie
            id: '36061'
            icon: '24051'
            ilvl: '554'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: A Gift from House Leveilleur
    level: 80
    rowId: 70061
    questId: SubCts672_04525
    genre:
      id: '140'
      name: Old Sharlayan Sidequests
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (15.7, 7.1)
      name: Meryld
    steps:
      - location: Old Sharlayan
        coords: (15.9, 7.5)
        name: Speak with the House Leveilleur maidservant.
    expansion:
      id: '4'
      name: Endwalker
    requires:
      - name: A Mother's Love
        level: 80
        rowId: 70060
        questId: SubCts671_04524
        genre: Old Sharlayan Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Ameliance satisfaction level:5
        id: '8'
        location: Old Sharlayan
        coords: (15.7, 7.2)
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 615
      items:
        - item:
            name: Appointed Attire Coffer
            id: '37493'
            icon: '26509'
            ilvl: '1'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: That's So Anden
    level: 80
    rowId: 70251
    questId: SubCts680_04715
    genre:
      id: '132'
      name: Crystarium Sidequests
    icon: '71140'
    issuer:
      location: The Crystarium
      coords: (9.3, 11.3)
      name: supplicant sheep
    steps:
      - location: Il Mheg
        coords: (16.6, 33.9)
        name: Speak with the loquacious leafman.
      - location: Il Mheg
        coords: (16.6, 33.9)
        name: Speak with Anden.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - type: satisfaction-npc
        id: '9'
        name: Anden
        npcId: '1044547'
        location: Il Mheg
        coords: (16.6, 33.9)
    requires:
      - name: Lance of a Lifetime
        level: 50
        rowId: 67533
        questId: ClsWdk502_01997
        genre: Carpenter Quests
        icon: '71140'
      - name: Endwalker
        level: 90
        rowId: 70000
        questId: AktKmg115_04464
        genre: Endwalker
        icon: '71000'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 984
      items:
        - item:
            name: Giant Haddock Dip
            id: '36053'
            icon: '24258'
            ilvl: '540'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Yakow Moussaka
            id: '36054'
            icon: '24112'
            ilvl: '540'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: Every Anden of the Rainbow
    level: 80
    rowId: 70252
    questId: SubCts681_04716
    genre:
      id: '137'
      name: Il Mheg Sidequests
    icon: '71140'
    issuer:
      location: Il Mheg
      coords: (16.6, 33.9)
      name: Anden
    steps:
      - location: Il Mheg
        coords: (16.6, 33.9)
        name: Speak with Anden.
      - location: The Rak'tika Greatwood
        coords: (30.0, 21.9)
        name: Travel to Fanow and wait for Anden to arrive.
      - location: Il Mheg
        coords: (16.6, 33.9)
        name: Speak with Anden in Lydha Lran.
    expansion:
      id: '4'
      name: Endwalker
    requires:
      - name: That's So Anden
        level: 80
        rowId: 70251
        questId: SubCts680_04715
        genre: Crystarium Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Anden satisfaction level:5
        id: '9'
        location: Il Mheg
        coords: (16.6, 33.9)
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 1359
      items:
        - item:
            name: Tsai tou Vounou
            id: '36060'
            icon: '24417'
            ilvl: '554'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Sideritis Cookie
            id: '36061'
            icon: '24051'
            ilvl: '554'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: A Labor of Leaf
    level: 80
    rowId: 70253
    questId: SubCts682_04717
    genre:
      id: '137'
      name: Il Mheg Sidequests
    icon: '71140'
    issuer:
      location: Il Mheg
      coords: (16.7, 33.9)
      name: Eo Tyr
    steps:
      - location: Il Mheg
        coords: (15.5, 33.5)
        name: Search for Another Anden.
    expansion:
      id: '4'
      name: Endwalker
    requires:
      - name: Every Anden of the Rainbow
        level: 80
        rowId: 70252
        questId: SubCts681_04716
        genre: Il Mheg Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Anden satisfaction level:5
        id: '9'
        location: Il Mheg
        coords: (16.6, 33.9)
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 615
      items:
        - item:
            name: Leafman Head
            id: '39629'
            icon: '56567'
            ilvl: '1'
            level: '1'
            category:
              id: '34'
              name: Head
              icon: '60124'
          count: 1
        - item:
            name: Anden III Horn
            id: '39488'
            icon: '26038'
            ilvl: '1'
            level: '1'
            category:
              id: '63'
              name: Other
              icon: '60159'
          count: 1
  - name: A Request of One's Own
    level: 80
    rowId: 70351
    questId: SubCts605_04815
    genre:
      id: '140'
      name: Old Sharlayan Sidequests
    icon: '71140'
    issuer:
      location: Old Sharlayan
      coords: (13.8, 15.0)
      name: Theopauldin
    steps:
      - location: Labyrinthos
        coords: (23.3, 21.3)
        name: Speak with the relaxing researcher in Sharlayan Hamlet.
      - location: Labyrinthos
        coords: (20.8, 20.4)
        name: Speak with Theopauldin.
    expansion:
      id: '4'
      name: Endwalker
    unlocks:
      - type: satisfaction-npc
        id: '10'
        name: Margrat
        npcId: '1046073'
        location: Labyrinthos
        coords: (20.4, 20.1)
    requires:
      - name: Going Haam
        level: 90
        rowId: 70272
        questId: AktKmk102_04736
        genre: Newfound Adventure
        icon: '71000'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '80'
        avg: 112200
      gil: 979
      items:
        - item:
            name: Tsai tou Vounou
            id: '36060'
            icon: '24417'
            ilvl: '554'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Sideritis Cookie
            id: '36061'
            icon: '24051'
            ilvl: '554'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: The Pride of Labyrinthos
    level: 80
    rowId: 70352
    questId: SubCts606_04816
    genre:
      id: '142'
      name: Labyrinthos Sidequests
    icon: '71140'
    issuer:
      location: Labyrinthos
      coords: (20.4, 20.1)
      name: Margrat
    steps:
      - location: Labyrinthos
        coords: (7.3, 27.1)
        name: Speak with Theopauldin.
      - location: Labyrinthos
        coords: (20.4, 20.1)
        name: Speak with Margrat.
      - location: Labyrinthos
        coords: (20.4, 20.1)
        name: Speak with Margrat again.
    expansion:
      id: '4'
      name: Endwalker
    requires:
      - name: A Request of One's Own
        level: 80
        rowId: 70351
        questId: SubCts605_04815
        genre: Old Sharlayan Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Margrat satisfaction level:5
        id: '10'
        location: Labyrinthos
        coords: (20.4, 20.1)
    rewards:
      xp:
        factor: 0
        paramGrowId: '80'
        avg: 0
      gil: 895
      items:
        - item:
            name: Gleaner's Coat
            id: '41596'
            icon: '42997'
            ilvl: '1'
            level: '1'
            category:
              id: '35'
              name: Body
              icon: '60126'
          count: 1
          stain:
            id: '91'
            name: Turquoise Blue
            color: '307149'
        - item:
            name: Gleaner's Work Gloves
            id: '41597'
            icon: '56137'
            ilvl: '1'
            level: '1'
            category:
              id: '37'
              name: Hands
              icon: '60129'
          count: 1
        - item:
            name: Gleaner's Breeches
            id: '41598'
            icon: '57538'
            ilvl: '1'
            level: '1'
            category:
              id: '36'
              name: Legs
              icon: '60128'
          count: 1
        - item:
            name: Gleaner's Longboots
            id: '41599'
            icon: '49632'
            ilvl: '1'
            level: '1'
            category:
              id: '38'
              name: Feet
              icon: '60130'
          count: 1
  - name: Laying New Tracks
    level: 90
    rowId: 70775
    questId: KinGsf101_05239
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (14.1, 12.1)
      name: railroad employee
    steps:
      - location: Shaaloani
        coords: (19.8, 16.6)
        name: Speak with Shenza at Shaaloani Station.
      - location: Shaaloani
        coords: (14.1, 19.7)
        name: Speak with Wawlika.
      - location: Shaaloani
        coords: (14.3, 19.3)
        name: Speak with Nitowikwe.
    expansion:
      id: '5'
      name: Dawntrail
    unlocks:
      - type: satisfaction-npc
        id: '11'
        name: Nitowikwe
        npcId: '1048605'
        location: Shaaloani
        coords: (14.3, 19.3)
    requires:
      - name: The Warmth of Family
        level: 100
        rowId: 70785
        questId: KinGmg106_05249
        genre: The New Dawn
        icon: '71000'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '90'
        avg: 248640
      gil: 826
  - name: The Weight of a Train
    level: 90
    rowId: 70776
    questId: KinGsf102_05240
    genre:
      id: '152'
      name: Shaaloani Sidequests
    icon: '71140'
    issuer:
      location: Shaaloani
      coords: (14.3, 19.3)
      name: Nitowikwe
    steps:
      - location: Shaaloani
        coords: (18.9, 15.6)
        name: Wait at the designated location.
      - location: Shaaloani
        coords: (18.9, 14.1)
        name: Speak with Nitowikwe.
      - location: Shaaloani
        coords: (14.3, 19.3)
        name: Speak with Nitowikwe again.
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: Laying New Tracks
        level: 90
        rowId: 70775
        questId: KinGsf101_05239
        genre: Tuliyollal Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Nitowikwe satisfaction level:5
        id: '11'
        location: Shaaloani
        coords: (14.3, 19.3)
    rewards:
      xp:
        factor: 100
        paramGrowId: '90'
        avg: 248640
      gil: 529
  - name: His Heart Blazes On
    level: 90
    rowId: 70777
    questId: KinGsf103_05241
    genre:
      id: '152'
      name: Shaaloani Sidequests
    icon: '71140'
    issuer:
      location: Shaaloani
      coords: (14.1, 19.7)
      name: Wawlika
    steps:
      - location: Shaaloani
        coords: (19.6, 16.1)
        name: Speak with Zawpya.
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: The Weight of a Train
        level: 90
        rowId: 70776
        questId: KinGsf102_05240
        genre: Shaaloani Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Nitowikwe satisfaction level:5
        id: '11'
        location: Shaaloani
        coords: (14.3, 19.3)
    rewards:
      xp:
        factor: 100
        paramGrowId: '90'
        avg: 248640
      gil: 613
      items:
        - item:
            name: Dawnblazer Attire Coffer
            id: '44660'
            icon: '26509'
            ilvl: '1'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1
  - name: Taco Time
    level: 90
    rowId: 70996
    questId: KinGsf201_05460
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (13.7, 12.1)
      name: Hhuki
    steps:
      - location: Tuliyollal
        coords: (15.1, 12.1)
        name: Speak with Tiisol Ja.
      - location: Tuliyollal
        coords: (15.0, 11.6)
        name: Wait for Tiisol Ja at the designated location.
      - location: Tuliyollal
        coords: (15.1, 12.1)
        name: Speak with Tiisol Ja.
    expansion:
      id: '5'
      name: Dawntrail
    unlocks:
      - type: satisfaction-npc
        id: '12'
        name: Tiisol Ja
        npcId: '1058167'
        location: Tuliyollal
        coords: (15.1, 12.1)
    requires:
      - name: The Promise of Tomorrow
        level: 100
        rowId: 70909
        questId: KinGmi110_05373
        genre: The New Dawn
        icon: '71000'
      - name: Inscrutable Tastes
        level: 50
        rowId: 67631
        questId: HeaVny801_02095
        genre: Ishgardian Sidequests
        icon: '71140'
    rewards:
      xp:
        factor: 100
        paramGrowId: '90'
        avg: 248640
      gil: 872
      items:
        - item:
            name: Rroneek Steak
            id: '44091'
            icon: '24360'
            ilvl: '684'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
        - item:
            name: Stuffed Peppers
            id: '44103'
            icon: '24372'
            ilvl: '684'
            level: '1'
            category:
              id: '46'
              name: Meal
              icon: '60146'
          count: 3
  - name: A Dream Realized
    level: 90
    rowId: 70997
    questId: KinGsf202_05461
    genre:
      id: '148'
      name: Tuliyollal Sidequests
    icon: '71140'
    issuer:
      location: Tuliyollal
      coords: (15.1, 12.1)
      name: Tiisol Ja
    steps:
      - location: Solution Nine
        coords: (19.3, 18.2)
        name: Speak with Strata in Solution Nine.
      - location: Solution Nine
        coords: (19.4, 18.2)
        name: Wait for taco orders at the designated location.
      - location: Solution Nine
        coords: (4.7, 16.6)
        name: Deliver tacos to waiting customers.
      - location: Solution Nine
        coords: (19.3, 18.2)
        name: Speak with Hhuki.
      - location: Solution Nine
        coords: (19.3, 18.2)
        name: Speak with Hhuki again.
      - location: Tuliyollal
        coords: (15.1, 12.1)
        name: Speak with Tiisol Ja in Tuliyollal.
    expansion:
      id: '5'
      name: Dawntrail
    requires:
      - name: Taco Time
        level: 90
        rowId: 70996
        questId: KinGsf201_05460
        genre: Tuliyollal Sidequests
        icon: '71140'
      - type: satisfaction-npc
        rank: 5
        name: Tiisol Ja satisfaction level:5
        id: '12'
        location: Tuliyollal
        coords: (15.1, 12.1)
    rewards:
      xp:
        factor: 100
        paramGrowId: '90'
        avg: 248640
      gil: 2717
      items:
        - item:
            name: Ballroom Etiquette - Trial by Taco
            id: '52294'
            icon: '26435'
            ilvl: '1'
            level: '1'
            category:
              id: '61'
              name: Miscellany
              icon: '60153'
          count: 1


---