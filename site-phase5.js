(()=>{
  const CSS='/site-phase5.css?v=20260811-1';
  const path=location.pathname;
  const params=new URLSearchParams(location.search);

  function isBook(){return path==='/' && params.get('view')==='book';}
  function isChurch(){return path==='/church-resources' || path==='/church-resources.html';}
  function isGuideAccess(){return path==='/2am-guide-access' || path==='/2am-guide-access.html';}
  function isUnsafe(){return path==='/unsafe' || path==='/unsafe.html';}
  function isThanks(){return /(?:^|\/)\w[\w-]*thanks(?:\.html)?$/.test(path);}

  function ensureCss(){
    if(document.querySelector('link[data-ab-heart-phase5]')) return;
    const link=document.createElement('link');
    link.rel='stylesheet'; link.href=CSS; link.setAttribute('data-ab-heart-phase5','1');
    document.head.appendChild(link);
  }

  function setClasses(){
    document.body.classList.toggle('phase5Book',isBook());
    document.body.classList.toggle('phase5Church',isChurch());
    document.body.classList.toggle('phase5GuideAccess',isGuideAccess());
    document.body.classList.toggle('phase5Unsafe',isUnsafe());
    document.body.classList.toggle('phase5Thanks',isThanks());
  }

  function enhanceBookHero(){
    if(!isBook()) return;
    const hero=document.querySelector('#app .subHero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase5Hero==='1') return;
    wrap.dataset.phase5Hero='1';
    const copy=document.createElement('div'); copy.className='phase5BookHeroCopy';
    Array.from(wrap.children).forEach(n=>copy.appendChild(n));
    const image=document.createElement('div'); image.className='phase5BookHeroImage'; image.setAttribute('role','img'); image.setAttribute('aria-label','An open Bible overlooking a peaceful mountain landscape');
    wrap.append(copy,image);
  }

  function enhanceChurchHero(){
    if(!isChurch()) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase5Hero==='1') return;
    wrap.dataset.phase5Hero='1';
    const copy=document.createElement('div'); copy.className='phase5ChurchHeroCopy';
    Array.from(wrap.children).forEach(n=>copy.appendChild(n));
    const image=document.createElement('div'); image.className='phase5ChurchHeroImage'; image.setAttribute('role','img'); image.setAttribute('aria-label','An open Bible overlooking a peaceful mountain landscape');
    wrap.append(copy,image);
  }

  function apply(){ensureCss();setClasses();enhanceBookHero();enhanceChurchHero();}
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply); else apply();
  new MutationObserver(apply).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
