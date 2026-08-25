class ElecProduct:  # 부모 클래스
    voulume = 0

    def volumeControl(self, volume):
        print(f"{volume}을 조절한다")
        # pass

class ElecTv(ElecProduct): # 자식클래스
    def volumeControl(self, volume): # 오버라이딩
        print('나는 TV')
        print(f"{volume}을 리모컨으로 조절한다")

class ElecRadio(ElecProduct): # 자식클래스
    def volumeControl(self, volume): # 오버라이딩
        print('나는 radio')
        sori = volume
        print(f"{sori}을 주파수로 조절한다")

if __name__ == "__main__":
    electro_product = ElecProduct()
    electro_product.volumeControl(1)

    print()
    tv = ElecTv()
    tv.volumeControl(3)
    print()
    radio = ElecRadio()
    radio.volumeControl(5)
    
    print('--\n다형성 1 -------')
    product = tv
    product.volumeControl(2)
    print()
    product = radio
    product.volumeControl(2)

    print('--\n다형성 2 -------')
    group = [ElecTv(), ElecRadio()]
    for g in group:
        g.volumeControl(3)
        print()

print('문3) 다중 상속 연습문제')

class Animal: #최상위 클래스
    def move(self):
        print("동물은 움직인다")

class Dog(Animal):
    name = "개"

    def move(self):#Animal() 클래스의 move()메서드와 이름만 갖고 기능은 다른 오버라이딩
        print(f"{self.name}는 기분 좋으면 꼬리를 흔든다")

class Cat(Animal): #Animal에서 move() 받아오기
    name = "고양이"

    def move(self):
        print(f"{self.name}는 그루밍을 한다")

class Wolf(Dog, Cat):
    pass

class Fox(Cat,Dog):
    def foxMethod(self):
        print("아리는 꼬리가 9개")
        
    def move(self): # move 오버라이딩
        print("여우의 움직임")

if __name__ =="__main__":
    Animal().move()

    print()
    d=Dog()
    d.move()
    print()
    c=Cat()
    c.move()
    print()
    w=Wolf()
    w.move()
    print()
    f=Fox()
    f.move()
    print()

    print('----다형성------')
    ani = [d, c, w, f]
    for a in ani:
        print(id(a))
        a.move()
        print()