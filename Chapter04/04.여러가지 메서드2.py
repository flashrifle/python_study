class Math:
    # 정적 메서드
    # 인스턴스를 만들필요가 없는 메서드

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def sub(x,y):
        return x-y

print(Math.add(3,4))