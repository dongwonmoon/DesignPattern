class CsvExtractor:
    """CSV 파일에서 데이터를 '추출'"""

    def extract(self):
        data = "[CSV Data: user_id, name, email]"
        print(f"추출: {data}")
        return data


class JsonExtractor:
    """JSON 파일에서 데이터를 '추출'"""

    def extract(self):
        data = "[JSON Data: {'user_id': 1, 'name': '...'} ]"
        print(f"추출: {data}")
        return data


class CleanTransform:
    """데이터를 '변환' (예: 결측치 제거)"""

    def run(self, data):
        transformed = f"{data} [CLEANED]"
        print(f"변환: {transformed}")
        return transformed


class AggregateTransform:
    """데이터를 '변환' (예: 그룹별 집계)"""

    def run(self, data):
        transformed = f"{data} [AGGREGATED]"
        print(f"변환: {transformed}")
        return transformed


# --- 우리의 '환자' 코드 ---
class DataPipeline:

    def run_pipeline(self, source_type, transform_logic):
        """파이프라인을 실행하는 메인 메서드"""

        # 🚨 문제 1: '객체 생성(추출)'의 if-else
        if source_type == "csv":
            data = CsvExtractor().extract()
        elif source_type == "json":
            data = JsonExtractor().extract()
        else:
            raise ValueError("알 수 없는 소스 타입")

        # 🚨 문제 2: '알고리즘(변환)'의 if-else
        if transform_logic == "clean":
            transformed_data = CleanTransform().run(data)
        elif transform_logic == "aggregate":
            transformed_data = AggregateTransform().run(data)
        else:
            raise ValueError("알 수 없는 변환 로직")

        print(f"파이프라인 완료: {transformed_data}")


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
pipeline = DataPipeline()

# 1. CSV에서 데이터를 '추출(E)'해서 '클린(T)'
pipeline.run_pipeline("csv", "clean")

# 2. JSON에서 데이터를 '추출(E)'해서 '집계(T)'
pipeline.run_pipeline("json", "aggregate")
