(()=>{
  const CSS='/site-phase2.css?v=20260811-1';

  function isLibrary(){
    return location.pathname==='/all-answers' || location.pathname==='/what-hurts-today.html';
  }

  function isAnswer(){
    return /^\/answer-\d{2}(?:\.html)?$/.test(location.pathname);
  }

  function ensureCss(){
    if(document.querySelector('link[data-ab-heart-phase2]')) return;
    const link=document.createElement('link');
    link.rel='stylesheet';
    link.href=CSS;
    link.setAttribute('data-ab-heart-phase2','1');
    document.head.appendChild(link);
  }

  function setClasses(){
    document.body.classList.toggle('phase2Library',isLibrary());
    document.body.classList.toggle('phase2Answer',isAnswer());
  }

  function enhanceLibraryHero(){
    if(!isLibrary()) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase2Hero==='1') return;
    wrap.dataset.phase2Hero='1';
    const copy=document.createElement('div');
    copy.className='phase2LibraryHeroCopy';
    Array.from(wrap.children).forEach(node=>copy.appendChild(node));
    const image=document.createElement('div');
    image.className='phase2LibraryHeroImage';
    image.setAttribute('role','img');
    image.setAttribute('aria-label','An open Bible overlooking a peaceful mountain landscape');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function enhanceAnswerHero(){
    if(!isAnswer()) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase2Hero==='1') return;
    wrap.dataset.phase2Hero='1';
    const copy=document.createElement('div');
    copy.className='phase2AnswerHeroCopy';
    Array.from(wrap.children).forEach(node=>copy.appendChild(node));
    const image=document.createElement('div');
    image.className='phase2AnswerHeroImage';
    image.setAttribute('role','img');
    image.setAttribute('aria-label','A peaceful mountain landscape with an open Bible');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function apply(){
    ensureCss();
    setClasses();
    enhanceLibraryHero();
    enhanceAnswerHero();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  new MutationObserver(apply).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
