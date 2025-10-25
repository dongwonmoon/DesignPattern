# --- (이 클래스들 자체는 이미 잘 만들어져 있다고 가정) ---
class EmailService:
    """[외부 시스템 1] 이메일을 발송"""

    def send_confirmation_email(self, order_id):
        print(f"이메일 발송: 주문({order_id})이 완료되었습니다.")


class InventorySystem:
    """[외부 시스템 2] 재고를 관리"""

    def decrease_stock(self, item_id):
        print(f"재고 감소: {item_id}의 재고를 1 줄입니다.")


# --- 우리의 '환자' 코드 ---
class OrderProcessor:

    def __init__(self):
        # 🚨 문제 1: '강한 결합'
        # OrderProcessor가 모든 외부 시스템을 '직접' 알고 있어야 함
        self.email_service = EmailService()
        self.inventory_system = InventorySystem()
        # '배송 시스템', '데이터 분석 시스템'이 추가되면?

    def place_order(self, cart_items):
        """주문을 처리하는 메인 메서드"""
        order_id = "ORDER-123"  # (주문 생성 로직...)
        print(f"주문 처리: {order_id} 생성 완료.")

        # 🚨 문제 1: '알림' 로직이 메서드에 하드코딩됨
        # (A) 이메일 시스템에 직접 알림
        self.email_service.send_confirmation_email(order_id)

        # (B) 재고 시스템에 직접 알림
        for item in cart_items:
            self.inventory_system.decrease_stock(item)

        # 만약 '배송 시스템(ShippingSystem)'에도 알려야 한다면?
        # -> 이 place_order 메서드를 '수정'해야 함! (OCP 위반)

    def cancel_order(self, order_id):
        """주문을 취소 (일단 간단히)"""
        print(f"주문 취소: {order_id} 취소 완료.")


# --- 사용 예시 (UI 또는 API 레이어라고 가정) ---
print("--- '안 좋은' 방식 사용 ---")
processor = OrderProcessor()

# 🚨 문제 2: '호출자'와 '수신자'의 강한 결합
# '사용 예시' 코드가 OrderProcessor의 '존재'와
# 'place_order'라는 '메서드 이름'을 직접 알고 있어야 함

# (가짜 UI 버튼 1) "주문 확정" 버튼 클릭
cart = ["item-A", "item-B"]
processor.place_order(cart)

# (가짜 UI 버튼 2) "주문 취소" 버튼 클릭
processor.cancel_order("ORDER-123")
