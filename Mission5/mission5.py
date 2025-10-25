# --- (이 클래스들 자체는 이미 잘 만들어져 있다고 가정) ---
class PortfolioDisplay:
    """[외부 시스템 1] 내 포트폴리오 화면"""

    def update_chart(self, symbol, price):
        print(f"📈 [화면] {symbol}의 차트를 {price}원으로 업데이트합니다.")


class AlertSystem:
    """[외부 시스템 2] 가격 알림 시스템"""

    def check_threshold(self, symbol, price):
        if symbol == "GOOG" and price > 150:
            print(f"🔔 [알림] GOOG 가격이 {price}원으로 올랐습니다! (목표가 도달)")


# --- 우리의 '환자' 코드 ---
class StockBroker:

    def __init__(self):
        # 🚨 문제 1: '강한 결합'
        # StockBroker가 모든 외부 시스템을 '직접' 알고 있어야 함
        self.portfolio_display = PortfolioDisplay()
        self.alert_system = AlertSystem()
        # '데이터 로거', '뉴스 봇'이 추가되면?

    def set_price(self, symbol, price):
        """가격 변동을 설정하고 전파하는 메인 메서드"""
        print(f"\n--- [중개소] {symbol} 가격이 {price}원으로 변동! ---")

        # 🚨 문제 1: '알림' 로직이 메서드에 하드코딩됨
        # (A) 포트폴리오 화면에 직접 알림
        self.portfolio_display.update_chart(symbol, price)

        # (B) 알림 시스템에 직접 알림
        self.alert_system.check_threshold(symbol, price)

        # 만약 '데이터 로거(DataLogger)'에도 알려야 한다면?
        # -> 이 set_price 메서드를 '수정'해야 함! (OCP 위반)


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
broker = StockBroker()

broker.set_price("GOOG", 140)
broker.set_price("MSFT", 180)
broker.set_price("GOOG", 151)  # <- 알림이 울려야 함
