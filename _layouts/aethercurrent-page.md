---
layout: quest-table
---
{% assign currents = site.data.aethercurrents.aethercurrents[page.map] %}




<table class="table">
    <thead>
        <tr>
          <th style="width: 5em">No.</th>
          <th>Coordinates</th>
          <th style="width: 20em"></th>
        </tr>
    </thead>
    <tbody>
        {% for current in currents %}
        <tr class="aethercurrent-row" data-rowid="{{current.id}}">
            <td>
                <label class="checkbox">
                  <input 
                    type="checkbox" 
                    class="checkbox questCheckbox" 
                    id="aethercurrent-complete-{{current.id}}"
                    onchange="handleAetherCurrentChecked({{current.id}})"
                    />
                  #{{forloop.index}}
                </label>
            </td>
            <td>
                {{ current.coords }}
            </td>
            <td>
              {{ current.description }}
              <span>[{{ current.id }}]</span>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>