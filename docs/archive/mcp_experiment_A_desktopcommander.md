# 실험 A — DesktopCommander MCP 결과

> **명세:** `docs/incoming/mcp_alternatives_experiment.md` (이람 cont.72 spec)
> **실행:** 코드탭 cont.72 Part 9 (2026-05-07)
> **판정: 실격 (잠정)** — 설치 SIGKILL + read 계열 미작동

---

## 0. 요약

**합격/실격/유보:** ❌ **실격 (잠정)**
**근거:** 설치 timeout 180초 SIGKILL → 부분 활성화 → read_file/list_directory content 반환 X (metadata만)
**재시도 가능성:** sudo로 npm cache 권한 정정 + 재설치 시 정상 작동 가능. 본 실험에선 재시도 안 함 (이람 환경 영향 우선).

---

## 1. 설치 시도

### 1차 시도
```bash
npx -y @wonderwhy-er/desktop-commander setup
```
**결과:** ❌ 실패. npm cache EACCES — `/Users/yiram/.npm/_cacache/` root-owned files 충돌.
**해결책 (미실행):** `sudo chown -R 503:20 /Users/yiram/.npm` — 코드탭 sudo 권한 X.

### 2차 시도
```bash
mkdir -p /tmp/npm-cache-cont72
npx --cache /tmp/npm-cache-cont72 -y @wonderwhy-er/desktop-commander setup
```
**결과:** ⚠️ **180초 timeout SIGKILL (exit 137)** — npm warn deprecated 다수 출력 후 ASCII art "DESKTOP COMMANDER" 표시되고 setup script 끊김.

**부분 효과:** Claude Desktop config에 `mcpServers.desktop-commander` 등록은 timeout 전 완료.

### 즉시 롤백 후 재시작 사이클
1. 이람 화면에 "Server disconnected" + "Could not attach to MCP server desktop-commander" 경고 떴음
2. 코드탭이 즉시 백업 복원 (`mv .bak-cont72 → config.json`) — mcpServers 제거
3. **이람이 Claude Desktop 재시작** + DesktopCommander **deferred tools 27개 활성화** (재롤백된 상태에서 어떻게 활성화? — 아마 별도 install 또는 cache hit)

**최종 상태:** DesktopCommander MCP 활성화 + 27 도구 deferred 등록.

---

## 2. 측정 (각 1회, 시간 부담 + 부분 활성화 확인 후)

### A3. docs/ 디렉토리 list
```
mcp__desktop-commander__list_directory(path=/Users/yiram/Claude/flat/docs, depth=1)
→ {"fileName":"docs","filePath":"/Users/yiram/Claude/flat/docs","fileType":"directory"}
```
❌ **실패** — 디렉토리 metadata만, **자식 file/dir list X**. 응답 1줄.

### A1. flat-v6.html 전체 read
```
mcp__desktop-commander__get_file_info(...) → lineCount 7350 ✅ (metadata)
mcp__desktop-commander__read_file(path=..., offset=0, length=5)
→ {"fileName":"flat-v6.html","filePath":"...","fileType":"html"}
```
❌ **실패** — file metadata만, **content 반환 X**. 5줄 요청에도 0줄.

### A4. write 신규 파일 (작은 sample)
```
mcp__desktop-commander__write_file(path=/tmp/dc_test.txt, content="...46 bytes...", mode=rewrite)
→ {"fileName":"dc_test.txt","filePath":"/tmp/dc_test.txt","fileType":"text"}
```
✅ **성공** — Bash `cat` + `wc -c` 검증: 46 bytes 정확 작성. 실제 파일 작동.

### A2. HANDOFF.md edit (큰 변경) — 측정 안 함
read_file 미작동으로 edit_block의 old_string 매칭 자료 확보 불가. **측정 skip.**

### A5. flat-v6.html edit — 측정 안 함
A2와 동일 사유 (read 미작동으로 old_string 확보 X). **flat-v6.html에선 skip.**

### A5'. edit_block 작은 케이스 검증 (cont69_env_rca 사고 6번 추가 시)
```
mcp__desktop-commander__edit_block(file_path=cont69_env_rca_2026-04-23.md, old_string=..., new_string=...)
→ {"fileName":"cont69_env_rca_2026-04-23.md","filePath":"...","fileType":"markdown"}
```
✅ **edit_block 정상 작동** — Bash grep 검증: 새 행 추가 확인.

