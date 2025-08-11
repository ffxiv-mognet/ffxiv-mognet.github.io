---
layout: profile-form
---

<button class="button is-danger" onclick="handleClickRemove()">Remove Character</button>

<script>

function handleClickRemove() {
    const active = getActiveProfile()
    if (active && confirm(`Are you sure you want to permanently remove ${active.characterName} and all their progress?`)) {
        removeProfile(active.id)
        window.history.back()
    }
}

function validate() {
    const active = getActiveProfile()
    const saveButton = document.getElementById("save-character")
    const nameInput = document.getElementById("characterName")
    if (nameInput.value && nameInput.value != active.characterName) {
        saveButton.disabled = false
        return true
    } else {
        saveButton.disabled = true
        return false
    }
}

function submit() {
    const active = getActiveProfile()
    const nameInput = document.getElementById("characterName")
    if (!validate()) {
        return
    }

    const profile = updateProfile(active.id, {characterName: nameInput.value})
    window.history.back()

    return false;
}

document.addEventListener("DOMContentLoaded", async () => {
    const active = getActiveProfile()
    if (!active) {
        window.history.back()
    }

    const nameInput = document.getElementById("characterName")

    nameInput.value = active.characterName
    nameInput.onkeyup = validate
    nameInput.onchange = validate
    validate()

    const form = document.getElementById("profile-form")
    form.onsubmit = submit
})
</script>