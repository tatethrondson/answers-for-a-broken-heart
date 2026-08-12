(()=>{
  if(!document.querySelector('link[data-ab-heart-home-hero]')){
    const link=document.createElement('link');
    link.rel='stylesheet';
    link.href='/homepage-hero.css?v=20260811-6';
    link.setAttribute('data-ab-heart-home-hero','1');
    document.head.appendChild(link);
  }

  const scripts=[
    ['/site-phase1.js?v=20260812-consolidated2','phase1'],
    ['/site-phase2.js?v=20260812-consolidated2','phase2'],
    ['/site-phase3.js?v=20260812-consolidated2','phase3'],
    ['/site-phase4.js?v=20260812-consolidated1','phase4'],
    ['/site-phase5.js?v=20260812-consolidated1','phase5'],
    ['/site-unified.js?v=20260812-consolidated1','unified'],
    ['/site-finish.js?v=20260812-consolidated1','finish'],
    ['/site-trust.js?v=20260812-minimal2','trust'],
    ['/site-youtube.js?v=20260812-1','youtube'],
    ['/site-editorial.js?v=20260811-2','editorial']
  ];
  scripts.forEach(([src,key])=>{
    if(document.querySelector(`script[data-ab-heart-${key}]`)) return;
    const s=document.createElement('script');
    s.src=src;
    s.defer=true;
    s.setAttribute(`data-ab-heart-${key}`,'1');
    document.head.appendChild(s);
  });
})();