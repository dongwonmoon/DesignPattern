from abc import ABC, abstractmethod


class Command(ABC):
    """'명령'의 추상 설계도 (인터페이스)"""

    @abstractmethod
    def execute(self):
        """명령을 실행"""
        pass

    @abstractmethod
    def undo(self):
        """명령을 실행 취소"""
        pass


class Light:
    """[외부 시스템 1] 스마트 전구 (Undo를 위해 상태 저장)"""

    def __init__(self, room):
        self.room = room
        self.brightness = 0
        self.color = "꺼짐"
        self.mode = "꺼짐"

    def set_config(self, brightness, color, mode):
        previous_state = (self.brightness, self.color, self.mode)

        self.brightness = brightness
        self.color = color
        self.mode = mode

        print(
            f"💡 [전구] {self.room} 조명 설정 (밝기:{brightness}, 색:{color}, 모드:{mode})"
        )
        return previous_state


class Thermostat:
    """[외부 시스템 2] 온도 조절기 (Undo를 위해 상태 저장)"""

    def __init__(self):
        self.temperature = 20

    def set_temperature(self, degree_celsius):
        previous_temp = self.temperature

        self.temperature = degree_celsius
        print(f"🌡️ [온도] {self.temperature}도로 설정합니다.")
        return previous_temp


class SetLightCommand(Command):
    """조명 설정을 '캡슐화'한 명령 객체"""

    def __init__(self, light: Light, brightness, color, mode):
        self.light = light
        self.new_brightness = brightness
        self.new_color = color
        self.new_mode = mode

        self.old_brightness = 0
        self.old_color = ""
        self.old_mode = ""

    def execute(self):
        print("[명령] 조명 설정 실행...")
        prev = self.light.set_config(self.new_brightness, self.new_color, self.new_mode)
        (self.old_brightness, self.old_color, self.old_mode) = prev

    def undo(self):
        print("[명령] 조명 설정 취소...")
        self.light.set_config(self.old_brightness, self.old_color, self.old_mode)


class SetThermostatCommand(Command):
    """온도 설정을 '캡슐화'한 명령 객체"""

    def __init__(self, thermostat: Thermostat, temp):
        self.thermostat = thermostat
        self.new_temp = temp
        self.old_temp = 0

    def execute(self):
        print("[명령] 온도 설정 실행...")
        self.old_temp = self.thermostat.set_temperature(self.new_temp)

    def undo(self):
        print("[명령] 온도 설정 취소...")
        self.thermostat.set_temperature(self.old_temp)


class NoCommand(Command):
    """'빈 슬롯'을 위한 널(Null) 커맨드 객체"""

    def execute(self):
        print("[명령] 할당된 명령이 없습니다.")

    def undo(self):
        pass


class RemoteControl:

    def __init__(self):
        self.slot_1_command = NoCommand()
        self.slot_2_command = NoCommand()

        self.last_command = NoCommand()

    def set_command(self, slot_number, command: Command):
        """리모컨 버튼에 명령을 '프로그래밍'합니다."""
        if slot_number == 1:
            self.slot_1_command = command
        elif slot_number == 2:
            self.slot_2_command = command

    def on_button_1_press(self):
        """1번 버튼은 그저 '실행'만 합니다."""
        self.slot_1_command.execute()
        self.last_command = self.slot_1_command

    def on_button_2_press(self):
        """2번 버튼도 그저 '실행'만 합니다."""
        self.slot_2_command.execute()
        self.last_command = self.slot_2_command

    def on_undo_button_press(self):
        """'Undo' 버튼은 '마지막 명령'을 '취소'합니다."""
        print("\n--- [UNDO] 버튼 누름 ---")
        self.last_command.undo()
        self.last_command = NoCommand()


print("--- '커맨드' 패턴 사용 ---")

living_room_light = Light("거실")
main_thermostat = Thermostat()

light_on = SetLightCommand(living_room_light, 100, "흰색", "집중 모드")
light_off = SetLightCommand(living_room_light, 0, "꺼짐", "꺼짐")
temp_22 = SetThermostatCommand(main_thermostat, 22)

remote = RemoteControl()

remote.set_command(1, light_on)
remote.set_command(2, temp_22)

print("\n--- 1번 버튼 누름 ---")
remote.on_button_1_press()

print("\n--- 2번 버튼 누름 ---")
remote.on_button_2_press()

remote.on_undo_button_press()

remote.set_command(1, light_off)
remote.on_button_1_press()
