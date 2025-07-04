---
layout: default
expansion: A Realm Reborn
partNo: 2
partChapterNo: 1
title: A Realm Reborn - Part 2 - Chapter 1
permalink: /guide/a-realm-reborn/part2/chapter1
quests:
  - name: Hall of the Novice
    level: 15
    type: novice
  - name: It's Probably Pirates
    dungeon: Satasha
    level: 15
    type: msq
    questId: 65781
  - name: Call of the Forest
    level: 15
    type: msq
  - name: Fire in the Gloom
    level: 16
    dungeon: The Tam-Tara Deepcroft
    type: msq
  - name: Call of the Desert
    level: 16
    type: msq
  - name: Into a Copper Hell
    level: 17
    type: msq
    dungeon: Copperbell Mines
    hasSoloDuty: true
  - name: The Scions of the Seventh Dawn
    level: 17
    type: msq
---

<container>
    <h2 class="title is-2">{{page.expansion}}</h2>
    <h3 class="subtitle is-3">Part {{page.partNo}}</h3>
    <div class="columns is-mobile">
        <div class="column is-two-fifths">
                <section class="section quests">
                    <h4 class="title is-4">Chapter {{page.partChapterNo}}</h4>
                    {% for quest in page.quests %}
                    <div class="quest msq">
                        <span class="icon-text">
                            <span class="icon"><i class="quest-{{quest.type}}"></i></span>
                            <span>{{quest.name}}</span> <span class="level">Lv. {{quest.level}}</span>
                        </span>
                        <ul class="unlocks">
                            {% if quest.hasSoloDuty %}
                            <li>
                                <span class="icon-text">
                                    <span class="icon"><i class="solo-duty"></i></span>
                                    <span>Solo Duty</span>
                                </span>
                            </li>
                            {% endif %}
                            {% if quest.dungeon %}
                            <li>
                                <span class="icon-text">
                                    <span class="icon"><i class="dungeon"></i></span>
                                    <span>{{quest.dungeon}}</span>
                                </span>
                            </li>
                            {% endif %}
                        </ul>
                    </div>
                    {% endfor %}
                </section>
        </div>
        <div class="column">
            <section class="section details">
                {% for q in page.quests %}
                    {% if q.questId %}
                        {% assign quest = site.quests | where:"questId", q.questId | first %}
                        {{quest.content | markdownify}}
                    {% endif %}
                {% endfor %}
            </section>
        </div>
    </div>
</container>
