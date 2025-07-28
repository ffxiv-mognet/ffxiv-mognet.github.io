---
layout: default
permalink: /sslog
---
<style>
.sslog-row .name {
    font-weight: bold;
}
</style>

<div class="container">
    <h1 class="title is-3 has-text-centered">Sightseeing Log Helper</h1>
    <h2 class="subtitle is-2 has-text-centered" id="current-time">X:XX</h2>
    <table class="table">
        <thead>
            <tr>
                <th style="width: 4em">No.</th>
                <th>Location</th>
                <th>Region</th>
                <th style="width: 9em">Next</th>
                <th style="width: 8em">Conditions</th>
                <th>Emote</th>
            </tr>
        </thead>
        <tbody>
            {% for entry in site.data.sslog.entries %}
            <tr class="sslog-row" data-index="{{entry.index}}">
                <td>
                    <input type="checkbox"/>
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
                    <div class="location">
                        {{entry.location}} 
                    </div>
                </td>
                <td class="nexttime"></td>
                <td>
                    <div class="times">{{entry.time[0]}} to {{entry.time[1]}}</div>
                    <div class="weather">
                    {% for weather in entry.weather %}
                        <img 
                            class="weather-icon" 
                            src="weather-icons/{{weather}}.png" 
                            title="{{site.data.sslog.weatherNames[weather]}}"
                            />
                    {% endfor %}
                    </div>
                </td>
                <td>{{entry.emote}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>


<script type="text/javascript" src="functions.js"></script>
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", async () => {
        setCurrentTime();

        window.sslog = undefined;
        fetch("sslog.json").then(async response => {
            window.sslog = await response.json()
            handleTick();
            startTicker();
        })
    })

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
            const item = itemForIndex(row.dataset.index)
            const isActive = isLogActive(item, now)

            eorzeaTimeCell.innerHTML = formatTimeSpan(item.time)

            if (isActive) {
                row.classList.add("is-selected")
                const goal = getNextActiveEnd(item);
                const pop = Math.ceil((goal.getTime() - Date.now()) / 1000);
                timeCell.innerHTML = humanizeDuration(pop) + ' left';
            } else {
                row.classList.remove("is-selected")
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
</script>