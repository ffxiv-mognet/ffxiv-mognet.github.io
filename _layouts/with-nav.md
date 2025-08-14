---
layout: default
---


<div class="container">
  <nav class="level">
      <div class="level-left">
          <p class="level-item">
              <h1 style="margin-bottom: 0" class="title is-3 has-text-centered">
                <a href="{{page.brandUrl}}">{{page.brandLabel}}</a>
              </h1>
          </p>
          <p class="level-item">
              {% if page.links.previous %}
              <a href="{{ page.links.previous }}">
                <span class="icon">
                  <i class="fas fa-chevron-circle-left"></i>
                </span>
              </a>
              {% endif %}
              <h4 style="margin-bottom: 0" class="subtitle is-4">{{page.title}}</h4>
              {% if page.links.next %}
              <a href="{{ page.links.next }}">
                <span class="icon">
                  <i class="fas fa-chevron-circle-right"></i>
                </span>
              </a>
              {% endif %}
          </p>
      </div>
      <div class="level-right">
        <p class="level-item">
          <div class="checkboxes">
              <label class="checkbox">
                  <input type="checkbox" id="check-showFinished"/> 
                  Show Finished
              </label>
          </div>
        </p>
        <p class="level-item">
          <div class="dropdown" id="profile-dropdown">
            <div class="dropdown-trigger">
              <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                <span id="profile-active">Switch Character</span>
                <span class="icon is-small">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu" role="menu">
              <div class="dropdown-content">
                <div id="profile-list"> 
                  <a href="#" class="dropdown-item">Another Character</a>
                  <a href="#" class="dropdown-item is-active">Character Name</a>
                </div>
                <hr class="dropdown-divider" />
                <a href="/characters/settings" class="dropdown-item is-hidden" id="profile-settings">Settings</a>
                <a href="/characters/add" class="dropdown-item">Add Character</a>
              </div>
            </div>
          </div>
        </p>
      </div>
  </nav>


{{content}}

<script>
document.addEventListener("DOMContentLoaded", async () => {
  updateProfiles()
})

function updateProfiles() {
  const activeProfile = getActiveProfile()
  const allProfiles = getAllProfiles()

  const profileDropdown = document.getElementById("profile-dropdown")
  const settingsButton = document.getElementById("profile-settings")
  const activeLabel = document.getElementById("profile-active")

  profileDropdown.onclick = () => {
    profileDropdown.classList.toggle("is-active")
  }

  if (activeProfile) {
    activeLabel.innerHTML = activeProfile.characterName
    settingsButton.classList.remove("is-hidden")
  } else {
    activeLabel.innerHTML = 'Select Character'
    settingsButton.classList.add("is-hidden")
  }

  const profileList = document.getElementById("profile-list")
  profileList.innerHTML = '';
  for (const it of allProfiles) {
    const el = document.createElement('a')
    el.classList.add("dropdown-item")
    el.innerHTML = it.characterName
    if (activeProfile && it.id === activeProfile.id) {
      el.classList.add("is-active")
    }
    el.onclick = () => { 
      setActiveProfile(it.id) 
      window.location.reload()
    }
    profileList.appendChild(el)
  }

}
</script>