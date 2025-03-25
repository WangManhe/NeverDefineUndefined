#include "mainWindow/mainWindow.h"

#include <QApplication>

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    app.setStyle("windows10");
    MainWindow window;
    window.show();
    return app.exec();
}
