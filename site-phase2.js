(()=>{
  const CSS='/site-phase2.css?v=20260811-1';

  function normalizedPath(){return location.pathname.replace(/\.html$/,'');}
  function isLibrary(){
    const p=normalizedPath();
    return p==='/all-answers' || p==='/what-hurts-today';
  }
  function isAnswer(){
    return /^\/answer-\d{2}$/.test(normalizedPath());
  }

  function ensureCss(){
    if(!document.querySelector('link[data-ab-heart-phase2]')){
      const link=document.createElement('link');
      link.rel='stylesheet';
      link.href=CSS;
      link.setAttribute('data-ab-heart-phase2','1');
      document.head.appendChild(link);
    }
    if(!document.querySelector('style[data-ab-heart-library-state]')){
      const style=document.createElement('style');
      style.setAttribute('data-ab-heart-library-state','1');
      style.textContent='body.phase2Library .card.hidden,body.phase2Library .group.hidden{display:none!important}';
      document.head.appendChild(style);
    }
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
    image.setAttribute('aria-label','A peaceful scene reflecting biblical hope');
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
    image.setAttribute('aria-label','A peaceful landscape reflecting hope and pastoral care');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function normalizeTaxonomy(){
    if(!isLibrary()) return;
    const replacements=[
      ['Why Did This Happen?','Suffering & Why'],
      ['People Who Hurt Me','Relational Hurt & Forgiveness'],
      ['Doubt & Faith','Doubt & Church Hurt']
    ];
    document.querySelectorAll('.filter,.groupHead h2,.num,.card small').forEach(el=>{
      let text=el.textContent;
      replacements.forEach(([from,to])=>{text=text.replace(from,to);});
      if(text!==el.textContent) el.textContent=text;
    });
  }

  function softenAnswer17(){
    if(normalizedPath()!=='/answer-17') return;
    document.title='Why Does Healing Feel Like It Is Going Backward? | Answers for a Broken Heart';
    const description=document.querySelector('meta[name="description"]');
    if(description) description.setAttribute('content','Healing after grief is not a straight line. Biblical and pastoral help for hard days, grief that comes in waves, and knowing when pain needs additional care.');
    const short=document.querySelector('.short');
    if(short){
      const h2=short.querySelector('h2');
      const p=short.querySelector('p:last-child');
      if(h2) h2.textContent='Healing is not a straight line.';
      if(p) p.textContent='A hard day does not automatically mean you are losing ground. Grief often moves in waves. The question is not whether you still hurt, but whether the hurt is slowly being brought into truth, grace, relationship, and wise care rather than hardening into isolation or bitterness.';
    }
  }

  function apply(){
    ensureCss();
    setClasses();
    enhanceLibraryHero();
    enhanceAnswerHero();
    normalizeTaxonomy();
    softenAnswer17();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  setTimeout(apply,120);
  setTimeout(apply,500);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
