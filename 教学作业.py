print("Welcome to ATM")
while True:
    name = input("请输入用户名:")
    password = input("请输入账号密码:")
    if password == "mrfzwdsj314314":
        print("登录成功")
        break
    else:
        print("密码错误,请重新输入")
def main_menu():
    print("----------主菜单----------")
    print(f"尊敬的{name},您好,欢迎使用银行自动ATM机,请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("输入操作:"))
def balance_inquiry(show_header):
    if show_header:
        print("---------查询余额----------")
        print(f"{name},您好,你的余额剩余:{money}元")
    else:
        print(f"{name},您好,你的余额剩余:{money}元")
def deposit(amount):
    print("-----------存款----------")
    global money
    money += amount
    print(f"{name},您好,您存款{amount}成功")
    balance_inquiry(False)
def withdrawal(amount):
    print("-----------取款----------")
    global money
    money -= amount
    print(f"{name},您好,你取款{amount}成功")
    balance_inquiry(False)
while True:
    keyboard_input = main_menu()
    if keyboard_input == 1:
        balance_inquiry(True)
        continue
    elif keyboard_input == 2:
        num = int(input("输入您想存款的数目:"))
        deposit(num)
        continue
    elif keyboard_input == 3:
        num = int(input("输入您想取款的数目:"))
        withdrawal(num)
        continue
    else:
        break