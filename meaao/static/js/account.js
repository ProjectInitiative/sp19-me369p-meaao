let curr_pass = document.querySelector('[name="current-password"]')
let new_pass1 = document.querySelector('[name="new-password1"]')
let new_pass2 = document.querySelector('[name="new-password2"]')

document.querySelector('#change-password').addEventListener('submit', function (event) {
  // @ts-ignore
  if (new_pass1.value.trim() != new_pass2.value.trim()) {
    event.preventDefault()
    alert('New password does not match with confirmation')
  // @ts-ignore
  } else if (curr_pass.value.trim() == new_pass1.value.trim()) {
    event.preventDefault()
    alert('New password cannot be the same as old password')
  // @ts-ignore
  } else if (new_pass1.value.trim().length === 0) {
    event.preventDefault()
    alert('New password must not be empty')
  }
})
