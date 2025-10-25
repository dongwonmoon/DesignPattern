# --- (이 클래스들 자체는 이미 잘 만들어져 있다고 가정) ---
class EmailMessage:
    """이메일 메시지 (제목, 본문)"""

    def __init__(self, content):
        self.subject = f"[알림] {content[:10]}..."
        self.body = content
        print(f"객체: 이메일 생성 (제목: {self.subject})")


class SmsMessage:
    """SMS 메시지 (짧은 텍스트)"""

    def __init__(self, content):
        if len(content) > 40:
            content = content[:40] + "..."
        self.text = content
        print(f"객체: SMS 생성 (내용: {self.text})")


# --- 우리의 '환자' 코드 ---
class NotificationManager:

    # 🚨 문제 1: '객체 생성'의 if-else
    def create_message(self, message_type, content):
        """알림 메시지 객체를 '생성'하는 메서드"""
        if message_type == "email":
            return EmailMessage(content)
        elif message_type == "sms":
            return SmsMessage(content)
        else:
            raise ValueError("알 수 없는 메시지 타입")

    # 🚨 문제 2: '알고리즘(행위)'의 if-else
    def send_notification(self, message, provider):
        """알림을 '전송'하는 메서드"""
        if provider == "provider_A":
            # (실제로는 복잡한 AWS SES API 연동 로직)
            print(f"로직: [Provider A]로 '{message.subject}' 발송")
        elif provider == "provider_B":
            # (실제로는 복잡한 Twilio API 연동 로직)
            print(f"로직: [Provider B]로 '{message.subject}' 발송")
        else:
            raise ValueError("알 수 없는 전송사")


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
manager = NotificationManager()

# 1. '회원가입' -> 이메일 생성
welcome_email = manager.create_message("email", "회원가입을 축하합니다!...")
# 2. Provider A로 전송
manager.send_notification(welcome_email, "provider_A")

# 3. '긴급 점검' -> SMS 생성
alert_sms = manager.create_message("sms", "긴급 서버 점검이 10분 뒤 시작됩니다...")
# 4. Provider B로 전송
# (이런! SMS인데 .subject가 없어서 오류가 나겠네요. 이건 일단 무시하죠.)
# manager.send_notification(alert_sms, "provider_B")
# (일단 이메일 객체를 쓴다고 가정)
manager.send_notification(welcome_email, "provider_B")
