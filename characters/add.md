---
layout: with-nav
---

<form id="profile-form">
<div class="field">
  <label class="label">Character Name</label>
  <div class="control">
    <input id="characterName" class="input" type="text" autoFocus>
  </div>
</div>  

<!--
<div class="field">
  <label class="label">Lodestone Character URL</label>
  <div class="control">
    <input id="lodestoneUrl" class="input" type="text" placeholder="https://na.finalfantasyxiv.com/lodestone/character/NNNNN">
  </div>
</div>  
-->

<div class="field is-grouped">
  <div class="control">
    <button class="button is-link is-light">Cancel</button>
  </div>
  <div class="control">
    <button type="submit" class="button is-link" id="save-character" disabled>Save Character</button>
  </div>
</div>
</form>


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
    console.log("submit")
    const profile = saveNewProfile({characterName: nameInput.value})
    setActiveProfile(profile.id)

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