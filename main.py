from 纹理混合界面UI import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QWidget,QMainWindow,QLineEdit
import sys
from PyQt5.QtGui import QIcon
import CyFunctionLibrary
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("com.example.myapp")
"""全局变量"""
Silder_Value = 0
class MainWindow(QMainWindow):
    def __init__(self,*args, **kwargs):
        super().__init__(
        )
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        app_icon = QtGui.QIcon()
        app_icon.addFile('A:\PROJECT_WORKS\PYTHON_PROJECT\TextureBlendTool\ICON16.ico', QtCore.QSize(16, 16))
        app_icon.addFile('A:\PROJECT_WORKS\PYTHON_PROJECT\TextureBlendTool\ICON.ico', QtCore.QSize(32, 32))
        # app_icon.addFile('ICON64.ico', QtCore.QSize(64, 64))
        # app_icon.addFile('ICON128.ico', QtCore.QSize(128, 128))
        app_icon.addFile('A:\PROJECT_WORKS\PYTHON_PROJECT\TextureBlendTool\QT2.ico', QtCore.QSize(256, 256))
        # app.setWindowIcon(QIcon("./ICON.ico"))
        self.setWindowIcon(app_icon)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Final_Img_R = QPixmap("")
        self.Final_Img_g = QPixmap("")
        self.Final_Img_B = QPixmap("")
        self.Final_Img_A = QPixmap("")
        self.Null_Img = QPixmap("")
