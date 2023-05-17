import time
import os

def start_pomodoro(total_time, break_time):
    print("专注时钟开始！")
    while True:
        print(f"专注倒计时: {total_time}分钟")
        time.sleep(total_time * 60)  # 等待专注时间结束
        os.system("say 专注时间结束，请休息")  # 在 macOS 上使用 say 命令朗读提示信息

        print(f"休息倒计时: {break_time}分钟")
        time.sleep(break_time * 60)  # 等待休息时间结束
        os.system("say 休息时间结束，请开始下一个专注时间")  # 在 macOS 上使用 say 命令朗读提示信息

        choice = input("是否开始下一个专注时间？(y/n) ")
        if choice.lower() != 'y':
            break

# 输入专注时间和休息时间
total_time = int(input("请输入专注时间（分钟）: "))
break_time = int(input("请输入休息时间（分钟）: "))

start_pomodoro(total_time, break_time)
