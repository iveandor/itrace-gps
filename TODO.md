# TODO — itrace-gps

## SEO 최적화 후속 작업 (2026-08-17 감사분)

### 1. 배포 (필수)
- [x] SEO 수정분 커밋 & 푸시 (GitHub Pages — 푸시 전에는 반영 안 됨) — **완료**: `12f2948`(2026-08-17) 푸시·반영
      (2026-09-14 확인: `sitemap.xml` x-default · 7개 HTML og:image:alt · `as="style"` 0건 · 라이브 `404.html` 200)
  - 변경 파일: `index.html`(iLog JSON-LD 노드·Organization logo·og:image:alt·문구),
    나머지 5개 HTML(`as="style"` 제거·og:image:alt), `sitemap.xml`(x-default·lastmod),
    신규 `404.html`

### 2. 검색엔진 소유확인 (사용자 직접 작업)
- [x] Google Search Console — **완료** (2026-09-06 확인: `itrace.iveandor.com` 도메인 속성 · 인증된 소유자 ·
      `iveandor.com` DNS TXT 로 상속 · 2026-07-07 등록). `google-site-verification` 메타는 도메인 속성에서
      쓰이지 않으므로 `index.html` 에서 **삭제**(`85e7be3` 으로 푸시됨 — 다시 넣지 말 것)
- [x] `naver-site-verification` 플레이스홀더를 네이버 서치어드바이저 발급 코드로 교체 — 2026-09-06 적용·푸시(`85e7be3`)
- [x] 서치어드바이저 소유확인 **통과** + `sitemap.xml` 제출 (2026-09-06)
- [x] 서치어드바이저 `요청 → 웹페이지 수집` 7개 URL 요청 완료 · `검증 → robots.txt` 정상 수집 확인(간단체크 "없음"=오탐 확정) ·
      Google Sitemaps 제출 성공(발견 7페이지) — 전부 2026-09-06
- [x] 다음(카카오) 검색 등록 신청 완료 (2026-09-06 — 결과는 support@ 메일로)
- [ ] 결과 확인(며칠~몇 주 뒤): 다음 처리 메일 · 네이버 `검증 → 사이트맵` 7개 인식 · 간단체크 재조회(경고 0건 기대) ·
      구글 `색인 생성 > 페이지` 색인 수(기대 7) — 체크리스트 E(SEO 문서)
- 절차 상세: `../iLogTerraform/docs/marketing/itrace-gps-seo-setup.md`
  (2026-09-06 이관 — 구 경로 `docs/04-report/seo-setup-user-actions.md`. 이 repo `docs/` 는 gitignore 라 동기화가 안 됐다)
- [x] `index.html` `description` 135→70자 · `og:description` 117→60자 + 하위 4개 페이지 `description` 80자 이내 축약 (2026-09-06)

### 3. 이미지 용량 최적화 (선택)
- [ ] `og-image.png` 262KB 압축 (카톡/슬랙 등 공유 미리보기 로딩 속도)
- [ ] `favicon-512.png` 391KB 압축 (manifest 아이콘)
- 압축 시 1200×630 / 512×512 해상도 유지, 재배포 필요

### 4. 출시 시점 작업 (기존, `CLAUDE.md` Launch state 참조)
- [x] CTA를 **앱별 스토어 버튼 구조**로 개편 (2026-08-17): `.cta__stores` 아래 3그룹 —
      iTrace(Play ✅ + App Store ✅), iLogMobile(Play ✅ · App Store ✅), iLog(Play 준비중).
      **iTrace Google Play 링크 라이브**: `https://play.google.com/store/apps/details?id=com.iveandor.itrace`
      (JSON-LD `installUrl`·모달·user_guide §2에도 링크 반영)
- [x] **iTrace App Store 라이브 (2026-09-05)**: `https://apps.apple.com/kr/app/itrace/id6761924543` —
      CTA 버튼 `--soon` 해제 + JSON-LD `installUrl` 배열화 + 모달 2번째 버튼 + user_guide §2 링크 반영
- [x] **iLogMobile Google Play 라이브 (사이트 반영 2026-09-05, 스토어 출시 08-31)**:
      `https://play.google.com/store/apps/details?id=com.iveandor.ilog.mobile` —
      CTA 버튼 `--soon` 해제 + JSON-LD `installUrl` + 모달 문구·인라인 링크 + user_guide §3 설치 링크 반영
- [x] **iLogMobile App Store 라이브 (2026-09-05)**: `https://apps.apple.com/kr/app/ilogmobile/id6768343628` —
      CTA 버튼 `--soon` 해제 + JSON-LD `installUrl` 배열화 + 모달 문구·인라인 링크 + user_guide §3 링크 반영.
      남은 플레이스홀더 = iLog Google Play 1개.
- [ ] 각 앱/스토어 출시 시: 해당 `.store-btn--soon` 버튼의 `href="#"` → 실제 URL 교체 +
      `store-btn--soon` 클래스·aria-label 제거 + `.top` 라벨을 "GET IT ON"/"Download on the"로 교체
      (모달 자동 제외됨 — 스크립트가 `href="#"`인 버튼만 모달로 연결)
- [ ] 전체 앱(iLog·iLogMobile·iOS) 출시 완료 시: `#launchModal` 및 자동표시 제거

