import pyautogui
import time

# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

print("按 Ctrl+C 结束程序")
try:
    while True:
        x, y = pyautogui.position()
        
        # 计算百分比（保留4位小数，例如 0.7523 表示 75.23%）
        x_percent = round(x / screen_width, 4)
        y_percent = round(y / screen_height, 4)
        
        # 实时显示原始坐标和百分比坐标
        print(
            f"原始坐标: X={x:<4} Y={y:<4} | "
            f"百分比坐标: X={x_percent:.2%} Y={y_percent:.2%}",
            end="\r"
        )
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n程序已终止")