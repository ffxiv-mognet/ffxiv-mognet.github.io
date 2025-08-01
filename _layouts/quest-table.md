---
layout: default
---


<div class="container">
  <nav class="level">
      <div class="level-left">
          <p class="level-item">
              <h1 style="margin-bottom: 0" class="title is-3 has-text-centered"><a href="/quests/">Quests</a></h1>
          </p>
          <p class="level-item">
              {% if page.links.previous %}
              <a href="{{ page.links.previous }}">
                <span class="icon">
                  <i class="fas fa-chevron-circle-left"></i>
                </span>
              </a>
              {% endif %}
              <h4 style="margin-bottom: 0" class="subtitle is-4">{{page.title}}</h4>
              {% if page.links.next %}
              <a href="{{ page.links.next }}">
                <span class="icon">
                  <i class="fas fa-chevron-circle-right"></i>
                </span>
              </a>
              {% endif %}
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

  <div class="level">
    <div class="level-left">
      <p class="level-item"></p>
    </div>
    <div class="level-right">
      <p class="level-item">
        <span id="quest-count-remain"></span> / <span id="quest-count-total">{{ page.quests|size}}</span>
      </p>
    </div>
  </div>

  <table class="table is-fullwidth">
      <thead>
          <tr>
              <th style="width: 5em">No.</th>
              <th>Quest</th>
              <th></th>
              <th style="width: 20em">Location</th>
              <th>Unlocks</th>
              <th>Requires</th>
          </tr>
      </thead>
      <tbody>
        {% for quest in page.quests %}
        <tr class="quest-row" data-rowid="{{quest.rowId}}" >
          <td>
            <input 
              type="checkbox" 
              class="checkbox questCheckbox" 
              id="completed-{{quest.rowId}}"
              onchange="handleQuestChecked({{quest.rowId}})"
              />
            <span>#{{quest.partQuestNo}}</span>
          </td>
          <!-- quest -->
          <td class="quest-col">
            <div class="level clickable" onclick="toggleDetail({{quest.rowId}})">
              <div class="level-left">
                <p class="level-item">
                  <span class="icon-text">
                    <span class="icon"><i class="quest-{{quest.icon}}"></i></span>
                    <span class="quest-name">{{quest.name}}</span>
                  </span>
                </p>
              </div>
              <div class="level-right">
                <p class="level-item">
                  <span class="icon"><i id="row-chevron-{{quest.rowId}}" class="row-chevron fas fa-chevron-down"></i></span>
                </p>
              </div>
            </div>
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
          <td class="clickable" onclick="toggleDetail({{quest.rowId}})">
              Lv.{{quest.level}}
          </td>
          <!-- issuer -->
          <td class="clickable" onclick="toggleDetail({{quest.rowId}})">
            <div class="npc">
              {{ quest.issuer.name }}
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
                {% if unlock.link %}<a href="{{unlock.link}}">{% endif %}
                <div>
                    <span class="icon-text">
                        <span class="icon"><i class="{{unlock.type}}"></i></span>
                        <span>{{unlock.name}}</span>
                    </span>
                </div>
                {% if unlock.link %}</a>{% endif %}
              {% endfor %}
          </td>
          <td><!-- requires -->
              {% for required in quest.requires %}
                  {% if required.link %}<a href="{{required.link}}">{% endif %}
                  <div class="quest">
                      <span class="icon-text">
                          <span class="icon"><i class="quest-{{required.icon}}"></i></span>
                          <span>{{required.name}}</span>
                      </span>
                  </div>
                  {% if required.link %}</a>{% endif %}
              {% endfor %}
          </td>
        </tr>
        {% endfor %}
      </tbody>
  </table>
</div>

<script type="text/javascript" src="/js/storage.js"></script>
<script type="text/javascript" src="/js/finished.js"></script>

<script>

window.QUEST_CONFIG_SHOW_FINISHED = "quest:config:showFinished"

document.addEventListener("DOMContentLoaded", async () => {
  var checkShowFinished = document.getElementById("check-showFinished");
  const showFinished = getLocalFlag("", QUEST_CONFIG_SHOW_FINISHED)
  setShowFinished(showFinished)
  checkShowFinished.checked = showFinished
  checkShowFinished.onchange = (evt) => { setShowFinished(evt.target.checked) }

  updateRows();
})

function updateRemainCount() {
  var questCountRemain = document.getElementById("quest-count-remain")

  var checks = document.getElementsByClassName("questCheckbox")
  var finishedCount = 0;
  for (const it of checks) {
    if (it.checked) finishedCount += 1
  }
  questCountRemain.innerHTML = checks.length - finishedCount
}

function setShowFinished(value) {
  window.questsShowFinished = value
  setLocalFlag("", QUEST_CONFIG_SHOW_FINISHED, value)

  if (window.questsShowFinished) {
    removeHiddenFinishedStyle('quest-row')
  } else {
    appendHiddenFinishedStyle('quest-row')
  }
}

function updateRows() {
  const rows = document.getElementsByClassName("quest-row");
  const tbody = rows[0].parentNode
  for (const row of rows) {
    const checkbox = row.getElementsByClassName("checkbox")[0]
    const isFinished = isQuestFinished(row.dataset.rowid)

    if (isFinished) {
        row.classList.add("is-finished")
        checkbox.checked = true
    } else {
        row.classList.remove("is-finished")
        checkbox.checked = false
    }
  }
  updateRemainCount();
}

function toggleDetail(rowId) {
  const chevron = document.getElementById(`row-chevron-${rowId}`)
  const detail = document.getElementById(`quest-detail-${rowId}`)
  const currentIsOpen = chevron.classList.contains("fa-chevron-up")

  // collapse all others
  const details = document.getElementsByClassName('quest-detail')
  for (const it of details) {
    it.classList.add("is-hidden")
  }
  const chevrons = document.getElementsByClassName('row-chevron')
  for (const it of chevrons) {
    it.classList.remove("fa-chevron-up")
    it.classList.add("fa-chevron-down")
  }

  // expand this one
  if (!currentIsOpen) {
    detail.classList.remove("is-hidden")
    chevron.classList.add("fa-chevron-up")
  }
}

function getAllNextSiblings(node) {
  return getAllSiblings(node, 'nextSibling')
}
function getAllPreviousSiblings(node) {
  return getAllSiblings(node, 'previousSibling')
}
function getAllSiblings(node, propertyName) {
  propertyName = propertyName || 'previousSibling'
  const siblings = []
  while (node[propertyName]) {
    if (node[propertyName].nodeType != Node.TEXT_NODE) {
      siblings.push(node[propertyName])
    }
    node = node[propertyName]
  }
  return siblings
}

function handleQuestChecked(rowId) {
  const row = document.querySelector(`[data-rowid="${rowId}"]`)
  const checkbox = document.getElementById(`completed-${rowId}`)

  const nodes = checkbox.checked 
    ? getAllPreviousSiblings(row) 
    : getAllNextSiblings(row)
  nodes.push(row)
  for (var node of nodes) {
    setQuestFinished(node.dataset.rowid, checkbox.checked)
  }

  updateRows();
}
</script>