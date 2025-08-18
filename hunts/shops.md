---
layout: with-nav
title: Hunt/FATE Shops
permalink: /hunts/shops
brandLabel: Mognet
brandUrl: /

npcLocations:
  Wilmetta:
    coords: (10.5, 7.4)
    location: Radz-at-Han
  Ilfroy:
    coords: (11.0, 10.8)
    location: Eulmore
  Aelina:
    coords: (22.7, 6.7)
    location: Mor Dhona
  Bertana:
    coords: (5.9, 5.2)
    location: Idyllshire
  Fathard:
    coords: (10.1, 11.7)
    location: Eulmore
  Nesvaaz:
    coords: (10.6, 10.0)
    location: Radz-at-Han
  "Uah'shepya":
    coords: (8.6, 13.5)
    location: Solution Nine
  Satsuya:
    coords: (10.4, 10.2)
    location: Kugane
  Billebaut:
    coords: (13.0, 11.7)
    location: Rhalgr's Reach

excludeItems:
  "Blissful Kamuy Fife": true
  "Reveling Kamuy Fife": true
  "Legendary Kamuy Fife": true
  "Auspicious Kamuy Fife": true
  "Lunar Kamuy Fife": true
  "Euphonious Kamuy Fife": true
  "Hallowed Kamuy Fife": true
  "White Lanner Whistle": true
  "Rose Lanner Whistle": true
  "Round Lanner Whistle": true
  "Warring Lanner Whistle": true
  "Dark Lanner Whistle": true
  "Sophic Lanner Whistle": true
  "Demonic Lanner Whistle": true
  "Lynx of Imperious Wind Flute": true
  "Lynx of Righteous Fire Flute": true
  "Lynx of Fallen Shadow Flute": true
  "Lynx of Abyssal Grief Flute": true
  "Lynx of Eternal Darkness Flute": true
  "Lynx of Divine Light Flute": true
  "Bluefeather Lynx Flute": true
  "Fae Gwiber Trumpet": true
  "Innocent Gwiber Trumpet": true
  "Shadow Gwiber Trumpet": true
  "Gwiber of Light Trumpet": true
  "Shroud of Darkness": true
  "Dais of Darkness": true
  "Clouddark Demimateria II": true
  "Modern Aesthetics - A Half Times Two": true
  "Wings of Ruin": true
  "Wings of Resolve": true
  "Wings of Eternity": true
  "Black Summer Top": true
  "Black Summer Halter": true
  "Black Summer Trunks": true
  "Black Summer Tanga": true

shopOrdering:
  "1769811": 1
  "1769577": 3
  "1769578": 4
  "1769782": 5
  "1769783": 6
  "1769987": 7
  "1770476": 8
  "1770761": 9

  "1769511": 20
  "1769728": 21
  "1769807": 22
  "1770015": 23
  "1770456": 24
  "1770885": 25

  "1770032": 100
---

<table class="table is-fullwidth">
  <thead>
    <tr>
        <th></th>
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
                        <div class="dropdown-item">
                            <div class="level">
                                <div class="level-left"><p class="level-item" onclick="setAllTypeFilters(true)">All</p></div>
                                <div class="level-right"><p class="level-item" onclick="setAllTypeFilters(false)">None</p></div>
                            </div>
                        </div>
                        {% for cat in site.data.huntShops.categories %}
                        <div class="dropdown-item">
                            <label class="checkbox">
                                <input 
                                    type="checkbox" 
                                    class="checkbox type-filter-check" 
                                    data-category="{{cat.id}}" 
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
        <th id="currency-filter-trigger" style="cursor: pointer; width: 10em;">
            Cost
            <div class="dropdown" id="currency-filter">
                <div class="dropdown-trigger">
                  <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                </div>
                <div class="dropdown-menu">
                    <div class="dropdown-content">
                        {% for currency in site.data.huntShops.currencies %}
                        <div class="dropdown-item">
                            <label class="checkbox">
                                <input 
                                    type="checkbox" 
                                    class="checkbox currency-filter-check" 
                                    data-currency="{{currency.id}}" 
                                    onchange="handleCurrencyFilterChecked(event)"
                                    checked
                                    />
                                {{currency.plural}}
                            </label>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </th>
        <th style="width: 22em">NPC</th>
        <th>Quest</th>
    </tr>
  </thead>
  <tbody>
    {% for shop in site.data.huntShops.shops %}
        {% for item in shop.inventory %}
        {% unless page.excludeItems[item.item.name] %}
        <tr class="hunt-shop-row" 
            data-shop="{{ shop.id }}"
            data-item="{{ item.item.id }}"
            data-currency="{{ item.currency.id }}"
            data-category="{{ item.item.category.id }}"
            data-categoryname="{{ item.item.category.name }}"
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
            <td>
              <span class="icon-text">
                {{item.cost}}
                {% if item.cost == 1%}
                    {{ item.currency.name }}
                {% else %}
                    {{ item.currency.plural }}
                {% endif %}
              </span>
            </td>
            <td>
              {% if shop.requires %}
              <div>
              <span class="icon-text" style="white-space: nowrap">
                <span class="icon"><i class="quest-{{shop.requires.icon}}"></i></span>
                <span style="font-size: 0.8em">{{shop.requires.name}}</span>
              </span>
              </div>
              {% endif   %}
                {% for npc in shop.npcs %}
                <div class="npc">
                    {{npc.name}}
                    {% if npc.location %}
                        <span class="tag is-light">{{npc.location}} {{npc.coords}}</span>
                    {% else %}
                        <span class="tag is-light">{{page.npcLocations[npc.name].location}} {{page.npcLocations[npc.name].coords}}</span>
                    {% endif %}
                </div>
                {% endfor %}
            </td>
            <td>
              {% if item.quest %}
              <span class="icon-text" style="white-space: nowrap">
                <span class="icon"><i class="quest-{{item.quest.icon}}"></i></span>
                <span style="font-size: 0.8em">{{item.quest.name}}</span>
              </span>
              {% endif %}
            </td>
        </tr>
        {% endunless %}
        {% endfor %}
    {% endfor %}
  </tbody>
