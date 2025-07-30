---
layout: default
---


<div class="container">
  <nav class="level">
      <div class="level-left">
          <p class="level-item">
              <h1 class="title is-3 has-text-centered">Quests</h1>
          </p>
      </div>
      <div class="level-right">
          <p class="level-item">
              <div class="checkboxes">
                  <label class="checkbox">
                      <input type="checkbox" id="check-showFinished"/> 
                      Show Finished
                  </label>
              </div>
          </p>
      </div>
  </nav>
  <table class="table is-fullwidth">
      <thead>
          <tr>
              <th style="width: 5em">No.</th>
              <th>Quest</th>
              <th></th>
              <th>Location</th>
              <th>Duty</th>
              <th>Requires</th>
          </tr>
      </thead>
      <tbody>
        {% for quest in page.quests %}
        <tr class="quest-row" data-rowId="{{quest.rowId}}">
          <td>
            <input type="checkbox" class="checkbox" id="completed-{{entry.index}}"/>
            <span>#{{quest.partQuestNo}}</span>
          </td>
          <!-- quest -->
          <td onclick="toggleDetail({{quest.rowId}})">
            <span class="icon-text">
              <span class="icon"><i class="quest-{{quest.icon}}"></i></span>
              <span class="quest-name">{{quest.name}}</span>
            </span>
            <div id="quest-detail-{{quest.rowId}}" class="quest-detail is-hidden">
              {% for step in quest.steps %}
                <ul class="quest-steps">
                    <li>
                        <input type="checkbox" class="checkbox" id="completed-step-{{quest.rowId}}-{{forloop.index}}"/>
                        <span class="name">{{ step.name }}</span>
                        <span class="tag is-light">
                            {{ step.location}} {{ step.coords }}
                        </span>
                    </li>
                </ul>
              {% endfor %}
              {% if quest.description %}
              <blockquote>
                {{quest.description}}
              </blockquote>
              {% endif %}
            </div>
          </td>
          <!-- level -->
          <td onclick="toggleDetail({{quest.rowId}})">
              Lv.{{quest.level}}
          </td>
          <!-- issuer -->
          <td onclick="toggleDetail({{quest.rowId}})">
            <div class="npc">{{ quest.issuer.name }}
              <span class="tag is-light">
                  {{ quest.issuer.location}} {{ quest.issuer.coords }}
              </span>
            </div>
          </td>
          <td><!-- unlocks -->
              {% if quest.soloDuty %}
              <div>
                  <span class="icon-text">
                      <span class="icon"><i class="solo-duty"></i></span>
                      <span>Solo Duty Lv.{{ quest.soloDuty.levelSync }}</span>
                  </span>
              </div>
              {% endif %}
              {% for unlock in quest.unlocks %}
              <div>
                  <span class="icon-text">
                      <span class="icon"><i class="{{unlock.type}}"></i></span>
                      <span>{{unlock.name}} Lv.{{ unlock.levelSync }}</span>
                  </span>
              </div>
              {% endfor %}
          </td>
          <td><!-- requires -->
              {% for required in quest.requires %}
                  <div class="quest">
                      <span class="icon-text">
                          <span class="icon"><i class="quest-{{required.icon}}"></i></span>
                          <span>{{required.name}}</span> 
                      </span>
                  </div>
              {% endfor %}
          </td>
        </tr>
        {% endfor %}
      </tbody>
  </table>
</div>

<script>
function toggleDetail(rowId) {
  const details = document.getElementsByClassName('quest-detail')
  for (const detail of details) {
    detail.classList.add("is-hidden")
  }

  const detail = document.getElementById(`quest-detail-${rowId}`)
  detail.classList.remove("is-hidden")
}
</script>