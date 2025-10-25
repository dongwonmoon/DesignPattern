from abc import ABC, abstractmethod


class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id, items):
        pass


class EmailService(OrderObserver):
    """[외부 시스템 1] 이메일을 발송"""

    def update(self, order_id, items):
        self.send_confirmation_email(order_id)

    def send_confirmation_email(self, order_id):
        print(f"이메일 발송: 주문({order_id})이 완료되었습니다.")


class InventorySystem(OrderObserver):
    """[외부 시스템 2] 재고를 관리"""

    def update(self, order_id, items):
        for item in items:
            self.decrease_stock(item)

    def decrease_stock(self, item_id):
        print(f"재고 감소: {item_id}의 재고를 1 줄입니다.")


# --- 우리의 '환자' 코드 ---
class OrderProcessor:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self, order_id, items):
        for observer in self.observers:
            observer.update(order_id, items)

    def place_order(self, order_id, cart_items):
        """주문을 처리하는 메인 메서드"""
        print(f"주문 처리: {order_id} 생성 완료.")

        self.notify(order_id, cart_items)

    def cancel_order(self, order_id):
        """주문을 취소 (일단 간단히)"""
        print(f"주문 취소: {order_id} 취소 완료.")


print("\n--- '옵저버' 패턴 사용 ---")

email_notifier = EmailService()
stock_manager = InventorySystem()

order_processor = OrderProcessor()

order_processor.register(email_notifier)
order_processor.register(stock_manager)

cart = ["item-A", "item-B"]
order_processor.place_order("ORDER-123", cart)
