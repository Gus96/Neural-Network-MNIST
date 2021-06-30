def open_picture_customization():#открывает картинку, переводит в оттенки серого, загружает в тензор
    from PIL import Image
    img = Image.open(r'C:\PythonPJ\NN\pictures\num4.png')
    from PIL import Image, ImageOps
    gray_image = ImageOps.grayscale(img)
    img = gray_image
    from torchvision.transforms import ToTensor
    tens_pic = ToTensor()(img)
    img = tens_pic.view(1, 784)
    return img