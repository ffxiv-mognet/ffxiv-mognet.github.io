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
    <button type="button" class="button is-link is-light" onclick="window.history.back()">Cancel</button>
  </div>
  <div class="control">
    <button type="submit" class="button is-link" id="save-character" disabled>Save Character</button>
  </div>
</div>
</form>

{{content}}