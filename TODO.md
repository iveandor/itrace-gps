# TODO — itrace-gps

## SEO 최적화 후속 작업 (2026-08-17 감사분)

### 1. 배포 (필수)
- [ ] SEO 수정분 커밋 & 푸시 (GitHub Pages — 푸시 전에는 반영 안 됨)
  - 변경 파일: `index.html`(iLog JSON-LD 노드·Organization logo·og:image:alt·문구),
    나머지 5개 HTML(`as="style"` 제거·og:image:alt), `sitemap.xml`(x-default·lastmod),
    신규 `404.html`

### 2. 검색엔진 소유확인 (사용자 직접 작업)
- [x] Google Search Console — **완료** (2026-09-06 확인: `itrace.iveandor.com` 도메인 속성 · 인증된 소유자 ·
      `iveandor.com` DNS TXT 로 상속 · 2026-07-07 등록). `google-site-verification` 메타는 도메인 속성에서
      쓰이지 않으므로 `index.html` 에서 **삭제**(⏳ 미푸시 — 다시 넣지 말 것)
- [ ] `naver-site-verification` 플레이스홀더를 네이버 서치어드바이저 발급 코드로 교체
- [ ] 교체 후 재배포 → 네이버 소유확인 → `sitemap.xml` 제출(구글은 Sitemaps 메뉴에서 제출 여부만 확인) → 수집(색인) 요청
- 절차 상세: `../iLogTerraform/docs/marketing/itrace-gps-seo-setup.md`
  (2026-09-06 이관 — 구 경로 `docs/04-report/seo-setup-user-actions.md`. 이 repo `docs/` 는 gitignore 라 동기화가 안 됐다)
- [ ] `index.html` `description` 135자 → 70자 · `og:description` 117자 → 60자 축약
      (네이버 권장 80자 초과 — 교체안은 위 문서 §1-B·§1-C). 하위 4개 페이지 `description` 도 80자 초과

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
