# 1. 환경 설정

## Python 환경 준비

### Python 버전 확인
```bash
python --version
# Python 3.8 이상 권장
```

### 가상환경 생성
```bash
# 프로젝트 디렉토리로 이동
cd python-backend

# 가상환경 생성
python -m venv venv
```

### 가상환경 활성화

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 가상환경 확인
```bash
# 터미널 프롬프트에 (venv)가 표시되어야 함
(venv) C:\path\to\python-backend>
```

## 개발 도구 설정

### IDE 설정 (VS Code 권장)
1. VS Code 설치
2. Python 확장 설치
3. 가상환경을 Python 인터프리터로 설정

### Git 설정
```bash
# .gitignore 파일이 이미 생성되어 있음
git init
git add .
git commit -m "Initial commit: FastAPI project setup"
```

## 환경 변수 설정

### .env 파일 생성
```bash
# env.example을 복사하여 .env 파일 생성
cp env.example .env
```

### .env 파일 편집
```env
# 데이터베이스 설정
DATABASE_URL=sqlite:///./test.db

# JWT 설정
SECRET_KEY=your-secret-key-here

# Redis 설정
REDIS_URL=redis://localhost:6379

# CORS 설정
ALLOWED_HOSTS=["http://localhost:3000", "http://localhost:8080"]
```

## 디렉토리 구조 확인

```bash
# 프로젝트 구조 확인
tree /f  # Windows
# 또는
find . -type f -name "*.py"  # macOS/Linux
```

예상 출력:
```
python-backend/
├── main.py
├── requirements.txt
├── env.example
├── .gitignore
├── README.md
└── app/
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   └── config.py
    ├── routers/
    │   ├── __init__.py
    │   ├── users.py
    │   └── items.py
    ├── schemas/
    │   ├── __init__.py
    │   ├── user.py
    │   └── item.py
    └── services/
        ├── __init__.py
        ├── user_service.py
        └── item_service.py
```

## 다음 단계

환경 설정이 완료되면 [의존성 관리](./02-dependencies.md)로 진행하세요. 