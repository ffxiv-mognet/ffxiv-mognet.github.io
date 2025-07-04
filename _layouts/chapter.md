---
layout: default
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
                            <span>{{quest.partQuestNo}}. {{quest.name}}</span> <span class="level">Lv. {{quest.level}}</span>
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
                    {% if q.rowId %}
                        {% assign quest = site.quests | where:"rowId", q.rowId | first %}
                        {{quest | markdownify}}
                    {% endif %}
                {% endfor %}
            </section>
        </div>
    </div>
    {{ content}}
</container>


