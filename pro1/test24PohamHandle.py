# 어딘 가에서 필요한 부품으로 핸들 클래스 작성

class PohamHandle:
    quantity = 0 # 핸들 회전량, 이건 톰아니고 포함핸들임

    def lefTurn(self, quantity):
        self.quantity = quantity
        return "좌회전"
    
    def rightTurn(self, quantity):
        self.quantity = quantity
        return "우회전"