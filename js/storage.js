

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
function deserializeFromStorage(namespace, key, defaultValue = undefined) {
    const blob = getLocalStorage(namespace, key)
    return blob ? JSON.parse(blob) : defaultValue
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

