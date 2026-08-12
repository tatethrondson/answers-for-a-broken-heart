(()=>{
  const scripts=[
    ['/site-phase1.js?v=20260811-1','phase1'],
    ['/site-phase2.js?v=20260811-1','phase2'],
    ['/site-phase3.js?v=20260811-1','phase3'],
    ['/site-phase4.js?v=20260811-1','phase4']
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
