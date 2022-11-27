import tkinter as tk
import ast

root = tk.Tk()
root.title('FCFF')
root.geometry('340x160')
tk.Label(root, text='z(过去几年净利润的平均增长率)').grid(column=0, row=0)
tk.Label(root, text='fcff(企业自由现金流)').grid(column=0, row=1)
tk.Label(root, text='Rwacc(加权平均资本成本)').grid(column=0, row=2)
tk.Label(root, text='g(永续增长率)').grid(column=0, row=3)
tk.Label(root, text='n(预测期)').grid(column=0, row=4)
e1 = tk.Entry(root)
e1.grid(column=1, row=0)
e2 = tk.Entry(root)
e2.grid(column=1, row=1)
e3 = tk.Entry(root)
e3.grid(column=1, row=2)
e4 = tk.Entry(root)
e4.grid(column=1, row=3)
e5 = tk.Entry(root)
e5.grid(column=1, row=4)


def get_z(net_profit):
    sum_profit = 0
    try:
        for x in range(len(net_profit) - 1):
            a = (net_profit[x + 1] - net_profit[x]) / net_profit[x]
            sum_profit = sum_profit + a
            x = x + 1
        z = sum_profit / (len(net_profit) - 1)
    except Exception as e:
        z = -1
    finally:
        return round(z, 2)


def get_fcff(list):
    fcff = 0
    net_profit = list[0]
    D_and_A = list[1]
    CAPX = list[2]
    NWC = list[3]
    try:
        fcff = net_profit + D_and_A - CAPX - NWC
        return fcff
    except Exception as e:
        fcff = -2
    finally:
        return round(fcff, 2)


def get_Rwacc(list):
    Rwacc = 0
    Rf = list[0]
    Beta = list[1]
    Rm = list[2]
    try:
        Rwacc = Rf + Beta * (Rm - Rf)
        return Rwacc
    except Exception as e:
        Rwacc = -3
    finally:
        return round(Rwacc, 4)


def get_value1(fcff, Rwacc, z, g, n):
    try:
        sum = 0
        for i in range(n):
            sum = sum + (fcff * (1 + z) ** (n + 1)/(1 + Rwacc) ** (n + 1))
        value = sum + (fcff * (1 + z) ** (n + 1)/((Rwacc - g) * (1 + Rwacc) ** n))
    except Exception as e:
        value = -4
    finally:
        return value


def show():
    try:
        net_profit = ast.literal_eval(e1.get())
        list1 = ast.literal_eval(e2.get())
        list2 = ast.literal_eval(e3.get())
        z = get_z(net_profit)
        fcff = get_fcff(list1)
        Rwacc = get_Rwacc(list2)
        g = float(e4.get())
        n = int(e5.get())
        value = round(get_value1(fcff, Rwacc, z, g, n), 3)
    except Exception as e:
        value = -5
    finally:
        if value != -5:
            lb = tk.Label(root, text=str(value))
            lb.grid(column=1, row=5)


bu = tk.Button(root, text='计算企业价值', command=show)
bu.grid(column=0, row=5)

root.mainloop()
