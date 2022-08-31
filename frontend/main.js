const { app, ipcMain, Menu, Tray, BrowserWindow } = require('electron')

let win;
let webcamWindow;
let tray = null;

function createWindow() {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        }
    })
    win.loadFile(__dirname + "./main_window/index.html")
    win.on('minimize', function (event) {
        event.preventDefault();
        win.hide();

    });

    win.on('close', function (event) {
        if (!app.isQuiting) {
            event.preventDefault();
            win.hide();
        }
        return false;
    });
}

app.whenReady().then(() => {
    createWindow()

    tray = new Tray('images/img8.jpg')
    const contextMenu = Menu.buildFromTemplate([
        {
            label: 'Quit',
            type: 'normal',
            click: function () {
                app.exit();
            }
        }
    ])
    tray.setToolTip('Sign Language Translator')
    tray.setContextMenu(contextMenu)

    tray.on('double-click', function (e) {
        win.show();
    });

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })

    function createWebcamWindow() {
        webcamWindow = new BrowserWindow({
            width: 800,
            height: 700,
            modal: true,
            show: false,
            parent: win,
            webPreferences: {
                nodeIntegration: true,
                contextIsolation: false,
                enableRemoteModule: true,
            }
        });
        webcamWindow.loadFile(__dirname + "./webcam_window/index.html");

        webcamWindow.once("ready-to-show", () => {
            webcamWindow.show();
        });
    }
    ipcMain.on("openWebcamWindow", () => {
        createWebcamWindow();
    })
})

app.on('window-all-closed', () => {
    app.quit()
})

