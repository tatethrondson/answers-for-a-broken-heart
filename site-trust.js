(()=>{
  function legacyRedirect(){
    const path=location.pathname;
    const params=new URLSearchParams(location.search);
    if(path!=='/') return false;
    const answer=params.get('answer');
    if(answer && /^\d{1,2}$/.test(answer)){
      const n=String(Math.min(24,Math.max(1,parseInt(answer,10)))).padStart(2,'0');
      location.replace(`/answer-${n}`);
      return true;
    }
    const view=params.get('view');
    const target=view==='book'?'/book':view==='about'?'/about':view==='hurts'?'/start-here':'';
    if(target){location.replace(target);return true;}
    return false;
  }

  function normalizeLinks(){
    document.querySelectorAll('a[href]').forEach(a=>{
      const href=a.getAttribute('href')||'';
      if(href==='/?view=book' || href==='?view=book') a.setAttribute('href','/book');
      if(href==='/?view=about' || href==='?view=about') a.setAttribute('href','/about');
      if(href==='/?view=hurts' || href==='?view=hurts' || href==='/what-hurts-today') a.setAttribute('href','/start-here');
    });
  }

  function replaceUnverifiedTestimonial(){
    if(!document.body.classList.contains('homeOriginal')) return;
    const quote=document.querySelector('.homeQuote blockquote');
    const cite=document.querySelector('.homeQuote cite');
    if(!quote || !cite || quote.dataset.trustClean==='1') return;
    quote.dataset.trustClean='1';
    quote.textContent='Come unto me, all ye that labour and are heavy laden, and I will give you rest.';
    cite.textContent='— Matthew 11:28';
  }

  function clarifyTwoAmSignup(){
    if(!/^\/2am-guide(?:\.html)?$/.test(location.pathname)) return;
    const p=document.querySelector('.hero .card > p:not(.eyebrow)');
    if(!p || p.dataset.trustClean==='1') return;
    p.dataset.trustClean='1';
    p.innerHTML='Enter your email and you’ll go straight to the guide. I’ll also send occasional pastoral encouragement and let you know when the <em>Answers for a Broken Heart</em> book is ready.';
  }

  function cleanBookConfirmation(){
    if(!/^\/book-updates-thanks(?:\.html)?$/.test(location.pathname)) return;
    const note=document.querySelector('.card .note');
    if(note && note.dataset.trustClean!=='1'){
      note.dataset.trustClean='1';
      note.innerHTML='No daily emails. Just occasional updates as the book moves toward release.';
    }
  }

  function trackBookClicks(){
    if(document.documentElement.dataset.bookTracking==='1') return;
    document.documentElement.dataset.bookTracking='1';
    document.addEventListener('click',e=>{
      const a=e.target.closest('a[href]');
      if(!a || a.getAttribute('href')!=='/book') return;
      try{
        if(typeof window.va==='function'){
          window.va('event',{name:'Book Interest Click',data:{page:location.pathname||'/',label:(a.textContent||'').trim().replace(/\s+/g,' ').slice(0,80)}});
        }
      }catch(err){}
    });
  }

  function apply(){
    if(legacyRedirect()) return;
    normalizeLinks();
    replaceUnverifiedTestimonial();
    clarifyTwoAmSignup();
    cleanBookConfirmation();
    trackBookClicks();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  setTimeout(apply,120);
  setTimeout(apply,500);
  setTimeout(apply,1000);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
