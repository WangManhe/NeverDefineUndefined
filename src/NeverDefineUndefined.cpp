#include "NeverDefineUndefined.h"

NeverDefineUndefined::NeverDefineUndefined(QWidget* parent)
    : QMainWindow(parent)
    , ui(new Ui_NeverDefineUndefined)
{
    ui->setupUi(this);
}

NeverDefineUndefined::~NeverDefineUndefined()
{
    delete ui; 
}