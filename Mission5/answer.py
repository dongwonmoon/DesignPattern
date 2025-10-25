from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass


class PortfolioDisplay(Observer):
    """[외부 시스템 1] 내 포트폴리오 화면"""

    def update(self, symbol, price):
        self.update_chart(symbol, price)

    def update_chart(self, symbol, price):
        print(f"📈 [화면] {symbol}의 차트를 {price}원으로 업데이트합니다.")


class AlertSystem(Observer):
    """[외부 시스템 2] 가격 알림 시스템"""

    def update(self, symbol, price):
        self.check_threshold(symbol, price)

    def check_threshold(self, symbol, price):
        if symbol == "GOOG" and price > 150:
            print(f"🔔 [알림] GOOG 가격이 {price}원으로 올랐습니다! (목표가 도달)")


# --- 우리의 '환자' 코드 ---
class StockBroker:

    def __init__(self):
        self.observers = []

    def notify(self, symbol, price):
        for observer in self.observers:
            observer.update(symbol, price)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_price(self, symbol, price):
        """가격 변동을 설정하고 전파하는 메인 메서드"""
        print(f"\n--- [중개소] {symbol} 가격이 {price}원으로 변동! ---")

        self.notify(symbol, price)


# --- 사용 예시 ---
broker = StockBroker()

portfolio_display = PortfolioDisplay()
alert_system = AlertSystem()

broker.add_observer(portfolio_display)
broker.add_observer(alert_system)

broker.set_price("GOOG", 140)
broker.set_price("MSFT", 180)
broker.set_price("GOOG", 151)  # <- 알림이 울려야 함
