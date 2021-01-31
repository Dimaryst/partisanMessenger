require('application.css')


window.onLoaded((_, data) => {

  const test_button_action = document.getElementById('test_button')
  test_button_action.addEventListener('click',()=>{
    window.test_button_pushed("Button was pushed")
  })

  // document.getElementById('title').innerHTML = data.appName + ' App'
  // document.getElementById('details').innerHTML = 'built with Electron v' + data.electronVersion
  // document.getElementById('versions').innerHTML = 'running on Node v' + data.nodeVersion + ' and Chromium v' + data.chromiumVersion
})
