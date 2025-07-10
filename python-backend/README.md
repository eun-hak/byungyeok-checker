# Python FastAPI Backend

Python FastAPI를 사용한 백엔드 API 서버입니다.

## 기능

- 사용자 관리 (CRUD)
- 아이템 관리 (CRUD)
- RESTful API
- 자동 API 문서 생성
- CORS 지원

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

```bash
cp env.example .env
# .env 파일을 편집하여 필요한 설정을 변경하세요
```

### 4. 서버 실행

```bash
python main.py
```

또는 uvicorn을 직접 사용:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 엔드포인트

### 사용자 API
- `GET /api/v1/users/` - 모든 사용자 조회
- `GET /api/v1/users/{user_id}` - 특정 사용자 조회
- `POST /api/v1/users/` - 새 사용자 생성
- `PUT /api/v1/users/{user_id}` - 사용자 정보 업데이트
- `DELETE /api/v1/users/{user_id}` - 사용자 삭제

### 아이템 API
- `GET /api/v1/items/` - 모든 아이템 조회
- `GET /api/v1/items/{item_id}` - 특정 아이템 조회
- `POST /api/v1/items/` - 새 아이템 생성
- `PUT /api/v1/items/{item_id}` - 아이템 정보 업데이트
- `DELETE /api/v1/items/{item_id}` - 아이템 삭제

## 프로젝트 구조

```
python-backend/
├── main.py                 # 애플리케이션 진입점
├── requirements.txt        # Python 의존성
├── env.example            # 환경 변수 예시
├── README.md              # 프로젝트 문서
└── app/
    ├── __init__.py
    ├── main.py            # FastAPI 애플리케이션
    ├── core/
    │   ├── __init__.py
    │   └── config.py      # 설정 관리
    ├── routers/
    │   ├── __init__.py
    │   ├── users.py       # 사용자 라우터
    │   └── items.py       # 아이템 라우터
    ├── schemas/
    │   ├── __init__.py
    │   ├── user.py        # 사용자 스키마
    │   └── item.py        # 아이템 스키마
    └── services/
        ├── __init__.py
        ├── user_service.py # 사용자 서비스
        └── item_service.py # 아이템 서비스
```

## 개발

### 테스트 실행

```bash
pytest
```

### 코드 포맷팅

```bash
black .
```

### 린팅

```bash
flake8 .
``` 