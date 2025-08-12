---
layout: with-nav
title: The Hunt Shops
permalink: /hunts/shops

npcLocations:
  Wilmetta:
    coords: (10.5, 7.4)
    location: Radz-at-Han
  Ilfroy:
    coords: (11.0, 10.8)
    location: Eulmore
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
        <th style="width: 10em">Cost</th>
        <th style="width: 22em">NPC</th>
        <th>Quest</th>
    </tr>
  </thead>
  <tbody>
    {% for shop in site.data.huntShops.shops %}
        {% for item in shop.inventory %}
        {% if item.item.name %}
        <tr class="hunt-shop-row" 
            data-item="{{ item.item.id }}"
            data-currency="{{ item.item.currency.id }}"
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
            <td>{{ item.item.name }}</td>
            <td>{{ item.item.category.name }}</td>
            <td>
              <span class="icon-text">
                {{item.cost}}
                {{item.currency.name}}
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
        {% endif %}
        {% endfor %}
    {% endfor %}
  </tbody>
</table>
