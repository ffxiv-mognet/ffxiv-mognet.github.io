---
layout: with-nav
---

<div class="container">
    {% for section in site.data.journal.sections %}
    {% if section.visible %}
    <section class="section">
        <h1 class="title">{{section.name}}</h1>
        {% for category in section.categories %}
        <div>
            <strong>{{category.name}}</strong>
            <ul class="list">
                {% for genre in category.genres %}
                        <li class="list-item">
                            <a href="/journal/{{section.name|slugify}}/{{genre.name|slugify}}">{{ genre.name }}</a>
                        </li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </section>
    {% endif %}
    {% endfor %}
</div>