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

FILE = r"C:\PythonPJ\NN\model\mnist_model.pth"
model = torch.load(FILE)
model.eval()
print(model)

img = open_picture_customization()#открывает картинку, переводит в оттенки серого, загружает в тензор
#prediction(img)


from tkinter import*


root = Tk()#окно приложения
root['bg'] = '#fafafa'#задний фон
root.title('Название программы')#название окна
root.wm_attributes('-alpha',0.7)#прозрачность окна
root.geometry('300x250')#размеры окна

root.resizable(width=False, height=False)#если не хотим, чтобы пользователь мог менять размер окна

canvas = Canvas(root,height=300, width=250)#сможем "рисовать" объекты, вывод графич. примитивов
canvas.pack()

frame = Frame(root,bg='red')#рамка, которая содержит в себе другие визуальные компоненты
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)#будет занимать 70 проц по ширине и высоте, и
                                                            #смещен по сторонам на 15 проц

title = Label(frame, text='Текст подсказка', bg='gray', font=40)#указ. какому окну принадлежит надпись, текст, цвет, шрифт
title.pack()#для расположения
btn = Button(frame, text='Кнопка', bg='yellow', command=lambda : prediction(img))#без lambda выполняет 1 раз без нажатия
btn.pack()

loginInput = Entry(frame, bg='white')#текстовое поле
loginInput.pack()

passField = Entry(frame, bg='white', show='*')#когда вводится текст, показываются '*'
passField.pack()

root.mainloop()#цикл
