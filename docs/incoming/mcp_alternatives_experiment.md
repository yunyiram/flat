# MCP 대안 실험 — 코드 탭용 명세

> **이람 cont.72 → 코드탭 spec (메시지 전달, 코드탭이 `docs/incoming/`에 저장).**
> 작성: 기획탭 / 저장: 코드탭 cont.72 Part 9 (2026-05-06)

## 파일 위치 약속

* 이 명세 파일 위치: `/Users/yiram/Claude/flat/docs/incoming/mcp_alternatives_experiment.md` (이람씨가 옮겨놓음)
   * 만약 이람씨가 파일을 옮기지 않고 메시지로 내용만 전달했다면, 코드 탭이 먼저 `/Users/yiram/Claude/flat/docs/incoming/`에 같은 파일명으로 저장한 뒤 진행.
* 실험 결과 기록 위치: `/Users/yiram/Claude/flat/docs/archive/mcp_experiment_A_desktopcommander.md`, `mcp_experiment_B_git_sync.md`
* 분리 이유: `incoming/` = 받은 작업 지시, `archive/` = 끝난 결과 기록. 코드 탭은 이 분리를 지킴.

## 목적

Filesystem MCP의 4분 timeout (Anthropic Issue #44032 — 클라이언트 측 하드코딩, 설정 무시) 의존도를 낮추는 두 가지 대안을 실험. 이람씨가 판단할 수 있도록 측정 가능한 결과를 만든다.

근거 자료: cont.72 RCA 사고 5 (긴 본문 hang) + GitHub anthropics/claude-code Issue #44032, #43791, #20335.

추가 작업: 본 실험과 별도로, cont.72 RCA에 사고 6번 (결론 강도 회피 — 안전한 답으로 첫 답을 깔고 사용자 푸시백 받아야 한 가지 답으로 좁히는 패턴. 메모리 Rule 10과 동일 패턴) 한 줄 추가.

## 실험 A — DesktopCommander MCP

### 가설
Filesystem MCP보다 안정적이라는 사용자 후기 다수. diff-based editing으로 큰 페이로드 전송을 회피하는 구조라 Issue #44032 4분 timeout에 덜 걸린다.

### 작업

1. 설치
```bash
npx @wonderwhy-er/desktop-commander setup
# 또는 npm install -g @wonderwhy-er/desktop-commander
```
설치 시 Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`)에 자동 추가. 설치 직전 config 백업 (`cp claude_desktop_config.json claude_desktop_config.json.bak`).

2. Claude Desktop 재시작 후 MCP 활성화 확인.

3. 측정 작업 5개 (Filesystem MCP에서 timeout 났던 케이스 재현):
   * A1. flat-v6.html 전체 read
   * A2. HANDOFF.md 큰 변경 1회 (50줄 이상 추가)
   * A3. docs/ 디렉토리 list
   * A4. collar_geometry_cheatsheet.md 같은 큰 .md 신규 write
   * A5. flat-v6.html에서 정확한 string match로 edit (예: 특정 함수 한 곳 수정)

각 작업 3회 반복. 결과 표:
```
| 작업 | 1차 (시간/성공) | 2차 | 3차 | 비고 |
```

### 성공 기준
* 합격: 5개 작업 × 3회 = 15회 중 13회 이상 성공 (약 87%). 평균 응답 시간 60초 이하.
* 실격: 13회 미만 성공, 또는 4분 timeout 4회 이상 발생, 또는 설치 자체 실패.
* 유보: 13-14회 성공이지만 특정 작업 유형에 편향된 실패 → 그 작업 유형만 bash로 우회하는 부분 채택.

### 시간 한계
설치 30분 + 측정 90분 = 총 2시간. 초과 시 일단 중단하고 이람씨에게 보고.

### 결과 기록 위치
`docs/archive/mcp_experiment_A_desktopcommander.md`

## 실험 B — git을 코드↔기획 탭 sync 채널로

### 가설
HANDOFF.md를 매번 write하지 않고 git commit/pull로 동기화하면, MCP write를 거치지 않으므로 4분 timeout이 일어날 곳이 없다. 양 탭이 둘 다 git 가능.

### 작업

1. 현재 git 상태 확인
```bash
cd /Users/yiram/Claude/flat
git status
git log -5 --oneline
git remote -v  # 원격 있는지
```
원격 없으면 로컬만 사용. 있으면 push/pull 사이클 검증.

2. 측정 시나리오 3개 (현재 워크플로우 미러):
   * B1. 코드 탭이 flat-v6.html 변경 + HANDOFF.md append → commit. 기획 탭이 해당 commit 읽음 (read 또는 conversation_search).
   * B2. 기획 탭이 docs/에 새 .md 작성 → commit. 코드 탭이 git pull 후 read.
   * B3. 양쪽이 충돌 없는 다른 파일을 동시 작업 → 양쪽 commit → 한쪽 pull 시 merge 자연 처리.

3. 비교 측정:
```
| 시나리오 | git 방식 시간 | 기존(MCP write) 방식 시간 | timeout 발생 |
```

### 성공 기준
* 합격: 3개 시나리오 모두 작동 + git 방식 평균 시간이 MCP write 방식보다 짧거나 비슷 + timeout 0회.
* 실격: 시나리오 1개 이상 git에서 막힘 (인증, conflict 빈발, 등) 또는 사용 복잡도가 MCP보다 큼.
* 유보: 작동하지만 양 탭 사이 commit 빈도 협의가 필요 — 워크플로우 변경 큰 경우.

### 시간 한계
검증 60분. 초과 시 중단·보고.

### 결과 기록 위치
`docs/archive/mcp_experiment_B_git_sync.md`

## 실험 종료 후 코드 탭이 할 일

세 가지 결과 보고 — 각각 한 줄 요약 + 합격/실격/유보 + 근거 데이터 링크:

1. 실험 A 결과
2. 실험 B 결과
3. 권장안 (코드 탭 판단): A 채택 / B 채택 / 둘 다 채택 / 둘 다 폐기 (현 bash 우회 룰 유지) / 부분 조합 — 그리고 그 이유

이람씨는 이 권장안 + 측정 데이터를 보고 최종 결정. 코드 탭이 결정하지 않음 (Rule 3 — 도메인 존중. 워크플로우 결정은 이람씨 도메인).

보고 시 다음 안내 함께 출력 (이람씨가 잊지 않도록):

> "실험 종료. 결정 후 메모리 항목 18 (진행 중 실험 표시) 삭제 부탁드립니다. 채택안이 있으면 항목 11 (FLAT 파일 관리)에 한 줄 반영도 같이."

## 실험 자체의 안전장치

* 백업: `claude_desktop_config.json` 백업 후 실험 A 시작.
* 롤백 명세: 실험 A 실패 시 `mv claude_desktop_config.json.bak claude_desktop_config.json` + Claude Desktop 재시작.
* 실험 중 메인 작업 중단: 마감 임박 항목(YC 5/4 already passed 또는 다음 마감) 작업 중에는 실험 시작하지 않음. 한가한 시간 블록에 진행.
* 측정 신뢰도: 같은 환경(Claude Desktop 재시작 직후 vs 장시간 사용 후)에서 결과 다를 수 있음. 가능하면 두 환경 다 측정.
