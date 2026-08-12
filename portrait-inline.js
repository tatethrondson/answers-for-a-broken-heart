(()=>{
  const P='/tate-throndson-portrait-final.jpg?v=20260811-restore';
  const THEME='/site-theme.css?v=20260811-1';

  function applyTheme(){
    if(!document.querySelector('link[data-ab-heart-theme]')){
      const link=document.createElement('link');
      link.rel='stylesheet';
      link.href=THEME;
      link.setAttribute('data-ab-heart-theme','journal');
      document.head.appendChild(link);
    }
    const themeMeta=document.querySelector('meta[name="theme-color"]');
    if(themeMeta) themeMeta.setAttribute('content','#fffaf5');
  }

  function applyPortrait(){
    document.querySelectorAll('img').forEach(img=>{
      const alt=(img.alt||'').toLowerCase();
      const src=img.getAttribute('src')||'';
      const isTate=alt.includes('tate throndson') || src.includes('tate-throndson-portrait') || src.includes('author-tate') || src.includes('avatars.githubusercontent.com/u/314793130') || src.includes('/api/portrait-sharp');
      if(isTate && img.getAttribute('src')!==P){
        img.removeAttribute('srcset');
        img.removeAttribute('sizes');
        img.loading='eager';
        img.decoding='sync';
        img.src=P;
      }
    });
  }

  function applyAll(){
    applyTheme();
    applyPortrait();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',applyAll);
  else applyAll();
  new MutationObserver(applyAll).observe(document.documentElement,{childList:true,subtree:true});
})();
