---
layout: profile-form
---


<script>

function validate() {
    const saveButton = document.getElementById("save-character")
    const nameInput = document.getElementById("characterName")
    if (nameInput.value) {
        saveButton.disabled = false
    } else {
        saveButton.disabled = true
    }
}

function submit() {
    const nameInput = document.getElementById("characterName")
    if (!nameInput.value) {
        return
    }

    const profile = saveNewProfile({characterName: nameInput.value})
    if (profile) {
        setActiveProfile(profile.id)
    }
    window.history.back()

    return false;
}

document.addEventListener("DOMContentLoaded", async () => {
    const nameInput = document.getElementById("characterName")
    nameInput.onkeyup = validate
    nameInput.onchange = validate
    validate()

    const form = document.getElementById("profile-form")
    form.onsubmit = submit
})
</script>