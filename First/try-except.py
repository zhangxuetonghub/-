"""
捕获异常的示例
"""

def safeIntegerInput(propmt):
    """
    获取一个用户输入的整数值，如果用户输入错误的整数值，提示用户重新输入
    """
    inputString = input(propmt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("输入的整数值 {0} 有误，请重新输入".format(inputString))
        return safeIntegerInput(propmt)


if __name__ == "__main__":
    i = safeIntegerInput("请输入你的年龄：")
print(i)
