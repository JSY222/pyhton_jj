# class Machine:
#     Count = 1

#     def showData(self):
#         coin = int(input("동전을 넣으세요 : "))

#         coinIn = CoinIn()
#         coinIn.coin = coin
#         coinIn.culc(self.Count)

# class CoinIn:
#     coin = 0
#     change = 0

#     def culc(self, Count):
#         price = 200

#         self.Count = self.coin // price     
#         self.change = self.coin % price

#         if self.Count == 0:
#             print("금액이 부족합니다.")
#         else:
#             print(f"몇 잔을 원하시나요 : {self.Count}")
#             print(f"커피 {self.Count}잔과 잔돈 {self.change}원")

# if __name__ == '__main__':
#     Machine = Machine()
#     Machine.showData() 


print("--------------")

class Machine:
    def __init__(self):
        self.coin_input = CoinIn(self)

    def showData(self):
        coin = input('동전 입력') # 문자열
        count = input('몇 잔 입력') # 문자열
        self.coin_input.coin = int(coin) # Coinin에서 coin에게줌
        self.coin_input.calc(int(count))
        change = self.coin_input.change

        if (change >=0) :
            print("커피", count, "잔과 돈", change, "원")
        else:
            print("잔액이 부족합니다")

class CoinIn:
    def __init__(self, coin = 0, change = 0):
        self.price = 200
        self.coin = coin
        self.change = change

    def calc(self, cupCount):
        total = cupCount * self.price
        self.change = self.coin - total

machine = Machine()
machine.showData()


