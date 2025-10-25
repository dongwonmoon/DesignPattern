from abc import ABC, abstractmethod


class SalesReport:
    """판매 리포트 데이터 (복잡한 로직)"""

    def __init__(self):
        self.data = "--- 2025년 10월 판매 데이터 ---"


class UserReport:
    """사용자 리포트 데이터 (복잡한 로직)"""

    def __init__(self):
        self.data = "--- 2025년 10월 사용자 목록 ---"


class ReportFactory(ABC):
    @abstractmethod
    def create_report(self):
        pass


class SalesReportFactory(ReportFactory):
    def create_report(self):
        print("로직: 판매 리포트를 생성합니다...")
        return SalesReport()


class UserReportFactory(ReportFactory):
    def create_report(self):
        print("로직: 사용자 리포트를 생성합니다...")
        return UserReport()


class BaseGenerator(ABC):
    @abstractmethod
    def export_report(self, report):
        pass


class PdfReportGenerator(BaseGenerator):
    def export_report(self, report):
        print(f"로직: '{report.data}'를 PDF 파일로 저장합니다.")


class CsvReportGenerator(BaseGenerator):
    def export_report(self, report):
        print(f"로직: '{report.data}'를 CSV 파일로 저장합니다.")


# --- 우리의 '환자' 코드 ---
class ReportGenerator:

    def __init__(self, generator):
        self.generator = generator

    # 🚨 문제 1: '객체 생성'의 if-else
    def generate_report(self, factory):
        """리포트 객체를 '생성'하는 메서드"""
        return factory.create_report()

    # 🚨 문제 2: '알고리즘(행위)'의 if-else
    def export_report(self, report):
        """리포트를 '내보내는' 메서드"""
        self.generator.export_report(report)


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
pdf_generator = ReportGenerator(PdfReportGenerator())

# 1. 판매 리포트를 생성해서
sales_report = pdf_generator.generate_report(SalesReportFactory())
# 2. PDF로 내보낸다
pdf_generator.export_report(sales_report)

csv_generator = ReportGenerator(CsvReportGenerator())
user_report = csv_generator.generate_report(UserReportFactory())
csv_generator.export_report(user_report)
