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
  <table class="table">
      <thead>
          <tr>
              <th style="width: 5em">No.</th>
              <th>Quest</th>
              <th></th>
              <th>Location</th>
              <th>Unlocks</th>
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
          <td>
            <div class="quest-name">
              <span class="icon"><i class="quest-{{quest.icon}}"></i></span>
              <span class="quest">{{quest.name}}</span>
            </div>
            {% if quest.description %}
            <blockquote>
              {{quest.description}}
            </blockquote>
            {% endif %}
          </td>
          <td>
              Lv.{{quest.level}}
          </td>
          <td>
            issuer...
          </td>
          <td>
            unlocks...
          </td>
          <td>
            requires...
          </td>
        </tr>
        {% endfor %}
      </tbody>
  </table>
</div>
