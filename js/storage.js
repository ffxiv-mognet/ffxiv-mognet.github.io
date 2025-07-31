


function readFinishedFromStorage(keyName) {
    const deserialized = localStorage.getItem(keyName)
    return deserialized ? JSON.parse(deserialized) : {}
}
function writeFinishedToStorage(keyName, finished) {
    const serialized = JSON.stringify(finished || {})
    return localStorage.setItem(keyName, serialized)
}



const QUEST_FINISHED_KEY = 'quests_finished'
function setQuestFinished(rowId, isFinished) {
    const finished = readFinishedFromStorage(QUEST_FINISHED_KEY)
    if (isFinished) {
        finished[rowId] = 1
    } else {
        delete finished[rowId]
    }
    writeFinishedToStorage(QUEST_FINISHED_KEY, finished)
}
function isQuestFinished(rowId) {
    return !!readFinishedFromStorage(QUEST_FINISHED_KEY)[rowId]
}
