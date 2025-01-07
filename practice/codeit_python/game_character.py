class GameCharacter:
   """게임 캐릭터를 생성하고 전투를 관리하는 클래스"""
   
   def __init__(self, name: str, hp: int, power: int):
       """캐릭터 초기화"""
       self.name = name
       self.hp = hp
       self.power = power
       
   def is_alive(self) -> bool:
       """생존 여부 확인"""
       return self.hp > 0
       
   def get_attacked(self, damage: int):
       """데미지를 받아 체력 감소"""
       if self.is_alive():
           if self.hp >= damage:
               self.hp -= damage
           else:
               self.hp = 0
       else:
           print(f"{self.name}님은 이미 죽었습니다.")
           
   def attack(self, other_character: 'GameCharacter'):
       """다른 캐릭터 공격"""
       if self.is_alive():
           other_character.get_attacked(self.power)
           
   def __str__(self) -> str:
       """캐릭터 정보 문자열로 반환"""
       return f"{self.name}님의 hp는 {self.hp}만큼 남았습니다."


if __name__ == "__main__":
   # 테스트 코드
   character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
   character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

   character_1.attack(character_2)
   character_2.attack(character_1)
   character_2.attack(character_1)
   character_2.attack(character_1)
   character_2.attack(character_1)
   character_2.attack(character_1)

   print(character_1)
   print(character_2)
