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


<div class="loading-wrapper" id="page-content">
    <div class="loading-icon has-text-centered">
        <span class="icon loading-spin">
            <i class="fas fa-spinner"></i>
        </span>
    </div>
    <div class="loading-content">

{% for expac in page.areaRanks %}
<nav class="level">
    <div class="level-left">
        <p class="level-item">{{expac.name}}</p>
    </div>
    {% for area in expac.areas %}
    <div class="level-left">
        <p class="level-item">
            {{ area.name }}
            <div class="select is-small">
                <select 
                    class="select fate-rank-select" 
                    data-version="{{ expac.versionId }}"
                    data-map="{{ area.mapId }}"
                    data-maxrank="{{ expac.maxRank }}"
                    onchange="handleChangeAreaRank(event)"
                    id="select-rank-area-{{area.mapId}}"
                    >
                    {% for i in (1..expac.maxRank) %}
                    <option value={{i}}>{{i}}</option>
                    {% endfor %}
                </select>
            </div>
        </p>
    </div>
    {% endfor %}
</nav>
{% endfor %}

<table class="table is-fullwidth">
  <thead>
    <tr>
        <th></th>
        <th>Item</th>
        <th>
            Type
            <div class="dropdown" id="type-filter">
                <div class="dropdown-trigger" id="type-filter-trigger">
                  <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                </div>
                <div class="dropdown-menu">
                    <div class="dropdown-content">
                        {% for cat in site.data.gemstoneShops.categories %}
                        <div class="dropdown-item">
                            <label class="checkbox">
                                <input type="checkbox" class="checkbox" 
                                    data-categoryId="{{cat.id}}" 
                                    id="cat-type-check-{{cat.id}}"
                                    checked
                                    />
                                {{cat.name}}
                            </label>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </th>
        <th>Cost</th>
        <th>Expansion</th>
        <th style="width: 20em">Gemstone Trader</th>
        <th>FATE Rank</th>
        <th>Quest</th>
    </tr>
  </thead>
  <tbody>
    {% for shop in site.data.gemstoneShops.shops %}
        {% for item in shop.inventory %}
        {% if item.item.name %}
        <tr class="gemstone-shop-row" 
            data-version="{{ shop.version.id }}" 
            data-map="{{ shop.map.id }}"
            data-rank="{{ item.rank }}"
            data-item="{{ item.item.id }}"
            >
            <td>
              <label class="checkbox">
                  <input 
                    type="checkbox" 
                    class="checkbox questCheckbox" 
                    data-item="{{item.item.id}}"
                    id="item-completed-{{item.item.id}}"
                    onchange="handleShopItemChecked(event)"
                    />
                </label>
            </td>
            <td>{{ item.item.name }}</td>
            <td>{{ item.item.category.name }}</td>
            <td style="text-align: right">{{ item.cost }}</td>
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
        {% endif %}
        {% endfor %}
    {% endfor %}
  </tbody>
</table>

</div>
</div>

<script>
function getAreaRanks() {
    var ret = {}
    for (var el of document.getElementsByClassName('fate-rank-select')) {
        ret[el.dataset.map] = Number(el.value)
    }
    return ret
}

function setAreaRanks() {
    for (var el of document.getElementsByClassName('fate-rank-select')) {
        const rank = loadAreaRank(el.dataset.map)
        el.value = rank || el.dataset.maxrank
    }
}

function getItemFinished(itemId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:item:finished:${itemId}`
    return getLocalFlag(namespace, key)
}
function setItemFinished(itemId, isFinished) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:item:finished:${itemId}`
    return setLocalFlag(namespace, key, isFinished)
}

function updateGemstoneShopRows() {
    const ranks = getAreaRanks()
    for (var row of document.getElementsByClassName('gemstone-shop-row')) {
        const max_rank = ranks[row.dataset.map]
        const row_rank = Number(row.dataset.rank)
        if (row_rank > max_rank) {
            row.classList.add('is-hidden')
        } else {
            row.classList.remove('is-hidden')
        }

        if (getItemFinished(row.dataset.item)) {
            row.classList.add('is-finished')
        } else {
            row.classList.remove('is-finished')
        }
    }


    for (var checkbox of document.getElementsByClassName('questCheckbox')) {
        const itemId = checkbox.dataset.item
        checkbox.checked = getItemFinished(itemId)
    }
}

function handleShopItemChecked(event) {
    const checkbox = event.target
    const itemId = checkbox.dataset.item
    setItemFinished(itemId, checkbox.checked)

    updateGemstoneShopRows()
}

function handleChangeAreaRank(evt) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const mapId = evt.target.dataset.map
    const key = `fateshop:rank:${mapId}`
    const rank = Number(evt.target.value)
    setLocalStorage(namespace, key, rank)
    updateGemstoneShopRows()
}
function loadAreaRank(mapId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:rank:${mapId}`
    return getLocalStorage(namespace, key)
}



document.addEventListener("DOMContentLoaded", async () => {
    setAreaRanks()
    updateGemstoneShopRows()

    const typeFilter = document.getElementById('type-filter')
    const typeFilterTrigger = document.getElementById('type-filter-trigger')
    typeFilterTrigger.onclick = () => {
        typeFilter.classList.toggle('is-active')
    }

    document.getElementById('page-content').classList.add('is-loaded')
})
</script>