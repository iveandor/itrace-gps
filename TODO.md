# TODO — itrace-gps

## SEO 최적화 후속 작업 (2026-08-17 감사분)

### 1. 배포 (필수)
- [ ] SEO 수정분 커밋 & 푸시 (GitHub Pages — 푸시 전에는 반영 안 됨)
  - 변경 파일: `index.html`(iLog JSON-LD 노드·Organization logo·og:image:alt·문구),
    나머지 5개 HTML(`as="style"` 제거·og:image:alt), `sitemap.xml`(x-default·lastmod),
    신규 `404.html`

### 2. 검색엔진 소유확인 (사용자 직접 작업)
- [ ] `index.html`의 `google-site-verification` 플레이스홀더(`REPLACE_WITH_…`)를
      Google Search Console 발급 코드로 교체
- [ ] `naver-site-verification` 플레이스홀더를 네이버 서치어드바이저 발급 코드로 교체
- [ ] 교체 후 재배포 → 각 콘솔에서 소유확인 → `sitemap.xml` 제출 → 수집(색인) 요청
- 절차 상세: `docs/04-report/seo-setup-user-actions.md`

### 3. 이미지 용량 최적화 (선택)
- [ ] `og-image.png` 262KB 압축 (카톡/슬랙 등 공유 미리보기 로딩 속도)
- [ ] `favicon-512.png` 391KB 압축 (manifest 아이콘)
- 압축 시 1200×630 / 512×512 해상도 유지, 재배포 필요

### 4. 출시 시점 작업 (기존, `CLAUDE.md` Launch state 참조)
- [ ] `.store-btn` placeholder `href="#"` → 실제 App Store / Google Play URL 교체
- [ ] `#launchModal`(출시 준비중 팝업) 및 자동표시 제거
