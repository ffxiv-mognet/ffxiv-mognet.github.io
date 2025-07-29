---
layout: default
permalink: /sslog
---
<style>
#modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: none;
}
#modal.is-active {
    display: block;
}
.sslog-row .name {
    font-weight: bold;
}

.is-finished {
    text-decoration: line-through;
}
.is-hidden {
    display: none;
}
</style>

<div class="container">
    <nav class="level">
        <div class="level-left">
            <p class="level-item">
                <h1 class="title is-3 has-text-centered">Sightseeing Log Helper</h1>
            </p>
        </div>
        <div class="level-right">
            <p class="level-item">
                <div class="checkboxes">
                    <label class="checkbox">
                        <input type="checkbox" id="check-showAll" checked/> 
                        Show #21..#80 
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" id="check-showFinished"/> 
                        Show Finished
                    </label>
                </div>
            </p>
        </div>
    </nav>
    <h2 class="subtitle is-2 has-text-centered" id="current-time">X:XX</h2>
    <table class="table">
        <thead>
            <tr>
                <th style="width: 5em">No.</th>
                <th>Log Entry</th>
                <th style="width: 20em">Location</th>
                <th style="width: 9em">Active</th>
                <th style="width: 8em">Conditions</th>
                <th>Emote</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            {% for entry in site.data.sslog.entries %}
            <tr class="sslog-row" data-index="{{entry.index}}">
                <td>
                    <input type="checkbox" class="checkbox" id="completed-{{entry.index}}" onchange="handleRowFinished({{entry.index}})"/>
                    <span>#{{entry.index}}</span>
                </td>
                <td>
                    <div class="name">
                          {{ entry.name }}
                    </div>
                    <blockquote>
                        {{entry.description}}
                    </blockquote>
                </td>
                <td>
                    <div class="region">
                      {{entry.region}} ({{entry.position.x}}, {{entry.position.y}})
                    </div>
                    <!--
                    <div class="location">
                        {{entry.location}} 
                    </div>
                    -->
                </td>
                <td class="nexttime"></td>
                <td>
                    <div class="times">{{entry.time[0]}} to {{entry.time[1]}}</div>
                    <div class="weather">
                    {% for weather in entry.weather %}
                        <img 
                            class="weather-icon" 
                            src="/sslog/weather-icons/{{weather}}.png" 
                            title="{{site.data.sslog.weatherNames[weather]}}"
                            />
                    {% endfor %}
                    </div>
                </td>
                <td>{{entry.emote}}</td>
                <td>
                    <button onclick="showModal({{entry.index}})">
                       <span class="icon">
                          <i class="fas fa-image"></i>
                       </span> 
                    </button>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>

<div id="modal" class="container" onclick="closeModal()">
    <div id="modal-image">
    </div>
</div>


