
const NS_PROFILE = "_profile"


function getActiveProfile() {
    const profileId = getLocalStorage(NS_PROFILE, 'active')
    return profileId ? loadProfile(profileId) : undefined
}
function setActiveProfile(profileId) {
    setLocalStorage(NS_PROFILE, "active", profileId)
}

function getAllProfiles() {
    const profileIds = deserializeFromStorage(NS_PROFILE, "all", []).filter(it => it)
    return profileIds.map(loadProfile).filter(it => it)
}

function loadProfile(profileId) {
    return deserializeFromStorage(NS_PROFILE, `profile:${profileId}`) 
}

function saveNewProfile({characterName}) {
    const profileId = idFromName(characterName)
    const profile = {
        id: profileId,
        characterName,
    }

    // save profile
    serializeToStorage(NS_PROFILE, `profile:${profileId}`, profile)

    // add profileId to index 
    const profileList = deserializeFromStorage(NS_PROFILE, "all", [])
    profileList.push(profileId)
    serializeToStorage(NS_PROFILE, "all", profileList)
    return profile
}
function updateProfile(profileId, {characterName}) {
    const profile = {
        id: profileId,
        characterName,
    }
    // save profile
    serializeToStorage(NS_PROFILE, `profile:${profileId}`, profile)
    return profile
}

function removeProfile(profileId) {
    localStorage.removeItem(keyForLocalStorage(NS_PROFILE, `profile:${profileId}`))
    const activeId = getLocalStorage(NS_PROFILE, 'active')
    if (activeId == profileId) {
        localStorage.removeItem(NS_PROFILE, 'active')
    }
}


function idFromName(name) {
    return name.replace(/[\W]+/g,'',).toLowerCase()
}