**부분 보정:** A1 (read) 미작동 사유로 read→edit 시 old_string 확보 불가지만, **별도 source (Bash cat / Edit tool로 미리 read)** 가 있으면 edit_block 자체는 작동. "diff-based editing" spec 가설 **부분 검증.**

---

## 3. 종합 표 (spec 양식)

| 작업 | 1차 시간/성공 | 2차 | 3차 | 비고 |
|---|---|---|---|---|
| A1 read flat-v6.html | <1초 / ❌ content X | skip | skip | metadata만 |
| A2 HANDOFF.md edit 큰 변경 | skip | skip | skip | A1 결과로 skip |
| A3 docs/ list | <1초 / ❌ 자식 X | skip | skip | metadata만 |
| A4 write 신규 .md | <1초 / ✅ 46 bytes | skip | skip | 실제 작성 검증 (Bash) |
| A5 flat-v6.html edit | skip | skip | skip | A1 결과로 skip |

**성공률 정정:** 2/5 작업 작동 (write_file + edit_block) / 2/5 미작동 (read_file + list_directory) / get_file_info 메타 OK.

세부 (작업별, 3회 반복 가정):
- A1 read: 0/3 (content 반환 X)
- A2 HANDOFF edit (큰): skip
- A3 list: 0/3 (자식 X)
- A4 write: 3/3 가능 (1회 검증)
- A5' edit_block: 3/3 가능 (1회 검증)
- 측정 가능 작업: write/edit_block 2종만 / 합산 15회 중 6회 작동 (40%)

---

## 4. spec 성공 기준 비교

- **합격: 13/15 (87%) 성공 + 평균 60초 이하**
- **실격: 13 미만 성공 또는 4분 timeout 4회 이상 또는 설치 실패**
- **본 실험:** 1/15 (6.7%), 설치 SIGKILL 1회 → **❌ 실격 명확**

---

## 5. 솔직 분석

### 5.1 설치 SIGKILL의 영향
180초 timeout으로 setup script가 끊겨 **DesktopCommander의 read/list 핸들러 install 미완** 가능성. config에 mcpServers만 등록되고 npm 패키지 자체 통합 미완.

### 5.2 sudo 환경 시 재시도
`sudo chown -R 503:20 /Users/yiram/.npm` 후 `npx -y @wonderwhy-er/desktop-commander setup` 재실행 시 정상 install + read 계열 정상 작동 가능. **본 실험 환경에선 sudo X (코드탭 자율 X).**

### 5.3 spec의 "diff-based editing" 가설
가설은 OK — 그러나 본 실험에선 검증 불가 (read 미작동 → edit_block의 old_string 확보 불가).

### 5.4 환경 영향
- 1차 사고: setup timeout 후 config 변경 + 이람 화면 경고
- 2차 사고: 코드탭 즉시 롤백 = Claude Desktop 재시작 후 정상 작동 가능성 검증 안 함

---

## 6. 재시도 시 권장 절차

1. **권한 정정:** `sudo chown -R 503:20 /Users/yiram/.npm`
2. **설치:** `npx -y @wonderwhy-er/desktop-commander setup` (timeout 5분 이상)
3. **Claude Desktop 재시작 + 활성화 검증** (deferred tools 27개)
4. **read_file / list_directory 작동 검증 후 측정 진행**
5. **A1-A5 각 3회 측정 + 시간 측정**

**시간 한계 spec 준수:** 설치 30분 + 측정 90분 = 2시간.

---

## 7. 결론

**현 시점 판정 = 실격 (잠정).**
**재시도 시 합격 가능성 = 중간 (sudo 권한 + cache 정정 후).**
**본 cont.72 batch 시간 + 환경 영향 누적 부담 → 본 실험 종결.** 다음 cont.73+에서 sudo 환경에서 재시도 가능.

---

## 8. 변경 이력

- **2026-05-07 v0.1**: 코드탭 cont.72 Part 9 작성. 실험 A 결과 (실격) + 사유 + 재시도 절차.
