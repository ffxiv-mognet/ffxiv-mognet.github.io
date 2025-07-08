---
---


<div class="card">
    <div class="card-content">
        <div class="content">
            <h6 class="subtitle is-6">
            <span class="icon-text">
                <span class="icon"><i class="quest-{{page.icon}}"></i></span>
                <span>{{ page.name }}</span> 
                <span class="level">Lv. {{ page.level }}</span>
            </span>
            </h6>
            {% if page.requires %}
            <div class="info-row">
                REQUIRES
                {% for quest in page.requires %}
                    <div class="quest">
                        <span class="icon-text">
                            <span class="icon"><i class="quest-{{quest.icon}}"></i></span>
                            <span>{{quest.name}}</span> 
                        </span>
                    </div>
                {% endfor %}
            </div>
            {% endif %}
            <div class="info-row">
                <span class="field">Starts at:</span>
                <span class="npc">{{ page.issuer.name }}</span>
                <span class="tag is-light">
                    {{ page.issuer.location}} {{ page.issuer.coords }}
                </span>
            </div>
            <div class="info-row">
                    <ul>
                        {% for step in page.steps %}
                        <li>
                            <div class="npc">
                                <span class="name">{{ step.name }}</span>
                                <span class="tag is-light">
                                    {{ step.location}} {{ step.coords }}
                                </span>
                            </div>
                        </li>
                        {% endfor %}
                    </ul>
            </div>
        </div>
    </div>
</div>
{{content}}