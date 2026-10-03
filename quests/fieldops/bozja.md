---
layout: quest-table
expansion: Field Operations
title: Save the Queen, Blades of Gunnhildr
permalink: /quests/fieldops/bozja
quests:
  - name: Hail to the Queen
    level: 80
    rowId: 69370
    questId: LucKsa001_03834
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Kugane
      coords: (12.2, 12.3)
      name: Keiten
    steps:
      - location: Ruby Bazaar Offices
        coords: (6.1, 6.0)
        name: Speak with Hancock.
      - location: Yanxia
        coords: (26.9, 13.2)
        name: Speak with the Doman attendant at the House of the Fierce in Yanxia.
      - location: Yanxia
        coords: (16.3, 8.5)
        name: Speak with the Doman attendant.
      - location: Yanxia
        coords: (16.3, 8.5)
        name: Speak with Marsak.
    requires:
      - name: Shadowbringers
        link: /quests/msq/shadowbringers/part2
        level: 80
        rowId: 69190
        questId: LucKmf111_03654
        genre: Shadowbringers
        icon: '71000'
      - name: The City of Lost Angels
        link: /quests/alliance/return-to-ivalice
        level: 70
        rowId: 68725
        questId: StmBdi303_03189
        genre: Return to Ivalice
        icon: '71140'
    partQuestNo: 1
  - name: Path to the Past
    level: 80
    rowId: 69371
    questId: LucKsa002_03835
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Yanxia
      coords: (16.3, 8.5)
      name: Marsak
    steps:
      - location: The Doman Enclave
        coords: (9.1, 8.7)
        name: Speak with the airship pilot at the Doman Enclave.
      - location: Gangos
        coords: (5.8, 5.7)
        name: Speak with the airship pilot at the Doman Enclave.
      - location: Gangos
        coords: (6.3, 6.2)
        name: Speak with Mikoto.
      - location: Gangos
        coords: (6.5, 5.8)
        name: Speak with Bajsaljen.
      - location: Rhalgr's Reach
        coords: (12.0, 11.7)
        name: Speak with the Ironworks engineer at Rhalgr's Reach.
      - location: Rhalgr's Reach
        coords: (11.8, 11.8)
        name: Speak with the Ironworks engineer.
    partQuestNo: 2
  - name: The Bozja Incident
    level: 80
    rowId: 69372
    questId: LucKsa003_03836
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Rhalgr's Reach
      coords: (11.8, 11.8)
      name: Ironworks engineer
    steps:
      - location: The Doman Enclave
        coords: (9.1, 8.7)
        name: Ask after Cid at the Doman Enclave.
      - location: Gangos
        coords: (6.3, 5.9)
        name: Speak with Mikoto.
      - location: Gangos
        coords: (5.8, 5.7)
        name: Speak with Mikoto.
      - location: Gangos
        coords: (6.4, 5.7)
        name: Speak with Marsak.
    soloDuty:
      levelSync: 80
      id: '5037'
    unlocks:
      - id: 2607
        name: Cidception
        type: achievement
    partQuestNo: 3
  - name: Where Eagles Nest
    level: 71
    rowId: 69477
    questId: LucKsa101_03941
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.4, 5.7)
      name: Marsak
    steps:
      - location: Gangos
        coords: (5.5, 5.4)
        name: Speak with Sjeros.
      - location: Bozjan Southern Front
        coords: (14.6, 29.6)
        name: Make for the Bozjan southern front and speak with Bajsaljen.
      - location: Bozjan Southern Front
        coords: (15.7, 29.2)
        name: Speak with Bajsaljen.
      - location: Bozjan Southern Front
        coords: (14.8, 29.3)
        name: Speak with Mikoto.
      - location: Bozjan Southern Front
        coords: (14.8, 29.3)
        name: Speak with Mikoto.
    partQuestNo: 4
  - name: Memoirs from the Front
    level: 1
    rowId: 69478
    questId: LucKsa102_03942
    genre: ''
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (15.0, 29.1)
      name: Resistance historian
    steps:
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
      - name: ''
    partQuestNo: 5
  - name: An Expected Engagement
    level: 71
    rowId: 69479
    questId: LucKsa103_03943
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (15.2, 29.2)
      name: Dmitar
    steps:
      - location: Bozjan Southern Front
        coords: (19.1, 26.2)
        name: Defeat 4th Legion slashers.
      - location: Bozjan Southern Front
        coords: (19.1, 26.2)
        name: Defeat 4th Legion nimrods.
      - location: Bozjan Southern Front
        coords: (15.2, 29.2)
        name: Speak with Dmitar.
    partQuestNo: 6
  - name: Lost No Longer
    level: 71
    rowId: 69480
    questId: LucKsa104_03944
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (15.2, 29.2)
      name: Dmitar
    steps:
      - location: Bozjan Southern Front
        coords: (15.2, 29.2)
        name: <If(LessThan(IntegerParameter(1),IntegerParameter(2)))>Obtain a forgotten
          fragment<Else/>Deliver the forgotten fragment to Dmitar</If>.
    partQuestNo: 7
  - name: On the Offensive
    level: 71
    rowId: 69481
    questId: LucKsa105_03945
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (15.2, 29.2)
      name: Dmitar
    steps:
      - location: Bozjan Southern Front
        coords: (28.8, 24.3)
        name: Speak with Dmitar.
    partQuestNo: 8
  - name: Time to Focus
    level: 71
    rowId: 69482
    questId: LucKsa106_03946
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (14.8, 29.3)
      name: Mikoto
    steps:
      - location: Bozjan Southern Front
        coords: (16.5, 20.1)
        name: Survey the designated area.
      - location: Bozjan Southern Front
        coords: (16.0, 17.7)
        name: Investigate the designated location.
      - location: Bozjan Southern Front
        coords: (16.2, 17.6)
        name: Investigate the designated location.
      - location: Bozjan Southern Front
        coords: (14.7, 29.3)
        name: Speak with Mikoto.
      - location: Bozjan Southern Front
        coords: (14.8, 29.3)
        name: Speak with Mikoto.
    partQuestNo: 9
  - name: Third Time's the Charm
    level: 71
    rowId: 69483
    questId: LucKsa107_03947
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (14.8, 29.3)
      name: Mikoto
    steps:
      - location: Bozjan Southern Front
        coords: (32.4, 15.2)
        name: Investigate the designated location.
      - location: Bozjan Southern Front
        coords: (14.7, 29.3)
        name: Speak with Mikoto.
      - location: Bozjan Southern Front
        coords: (14.8, 29.3)
        name: Speak with Mikoto.
    partQuestNo: 10
  - name: Pressing Forward
    level: 71
    rowId: 69484
    questId: LucKsa108_03948
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (15.2, 29.2)
      name: Dmitar
    steps:
      - location: Bozjan Southern Front
        coords: (14.3, 23.6)
        name: Speak with Dmitar.
    partQuestNo: 11
  - name: Signature Acquired
    level: 71
    rowId: 69485
    questId: LucKsa109_03949
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (14.7, 29.3)
      name: Mikoto
    steps:
      - location: Bozjan Southern Front
        coords: (19.0, 17.7)
        name: Rendezvous with Mikoto.
      - location: Bozjan Southern Front
        coords: (18.9, 17.8)
        name: Rescue Mikoto.
      - location: Bozjan Southern Front
        coords: (14.6, 29.6)
        name: Speak with Bajsaljen.
      - location: Bozjan Southern Front
        coords: (14.6, 29.6)
        name: Speak with Bajsaljen.
    partQuestNo: 12
  - name: Picking Up the Trail
    level: 71
    rowId: 69486
    questId: LucKsa110_03950
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (14.7, 29.3)
      name: Lilja
    steps:
      - location: Bozjan Southern Front
        coords: (28.9, 30.7)
        name: Investigate the designated location.
      - location: Bozjan Southern Front
        coords: (23.3, 18.4)
        name: Investigate the designated location.
      - location: Bozjan Southern Front
        coords: (14.6, 29.3)
        name: Speak with Lilja.
      - location: Bozjan Southern Front
        coords: (14.6, 29.3)
        name: Speak with Lilja.
    partQuestNo: 13
  - name: The Lady of Blades
    level: 71
    rowId: 69487
    questId: LucKsa111_03951
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Bozjan Southern Front
      coords: (14.6, 29.6)
      name: Bajsaljen
    steps:
      - location: Bozjan Southern Front
        coords: (11.2, 4.1)
        name: "Clear the critical engagement \u201Cthe Battle of Castrum Lacus Litore.\u201D\
          \ "
      - location: Bozjan Southern Front
        coords: (14.6, 29.6)
        name: Speak with Bajsaljen.
      - location: Gangos
        coords: (6.4, 5.7)
        name: Speak with Marsak.
    unlocks:
      - id: 2670
        name: In the Trenches
        type: achievement
    partQuestNo: 14
  - name: A Sign of What's to Come
    level: 80
    rowId: 69561
    questId: LucKsa201_04025
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.4, 5.7)
      name: Marsak
    steps:
      - location: Gangos
        coords: (6.5, 5.8)
        name: Speak with Bajsaljen.
      - location: Bozjan Southern Front
        coords: (14.8, 29.7)
        name: Speak with Marsak on the Bozjan southern front.
      - location: Bozjan Southern Front
        coords: (29.5, 19.6)
        name: Speak with Mikoto.
      - location: Gangos
        coords: (6.5, 5.8)
        name: Speak with Bajsaljen at Gangos.
    partQuestNo: 15
  - name: Fit for a Queen
    level: 80
    rowId: 69562
    questId: LucKsa202_04026
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.5, 5.8)
      name: Bajsaljen
    steps:
      - location: Gangos
        coords: (5.6, 5.5)
        name: Speak with Mikoto.
      - location: The Last Trace
        coords: (11.2, 10.5)
        name: Speak with Mikoto.
      - location: Delubrum Reginae
        coords: (11.2, 7.9)
        name: Enter Delubrum Reginae.
      - location: Gangos
        coords: (6.1, 6.1)
        name: Enter Delubrum Reginae.
      - location: Gangos
        coords: (6.4, 5.7)
        name: Speak with Marsak.
    soloDuty:
      levelSync: 80
      id: '5043'
    unlocks:
      - name: the Wanderer's Palace (Hard)
        type: dungeon
        levelRequired: 50
        levelSync: 50
        ilevelRequired: 90
        ilevelSync: 0
      - id: 2760
        name: She's a Killer Queen
        type: achievement
    partQuestNo: 16
  - name: A New Playing Field
    level: 71
    rowId: 69620
    questId: LucKsa301_04084
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.4, 5.7)
      name: Marsak
    steps:
      - location: Gangos
        coords: (5.5, 5.4)
        name: Speak with Sjeros.
      - location: Zadnor
        coords: (35.4, 33.9)
        name: Speak with Bajsaljen at Zadnor.
      - location: Zadnor
        coords: (35.4, 35.0)
        name: Speak with Lilja.
      - location: Zadnor
        coords: (35.4, 35.0)
        name: Speak with Mikoto.
    partQuestNo: 17
  - name: What Dreams Are Made Of
    level: 80
    rowId: 69632
    questId: LucKsa350_04096
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.2, 5.0)
      name: Gerolt
    steps:
      - location: Gangos
        coords: (6.1, 4.9)
        name: Speak with Zlatan.
    partQuestNo: 18
  - name: Spare Parts
    level: 80
    rowId: 69633
    questId: LucKsa351_04097
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.1, 4.9)
      name: Zlatan
    steps:
      - location: Gangos
        coords: (6.1, 4.9)
        name: Deliver the compact axles and compact springs to Zlatan at Gangos.
    partQuestNo: 19
  - name: A Done Deal
    level: 80
    rowId: 69636
    questId: LucKsa354_04100
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.2, 5.0)
      name: Gerolt
    steps:
      - location: Gangos
        coords: (6.1, 4.9)
        name: Speak with Zlatan.
    partQuestNo: 20
  - name: "\uE0BF Irresistible"
    level: 80
    rowId: 69637
    questId: LucKsa355_04101
    genre: Resistance Weapons
    icon: '71140'
    issuer:
      location: Gangos
      coords: (6.1, 4.9)
      name: Zlatan
    steps:
      - location: Gangos
        coords: (6.1, 4.9)
        name: <If(LessThan(IntegerParameter(1),IntegerParameter(2)))>Obtain raw emotions<Else/>With
          <If(Equal(IntegerParameter(4),19))><SheetEn(Item,2,32669,1,1)/> and <SheetEn(Item,2,32686,1,1)/><Else/><If(Equal(IntegerParameter(4),20))><SheetEn(Item,2,32670,1,1)/><Else/><If(Equal(IntegerParameter(4),21))><SheetEn(Item,2,32671,1,1)/><Else/><If(Equal(IntegerParameter(4),22))><SheetEn(Item,2,32672,1,1)/><Else/><If(Equal(IntegerParameter(4),23))><SheetEn(Item,2,32673,1,1)/><Else/><If(Equal(IntegerParameter(4),24))><SheetEn(Item,2,32677,1,1)/><Else/><If(Equal(IntegerParameter(4),25))><SheetEn(Item,2,32678,1,1)/><Else/><If(Equal(IntegerParameter(4),27))><SheetEn(Item,2,32679,1,1)/><Else/><If(Equal(IntegerParameter(4),28))><SheetEn(Item,2,32680,1,1)/><Else/><If(Equal(IntegerParameter(4),30))><SheetEn(Item,2,32674,1,1)/><Else/><If(Equal(IntegerParameter(4),31))><SheetEn(Item,2,32676,1,1)/><Else/><If(Equal(IntegerParameter(4),32))><SheetEn(Item,2,32675,1,1)/><Else/><If(Equal(IntegerParameter(4),33))><SheetEn(Item,2,32681,1,1)/><Else/><If(Equal(IntegerParameter(4),34))><SheetEn(Item,2,32682,1,1)/><Else/><If(Equal(IntegerParameter(4),35))><SheetEn(Item,2,32683,1,1)/><Else/><If(Equal(IntegerParameter(4),37))><SheetEn(Item,2,32684,1,1)/><Else/><If(Equal(IntegerParameter(4),38))><SheetEn(Item,2,32685,1,1)/><Else/></If></If></If></If></If></If></If></If></If></If></If></If></If></If></If></If></If>
          in your inventory or Armoury Chest, deliver the raw emotions to Zlatan at
          Gangos</If>.
    unlocks:
      - id: 2857
        name: 'Fit for a Queen: Blade''s Honor & Blade''s Fortitude'
        type: achievement
      - id: 2858
        name: 'Fit for a Queen: Blade''s Valor'
        type: achievement
      - id: 2859
        name: 'Fit for a Queen: Blade''s Justice'
        type: achievement
      - id: 2860
        name: 'Fit for a Queen: Blade''s Resolve'
        type: achievement
      - id: 2861
        name: 'Fit for a Queen: Blade''s Glory'
        type: achievement
      - id: 2862
        name: 'Fit for a Queen: Blade''s Serenity'
        type: achievement
      - id: 2863
        name: 'Fit for a Queen: Blade''s Subtlety'
        type: achievement
      - id: 2864
        name: 'Fit for a Queen: Blade''s Fealty'
        type: achievement
      - id: 2865
        name: 'Fit for a Queen: Blade''s Muse'
        type: achievement
      - id: 2866
        name: 'Fit for a Queen: Blade''s Ingenuity'
        type: achievement
      - id: 2867
        name: 'Fit for a Queen: Blade''s Euphoria'
        type: achievement
      - id: 2868
        name: 'Fit for a Queen: Blade''s Fury'
        type: achievement
      - id: 2869
        name: 'Fit for a Queen: Blade''s Acumen'
        type: achievement
      - id: 2870
        name: 'Fit for a Queen: Blade''s Temperance'
        type: achievement
      - id: 2871
        name: 'Fit for a Queen: Blade''s Mercy'
        type: achievement
      - id: 2872
        name: 'Fit for a Queen: Blade''s Wisdom'
        type: achievement
      - id: 2873
        name: 'Fit for a Queen: Blade''s Providence'
        type: achievement
    partQuestNo: 21


---