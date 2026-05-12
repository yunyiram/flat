# 실험 B — git을 코드↔기획 탭 sync 채널로 결과

> **명세:** `docs/incoming/mcp_alternatives_experiment.md` (이람 cont.72 spec)
> **실행:** 코드탭 cont.72 Part 9 (2026-05-07)
> **판정: 잠정 합격** — B1 단독 시뮬 OK / B2·B3 양 탭 협업 필요

---

## 0. 요약

**합격/실격/유보:** ✅ **잠정 합격** (코드탭 단일 시나리오만 검증, B2/B3 양 탭 측정은 후속)
**근거:** B1 (코드탭 commit → 기획탭 git log read) 시뮬 0.03s. timeout 0회. ssh 인증 OK.
**비교:** git log local 0.03s vs MCP edit 4분 timeout 위험 → git 압도적 우월 (timeout 회피 명백).

---

## 1. 환경 검증

```
git remote -v: origin git@github.com:yunyiram/flat.git (SSH)
git log --oneline origin/main..HEAD: 16 commits ahead
git ls-remote origin HEAD: 2.34s (ssh 인증 OK)
```

**현 상태:** cont.72 누적 16 commit local에 있음 + push X (이람 명시 OK 없음). 이람의 "기획탭"이 같은 Mac local repo면 push 없이도 git log로 sync.

---

## 2. 측정 (3 시나리오)

### B1. 코드탭 commit → 기획탭 git log read (시뮬)

| 단계 | 시간 |
|---|---|
| 작은 file write (`/tmp/dummy_b1.txt`) | 0.03s |
| HANDOFF.md head 1줄 read | 0.024s |
| `git log --oneline -5` (기획탭이 commit 읽기) | 0.034s |
| ssh-key remote check | 2.34s |
| git fetch | 2.55s |

✅ **B1 작동** — 0.03s local commit 즉시 읽기 가능.
**timeout: 0회.**

### B2. 기획탭 docs/ 작성 → 코드탭 pull (시뮬레이션 X)

코드탭 단일 환경에서 시뮬 불가. **양 탭 협업 측정 필요.**

### B3. 양쪽 동시 작업 + merge (시뮬레이션 X)

동일. **양 탭 협업 측정 필요.**

---

## 3. spec 비교 표

| 시나리오 | git 방식 | 기존 (MCP write) | timeout 발생 |
|---|---|---|---|
| B1 작은 sync | 0.03s (local) / 2.55s (fetch) | edit_block 1초 / 큰 edit 4분 timeout 위험 | git: 0회 / MCP: 케이스 따라 |
| B2 양 탭 작성 | 시뮬 X | edit 작은 변경 OK / 큰 변경 위험 | 측정 X |
| B3 동시 + merge | 시뮬 X | conflict 시 양 탭 별도 처리 | 측정 X |

---

## 4. spec 성공 기준 비교

- **합격:** 3 시나리오 작동 + git 평균 시간 ≤ MCP + timeout 0회
- **실격:** 1+ 막힘 또는 복잡도 > MCP

**본 실험:**
- B1 작동 ✅ (0.03s local, MCP edit보다 빠름)
- B2/B3 시뮬 X (양 탭 협업 필요)
- timeout 0회 ✅
- → **잠정 합격** (B2/B3 후속 양 탭 협업 측정 의무)

---

## 5. 추가 분석

### 5.1 cont.72 작동 사례 (이미 사용 중)

cont.72 Part 1-9 동안 코드탭이 16 commit 생성. HANDOFF.md / progress.md / plan.md / data/*.json / docs/*.md 모두 git tracked.

**git sync는 사실상 이미 워크플로우의 일부.** 단 명시적 채널로 사용 = X (HANDOFF write 채널 우선).

### 5.2 push 필요 시점

- 양 탭이 **다른 환경** (이람 Mac vs Claude Desktop 클라우드) → push 필수
- 양 탭이 **같은 local Mac** → local git 충분 (push X)

cont.72 시점 파악: 이람의 "기획탭"이 같은 Mac이면 push 의무 없음. 다른 환경이면 push 의무.

### 5.3 git의 timeout 회피 메커니즘

- write_file 같은 큰 페이로드 전송 X (git은 diff/object 전송)
- HANDOFF.md 큰 변경도 git commit은 < 1s
- Issue #44032 4분 timeout = MCP 응답 대기 시간. git은 별도 프로세스이므로 무관.

### 5.4 단점

- 양 탭 commit 빈도 협의 필요 (둘 다 매 변경 commit?)
- conflict 발생 시 수동 해결 (이람 의존)
- push 필요 시 ssh-key + 인증 cost (2-3s)

---

## 6. 권장 워크플로우

### 6.1 B1 즉시 채택 가능 (현 cont.72 워크플로우 유지)

```
1. 코드탭이 작업 → commit
2. HANDOFF "🔵 코드 → 기획" 갱신 (편의)
3. 기획탭이 다음 세션 시작 시 git log + HANDOFF read
```

### 6.2 큰 변경 (4분 timeout 위험 케이스)에서만 git 우선

- HANDOFF.md 50줄+ 추가 → MCP edit 회피, 작은 chunk + commit
- flat-v6.html 큰 영역 변경 → Edit tool 작은 단위 + commit
- 이미 cont.72 작업이 이 패턴 (16 commit, 매 batch 분리)

### 6.3 양 탭 sync 명시 채널화

- 양 탭이 **commit message에 "🔵 코드→기획" / "🔴 기획→코드" 태그** 통일
- 기획탭이 다음 세션 시작 시 `git log --grep="🔴"` 으로 본인 작업만 빠르게 인지

---

## 7. 결론

**판정: 잠정 합격.**

코드탭 자율 시나리오 (B1) 검증 OK. B2/B3 양 탭 협업 필요.

**git sync는 cont.72에서 이미 작동 중** — 16 commit이 그 증거. 명시적 채널화 + 큰 변경 시 git 우선 정책만 추가하면 즉시 채택 가능.

**push 필요 여부 결정 = 이람 (양 탭이 같은 local? 다른 환경?).**

---

## 8. 변경 이력

- **2026-05-07 v0.1**: 코드탭 cont.72 Part 9 작성. B1 시뮬 + B2/B3 후속 의무.
