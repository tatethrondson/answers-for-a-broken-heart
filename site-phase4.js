(()=>{
  const CSS='/site-phase4.css?v=20260811-1';

  function isAbout(){ return location.pathname==='/about' || location.pathname==='/about.html'; }
  function isContact(){ return location.pathname==='/contact' || location.pathname==='/contact.html'; }

  function ensureCss(){
    if(document.querySelector('link[data-ab-heart-phase4]')) return;
    const link=document.createElement('link');
    link.rel='stylesheet';
    link.href=CSS;
    link.setAttribute('data-ab-heart-phase4','1');
    document.head.appendChild(link);
  }

  function setClasses(){
    document.body.classList.toggle('phase4About',isAbout());
    document.body.classList.toggle('phase4Contact',isContact());
  }

  function enhanceContactHero(){
    if(!isContact()) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase4Hero==='1') return;
    wrap.dataset.phase4Hero='1';
    const copy=document.createElement('div');
    copy.className='phase4ContactHeroCopy';
    Array.from(wrap.children).forEach(node=>copy.appendChild(node));
    const image=document.createElement('div');
    image.className='phase4ContactHeroImage';
    image.setAttribute('role','img');
    image.setAttribute('aria-label','An open Bible overlooking a peaceful mountain landscape');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function apply(){
    ensureCss();
    setClasses();
    enhanceContactHero();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  new MutationObserver(apply).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
