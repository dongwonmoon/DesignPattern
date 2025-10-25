from abc import ABC, abstractmethod


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


class MessageFactory(ABC):
    @abstractmethod
    def create_message(self, content):
        pass


class EmailMessageFactory(MessageFactory):
    def create_message(self, content):
        return EmailMessage(content)


class SMSMessageFactory(MessageFactory):
    def create_message(self, content):
        return SmsMessage(content)


class BaseNotificationProvider(ABC):
    @abstractmethod
    def send(self, message):
        pass


class ProviderA(BaseNotificationProvider):
    def send(self, message):
        if isinstance(message, EmailMessage):
            print(f"로직: [Provider A]로 '{message.subject}' 발송")
        elif isinstance(message, SmsMessage):
            print(f"로직: [Provider A]로 '{message.text}' 발송")
        else:
            raise ValueError("지원하지 않는 메시지 타입")


class ProviderB(BaseNotificationProvider):
    def send(self, message):
        if isinstance(message, EmailMessage):
            print(f"로직: [Provider B]로 '{message.subject}' 발송")
        elif isinstance(message, SmsMessage):
            print(f"로직: [Provider B]로 '{message.text}' 발송")
        else:
            raise ValueError("지원하지 않는 메시지 타입")


# --- 우리의 '환자' 코드 ---
class NotificationManager:

    def __init__(self, provider):
        self.provider = provider

    # 🚨 문제 1: '객체 생성'의 if-else
    def create_message(self, factory, content):
        """알림 메시지 객체를 '생성'하는 메서드"""
        return factory.create_message(content)

    # 🚨 문제 2: '알고리즘(행위)'의 if-else
    def send_notification(self, message):
        """알림을 '전송'하는 메서드"""
        self.provider.send(message)


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
a_manager = NotificationManager(ProviderA())

welcome_email = a_manager.create_message(
    EmailMessageFactory(), "회원가입을 축하합니다!..."
)
a_manager.send_notification(welcome_email)

b_manager = NotificationManager(ProviderB())

welcome_email = b_manager.create_message(
    SMSMessageFactory(), "회원가입을 축하합니다!..."
)
b_manager.send_notification(welcome_email)
