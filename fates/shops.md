---
layout: with-nav
title: Bicolor Gemstone Shops
permalink: /fates/shops

areaRanks:
  - name: Shadowbringers
    versionId: 3
    maxRank: 3
    areas:
      - name: Lakeland
        mapId: 491
      - name: Kholusia
        mapId: 492
      - name: Amh Arang
        mapId: 493
      - name: Il Mheg
        mapId: 494
      - name: The Rak'Tika Greatwood
        mapId: 495
      - name: The Tempest
        mapId: 496
  - name: Endwalker
    versionId: 4
    maxRank: 3
    areas:
      - name: Labyrinthos
        mapId: 695
      - name: Thavnair
        mapId: 696
      - name: Garlemald
        mapId: 697
      - name: Mare Lamentorum
        mapId: 698
      - name: Ultima Thule
        mapId: 699
      - name: Elpis
        mapId: 700
  - name: Dawntrail
    versionId: 5
    maxRank: 4
    areas:
      - name: Urqopacha
        mapId: 857
      - name: Kozama'uka
        mapId: 858
      - name: Yak T'el
        mapId: 859
      - name: Shaaloani
        mapId: 860
      - name: Heritage Found
        mapId: 861
      - name: Living Memory
        mapId: 862
---


{% for expac in page.areaRanks %}
<nav class="level">
    <div class="level-left">
        <p class="level-item">{{expac.name}}</p>
    </div>
    {% for area in expac.areas %}
    <div class="level-left">
        <p class="level-item">
            {{ area.name }}
            <select class="select" id="rank-select-{{area.key}}">
                {% for i in (1..expac.maxRank) %}
                <option value={{i}}>{{i}}</option>
                {% endfor %}
            </select>
        </p>
    </div>
    {% endfor %}
</nav>
{% endfor %}

<table class="table is-fullwidth">
  <thead>
    <tr>
        <th>Item</th>
        <th>Type</th>
        <th>Cost</th>
        <th>Expansion</th>
        <th style="width: 20em">Location</th>
        <th>FATE Rank</th>
        <th>Quest</th>
    </tr>
  </thead>
  <tbody>
    {% for shop in site.data.gemstoneShops %}
        {% for item in shop.inventory %}
        <tr>
            <td>{{ item.item.name }}</td>
            <td>{{ site.data.UiItemCategory[item.item.uiCategoryId].name }}</td>
            <td>{{ item.cost }}</td>
            <td>{{ shop.version.name }}</td>
            <td>
                <div class="npc">
                    {{shop.npc.name}}
                    <span class="tag is-light">{{shop.npc.location}} {{shop.npc.coords}}</span>
                </div>
            </td>
            <td>
                {{item.rank}}
            </td>
            <td>
                {{item.quest}}
            </td>
        </tr>
        {% endfor %}
    {% endfor %}
  </tbody>
</table>
