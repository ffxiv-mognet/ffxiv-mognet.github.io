---
layout: default
---
<container>
    <h2 class="title is-2">{{page.expansion}}</h2>
    <h3 class="subtitle is-3">Part {{page.partNo}}</h3>
    <div class="columns is-mobile">
        <div class="column is-one-quarter">
                <section class="section quests">
                    <h4 class="title is-4">Chapter {{page.partChapterNo}}</h4>
                    {% for quest in page.quests %}
                    <div class="quest">
                        <span class="icon-text">
                            <span class="icon"><i class="quest-{{quest.icon}}"></i></span>
                            <span>{{quest.partQuestNo}}. {{quest.name}}</span> <span class="level">Lv.{{quest.level}}</span>
                        </span>
                        <ul class="unlocks">
                            {% if quest.soloDuty %}
                            <li>
                                <span class="icon-text">
                                    <span class="icon"><i class="solo-duty"></i></span>
                                    <span>Solo Duty Lv.{{quest.level}}-{{ quest.soloDuty.levelSync }}</span>
                                </span>
                            </li>
                            {% endif %}
                            {% for unlock in quest.unlocks %}
                            <li>
                                <span class="icon-text">
                                    <span class="icon"><i class="{{unlock.type}}"></i></span>
                                    <span>{{unlock.name}} Lv.{{unlock.levelRequired}}-{{unlock.levelSync}}</span>
                                </span>
                            </li>
                            {% endfor %}
                        </ul>
                    </div>
                    {% endfor %}
                </section>
        </div>
        <div class="column">
            <section class="section details">
                {% for q in page.quests %}
                    {% if q.localRowId %}
                        {% assign quest = site.localQuests | where:"localRowId", q.localRowId | first %}
                        {{quest | markdownify}}
                    {% endif %}
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