#

        '''输入纹理通道阶段'''
        self.ui.Image01_Button_R.clicked.connect(self.F_Image01_Button_R)  #通道按钮
        self.ui.Image01_Button_G.clicked.connect(self.F_Image01_Button_G)  #通道按钮
        self.ui.Image01_Button_B.clicked.connect(self.F_Image01_Button_B)  #通道按钮
        self.ui.Image01_Button_A.clicked.connect(self.F_Image01_Button_A)  #通道按钮
        self.ui.Image01_Button_Clear.clicked.connect(self.F_Image01_Button_Clear)  #清除纹理按钮
        self.ui.Image01_Button_CopyPath.clicked.connect(self.F_Image01_Button_CopyPath) #复制区域纹理

        self.ui.Image02_Button_R.clicked.connect(self.F_Image02_Button_R)  #通道按钮
        self.ui.Image02_Button_G.clicked.connect(self.F_Image02_Button_G)  #通道按钮
        self.ui.Image02_Button_B.clicked.connect(self.F_Image02_Button_B)  #通道按钮
        self.ui.Image02_Button_A.clicked.connect(self.F_Image02_Button_A)  #通道按钮
        self.ui.Image02_Button_Clear.clicked.connect(self.F_Image02_Button_Clear)  #清除纹理按钮
        self.ui.Image02_Button_CopyPath.clicked.connect(self.F_Image02_Button_CopyPath) #复制区域纹理

        self.ui.Image03_Button_R.clicked.connect(self.F_Image03_Button_R)  #通道按钮
        self.ui.Image03_Button_G.clicked.connect(self.F_Image03_Button_G)  #通道按钮
        self.ui.Image03_Button_B.clicked.connect(self.F_Image03_Button_B)  #通道按钮
        self.ui.Image03_Button_A.clicked.connect(self.F_Image03_Button_A)  #通道按钮
        self.ui.Image03_Button_Clear.clicked.connect(self.F_Image03_Button_Clear)  #清除纹理按钮
        self.ui.Image03_Button_CopyPath.clicked.connect(self.F_Image03_Button_CopyPath) #复制区域纹理

        self.ui.Image04_Button_R.clicked.connect(self.F_Image04_Button_R)  #通道按钮
        self.ui.Image04_Button_G.clicked.connect(self.F_Image04_Button_G)  #通道按钮
        self.ui.Image04_Button_B.clicked.connect(self.F_Image04_Button_B)  #通道按钮
        self.ui.Image04_Button_A.clicked.connect(self.F_Image04_Button_A)  #通道按钮
        self.ui.Image04_Button_Clear.clicked.connect(self.F_Image04_Button_Clear)  #清除纹理按钮
        self.ui.Image04_Button_CopyPath.clicked.connect(self.F_Image04_Button_CopyPath) #复制区域纹理

        self.ui.Export_Button_PaintWhite.clicked.connect(self.F_Export_Button_PaintWhite) #填充单通道白色按钮
        self.ui.Export_Button_PaintBlack.clicked.connect(self.F_Export_Button_PaintBlack) #填充单通道黑色按钮
        self.ui.horizontalSlider.valueChanged.connect(self.F_horizontalSlider)            #填充自定义颜色(滑动条控制)
        self.ui.Export_Button_PaintCustomColor.clicked.connect(self.F_Export_Button_PaintCustomColor)#填充自定义颜色按钮
        self.ui.Export_Button_ClearAllChannel.clicked.connect(self.F_Export_Button_ClearAllChannel)#清除所有通道按钮
        self.ui.Export_Button_ClearAllTexture.clicked.connect(self.F_Export_Button_ClearAllTexture)#清除所有纹理按钮

        self.ui.Export_Button_CR.clicked.connect(self.F_Export_Button_CR)    #单独显示R通道按钮
        self.ui.Export_Button_CG.clicked.connect(self.F_Export_Button_CG)    #单独显示G通道按钮
        self.ui.Export_Button_CB.clicked.connect(self.F_Export_Button_CB)    #单独显示B通道按钮
        self.ui.Export_Button_CA.clicked.connect(self.F_Export_Button_CA)    #单独显示A通道按钮
        self.ui.Export_Button_CAll.clicked.connect(self.F_Export_Button_CAll)#单独显示ALL通道按钮

        self.ui.checkBox_Use01Path.toggled.connect(self.F_checkBox_Use01Path)#使用01纹理通道按钮(路径作用到lineEdit_CustomPath)
        self.ui.checkBox_Use02Path.toggled.connect(self.F_checkBox_Use02Path)#使用02纹理通道按钮(路径作用到lineEdit_CustomPath)
        self.ui.checkBox_Use03Path.toggled.connect(self.F_checkBox_Use03Path)#使用03纹理通道按钮(路径作用到lineEdit_CustomPath)
        self.ui.checkBox_Use04Path.toggled.connect(self.F_checkBox_Use04Path)#使用04纹理通道按钮(路径作用到lineEdit_CustomPath)
        self.ui.pushButton_CustomPath.clicked.connect(self.F_pushButton_CustomPath)#使用自定义纹理路径

        self.ui.checkBox_Jpge.toggled.connect(self.F_checkBox_Jpge)          #使用JPG格式
        self.ui.checkBox_Tga.toggled.connect(self.F_checkBox_Tga)            #使用TGA格式
        self.ui.checkBox_Png.toggled.connect(self.F_checkBox_Png)            #使用PNG格式
        self.ui.checkBox_Ico.toggled.connect(self.F_checkBox_Ico)            #使用ICO格式


        self.ui.checkBox_128px.toggled.connect(self.F_checkBox_128px)        #使用分辨率128PX
        self.ui.checkBox_256px.toggled.connect(self.F_checkBox_256px)        #使用分辨率256PX
        self.ui.checkBox_512px.toggled.connect(self.F_checkBox_512px)        #使用分辨率512PX
        self.ui.checkBox_1k.toggled.connect(self.F_checkBox_1k)              #使用分辨率1024PX
        self.ui.checkBox_2k.toggled.connect(self.F_checkBox_2k)              #使用分辨率2048PX


        self.ui.ConvertBinary.clicked.connect(self.F_ConvertBinary)          #转换为二进制(复制到剪切板)
        self.ui.Export_Button_ExportTexture.clicked.connect(self.F_Export_Button_ExportTexture) #导出纹理按钮

        self.show()

    #拖拽
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标
    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()
    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def F_Image01_Button_R(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image01.img_R, "", 0)
    def F_Image01_Button_G(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image01.img_G, "", 0)
    def F_Image01_Button_B(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image01.img_B, "", 0)
    def F_Image01_Button_A(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image01.img_A, "", 0)
    def F_Image01_Button_Clear(self):  #清除纹理按钮
        self.ui.Image01.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Final_Image.ClearGlobalChannelNum()  # 清空通道数
        self.ui.Image01.isNoImage()
        self.ui.Log.setText("清空01纹理插槽")  # 显示LOG信息
        print("清空 IMAGE 01 纹理")
        self.ui.Final_Image.ClearImage(":/Image/Icon/FinalImage_Max_sign_4802px.png")
        self.ui.Final_Image_Channel_R.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_G.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_B.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_A.ClearGlobalChannel()#将通道颜色提示改为默认白色
    def F_Image01_Button_CopyPath(self):
        self.ui.Image01.GetPath()
        self.ui.Log.setText("成功复制01路径")  # 显示LOG信息

    def F_Image02_Button_R(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image02.img_R, "", 0)
    def F_Image02_Button_G(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image02.img_G, "", 0)
    def F_Image02_Button_B(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image02.img_B, "", 0)
    def F_Image02_Button_A(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image02.img_A, "", 0)
    def F_Image02_Button_Clear(self):  #清除纹理按钮
        self.ui.Image02.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Final_Image.ClearGlobalChannelNum()  # 清空通道数
        self.ui.Image02.isNoImage()
        self.ui.Log.setText("清空02纹理插槽")  # 显示LOG信息
        print("清空 IMAGE 02 纹理")
        self.ui.Final_Image.ClearImage(":/Image/Icon/FinalImage_Max_sign_4802px.png")
        self.ui.Final_Image_Channel_R.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_G.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_B.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_A.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
    def F_Image02_Button_CopyPath(self):
        self.ui.Image02.GetPath()
        self.ui.Log.setText("成功复制02路径")  # 显示LOG信息

    def F_Image03_Button_R(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image03.img_R, "", 0)
    def F_Image03_Button_G(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image03.img_G, "", 0)
    def F_Image03_Button_B(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image03.img_B, "", 0)
    def F_Image03_Button_A(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image02.img_A, "", 0)
    def F_Image03_Button_Clear(self):
        self.ui.Image03.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Final_Image.ClearGlobalChannelNum()  # 清空通道数
        self.ui.Image03.isNoImage()
        self.ui.Log.setText("清空03纹理插槽")  # 显示LOG信息
        self.ui.Final_Image.ClearImage(":/Image/Icon/FinalImage_Max_sign_4802px.png")
        self.ui.Final_Image_Channel_R.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_G.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_B.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_A.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
    def F_Image03_Button_CopyPath(self):
        self.ui.Image03.GetPath()
        self.ui.Log.setText("成功复制03路径")  # 显示LOG信息

    def F_Image04_Button_R(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image04.img_R, "", 0)
    def F_Image04_Button_G(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image04.img_G, "", 0)
    def F_Image04_Button_B(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image04.img_B, "", 0)
    def F_Image04_Button_A(self): #通道按钮
        CyFunctionLibrary.ChannelButton(self, self.ui.Image04.img_A, "", 0)
    def F_Image04_Button_Clear(self):
        self.ui.Image04.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Final_Image.ClearGlobalChannelNum()  # 清空通道数
        self.ui.Image04.isNoImage()
        self.ui.Log.setText("清空04纹理插槽")  # 显示LOG信息
        self.ui.Final_Image.ClearImage(":/Image/Icon/FinalImage_Max_sign_4802px.png")
        self.ui.Final_Image_Channel_R.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_G.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_B.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_A.ClearGlobalChannel()  # 将通道颜色提示改为默认白色
    def F_Image04_Button_CopyPath(self):
        self.ui.Image04.GetPath()
        self.ui.Log.setText("成功复制04路径")  # 显示LOG信息

    def F_Export_Button_PaintBlack(self):
        print("绘制黑色通道")
        CyFunctionLibrary.ChannelButton(self, self.Null_Img, "black",0)
        self.ui.Log.setText("通道填充了黑色")  # 显示LOG信息
    def F_Export_Button_PaintWhite(self):
        print("绘制白色通道")
        CyFunctionLibrary.ChannelButton(self, self.Null_Img , "white",0)
        self.ui.Log.setText("通道填充了白色")  # 显示LOG信息
    def F_Export_Button_PaintCustomColor(self):
        CyFunctionLibrary.ChannelButton(self, self.Null_Img, "custom", Silder_Value)
        self.ui.Log.setText("通道填充了自定义颜色")  # 显示LOG信息
    def F_horizontalSlider(self):
        Value = self.ui.horizontalSlider.ChangeValue()
        self.ui.lineEdit_2.SetValue(Value)
        global Silder_Value
        Silder_Value = Value
    #清空Final Image所有通道
    def F_Export_Button_ClearAllChannel(self):
        """01.清空所有通道 NUM = 0"""
        """02.将导出纹理RGBA颜色清空"""
        """03.清空 Final_Image替换为默认纹理"""
        self.ui.Final_Image.ClearGlobalChannelNum()           #清空通道数
        self.ui.Final_Image.ClearImage(":/Image/Icon/FinalImage_Max_sign_4802px.png")
        self.ui.Final_Image_Channel_R.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_G.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_B.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_A.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Log.SetLog()#显示LOG信息


    #清空纹理槽中的所有纹理
    def F_Export_Button_ClearAllTexture(self):
        self.ui.Final_Image.ClearGlobalChannelNum()  # 清空通道数
        self.ui.Final_Image.ClearImage(":/Image/Icon/FinalImage_Max_sign_4802px.png")
        self.ui.Image01.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Image02.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Image03.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Image04.ClearImage(":/Icon/Icon/ADD2_480px.png")
        self.ui.Final_Image_Channel_R.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_G.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_B.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Final_Image_Channel_A.ClearGlobalChannel()#将通道颜色提示改为默认白色
        self.ui.Image01.isNoImage()
        self.ui.Image02.isNoImage()
        self.ui.Image03.isNoImage()
        self.ui.Image04.isNoImage()
        self.ui.Log.setText("以清空所有纹理槽纹理")  # 显示LOG信息

    def F_Export_Button_CR(self):
        self.ui.Final_Image.ShowFinalImage(1)
        self.ui.Log.SetLog()  # 显示LOG信息
    def F_Export_Button_CG(self):
        self.ui.Final_Image.ShowFinalImage(2)
        self.ui.Log.SetLog()  # 显示LOG信息
    def F_Export_Button_CB(self):
        self.ui.Final_Image.ShowFinalImage(3)
        self.ui.Log.SetLog()  # 显示LOG信息
    def F_Export_Button_CA(self):
        self.ui.Final_Image.ShowFinalImage(4)
        self.ui.Log.SetLog()  # 显示LOG信息
    def F_Export_Button_CAll(self):
        self.ui.Final_Image.ShowFinalImage(5)
        self.ui.Log.SetLog()  # 显示LOG信息

    def F_checkBox_Use01Path(self):
        self.ui.checkBox_Use01Path.OpenPathCheck("path01",self.ui.checkBox_Use01Path,self.ui.checkBox_Use02Path,self.ui.checkBox_Use03Path,self.ui.checkBox_Use04Path)
        TempText = self.ui.Image01.Image_Path
        self.ui.lineEdit_CustomPath.setText(TempText)
        self.ui.Log.setText("将图片01当作输出目录")  # 显示LOG信息
    def F_checkBox_Use02Path(self):
        self.ui.checkBox_Use02Path.OpenPathCheck("path02",self.ui.checkBox_Use01Path,self.ui.checkBox_Use02Path,self.ui.checkBox_Use03Path,self.ui.checkBox_Use04Path)
        TempText = self.ui.Image02.Image_Path
        self.ui.lineEdit_CustomPath.setText(TempText)
        self.ui.Log.setText("将图片02当作输出目录")  # 显示LOG信息
    def F_checkBox_Use03Path(self):
        self.ui.checkBox_Use02Path.OpenPathCheck("path03",self.ui.checkBox_Use01Path,self.ui.checkBox_Use02Path,self.ui.checkBox_Use03Path,self.ui.checkBox_Use04Path)
        TempText = self.ui.Image03.Image_Path
        self.ui.lineEdit_CustomPath.setText(TempText)
        self.ui.Log.setText("将图片03当作输出目录")  # 显示LOG信息
    def F_checkBox_Use04Path(self):
        self.ui.checkBox_Use02Path.OpenPathCheck("path04",self.ui.checkBox_Use01Path,self.ui.checkBox_Use02Path,self.ui.checkBox_Use03Path,self.ui.checkBox_Use04Path)
        TempText = self.ui.Image04.Image_Path
        self.ui.lineEdit_CustomPath.setText(TempText)
        self.ui.Log.setText("将图片04当作输出目录")  # 显示LOG信息
    def F_pushButton_CustomPath(self):
        TempText = self.ui.pushButton_CustomPath.SetCustomFilePath()
        self.ui.lineEdit_CustomPath.setText(TempText)
        self.ui.Log.setText("定义自定义输出目录")  # 显示LOG信息

    def F_checkBox_Jpge(self):
        self.ui.checkBox_Jpge.OpenFormatCheck("JPGE", self.ui.checkBox_Jpge, self.ui.checkBox_Tga,
                                                 self.ui.checkBox_Png, self.ui.checkBox_Ico)
        self.ui.Log.setText("JPG格式 只支持RGB三通道")  # 显示LOG信息
    def F_checkBox_Tga(self):
        self.ui.checkBox_Tga.OpenFormatCheck("TGA", self.ui.checkBox_Jpge, self.ui.checkBox_Tga,
                                                 self.ui.checkBox_Png, self.ui.checkBox_Ico)
        self.ui.Log.setText("TGA格式 支持RGB RGBA两个模式")  # 显示LOG信息
    def F_checkBox_Png(self):
        self.ui.checkBox_Png.OpenFormatCheck("PNG", self.ui.checkBox_Jpge, self.ui.checkBox_Tga,
                                                 self.ui.checkBox_Png, self.ui.checkBox_Ico)
        self.ui.Log.setText("PNG格式 支持RGB RGBA两个模式")  # 显示LOG信息
    def F_checkBox_Ico(self):
        self.ui.checkBox_Ico.OpenFormatCheck("ICO", self.ui.checkBox_Jpge, self.ui.checkBox_Tga,
                                                 self.ui.checkBox_Png, self.ui.checkBox_Ico)
        self.ui.Log.setText("ICO格式 支持RGB RGBA两个模式")  # 显示LOG信息


    def F_checkBox_128px(self):
        self.ui.checkBox_128px.OpenResolutionCheck("128", self.ui.checkBox_128px,
                                             self.ui.checkBox_256px, self.ui.checkBox_512px, self.ui.checkBox_1k
                                                  ,self.ui.checkBox_2k)
    def F_checkBox_256px(self):
        self.ui.checkBox_256px.OpenResolutionCheck("256", self.ui.checkBox_128px,
                                             self.ui.checkBox_256px, self.ui.checkBox_512px, self.ui.checkBox_1k
                                                  ,self.ui.checkBox_2k)
    def F_checkBox_512px(self):
        self.ui.checkBox_512px.OpenResolutionCheck("512", self.ui.checkBox_128px,
                                             self.ui.checkBox_256px, self.ui.checkBox_512px, self.ui.checkBox_1k
                                                  ,self.ui.checkBox_2k)
    def F_checkBox_1k(self):
        self.ui.checkBox_1k.OpenResolutionCheck("1k", self.ui.checkBox_128px,
                                             self.ui.checkBox_256px, self.ui.checkBox_512px, self.ui.checkBox_1k
                                                  ,self.ui.checkBox_2k)
    def F_checkBox_2k(self):
        self.ui.checkBox_2k.OpenResolutionCheck("2k", self.ui.checkBox_128px,
                                             self.ui.checkBox_256px, self.ui.checkBox_512px, self.ui.checkBox_1k
                                                  ,self.ui.checkBox_2k)

    def F_ConvertBinary(self):
        self.ui.Final_Image.ConImgtobyte()
        self.ui.Log.SetLog()  # 显示LOG信息
    def F_Export_Button_ExportTexture(self):
        print("图片输出环节开始")
        OutPutPath = self.ui.lineEdit_CustomPath.text() #获取路径名称中的字符内容
        OutPutName = self.ui.Name_lineEdit.text()       #获取纹理名称中的字符内容
        OutPutResX = self.ui.CustomResX_lineEdit.text()        #获取自定义纹理的X
        OutPutResY = self.ui.CustomResY_lineEdit.text()        #获取自定义纹理的Y
        self.ui.Export_Button_ExportTexture.OutPutTexture(OutPutPath,OutPutName,OutPutResX,OutPutResY)
        self.ui.Log.SetLog()  # 显示LOG信息

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    app.exec_()
