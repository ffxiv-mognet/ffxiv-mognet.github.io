---
permalink: /clock
title: Eorzea Hunt Clock
---

<style>
.huntTime {
    color: rgb(255, 255, 255);
    background-color: rgb(232, 91, 88);
    font-family: Nunito, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-weight: 700;
    padding: 6px 4px 4px 6px;
    text-shadow: rgba(0, 0, 0, 0.85) 1px 1px 1px 1px;
    border-radius: 800px 0 0 800px;
}
.offsetLabel {
    text-align: right !important;
    padding: 6px 0 0 0 !important;
    border: none !important;
}

table.huntClock {
    margin: auto;
}
.huntClock td.clock {
    text-align: center;
}

.clockFace {
    font-size: 24px;
    border-width: 1px;
    border-style: solid;
    border-color: black;
    border-radius: 4px;
    padding: 4px;
}
.clockFace .clockLabel {
    font-size: 12px;
    text-align: center;
    position: relative;
    top: -10px;
    background-color: white;
}
.clockFace .clock {
    position: relative;
    top: -5px;
}

@media (prefers-color-scheme: dark) {
  .clockFace {
    border-color: white;
  }
  .clockFace .clockLabel {
    background-color: black;
  }
}
.settings {
    margin: 8px;
}
.text-setting input {
    width: 5em;
    margin-left: 4px;
    margin-right: 20px;
}
.text-setting margin
</style>

<div class="container">
    <div class="level settings">
        <div class="level-left">
        </div>
        <div class="level-right toggled-setting is-hidden">
            <p class="level-item">
                <label class="text-setting">
                    Pull Time: 
                    <input type="text" value="5m" id="config-pulltime" onchange="handleSettingsChanged()" />
                </label>
                <label class="text-setting">
                    Interval: 
                    <input type="text" value="30s" id="config-interval" onchange="handleSettingsChanged()" />
                </label>
                <label class="checkbox" style="margin-left: auto">
                    24hr <input type="checkbox" id="config-24hr" onchange="handleSettingsChanged()"/>
                </label>
            </p>
        </div>
        <div class="level-right">
           <span class="icon is-small clickable" onclick="handleClickCog()">
               <i class="fas fa-cog" aria-hidden="true"></i>
           </span>
        </div>
    </div>
    <section class="section">
        <table class="table is-striped is-hoverable huntClock">
            <thead>
                <tr>
                    <td class="offsetLabel"></td>
                    <td>
                        <div class="clockFace">
                            <div class="clockLabel">Eorzea</div>
                            <div class="clock eorzea" data-offset="0"></div>
                        </div>
                    </td>
                    <td>
                        <div class="clockFace">
                            <div class="clockLabel">Earth</div>
                            <div class="clock local" data-offset="0"></div>
                        </div>
                    </td>
                </tr>
            </thead>
            <tbody id="clock-body">
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">4m 30s</span> </td>
                    <td class="clock eorzea" data-offset="30"></td>
                    <td class="clock world" data-offset="30"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">4m</span> </td>
                    <td class="clock eorzea" data-offset="60"></td>
                    <td class="clock world" data-offset="60"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">3m 30s</span> </td>
                    <td class="clock eorzea" data-offset="90"></td>
                    <td class="clock world" data-offset="90"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">3m</span> </td>
                    <td class="clock eorzea" data-offset="120"></td>
                    <td class="clock world" data-offset="120"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">2m 30s</span> </td>
                    <td class="clock eorzea" data-offset="150"></td>
                    <td class="clock world" data-offset="150"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">2m</span> </td>
                    <td class="clock eorzea" data-offset="180"></td>
                    <td class="clock world" data-offset="180"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">1m 30s</span> </td>
                    <td class="clock eorzea" data-offset="210"></td>
                    <td class="clock world" data-offset="210"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">1m</span> </td>
                    <td class="clock eorzea" data-offset="240"></td>
                    <td class="clock world" data-offset="240"></td>
                </tr>
                <tr>
                    <td class="offsetLabel"> <span class="huntTime">30s</span> </td>
                    <td class="clock eorzea" data-offset="270"></td>
                    <td class="clock world" data-offset="270"></td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td></td>
                    <td>
                        <div class="clockFace">
                            <div class="clockLabel" id="final-label">5min PT</div>
                            <div class="clock eorzea" id="final-clock" data-offset="300"></div>
                        </div>
                    </td>
                    <td></td>
                </tr>
            </tfoot>
        </table>
    </section>
</div>


<template id="tmpl-clock-row">
    <tr>
        <td class="offsetLabel"> <span class="huntTime">2m</span> </td>
        <td class="clock eorzea" data-offset="180"></td>
        <td class="clock world" data-offset="180"></td>
    </tr>
</template>

<script type="text/javascript">

window.TICK_INTERVAL_MS = 3000
window.TICK_TIMER = undefined
window.CONFIG_KEY_24HRS = '_huntclock:24hr'
window.CONFIG_KEY_PULLTIME = '_huntclock:pulltime'
window.CONFIG_KEY_INTERVAL = '_huntclock:interval'

