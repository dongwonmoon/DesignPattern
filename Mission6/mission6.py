# --- (이 클래스들 자체는 이미 잘 만들어져 있다고 가정) ---
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


class UIHealthBar:
    """[외부 시스템 1] 체력바 UI"""

    def update_bar(self, character_name, new_health):
        print(f"📈 [UI] {character_name}의 체력바가 {new_health}HP로 업데이트됨.")


class AudioManager:
    """[외부 시스템 2] 오디오"""

    def play_pain_sound(self, character_name):
        print(f"🔊 [Audio] {character_name}가 '으악!' 소리를 냄.")


# --- 우리의 '환자' 코드 ---
class GameEngine:

    def __init__(self):
        # 🚨 문제 3: '강한 결합'
        # GameEngine이 모든 외부 시스템을 '직접' 알고 있음
        self.ui_bar = UIHealthBar()
        self.audio_manager = AudioManager()
        # '분석 시스템(Analytics)'이 추가되면? __init__과 take_damage를 둘 다 수정!

    # 🚨 문제 1: '객체 생성'의 if-else
    def create_character(self, char_type):
        if char_type == "warrior":
            print("로직: 전사를 생성합니다...")
            return Warrior()
        elif char_type == "mage":
            print("로직: 마법사를 생성합니다...")
            return Mage()
        else:
            raise ValueError("알 수 없는 캐릭터 타입")

    # 🚨 문제 2: '알고리즘(행위)'의 if-else
    def move_character(self, character, move_type):
        if move_type == "walk":
            # (복잡한 걷기 로직...)
            print(f"로직: {character.name}이(가) 앞으로 걷습니다.")
        elif move_type == "fly":
            # (복잡한 날기 로직...)
            print(f"로직: {character.name}이(가) 하늘로 날아오릅니다.")
        else:
            raise ValueError("알 수 없는 이동 타입")

    # 🚨 문제 3: '알림' 로직이 메서드에 하드코딩됨
    def character_takes_damage(self, character, damage):
        character.health -= damage
        print(
            f"\n💥 {character.name}이(가) {damage}의 데미지를 입음! (남은 체력: {character.health})"
        )

        # (A) UI 시스템에 직접 알림
        self.ui_bar.update_bar(character.name, character.health)

        # (B) 오디오 시스템에 직접 알림
        self.audio_manager.play_pain_sound(character.name)

        # 만약 '분석 시스템(AnalyticsLogger)'에도 알려야 한다면?
        # -> 이 메서드를 '수정'해야 함! (OCP 위반)


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
engine = GameEngine()

# 1. (팩토리 문제) 캐릭터 생성
warrior = engine.create_character("warrior")

# 2. (스트래티지 문제) 캐릭터 이동
engine.move_character(warrior, "walk")

# 3. (옵저버 문제) 데미지 발생
engine.character_takes_damage(warrior, 15)
