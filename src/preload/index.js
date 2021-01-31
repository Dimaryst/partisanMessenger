// https://electronjs.org/docs/tutorial/security
// Preload File that should be loaded into browser window instead of
// setting nodeIntegration: true for browser window

import {
  ipcRenderer,
} from 'electron'

window.onLoaded = callback => {
  ipcRenderer.on('loaded', callback)
}

window.test_button_pushed = data => {
  alert(data)
}

document.addEventListener('DOMContentLoaded', () => {
  window.addEventListener('offline', () => ipcRenderer.send('offline'))
  window.addEventListener('online', () => ipcRenderer.send('online'))
})

