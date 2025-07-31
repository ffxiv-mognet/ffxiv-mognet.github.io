

function writeConfigToStorage(keyName, feature, value) {
    const config = deserializeFromStorage(keyName)
    config[feature] = value
    serializeToStorage(keyName, config)
}
function getConfigFromStorage(keyName, feature) {
    const config = deserializeFromStorage(keyName)
    return config[feature]
}



function deserializeFromStorage(keyName) {
    const deserialized = localStorage.getItem(keyName)
    return deserialized ? JSON.parse(deserialized) : {}
}
function serializeToStorage(keyName, finished) {
    const serialized = JSON.stringify(finished || {})
    return localStorage.setItem(keyName, serialized)
}



const QUEST_FINISHED_KEY = 'quests_finished'
function setQuestFinished(rowId, isFinished) {
    const finished = deserializeFromStorage(QUEST_FINISHED_KEY)
    if (isFinished) {
        finished[rowId] = 1
    } else {
        delete finished[rowId]
    }
    serializeToStorage(QUEST_FINISHED_KEY, finished)
}
function isQuestFinished(rowId) {
    return !!deserializeFromStorage(QUEST_FINISHED_KEY)[rowId]
}