<script type="text/javascript" src="/sslog/functions.js"></script>
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", async () => {
        window.sslog_show_finished = false;
        window.sslog_show_all = true;

        setCurrentTime();

        window.sslog = undefined;
        fetch("/sslog/sslog.json").then(async response => {
            window.sslog = await response.json()
            handleTick();
            startTicker();
        })


        setShowFinished(window.sslog_finished_style)
        //setShowAll(window.sslog_show_all)

        var checkShowFinished = document.getElementById("check-showFinished");
        checkShowFinished.onchange = handleShowFinishedChanged

        var checkShowAll = document.getElementById("check-showAll");
        checkShowAll.onchange = handleShowAllChanged
    })

    function handleShowFinishedChanged(evt) {
        setShowFinished(evt.target.checked)
    }
    function handleShowAllChanged(evt) {
        setShowAll(evt.target.checked)
    }

    function setShowFinished(value) {
        window.sslog_show_finished = value

        if (sslog_show_finished) {
            document.head.removeChild(window.sslog_finished_style)
            window.sslog_finished_style = undefined
        } else {
            window.sslog_finished_style = document.createElement("style")
            window.sslog_finished_style.innerHTML = ".sslog-row.is-finished {display:none;}"
            document.head.appendChild(window.sslog_finished_style)
        }
    }

    function setShowAll(value) {
        window.sslog_show_all = value
        updateNextTimes();
    }

    function handleRowFinished(index) {
        const checkbox = document.getElementById(`completed-${index}`)
        setFinished(index, checkbox.checked)
        updateNextTimes();
    }


    function startTicker() {
        window.TICK_TIMER = setInterval(handleTick, 3000)
    }

    function stopTicker() {
        clearTimeout(window.TICK_TIMER)
    }

    function handleTick() {
        setCurrentTime();
        updateNextTimes();
    }
    function setCurrentTime() {
        const timestr = formatTime(getEorzeaTime(new Date()))
        const el = document.getElementById("current-time")
        el.innerHTML = timestr
    }
    function updateNextTimes() {
        const now = new Date()
        const rows = document.getElementsByClassName("sslog-row");
        const tbody = rows[0].parentNode
        for (const row of rows) {
            const timeCell = row.getElementsByClassName("nexttime")[0]
            const eorzeaTimeCell = row.getElementsByClassName("times")[0]
            const checkbox = row.getElementsByClassName("checkbox")[0]
            const item = itemForIndex(row.dataset.index)
            const isActive = isLogActive(item, now)
            const isFinished = getFinished(row.dataset.index)
            if (isFinished) {
                row.classList.add("is-finished")
                checkbox.checked = true
            } else {
                row.classList.remove("is-finished")
                checkbox.checked = false
            }

            if (window.sslog_show_all === false && item.index > 20) {
                row.classList.add("is-hidden")
            } else {
                row.classList.remove("is-hidden")
            }

            eorzeaTimeCell.innerHTML = formatTimeSpan(item.time)

            if (isActive) {
                row.classList.add("is-info")
                const goal = getNextActiveEnd(item);
                const pop = Math.ceil((goal.getTime() - Date.now()) / 1000);
                timeCell.innerHTML = humanizeDuration(pop) + ' left';
            } else {
                row.classList.remove("is-info")
                const goal = getNextActive(item)
                const pop = Math.ceil((goal.getTime() - Date.now()) / 1000);
                timeCell.innerHTML = 'in ' + humanizeDuration(pop);
            }
        }
        sortRows(tbody);
    }

    function itemForIndex(index) {
        for (const it of window.sslog.entries) {
            if (it.index == index) return it
        }
    }

    function sortRows(tbody) {
        const now = new Date()
        Array.from(tbody.children)
            .sort((rowA, rowB) => { 
                const a = itemForIndex(rowA.dataset.index)
                const b = itemForIndex(rowB.dataset.index)
                const aActive = isLogActive(a, now)
                const bActive = isLogActive(b, now)
                if (aActive && bActive) {
                    const aEnd = getNextActiveEnd(a)
                    const bEnd = getNextActiveEnd(b)
                    if (aEnd == bEnd) {
                        return rowB.dataset.index - rowA.dataset.index
                    }
                    return aEnd - bEnd
                }
                else if (!aActive && !bActive) {
                    const aNext = getNextActive(a)
                    const bNext = getNextActive(b)
                    return aNext - bNext
                }
                else if (aActive) return -1
                else if (bActive) return 1
            })
            .forEach(it => tbody.appendChild(it))
    }

    function showModal(index) {
        const item = itemForIndex(index)

        const modal = document.getElementById("modal");
        console.log("show", item, modal)
        modal.classList.add("is-active")

        const img = document.createElement("img")
        img.setAttribute("src", item.image)

        const wrapper = document.getElementById("modal-image")
        wrapper.innerHTML = ''
        wrapper.appendChild(img)
    }
    function closeModal() {
        const modal = document.getElementById("modal");
        modal.classList.remove("is-active")
    }



</script>