// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
import path from 'path'
import { app, BrowserWindow, screen, Menu, MenuItem } from 'electron'
import { type } from 'os'

const menuTemplate = [{
    label: 'partisan',
    submenu: [
      {
        role: 'about'
      },
      {type: 'separator'},
      {
        label: 'Quit',
        click() {
          app.quit()
        }
      },
    ]},
    {
    label: 'App',
    submenu:[
      {type: 'separator'},
      {
        label: 'Show my ID',
        click() {
          alert('Not available')
        }
      },
      {
        label: 'Add new contact',
        click() {
          alert('Not available')
        }
      },
    ]
}]

const createWindow = () => {
  const {max_width, max_height} = screen.getPrimaryDisplay().workAreaSize;
  // Create the browser window.

  const menu = new Menu.buildFromTemplate(menuTemplate)
  Menu.setApplicationMenu(menu)

  let win = new BrowserWindow({ 
    show: false,
    backgroundColor: '#2d3436',
    title: CONFIG.name,
    // titleBarStyle: 'hidden',
    width: CONFIG.width,
    height: CONFIG.height,
    minWidth: 800,
    minHeight: 600,
    maxWidth: max_width,
    maxHeight: max_height,
    webPreferences: {
      worldSafeExecuteJavaScript: true,
      preload: path.join(app.getAppPath(), 'preload', 'index.js')
    }
  })

  // and load the index.html of the app.
  win.loadFile('renderer/index.html')

  // Disabling flicker effect
  win.once('ready-to-show', () => {
    win.show()
  })

  // if win.webContents.openDevTools() 

  // send data to renderer process
  win.webContents.on('did-finish-load', () => {
    win.webContents.send('loaded', {
      appName: CONFIG.name,
      electronVersion: process.versions.electron,
      nodeVersion: process.versions.node,
      chromiumVersion: process.versions.chrome
    })
  })

  win.on('closed', () => {
    win = null
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

app.on('before-quit',() => console.log("Exiting..."))

app.whenReady().then(() => console.log("App is running"))