</table>


<script>


function getHuntItemFinished(itemId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `huntshop:item:finished:${itemId}`
    return getLocalFlag(namespace, key)
}
function setHuntItemFinished(itemId, isFinished) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `huntshop:item:finished:${itemId}`
    return setLocalFlag(namespace, key, isFinished)
}
function getHuntItemCategoryVisible(categoryId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `huntshop:filter:category:${categoryId}`
    return !getLocalFlag(namespace, key)
}
function setHuntItemCategoryVisible(categoryId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `huntshop:filter:category:${categoryId}`
    return setLocalFlag(namespace, key, !isVisible)
}
function getHuntItemCurrencyVisible(currencyId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `huntshop:filter:currency:${currencyId}`
    return !getLocalFlag(namespace, key)
}
function setHuntItemCurrencyVisible(currencyId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `huntshop:filter:currency:${currencyId}`
    return setLocalFlag(namespace, key, !isVisible)
}

function updateHuntShopRows() {
    for (var row of document.getElementsByClassName('hunt-shop-row')) {
        let visible = getHuntItemCategoryVisible(row.dataset.category)
                        && getHuntItemCurrencyVisible(row.dataset.currency)
        let checkbox = row.querySelector('input[type=checkbox]')

        if (visible) {
            row.classList.remove('is-hidden')
        } else {
            row.classList.add('is-hidden')
        }

        const finished = getHuntItemFinished(row.dataset.item)
        checkbox.checked = finished

        if (finished) {
            row.classList.add('is-finished')
        } else {
            row.classList.remove('is-finished')
        }
    }

}

const _shopordering = JSON.parse('{{page.shopOrdering|jsonify}}')
function sortRows() {
    const tbody = document.querySelector('tr.hunt-shop-row').parentNode
    Array.from(tbody.children).sort((a, b) => {
        return (
            _shopordering[a.dataset.shop] - _shopordering[b.dataset.shop] ||
            a.dataset.currency - b.dataset.currency ||
            a.dataset.categoryname.localeCompare(b.dataset.categoryname)
        )
    }).forEach(it => tbody.appendChild(it))
}

function handleTypeFilterChecked(event) {
    const checkbox = event.target
    const categoryId = checkbox.dataset.category
    setHuntItemCategoryVisible(categoryId, checkbox.checked)
    updateHuntShopRows()
}
function setAllTypeFilters(isChecked) {
    for (const el of document.getElementsByClassName('type-filter-check')) {
        el.checked = isChecked
        setHuntItemCategoryVisible(el.dataset.category, isChecked)
    }
    updateHuntShopRows()
}
function handleCurrencyFilterChecked(event) {
    const checkbox = event.target
    const currencyId = checkbox.dataset.currency
    setHuntItemCurrencyVisible(currencyId, checkbox.checked)
    updateHuntShopRows()
}


function handleShopItemChecked(event) {
    const checkbox = event.target
    const itemId = checkbox.dataset.item
    const finished = checkbox.checked
    setHuntItemFinished(itemId, finished)

    const row = document.querySelector(`tr.hunt-shop-row[data-item="${itemId}"]`)
    if (finished) {
        row.classList.add('is-finished')
    } else {
        row.classList.remove('is-finished')
    }
}


function setShowFinished(value) {
  window.huntsShowFinished = value
  setLocalFlag("huntshop:config", "showFinished", value)

  if (window.huntsShowFinished) {
    removeHiddenFinishedStyle('hunt-shop-row')
  } else {
    appendHiddenFinishedStyle('hunt-shop-row')
  }
  updateHuntShopRows()
}


document.addEventListener('DOMContentLoaded', async () => {

    // initialize showFinished check
    var checkShowFinished = document.getElementById("check-showFinished");
    const showFinished = getLocalFlag("huntshop:config", "showFinished")
    setShowFinished(showFinished)
    checkShowFinished.checked = showFinished
    checkShowFinished.onchange = (evt) => { setShowFinished(evt.target.checked) }


    // initialize category filter dropdown
    const typeFilter = document.getElementById('type-filter')
    const typeFilterTrigger = document.getElementById('type-filter-trigger')
    typeFilterTrigger.onclick = () => {
        typeFilter.classList.toggle('is-active')
    }

    // initialize currency filter dropdown
    const currencyFilter = document.getElementById('currency-filter')
    const currencyFilterTrigger = document.getElementById('currency-filter-trigger')
    currencyFilterTrigger.onclick = () => {
        currencyFilter.classList.toggle('is-active')
    }

    updateHuntShopRows()
    sortRows()
})

</script>