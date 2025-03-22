#pragma once
#include "ui_NeverDefineUndefined.h"
#include <QMainWindow>

class NeverDefineUndefined : public QMainWindow {
    Q_OBJECT
    
public:
    NeverDefineUndefined(QWidget* parent = nullptr);
    ~NeverDefineUndefined();

private:
    Ui_NeverDefineUndefined* ui;
};