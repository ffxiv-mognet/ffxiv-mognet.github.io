---
layout: with-nav
title: Allied Society Shops
permalink: /allied/shops
brandLabel: Mognet
brandUrl: /

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
                        {% for cat in site.data.alliedShops.categories %}
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
                        {% for currency in site.data.alliedShops.currencies %}
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
    {% for shop in site.data.alliedShops.shops %}
        {% for inv in shop.inventory %}
        {% unless page.excludeItems[inv.items[0].item.name] %}
        <tr class="allied-shop-row" 
            data-shop="{{ shop.id }}"
            data-item="{{ inv.items[0].item.id }}"
            data-currency="{{ inv.costs[0].currency.id }}"
            data-category="{{ inv.items[0].item.category.id }}"
            data-categoryname="{{ inv.items[0].item.category.name }}"
            >
            <td>
              <label class="checkbox">
                  <input 
                    type="checkbox" 
                    class="checkbox questCheckbox" 
                    data-item="{{inv.items[0].item.id}}"
                    id="item-completed-{{inv.items[0].item.id}}"
                    onchange="handleShopItemChecked(event)"
                    />
                </label>
            </td>
            <td>
             {% for item in inv.items %}
                 <div>{{ item.item.name }}</div>
             {% endfor %} 
            </td>
            <td>{{ inv.items[0].item.category.name }}</td>
            <td>
              {% for cost in inv.costs %}
              <div>
                  <span class="icon-text">
                    {{cost.quantity}}
                    {% if cost.quantity == 1%}
                        {{ cost.currency.name }}
                    {% else %}
                        {{ cost.currency.plural }}
                    {% endif %}
                  </span>
              </div>
              {% endfor %}
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
              {% if inv.quest %}
              <span class="icon-text" style="white-space: nowrap">
                <span class="icon"><i class="quest-{{inv.quest.icon}}"></i></span>
                <span style="font-size: 0.8em">{{inv.quest.name}}</span>
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


function getAlliedItemFinished(itemId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `alliedshop:item:finished:${itemId}`
    return getLocalFlag(namespace, key)
}
function setAlliedItemFinished(itemId, isFinished) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `alliedshop:item:finished:${itemId}`
    return setLocalFlag(namespace, key, isFinished)
}
function getAlliedItemCategoryVisible(categoryId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `alliedshop:filter:category:${categoryId}`
    return !getLocalFlag(namespace, key)
}
function setAlliedItemCategoryVisible(categoryId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `alliedshop:filter:category:${categoryId}`
    return setLocalFlag(namespace, key, !isVisible)
}
function getAlliedItemCurrencyVisible(currencyId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `alliedshop:filter:currency:${currencyId}`
    return !getLocalFlag(namespace, key)
}
function setAlliedItemCurrencyVisible(currencyId, isVisible) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `alliedshop:filter:currency:${currencyId}`
    return setLocalFlag(namespace, key, !isVisible)
}

function updateAlliedShopRows() {
    for (var row of document.getElementsByClassName('allied-shop-row')) {
        let visible = getAlliedItemCategoryVisible(row.dataset.category)
                        && getAlliedItemCurrencyVisible(row.dataset.currency)
        let checkbox = row.querySelector('input[type=checkbox]')

        if (visible) {
            row.classList.remove('is-hidden')
        } else {
            row.classList.add('is-hidden')
        }

        const finished = getAlliedItemFinished(row.dataset.item)
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
    const tbody = document.querySelector('tr.allied-shop-row').parentNode
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
    setAlliedItemCategoryVisible(categoryId, checkbox.checked)
    updateAlliedShopRows()
}
function setAllTypeFilters(isChecked) {
    for (const el of document.getElementsByClassName('type-filter-check')) {
        el.checked = isChecked
        setAlliedItemCategoryVisible(el.dataset.category, isChecked)
    }
    updateAlliedShopRows()
}
function handleCurrencyFilterChecked(event) {
    const checkbox = event.target
    const currencyId = checkbox.dataset.currency
    setAlliedItemCurrencyVisible(currencyId, checkbox.checked)
    updateAlliedShopRows()
}


function handleShopItemChecked(event) {
    const checkbox = event.target
    const itemId = checkbox.dataset.item
    const finished = checkbox.checked
    setAlliedItemFinished(itemId, finished)

    const row = document.querySelector(`tr.allied-shop-row[data-item="${itemId}"]`)
    if (finished) {
        row.classList.add('is-finished')
    } else {
        row.classList.remove('is-finished')
    }
}


function setShowFinished(value) {
  window.alliedsShowFinished = value
  setLocalFlag("alliedshop:config", "showFinished", value)

  if (window.alliedsShowFinished) {
    removeHiddenFinishedStyle('allied-shop-row')
  } else {
    appendHiddenFinishedStyle('allied-shop-row')
  }
  updateAlliedShopRows()
}


document.addEventListener('DOMContentLoaded', async () => {

    // initialize showFinished check
    var checkShowFinished = document.getElementById("check-showFinished");
    const showFinished = getLocalFlag("alliedshop:config", "showFinished")
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

    updateAlliedShopRows()
    sortRows()
})

</script>