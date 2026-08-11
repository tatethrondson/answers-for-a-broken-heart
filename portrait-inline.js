(()=>{
  const P='/tate-throndson-portrait-final.jpg?v=20260810-2';
  function applyPortrait(){
    document.querySelectorAll('img').forEach(img=>{
      const alt=(img.alt||'').toLowerCase();
      const src=img.getAttribute('src')||'';
      const isTate=alt.includes('tate throndson') || src.includes('tate-throndson-portrait') || src.includes('author-tate') || src.includes('avatars.githubusercontent.com/u/314793130');
      if(isTate && img.getAttribute('src')!==P){
        img.removeAttribute('srcset');
        img.removeAttribute('sizes');
        img.loading='eager';
        img.decoding='sync';
        img.src=P;
      }
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',applyPortrait);
  else applyPortrait();
  new MutationObserver(applyPortrait).observe(document.documentElement,{childList:true,subtree:true});
})();
