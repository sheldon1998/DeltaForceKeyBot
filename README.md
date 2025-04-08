# 免责声明
免责声明
脚本仅供学习和研究目的使用，作者不对因使用该脚本而导致的任何后果负责。使用该脚本的风险完全由用户自行承担。

交流🐧群:🐧:785637447

用户须知：

尽管脚本设计为非侵入性，但使用第三方工具可能违反目标平台的使用条款或服务协议。
使用该脚本可能导致账号被封禁或其他形式的处罚。

作者不保证脚本的稳定性、安全性或合法性。
# DeltaForceKeyBot
三角洲行动拍卖行自动挂卡工具(单三跑刀巴克什匹配实在太久,所以利用匹配时间进行补卡),通过ocr+模拟鼠标点击实现自动购买钥匙卡
项目默认只配置了交易行>钥匙>巴克什 页面的的部分钥匙坐标数据,如有其他地图的钥匙可以将钥匙添加到收藏，然后通过debug.py 记录钥匙卡的位置来进行监控购买


## 开始
### 安装
1. 下载本代码,安装requirement.txt
2. 安装[tesseract](https://github.com/tesseract-ocr/tesseract )
3. 下载[tesseract中文识别库](https://github.com/tesseract-ocr/tessdata)
4. 修改代码中的环境变量为本机安装的位置
```
# Tesseract 环境配置
os.environ["LANGDATA_PATH"] = r"E:\Code\DeltaForce\tessdata-4.1.0\tessdata-4.1.0"
os.environ["TESSDATA_PREFIX"] = r"E:\Code\DeltaForce\tessdata-4.1.0\tessdata-4.1.0"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 运行
```
python main.py
```
F8开始抢卡,F9暂停抢卡,脚本已适配不同分辨率(16:9)以及多显示器的场景
开始抢卡时需要将页面点击到买卡的区域,如下图项目默认只配置了交易行>钥匙>巴克什 页面如下图的的部分钥匙坐标数据,
![image](https://github.com/user-attachments/assets/b76727bc-d126-47a5-a3ed-964f9221d38c)

**如有其他地图的钥匙可以将钥匙添加到收藏，然后通过debug.py 记录钥匙卡的位置来进行监控购买**

## 其他说明
### debug.py
运行debug.py 实时获取鼠标坐标 如得到 58.21%,21.25% 则坐标应该为[0.5821,0.2125]

### keys.json
```

{
    "name": "巴别塔供电权限卡", #目标卡牌名称，需与游戏保持一致
    "base_price": 489859,  #目标卡牌参考价格,该价格溢价10w内也会自动购买,不需要自行修改代码
    "ideal_price": 500000, #理想购买价格
    "position": [0.6148,0.5174], #卡牌坐标
    "wantBuy":1 #是否加入监控
    }

```

### 购买逻辑

1. 当前价格小于理想购买价格,自动购买
2. 卡牌溢价10w以内,自动购买
3. 卡牌负溢价,自动购买


## FAQ:
1. 为什么截图区域不对
> 检查自己的屏幕分辨率是否为16:9

2. ESC按键没反应/脚本无法获取截图
> 使用管理员运行cmd
