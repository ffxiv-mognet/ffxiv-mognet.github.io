---
layout: with-nav
title: Bicolor Gemstone Shops
permalink: /fates/shops

maxRanks:
  "3": "Max"
  "4": "Max"
  "5": "Max"

mapOrdering:
  "491": 31
  "492": 32
  "493": 33
  "494": 34
  "495": 35
  "496": 36
  "497": 37
  "555": 38
  "695": 41
  "696": 42
  "697": 43
  "698": 44
  "699": 45
  "700": 46
  "693": 47
  "694": 48
  "857": 51
  "858": 52
  "859": 53
  "860": 54
  "861": 55
  "862": 56
  "855": 57
  "856": 58

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
      - name: The Rak&rsquo;Tika Greatwood
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
      - name: Kozama&rsquo;uka
        mapId: 858
      - name: Yak T&rsquo;el
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


<div class="level">
    <div class="level-left">
        <p class="level-item">
            <label class="checkbox">
                <input type="checkbox" class="checkbox"
                    id="filter-by-rank-check"
                    onchange="handleFilterByRankChecked(event)"
                    />
                Filter by FATE Rank
            </label>
        </p>
    </div>
</div>
<section id="rank-filter-container">
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
</section>

<table class="table is-fullwidth">
  <thead>
    <tr>
        <th></th>
        <th>Rank</th>
        <th>Item</th>
        <th id="type-filter-trigger" style="cursor: pointer; width: 11em;">
            Type
            <div class="dropdown" id="type-filter">
                <div class="dropdown-trigger">
                  <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                </div>
                <div class="dropdown-menu">
                    <div class="dropdown-content">
                        {% for cat in site.data.gemstoneShops.categories %}
                        <div class="dropdown-item">
                            <label class="checkbox">
                                <input 
                                    type="checkbox" 
                                    class="checkbox type-filter-check" 
                                    data-category="{{cat.id}}" 
                                    id="cat-type-check-{{cat.id}}"
                                    onchange="handleTypeFilterChecked(event)"
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
        <th style="width: 5em">Cost</th>
        <th style="width: 18em">Gemstone Trader</th>
        <th id="version-filter-trigger" style="cursor: pointer">
            Expansion
            <div class="dropdown" id="version-filter">
                <div class="dropdown-trigger">
                  <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                  </span>
                </div>
                <div class="dropdown-menu">
                    <div class="dropdown-content">
                        {% for expac in page.areaRanks %}
                        <div class="dropdown-item">
                            <label class="checkbox">
                                <input 
                                    type="checkbox" 
                                    class="checkbox version-filter-check" 
                                    data-version="{{expac.versionId}}" 
                                    id="version-type-check-{{expac.versionId}}"
                                    onchange="handleVersionFilterChecked(event)"
                                    checked
                                    />
                                {{expac.name}}
                            </label>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </th>
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
            data-category="{{ item.item.category.id }}"
            data-categoryName="{{ item.item.category.name }}"
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
            <td>
                {% if item.rank != -1 %}
                    {{item.rank}}
                {% else %}
                    {{ page.maxRanks[shop.version.id] }}
                {% endif %}
            </td>
            <td>{{ item.item.name }}</td>
            <td>{{ item.item.category.name }}</td>
            <td style="text-align: right">
              <span class="icon-text">
                {{item.cost}}
                <span class="icon"><i class="bicolor-gemstone"></i></span>
              </span>
            </td>
            <td>
                <div class="npc">
                    {{shop.npc.name}}
                    <span class="tag is-light">{{shop.npc.location}} {{shop.npc.coords}}</span>
                </div>
            </td>
            <td>{{ shop.version.name }}</td>
            <td>
              <span class="icon-text" style="white-space: nowrap">
                <span class="icon"><i class="quest-{{item.quest.icon}}"></i></span>
                <span style="font-size: 0.8em">{{item.quest.name}}</span>
              </span>
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
    const filterByRank = getFilterByRank()

    const container = document.getElementById('rank-filter-container')
    if (filterByRank) {
        container.classList.remove('is-hidden')
    } else {
        container.classList.add('is-hidden')
    }
    document.getElementById('filter-by-rank-check').checked = filterByRank

    for (var el of document.getElementsByClassName('fate-rank-select')) {
        const rank = loadAreaRank(el.dataset.map)
        el.value = rank || 1
    }
}
function setTypeFilters() {
    for (var el of document.getElementsByClassName('type-filter-check')) {
        const isVisible = getCategoryVisible(el.dataset.category)
        el.checked = isVisible
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

function getCategoryVisible(categoryId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:filter:category:${categoryId}`
    return !getLocalFlag(namespace, key)
}
function setCategoryVisible(categoryId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:filter:category:${categoryId}`
    return setLocalFlag(namespace, key, !isVisible)
}

function getVersionVisible(versionId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:filter:version:${versionId}`
    return !getLocalFlag(namespace, key)
}
function setVersionVisible(versionId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `fateshop:filter:version:${versionId}`
    return setLocalFlag(namespace, key, !isVisible)
}


function getFilterByRank() {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    key = `fateshop:filter:byrank`
    return getLocalFlag(namespace, key)
}
function setFilterByRank(isEnabled) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    key = `fateshop:filter:byrank`
    setLocalFlag(namespace, key, isEnabled)
}

function updateGemstoneShopRows() {
    const ranks = getAreaRanks()
    for (var row of document.getElementsByClassName('gemstone-shop-row')) {
        const cur_rank = ranks[row.dataset.map]
        const row_rank = Number(row.dataset.rank)

        let visible = getCategoryVisible(row.dataset.category) 
                        && getVersionVisible(row.dataset.version);

        if (getFilterByRank()) {
            if (row_rank == -1) {
                visible = visible && areAreasMaxRank(row.dataset.version)
            } else {
                visible = visible && (row_rank <= cur_rank)
            }
        } 

        if (visible) {
            row.classList.remove('is-hidden')
        } else {
            row.classList.add('is-hidden')
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

    sortRows()
}

const _maporder = JSON.parse('{{page.mapOrdering|jsonify}}');
function sortRows() {
    const rows = document.getElementsByClassName('gemstone-shop-row')
    const tbody = rows[0].parentNode
    Array.from(tbody.children).sort((rowA, rowB) => {

        return (
            (rowA.dataset.version - rowB.dataset.version) ||
            (_maporder[rowA.dataset.map] - _maporder[rowB.dataset.map]) ||
            (rowA.dataset.rank - rowB.dataset.rank) ||
            rowA.dataset.categoryname.localeCompare(rowB.dataset.categoryname)
        )

    }).forEach(it => tbody.appendChild(it))

}

function handleVersionFilterChecked(event) {
    const checkbox = event.target
    const versionId = checkbox.dataset.version
    setVersionVisible(versionId, checkbox.checked)
    updateGemstoneShopRows()
}

function handleTypeFilterChecked(event) {
    const checkbox = event.target
    const categoryId = checkbox.dataset.category
    setCategoryVisible(categoryId, checkbox.checked)
    updateGemstoneShopRows()
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


function handleFilterByRankChecked(event) {
    const checkbox = event.target
    setFilterByRank(checkbox.checked)
    update()
}

const _arearanks = JSON.parse('{{page.areaRanks|jsonify}}');
function areAreasMaxRank(versionId) {
    const ex = _arearanks.find(it => it.versionId == Number(versionId))
    return ex.areas.map(it => loadAreaRank(it.mapId) == ex.maxRank).every(it => it)
}

function update() {
    setAreaRanks()
    setTypeFilters()
    updateGemstoneShopRows()
}


document.addEventListener("DOMContentLoaded", async () => {
    update()

    const typeFilter = document.getElementById('type-filter')
    const typeFilterTrigger = document.getElementById('type-filter-trigger')
    typeFilterTrigger.onclick = () => {
        typeFilter.classList.toggle('is-active')
    }

    const versionFilter = document.getElementById('version-filter')
    const versionFilterTrigger = document.getElementById('version-filter-trigger')
    versionFilterTrigger.onclick = () => {
        versionFilter.classList.toggle('is-active')
    }

    document.getElementById('page-content').classList.add('is-loaded')
})
</script>