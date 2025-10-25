class SalesReport:
    """판매 리포트 데이터 (복잡한 로직)"""

    def __init__(self):
        self.data = "--- 2025년 10월 판매 데이터 ---"


class UserReport:
    """사용자 리포트 데이터 (복잡한 로직)"""

    def __init__(self):
        self.data = "--- 2025년 10월 사용자 목록 ---"


# --- 우리의 '환자' 코드 ---
class ReportGenerator:

    # 🚨 문제 1: '객체 생성'의 if-else
    def generate_report(self, report_type):
        """리포트 객체를 '생성'하는 메서드"""
        if report_type == "sales":
            print("로직: 판매 리포트를 생성합니다...")
            return SalesReport()
        elif report_type == "user":
            print("로직: 사용자 리포트를 생성합니다...")
            return UserReport()
        else:
            raise ValueError("알 수 없는 리포트 타입")

    # 🚨 문제 2: '알고리즘(행위)'의 if-else
    def export_report(self, report, format):
        """리포트를 '내보내는' 메서드"""
        if format == "pdf":
            print(f"로직: '{report.data}'를 PDF 파일로 저장합니다.")
        elif format == "csv":
            print(f"로직: '{report.data}'를 CSV 파일로 저장합니다.")
        else:
            raise ValueError("알 수 없는 포맷")


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
generator = ReportGenerator()

# 1. 판매 리포트를 생성해서
sales_report = generator.generate_report("sales")
# 2. PDF로 내보낸다
generator.export_report(sales_report, "pdf")

# 3. 사용자 리포트를 생성해서
user_report = generator.generate_report("user")
# 4. CSV로 내보낸다
generator.export_report(user_report, "csv")
