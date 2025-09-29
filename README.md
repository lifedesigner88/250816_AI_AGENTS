# 250816_AI_AGENTS# 250816_AI_AGENTS

Windows WSL2를 활용해서 GitHub Python 프로젝트를 다운받고 PyCharm으로 실행하는 방법을 정리해드리겠습니다.

## 1. WSL2 및 Ubuntu 설치

### WSL2 설치
```textmate
# PowerShell을 관리자 권한으로 실행
wsl --install
# 재부팅 후
wsl --set-default-version 2
```


### Ubuntu 설치
```textmate
wsl --install -d Ubuntu
```


## 2. Windows에 PyCharm 설치

1. **PyCharm 다운로드 및 설치**
   - JetBrains 홈페이지에서 Windows용 PyCharm Community Edition 다운로드
   - 일반적인 Windows 설치 과정 진행

## 3. WSL2 Ubuntu에서 개발 환경 설정

### WSL2 Ubuntu 접속
```textmate
wsl
```


### 필수 도구 설치
```shell script
# 패키지 업데이트
sudo apt update && sudo apt upgrade -y

# Git 설치
sudo apt install git

# Python 3.13 설치
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13 python3.13-venv python3.13-dev python3-pip

# UV 패키지 매니저 설치
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```


## 4. GitHub 프로젝트 클론 및 환경 설정

```shell script
# 프로젝트 디렉토리 생성
mkdir ~/projects
cd ~/projects

# GitHub 프로젝트 클론
git clone https://github.com/username/repository-name.git
cd repository-name

# UV로 가상환경 생성 및 의존성 설치
uv venv --python 3.13
source .venv/bin/activate

# 의존성 설치
uv sync  # pyproject.toml이 있는 경우
# 또는
uv pip install -r requirements.txt  # requirements.txt가 있는 경우

# Jupyter 설치 (main.ipynb가 있는 경우)
uv add jupyter
```


## 5. PyCharm에서 WSL2 프로젝트 열기

### 프로젝트 열기
1. **PyCharm 실행** (Windows에서)
2. **Open** 클릭
3. **\\wsl$\Ubuntu\home\username\projects\repository-name** 경로로 이동
4. 프로젝트 폴더 선택 후 **Open**

### WSL2 Python 인터프리터 설정
1. **File** → **Settings** (또는 `Ctrl+Alt+S`)
2. **Project: [project-name]** → **Python Interpreter**
3. 톱니바퀴 아이콘 → **Add...**
4. **WSL** 선택
5. **Linux distribution**: Ubuntu 선택
6. **Python interpreter path**: `/home/username/projects/repository-name/.venv/bin/python`
7. **OK** 클릭

## 6. 프로젝트 실행

### Python 스크립트 실행
- 파일 우클릭 → **Run 'filename.py'**
- 또는 `Ctrl+Shift+F10`

### Jupyter Notebook 실행 (main.ipynb)
1. **main.ipynb** 파일 더블클릭
2. PyCharm이 WSL2에서 Jupyter 서버 자동 시작
3. 셀 실행: `Shift+Enter`

### 터미널 사용
1. **View** → **Tool Windows** → **Terminal**
2. WSL2 터미널이 자동으로 열림
3. 가상환경 자동 활성화 확인

## 7. 추가 설정 및 팁

### Git 설정 (WSL2에서)
```shell script
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```


### Windows-WSL2 파일 접근
- **Windows에서 WSL2 파일**: `\\wsl$\Ubuntu\home\username\`
- **WSL2에서 Windows 파일**: `/mnt/c/Users/username/`

### 의존성 추가 설치
```shell script
# WSL2 터미널에서
source .venv/bin/activate
uv add package-name
```


### 성능 최적화
- 프로젝트 파일을 WSL2 파일시스템에 저장 (Windows 파일시스템보다 빠름)
- PyCharm 인덱싱 완료까지 기다리기

## 8. 트러블슈팅

### WSL2 연결 문제
```textmate
# WSL2 재시작
wsl --shutdown
wsl
```


### Python 인터프리터 인식 안 됨
- PyCharm에서 **File** → **Invalidate Caches and Restart**

이제 Windows에서 PyCharm을 사용해 WSL2 Ubuntu 환경의 Python 프로젝트를 효율적으로 개발할 수 있습니다!