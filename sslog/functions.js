//taken from https://tylian.net/sslog/js/functions.js

var CONST_EORZEA = 20.571428571428573;

function getEorzeaTime(date) {
  return new Date(date.getTime() * CONST_EORZEA);
}

function getEarthTime(date) {
  return new Date(date.getTime() / CONST_EORZEA);
}

function getWeather(date) {
    var unixSeconds = parseInt(date.getTime() / 1000);
    var bell = unixSeconds / 175;
    var increment = (bell + 8 - (bell % 8)) % 24;
    var totalDays = ((unixSeconds / 4200) << 32) >>> 0;
    var calcBase = totalDays * 100 + increment;
    var step1 = ((calcBase << 11) ^ calcBase) >>> 0;
    var step2 = ((step1 >>> 8) ^ step1) >>> 0;
    return step2 % 100;
}

function findZoneWeather(rates, date) {
    var weather = getWeather(date)
    for(var i = 0; i < rates.length; i++) {
        if(weather < rates[i].rate) {
            return rates[i].weather;
        }
    }
    return "the fuck";
}

function isLogTimeActive(item, now) {
    now = now || new Date();
    var enow = getEorzeaTime(now);
    var time = enow.getUTCHours() + enow.getUTCMinutes() / 60;

    var start = item.time[0];
    var end = item.time[1];

    return (start <= end && start <= time && time < end) || (start > end && (start <= time || time < end));
}

function isLogWeatherActive(item, now) {
    now = now || new Date();
    var weather = findZoneWeather(item.weatherRate, now);

    return item.weather.indexOf(weather) > -1;
}

function isLogActive(item, now) {
    now = now || new Date();
    return isLogTimeActive(item, now) && isLogWeatherActive(item, now);
}

function getNextActive(item) {
    var enow = getEorzeaTime(new Date());
    enow.setUTCMinutes(0);
    enow.setUTCSeconds(0);

    var now = getEarthTime(enow);
    var timeLength = ((24 + item.time[1]) - item.time[0]) % 24;

    for(var i = 0; i < 10000; i++) {
        enow.setUTCHours(enow.getUTCHours() + (item.time[0] + 24 - enow.getUTCHours()) % 24);
        now.setTime(enow / CONST_EORZEA);
        for(var d = 0; d < timeLength; d++) {
            if(isLogWeatherActive(item, now)) {
                return now;
            }

            enow.setUTCHours(enow.getUTCHours() + 1);
            now.setTime(enow.getTime() / CONST_EORZEA)
        }
    }

    throw new Error('Infinite loop detected!');
}

function getNextActiveEnd(item) {
    var now = isLogActive(item) ? new Date() : getNextActive(item);
    var enow = getEorzeaTime(now);

    enow.setUTCMinutes(0);
    enow.setUTCSeconds(0);

    now.setTime(enow.getTime() / CONST_EORZEA);
    while(enow.getUTCHours() !== item.time[1]) {
        if(!isLogActive(item, now)) {
            return now;
        }

        enow.setUTCHours(enow.getUTCHours() + 1);
        now.setTime(enow.getTime() / CONST_EORZEA)
    }
    return now;
}


function addZero(num) {
  return (num >= 0 && num < 10) ? "0" + num : num + "";
}

function formatTime(dt) {
  var hours24 = dt.getUTCHours();
  var hours = ((hours24 + 11) % 12) + 1;
  return hours + ":" + addZero(dt.getUTCMinutes()) + " " + (hours24 > 11 ? "p.m." : "a.m.");            
}