---
layout: quests-with-shops
---

<table class="table">
  <thead>
      <tr>
        <th>Count</th>
        <th>Totem</th>
        <th>Extreme Trial</th>
        <th>Whistle</th>
      </tr>
  </thead>
  <tbody>
    {% for totem in page.totems %}
    <tr class="totem-row" 
        data-totem="{{totem.totem.id}}"
        data-item="{{totem.item.id}}"
        >
      <td>
        <input 
          type="number" 
          class="totem-count"
          value="" 
          min="0" 
          max="99"
          data-totem="{{totem.totem.id}}"
          onchange="handleTotemCountChanged(event)"
          />
      </td>
      <td>{{ totem.totem.name }}</td>
      <td>
        <div>
            <span class="icon-text">
                <span class="icon"><i class="{{totem.trial.type}}"></i></span>
                <span>{{totem.trial.name}}</span>
            </span>
        </div>
      </td>
      <td>
        {{totem.item.name}}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>


<script>
function handleTotemCountChanged(event) {
    const input = event.target
    const totemId = input.dataset.totem
    setTotemCount(totemId, input.value)
}
function getTotemCount(totemId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `mount:totem:${totemId}`
    return getLocalStorage(namespace, key) || 0
}
function setTotemCount(totemId, count) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `mount:totem:${totemId}`
    return setLocalStorage(namespace, key, count)
}

function updateTotemRows() {
    for (var row of document.getElementsByClassName('totem-row')) {
        let input = row.querySelector('input[type=number]')

        const finished = getItemFinished(row.dataset.item)
        const count = getTotemCount(row.dataset.totem)

        input.value = count

        if (finished) {
            row.classList.add('is-finished')
        } else {
            row.classList.remove('is-finished')
        }
    }

}

function setShowTotemFinished(value) {
  if (value) {
    removeHiddenFinishedStyle('totem-row')
  } else {
    appendHiddenFinishedStyle('totem-row')
  }
  updateTotemRows()
}

document.addEventListener('DOMContentLoaded', async () => {
    // initialize showFinished check
    const showFinished = getLocalFlag("quest:config", "showFinished")
    setShowTotemFinished(showFinished)
    var checkShowFinished = document.getElementById("check-showFinished");
    checkShowFinished.addEventListener('change', (evt) => {
        setShowTotemFinished(evt.target.checked)
    })


    updateTotemRows()
})
</script>