document.addEventListener("DOMContentLoaded", async () => {
    const check = document.getElementById('config-24hr')
    check.checked = getLocalFlag(CONFIG_KEY_24HRS)

    const ptInput = document.getElementById('config-pulltime')
    const ptSaved = localStorage.getItem(CONFIG_KEY_PULLTIME)
    if (ptSaved) {
        ptInput.value = formatDuration(ptSaved)
    }

    const intervalInput = document.getElementById('config-interval')
    const intervalSaved = localStorage.getItem(CONFIG_KEY_INTERVAL)
    if (intervalSaved) {
        intervalInput.value = formatDuration(intervalSaved)
    }

    if (ptSaved || intervalSaved) {
        redrawClocks();
    }


    handleTick();
    startTicker();
})


function updateClocks(earthTime) {
    const clocks = document.getElementsByClassName('clock')
    const is24Hour = getLocalFlag(CONFIG_KEY_24HRS)
    for (const clockEl of clocks) {
        const offset = Number(clockEl.dataset.offset || "0")
        const adjusted = new Date(earthTime)
        adjusted.setSeconds(adjusted.getSeconds() + offset)

        if (clockEl.classList.contains('eorzea')) {
            const ezt = getEorzeaTime(adjusted)
            clockEl.innerHTML = formatTime(ezt.getUTCHours(), ezt.getUTCMinutes(), is24Hour)
        } 
        else if (clockEl.classList.contains('world')) {
            const m = String(adjusted.getMinutes()).padStart(2, "0")
            clockEl.innerHTML = `XX:${m}`
        }
        else {
            clockEl.innerHTML = formatTime(adjusted.getHours(), adjusted.getMinutes(), is24Hour)
        }
    }
}



function startTicker() {
    window.TICK_TIMER = setInterval(handleTick, TICK_INTERVAL_MS)
}

function stopTicker() {
    if (window.TICK_TIMER) {
        clearInterval(window.TICK_TIMER)
    }
}

function handleTick() {
    const now = new Date()
    updateClocks(now)
}

function formatTime(hrs, mins, is24Hour = true)  {
    const m = String(mins).padStart(2, "0")
    if (is24Hour) {
        const h = String(hrs).padStart(2, "0")
        return `${h}:${m}`
    } else {
        return `${hrs > 12 ? hrs - 12 : hrs}:${m} ${hrs > 11 ? 'p': 'a'}m`
    }
}

var CONST_EORZEA = 20.571428571428573;

function getEorzeaTime(date) {
  return new Date(date.getTime() * CONST_EORZEA);
}

function getEarthTime(date) {
  return new Date(date.getTime() / CONST_EORZEA);
}

function parseDuration(s) {
    const matches = s.match(/(\d+)\s*(\w?)/)
    const units = {
        's': 1,
        'm': 60,
    }
    if (!matches) return undefined

    const d = Number(matches[1])
    const unit = matches[2].toLowerCase() || 's'
    const value = d * units[unit];
    return {
        'seconds': value,
        'unit': unit,
        'value': `${d}${unit}`
    }
}

function formatDuration(seconds) {
    const m = Math.floor(seconds / 60)
    const s = seconds % 60
    return (m > 0 ? `${m}m` : '') + (s > 0 ? ` ${s}s` : '')
}


function handleSettingsChanged() {
    const checkbox = document.getElementById('config-24hr')
    setLocalFlag(window.CONFIG_KEY_24HRS, checkbox.checked)

    const ptInput = document.getElementById('config-pulltime')
    const pt = parseDuration(ptInput.value)
    console.log("pt", pt)
    ptInput.value = pt.value
    ptInput.dataset.seconds = pt.seconds
    localStorage.setItem(CONFIG_KEY_PULLTIME, pt.seconds)

    const intervalInput = document.getElementById('config-interval')
    const interval = parseDuration(intervalInput.value)
    intervalInput.value = interval.value
    intervalInput.dataset.seconds = interval.seconds
    localStorage.setItem(CONFIG_KEY_INTERVAL, interval.seconds)

    redrawClocks()
    handleTick()
}

function redrawClocks() {
    const tbody = document.getElementById('clock-body')
    tbody.innerHTML = ''

    const template = document.querySelector('#tmpl-clock-row')

    const interval = Number(localStorage.getItem(CONFIG_KEY_INTERVAL))
    const ptSeconds = Number(localStorage.getItem(CONFIG_KEY_PULLTIME))

    let t = ptSeconds - interval
    while (t > 0) {
        const row = template.content.cloneNode(true)
        const huntTime = row.querySelector('.huntTime')
        huntTime.innerHTML = formatDuration(t)

        const eorzeaTime = row.querySelector('.clock.eorzea')
        const worldTime = row.querySelector('.clock.world')
        eorzeaTime.dataset.offset = ptSeconds - t
        worldTime.dataset.offset = ptSeconds - t
        tbody.appendChild(row)

        t -= interval
    }

    const label = document.querySelector('#final-label')
    label.innerHTML = `${formatDuration(ptSeconds)} PT`
    const ptClock = document.querySelector('#final-clock')
    ptClock.dataset.offset = ptSeconds
}

function setLocalFlag(key, value = true) {
    if (!!value) {
        localStorage.setItem(key, value, "1")
    } else {
        localStorage.removeItem(key, value)
    }
}
function getLocalFlag(key) {
    return localStorage.hasOwnProperty(key)
}

function handleClickCog() {
    const els = document.getElementsByClassName('toggled-setting');
    for (const el of els) {
        el.classList.toggle("is-hidden")
    }
}
</script>