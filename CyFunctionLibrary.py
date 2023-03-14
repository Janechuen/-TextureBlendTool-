def ChannelButton(self,input_img,type,customnum):
    img = input_img  # 获取当前按钮代表的纹理
    self.ui.Final_Image.SetGlobalChannelNum()        # 设置当前的点击次数
    num = self.ui.Final_Image.getGlobalChannelNum()                 #获取当前点击次数并且打印
    self.ui.Final_Image.SetImgChannel(img, num, type,customnum)    #根据当前按钮代表的图片和点击数制作最终图片
    self.ui.Final_Image_Channel_R.ShowChannelResult(1)
    self.ui.Final_Image_Channel_G.ShowChannelResult(2)
    self.ui.Final_Image_Channel_B.ShowChannelResult(3)
    self.ui.Final_Image_Channel_A.ShowChannelResult(4)

def ChannelButton_Black(self):
     # 获取当前按钮代表的纹理
    self.ui.Final_Image.SetGlobalChannelNum()        # 设置当前的点击次数
    num = self.ui.Final_Image.getGlobalChannelNum()  # 获取当前点击次数并且打印
    self.ui.Final_Image.SetBlackColor(num)      # 根据当前按钮代表的图片和点击数制作最终图片
    self.ui.Final_Image_Channel_R.ShowChannelResult(1)
    self.ui.Final_Image_Channel_G.ShowChannelResult(2)
    self.ui.Final_Image_Channel_B.ShowChannelResult(3)
    self.ui.Final_Image_Channel_A.ShowChannelResult(4)

def ChannelButton_White(self):
    self.ui.Final_Image.SetGlobalChannelNum()        # 设置当前的点击次数
    num = self.ui.Final_Image.getGlobalChannelNum()  # 获取当前点击次数并且打印
    self.ui.Final_Image.SetWhiteColor(num)      # 根据当前按钮代表的图片和点击数制作最终图片
    self.ui.Final_Image_Channel_R.ShowChannelResult(1)
    self.ui.Final_Image_Channel_G.ShowChannelResult(2)
    self.ui.Final_Image_Channel_B.ShowChannelResult(3)
    self.ui.Final_Image_Channel_A.ShowChannelResult(4)

def ChannelButton_Custom(self,input_img,Button):
    img = input_img  # 获取当前按钮代表的纹理
    self.ui.Final_Image.SetGlobalChannelNum()        # 设置当前的点击次数
    num = self.ui.Final_Image.getGlobalChannelNum()  # 获取当前点击次数并且打印
    self.ui.Final_Image.SetImgChannel(img, num)      # 根据当前按钮代表的图片和点击数制作最终图片
    self.ui.Final_Image_Channel_R.ShowChannelResult(1)
    self.ui.Final_Image_Channel_G.ShowChannelResult(2)
    self.ui.Final_Image_Channel_B.ShowChannelResult(3)
    self.ui.Final_Image_Channel_A.ShowChannelResult(4)

