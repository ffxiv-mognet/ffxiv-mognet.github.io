---
---


<div class="card">
    <div class="card-content">
        <div class="content">
            <h6 class="subtitle is-6">
            <span class="icon-text">
                <span class="icon"><i class="quest-msq"></i></span>
                <span>{{ page.name }}</span> 
                <span class="level">Lv. {{ page.level }}</span>
            </span>
            </h6>
            <div class="info-row">
                <span class="field">Issuer:</span>
                <span class="value">
                    <div class="npc">
                        <span class="name">{{ page.issuer.name }}</span>
                        <span class="location">{{ page.issuer.location}} {{ page.issuer.coords }}</span>
                    </div>
                </span>
            </div>
            <div class="info-row">
                <span class="field">Steps</span>
                <span class="value">
                    <ul>
                        {% for step in page.steps %}
                        <li>
                            <div class="npc">
                                <span class="name">{{ step.name }}</span>
                                {% if step.location %}
                                <span class="location">{{ step.location}} {{ step.coords }}</span>
                                {% endif %}
                            </div>
                        </li>
                        {% endfor %}
                    </ul>
                </span>
            </div>
        </div>
    </div>
</div>

{{content}}