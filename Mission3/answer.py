from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class BaseTransformer(ABC):
    @abstractmethod
    def run(self, data):
        pass


class CsvExtractor(BaseExtractor):
    """CSV 파일에서 데이터를 '추출'"""

    def extract(self):
        data = "[CSV Data: user_id, name, email]"
        print(f"추출: {data}")
        return data


class JsonExtractor(BaseExtractor):
    """JSON 파일에서 데이터를 '추출'"""

    def extract(self):
        data = "[JSON Data: {'user_id': 1, 'name': '...'} ]"
        print(f"추출: {data}")
        return data


class CleanTransform(BaseTransformer):
    """데이터를 '변환' (예: 결측치 제거)"""

    def run(self, data):
        transformed = f"{data} [CLEANED]"
        print(f"변환: {transformed}")
        return transformed


class AggregateTransform(BaseTransformer):
    """데이터를 '변환' (예: 그룹별 집계)"""

    def run(self, data):
        transformed = f"{data} [AGGREGATED]"
        print(f"변환: {transformed}")
        return transformed


# --- 우리의 '환자' 코드 ---
class DataPipeline:
    def __init__(self):
        self.extractor = None
        self.transformer = None

    def add_extractor(self, extractor):
        self.extractor = extractor
        return self

    def add_transformer(self, transformer):
        self.transformer = transformer
        return self

    def build(self):
        return DataPipeline(self.extractor, self.transformer)

    def _extract(self):
        return self.extractor.extract()

    def _transform(self, data):
        return self.transformer.run(data)

    def run_pipeline(self):
        """파이프라인을 실행하는 메인 메서드"""

        data = self._extract()

        transformed_data = self._transform(data)

        print(f"파이프라인 완료: {transformed_data}")


# --- 사용 예시 ---
print("--- '안 좋은' 방식 사용 ---")
csv_clean_pipeline = (
    DataPipeline()
    .add_extractor(CsvExtractor())
    .add_transformer(CleanTransform())
    .build()
)
json_aggregate_pipeline = (
    DataPipeline()
    .add_extractor(JsonExtractor())
    .add_transformer(AggregateTransform())
    .build()
)


csv_clean_pipeline.run_pipeline()
json_aggregate_pipeline.run_pipeline()