### 5. 자녀 앱 개명("iTrace 자녀") 과도기 표기 (2026-09-13 반영 → 2026-09-18 정리 완료)
자녀 앱 표시명이 iLogMobile·iLog → 「iTrace 자녀」로 바뀌었지만 3앱 배포·스토어명 변경이 날짜별로 나뉘어,
사이트는 한동안 **새 이름 + "이전 이름" 병기**로 썼다. 2026-09-18 오너 확인(Android·iOS 모두 새 이름으로 배포됨)으로
"이전 이름" 표기를 전부 걷어냈다.
- [x] **push 시점**: `1dd9fcf` origin/main 반영 · 라이브에 "이전 이름" 병기 노출 확인(2026-09-14)
- [x] 스토어 제목이 새 이름인지 공개 데이터로 확인(2026-09-18): App Store `iTrace - 자녀 위치 안심`(id6761924543) ·
      `iTrace 자녀`(id6768343628, 1.2.2 · 09-17) / Play `iTrace - 자녀 위치 안심` · `iTrace 자녀 - 스마트폰용`.
      갤럭시 워치용 Play 는 여전히 미출시(웹 페이지 404) — CTA `--soon` 유지
- [x] "이전 이름 …" 표기 제거(2026-09-18): 안내 박스(`user_guide` §1 · `permissions_guide` 상단 · `index` `#apps` 한 줄 + CSS
      `.apps__rename`) · 카드·CTA `<small>` · 런치 모달 · JSON-LD HowTo/HowToTool 문구 · `pairing_guide` "업데이트 전" 보조문구 ·
      FAQ "iLogMobile · iLog 앱이 보이지 않아요"(화면 + FAQPage JSON-LD 함께 삭제, 12↔12 유지) · Tweaks 라벨 · 주석
- [x] 브랜드 워드마크 `iTrace & iLog & iLogMobile` → **`iTrace`** 로 통일(2026-09-18): 8개 HTML 의 title · og/twitter · nav
      aria-label · footer · © · WebSite JSON-LD `name` · `site.webmanifest` `name`. `keywords` 메타의 옛 이름도 제거
- [x] JSON-LD `alternateName`(`index.html` 자녀 앱 노드 2개의 `iLog` · `iLogMobile`)은 **의도적으로 유지** — 화면에 안 보이고,
      옛 이름으로 검색하는 기존 사용자를 사이트로 연결하는 유일한 기계용 단서. 지우려면 이 항목을 근거로 결정
- [ ] 법적 문서 3종(`privacy_policy`·`terms_of_use`·`account_deletion`)은 **본문 앱명(iLog · iLogMobile)을 그대로 두었다** —
      09-18 정리는 title/meta/nav/footer 의 워드마크만. 본문 전환은 다음 개정(시행일 변경) 때 법률 검토와 함께, 아래 §6 절차로.
      `legal/versions.json` 미변경(시행일이 안 바뀌었으므로)

### 6. 법적 문서 개정 절차 (약관 버전관리, 2026-09-14 도입)
앱(iTrace 가입·iLogMobile 연동)은 `legal/versions.json` 의 `version`(= **시행일**, `YYYY-MM-DD`)을 동의 버전으로 서버에
기록하고, 기존 사용자에게는 저장된 버전과 매니페스트를 비교해 개정 안내(또는 재동의)를 띄운다. 따라서
`terms_of_use.html`·`privacy_policy.html` 본문을 개정할 때는 **아래 항목을 한 커밋으로** 올려야 한다(GitHub Pages 는
커밋 단위 배포라 원자적). 정본 절차: `../iLogTerraform/docs/guide/itrace-gps-site.md` "법적 문서 버전 매니페스트".
- [ ] 두 HTML 헤더의 `최종 수정일`·`시행일` 갱신(시행일 = 고지일 + 7일 이상 — 약관 §3④·방침 §11. 이용자에게 불리한
      변경이면 30일 유예 검토)
- [ ] `terms_of_use.html` 부칙에 `제N조 (개정 약관의 시행일)` 추가(개정일·시행일·개정 요지)
- [ ] `legal/versions.json` — 해당 문서의 `version`(새 시행일) · `revisedAt`(최종 수정일) · `noticeFrom`(공지 시작일 = 보통
      최종 수정일) · `requiresExplicitConsent`(새 수집 항목 등 명시 재동의가 필요한 개정이면 `true`) · `summary`(앱 안내 문구) ·
      `history`(직전 시행일을 맨 앞에 추가). 개정하지 않은 문서는 건드리지 않는다
- [ ] `python3 check_legal_versions.py` exit 0 확인(헤더·부칙·매니페스트 정합 검사)
      — 같은 검사가 GitHub Actions `legal-check`(`.github/workflows/legal-check.yml`)로 push/PR 마다 자동 실행된다(Pages 는
      파이썬을 실행하지 않으므로 CI 가 유일한 자동 관문). 빨간 체크면 매니페스트나 헤더 중 하나가 덜 바뀐 것
- [ ] `sitemap.xml` 의 해당 페이지 `lastmod` 갱신
- [ ] 한 커밋으로 push → `curl -s https://itrace.iveandor.com/legal/versions.json` 로 반영 확인(GitHub Pages 캐시 최대 10분)
- [ ] 앱에서 확인: iTrace 로그인 후 개정 안내 게이트가 `noticeFrom` 부터 뜨는지, 가입 화면 시행일 표기가 새 값인지
- 앱 폴백 상수(`iTrace/src/shared/constants/legal.ts`·`iLogMobile/src/constants/legal.ts` 의 `LEGAL_FALLBACK_VERSIONS`)는
  매니페스트 fetch 실패 시에만 쓰인다 — 다음 앱 릴리스 때 맞춰 올리면 되고, 사이트 개정을 막지 않는다
