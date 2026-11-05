---
layout: quest-table
---
{% assign currents = site.data.aethercurrents.aethercurrents[page.map] %}
{% assign compflgset = site.data.aethercurrents.compflgset[page.map] %}

<!--

<table class="table is-fullwidth">
    <thead>
        <tr>
            {% for i in (0..14) %}
            <th>{{i}}</th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
            {% for i in (0..14) %}
            <td>{% if compflgset[i] != "0" %}{{ compflgset[i] }}{% endif %}</td>
            {% endfor %}
    </tbody>
</table>
-->

<div class="columns">
    <div class="column is-one-quarter">

{% if currents %}
<table class="table">
    <thead>
        <tr>
          <th style="width: 5em">No.</th>
          <th>Coordinates</th>
          <th></th>
        </tr>
    </thead>
    <tbody>
        {% for current in currents %}
        <tr class="quest-row" data-rowid="aethercurrent-{{current.id}}">
            <td>
                <label class="checkbox">
                  <input 
                    type="checkbox" 
                    class="checkbox questCheckbox" 
                    id="completed-aethercurrent-{{current.id}}"
                    onchange="handleQuestChecked('aethercurrent-{{current.id}}')"
                    />
                  #{{forloop.index}}
                </label>
            </td>
            <td>
                {{ current.coords }}
            </td>
            <td>
              {{ current.description }}
              <!--<span>[{{ current.id }}]</span>-->
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endif %}

</div>
    <div class="column is-three-quarters">
        {% if page.currentmap %}
        <img src="{{page.currentmap}}" class="aethercurrent-map" />
        {% endif %}
    </div>
</div>

