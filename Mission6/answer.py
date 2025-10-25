from abc import ABC, abstractmethod


class CharacterFactory:
    def create_character(self):
        pass


class Warrior:
    def __init__(self):
        self.name = "전사"
        self.health = 100

    def attack(self):
        print("🗡️ 전사가 검으로 공격!")


class Mage:
    def __init__(self):
        self.name = "마법사"
        self.health = 60

    def cast_spell(self):
        print("🔥 마법사가 파이어볼 시전!")


class WarriorFactory(CharacterFactory):
    def create_character(self):
        print("로직: 전사를 생성합니다...")
        return Warrior()


class MageFactory(CharacterFactory):
    def create_character(self):
        print("로직: 마법사를 생성합니다...")
        return Mage()


class Observer(ABC):
    @abstractmethod
    def update(self, character, damage):
        pass


class UIHealthBar(Observer):
    """[외부 시스템 1] 체력바 UI"""

    def update(self, character, damage):
        self.update_bar(character.name, character.health)

    def update_bar(self, character_name, new_health):
        print(f"📈 [UI] {character_name}의 체력바가 {new_health}HP로 업데이트됨.")


class AudioManager(Observer):
    """[외부 시스템 2] 오디오"""

    def update(self, character, damage):
        self.play_pain_sound(character.name)

    def play_pain_sound(self, character_name):
        print(f"🔊 [Audio] {character_name}가 '으악!' 소리를 냄.")


class MoveStrategy(ABC):
    @abstractmethod
    def move(self, character):
        pass


class WalkStrategy(MoveStrategy):
    def move(self, character):
        print(f"로직: {character.name}이(가) 앞으로 걷습니다.")


class FlyStrategy(MoveStrategy):
    def move(self, character):
        print(f"로직: {character.name}이(가) 하늘로 날아오릅니다.")


# --- 우리의 '환자' 코드 ---
class GameEngine:

    def __init__(self, strategy):
        self.observers = []
        self.strategy = strategy

    def create_character(self, factory):
        return factory.create_character()

    # 🚨 문제 2: '알고리즘(행위)'의 if-else
    def move_character(self, character):
        self.strategy.move(character)

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, character, damage):
        for observer in self.observers:
            observer.update(character, damage)

    # 🚨 문제 3: '알림' 로직이 메서드에 하드코딩됨
    def character_takes_damage(self, character, damage):
        character.health -= damage
        print(
            f"\n💥 {character.name}이(가) {damage}의 데미지를 입음! (남은 체력: {character.health})"
        )

        self.notify_observers(character, damage)


# --- 사용 예시 ---
print("--- '리팩토링' 방식 사용 ---")

engine = GameEngine(WalkStrategy())

engine.add_observer(UIHealthBar())
engine.add_observer(AudioManager())

warrior = engine.create_character(WarriorFactory())

engine.move_character(warrior)
engine.character_takes_damage(warrior, 15)
