window.HIDDEN_FINISHED_STYLES = {}

function appendHiddenFinishedStyle(className) {
  const el = document.createElement("style")
  el.innerHTML = `.${className}.is-finished {display:none;}`
  document.head.appendChild(el)
  window.HIDDEN_FINISHED_STYLES[className] = el
  return el
}
function removeHiddenFinishedStyle(className) {
  var style = window.HIDDEN_FINISHED_STYLES[className]
  if (style) {
    document.head.removeChild(style)
    delete window.HIDDEN_FINISHED_STYLES[className]
  }
}

function setQuestFinished(rowId, isFinished) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `quest:finished:${rowId}`
    setLocalFlag(namespace, key, isFinished)
}
function isQuestFinished(rowId) {
    const namespace = getLocalStorage(NS_PROFILE, 'active') || ""
    const key = `quest:finished:${rowId}`
    return getLocalFlag(namespace, key)
}
