# 獲得評分
available_trader_count = 2
trader_now_list = ["Trader B", "Trader C"]
trader_after_rerange_list = []
trader_score_dict = {
    "Trader A": 5,
    "Trader B": 4,
    "Trader C": 3,
}
# 完整 trader_after_rerange_list

# 是否需要條倉
if sorted(trader_now_list) != sorted(trader_after_rerange_list):

    need_rerange = True
else:
    need_rerange = False

print("當前訂閱者數量：", 2)
# print("===========")
# print("Trader A")
# print("近30天收益率: +165.03% ")
# print("部位價值: 100U")
# print("-----------------")
# print("Trader B")
# print("近30天收益率: +165.03% ")
# print("部位價值: 100U")
# print("===========")
if need_rerange:
    print("是否需要調倉: 是")
    print("-----------------")
    print("調倉方向: Trader A to Trader B")
    print("現有交易員: Trader C, Trader B")
    print("調倉後交易員: Trader A, Trader B")
else:
    print("是否需要調倉: 否")
    print("-----------------")
    print("調倉方向: None")
    print("現有交易員: Trader C, Trader B")
    print("調倉後交易員: Trader C, Trader B")
