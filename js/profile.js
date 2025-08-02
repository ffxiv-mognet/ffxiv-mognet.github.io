
const NS_PROFILE = "_profile"


function getActiveProfile() {
    const profileId = getLocalStorage(NS_PROFILE, 'active')
    return profileId ? loadProfile(profileId) : undefined
}
function setActiveProfile(profileId) {
    setLocalStorage(NS_PROFILE, "active", profileId)
}

function getAllProfiles() {
    const profileIds = deserializeFromStorage(NS_PROFILE, "all", [])
    return profileIds.map(loadProfile)
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

function idFromName(name) {
    return name.replace(/[\W]+/g,'',).toLowerCase()
}