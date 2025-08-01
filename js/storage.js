

function keyForLocalStorage(namespace, key) {
    return `${namespace}:${key}`
}
function setLocalStorage(namespace, key, value) {
    return localStorage.setItem(keyForLocalStorage(namespace, key), value)
}
function getLocalStorage(namespace, key) {
    return localStorage.getItem(keyForLocalStorage(namespace, key))
}
function removeLocalStorage(namespace, key) {
    return localStorage.removeItem(keyForLocalStorage(namespace, key))
}
function deserializeFromStorage(namespace, key) {
    return JSON.parse(getLocalStorage(namespace, key))
}
function serializeToStorage(namespace, key, value) {
    setLocalStorage(namespace, key, JSON.stringify(value))
}
function setLocalFlag(namespace, key, value = true) {
    if (!!value) {
        setLocalStorage(namespace, key, "1")
    } else {
        removeLocalStorage(namespace, key)
    }
}
function getLocalFlag(namespace, key) {
    return localStorage.hasOwnProperty(keyForLocalStorage(namespace, key))
}


function setQuestFinished(rowId, isFinished) {
    const namespace = "" // TODO: eventually this becomes active character name
    const key = `quest:finished:${rowId}`
    setLocalFlag(namespace, key, isFinished)
}
function isQuestFinished(rowId) {
    const namespace = "" 
    const key = `quest:finished:${rowId}`
    return getLocalFlag(namespace, key)
}
