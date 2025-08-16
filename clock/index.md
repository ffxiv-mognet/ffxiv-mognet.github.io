---
permalink: /clock
title: Eorzea Hunt Clock
---

<style>
.huntTime {
    background-color: rgb(232, 91, 88);
    font-family: Nunito, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-weight: 700;
    padding: 6px 4px 4px 6px;
    color: rgb(255, 255, 255);
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
    border: 1px solid black;
    border-radius: 4px;
    padding: 4px;
}
.clockFace .clockLabel {
    font-size: 12px;
    text-align: center;
    position: relative;
    top: -10px;
    background: white;
}
.clockFace .clock {
    position: relative;
    top: -5px;
}
</style>

<div class="container">
    <div class="is-flex">
        <label class="checkbox" style="margin-left: auto">
            24hr <input type="checkbox" id="config-24hr" onchange="handle24HourChanged(event)"/>
        </label>
    </div>
    <section class="section">
        <table class="table is-striped is-hoverable huntClock">
            <tbody>
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
                <tr>
                    <td></td>
                    <td>
                        <div class="clockFace">
                            <div class="clockLabel">5min PT</div>
                            <div class="clock eorzea" data-offset="300"></div>
                        </div>
                    </td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </section>
</div>

<script type="text/javascript">

window.TICK_INTERVAL_MS = 3000
window.TICK_TIMER = undefined
window.CONFIG_KEY_24HRS = '_huntclock:24hr'

document.addEventListener("DOMContentLoaded", async () => {
    const check = document.getElementById('config-24hr')
    check.checked = getLocalFlag(CONFIG_KEY_24HRS)

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
        return `${hrs % 12}:${m} ${hrs > 11 ? 'p': 'a'}m`
    }
}

var CONST_EORZEA = 20.571428571428573;

function getEorzeaTime(date) {
  return new Date(date.getTime() * CONST_EORZEA);
}

function getEarthTime(date) {
  return new Date(date.getTime() / CONST_EORZEA);
}


function handle24HourChanged(evt) {
    setLocalFlag(window.CONFIG_KEY_24HRS, evt.target.checked)
    handleTick()
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
</script>