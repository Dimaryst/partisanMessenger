const path = require('path')
const { Application } = require('spectron')

const appPath = () => {
  switch (process.platform) {
    case 'darwin':
      return path.join(__dirname, '..', '.tmp', 'mac', 'Partisan.app', 'Contents', 'MacOS', 'Partisan')
    case 'linux':
      return path.join(__dirname, '..', '.tmp', 'linux', 'Partisan')
    case 'win32':
      return path.join(__dirname, '..', '.tmp', 'win-unpacked', 'Partisan.exe')
    default:
      throw Error(`Unsupported platform ${process.platform}`)
  }
}
global.app = new Application({ path: appPath() })
