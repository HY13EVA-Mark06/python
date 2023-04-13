class Member:
  def __init__(self, name="", point=100):
    self.name = name
    self.point = point
  def print_member(self):   # 名前とポイントを表示するメソッド
    print("NAME:" + self.name + " POINT:" + str(self.point))
  def pointup(self):   # ポイントUpするメソッド
    self.point += 100

m1 = Member("SATO")
m1.print_member()
m1.pointup()
m1.print_member()

class GoldMember(Member):
  def pointup(self):
    self.point += 500

m2 = GoldMember("GOTO")
m2.print_member()
m2.pointup()
m2.print_member()

class FreeMember(Member):
  def __init__(self, name="", point=0):
    self.name = name
    self.point = point
  def pointup(self):
    self.point = 0

m3 = FreeMember("YAMADA")
m3.print_member()
m3.pointup()
m3.print_member()

#学生会員クラス
class StudentMember(Member):
  def pointup(self):
    self.point += 200
  def print_member(self):
    print("NAME:" + self.name + " POINT:" + str(self.point) + "｢学生会員です｣")

m4 = StudentMember("HAMADA")
m4.print_member()
m4.pointup()
m4.print_member()