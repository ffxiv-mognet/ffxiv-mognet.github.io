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
                <span class="field">Giver:</span>
                <span class="value">
                    <div class="npc">
                        <span class="name">{{ page.giver }}</span>
                        <span class="location">{{ page.location}} {{ page.coords }}</span>
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
                                <span class="name">{{ step.text }}</span>
                                <span class="location">{{ step.location}} {{ step.coords }}</span>
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