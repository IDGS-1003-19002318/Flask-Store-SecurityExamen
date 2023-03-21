from wtforms import Form, StringField, IntegerField, FileField


class ProductForm(Form):
    id = IntegerField('Id')
    name = StringField('Nombre')
    price = StringField('Precio')
    stock = IntegerField('Stock')
    description = StringField('Descripcion')
    image = StringField('Imagen')
    #image = FileField('Imagen')