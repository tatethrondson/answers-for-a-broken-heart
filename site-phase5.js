(()=>{
  const CSS='/site-phase5.css?v=20260811-1';
  const path=location.pathname;
  const params=new URLSearchParams(location.search);

  function isBook(){return path==='/book' || path==='/book.html' || (path==='/' && params.get('view')==='book');}
  function isChurch(){return path==='/church-resources' || path==='/church-resources.html';}
  function isGuideAccess(){return path==='/2am-guide-access' || path==='/2am-guide-access.html';}
  function isUnsafe(){return path==='/unsafe' || path==='/unsafe.html';}
  function isThanks(){return /(?:^|\/)\w[\w-]*thanks(?:\.html)?$/.test(path);}
  function isBookThanks(){return path==='/book-updates-thanks' || path==='/book-updates-thanks.html';}

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

  function ensureThanksNoindex(){
    if(!isThanks()) return;
    let meta=document.querySelector('meta[name="robots"]');
    if(!meta){meta=document.createElement('meta');meta.name='robots';document.head.appendChild(meta);}
    meta.setAttribute('content','noindex,follow');
  }

  function cleanBookConfirmation(){
    if(!isBookThanks()) return;
    const note=document.querySelector('.card .note');
    if(!note || note.dataset.phase5Clean==='1') return;
    note.dataset.phase5Clean='1';
    note.innerHTML='No daily emails. Just occasional updates as the book moves toward release.';
  }

  function enhanceBookHero(){
    if(!isBook()) return;
    const hero=document.querySelector('#app .subHero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase5Hero==='1') return;
    wrap.dataset.phase5Hero='1';
    const copy=document.createElement('div'); copy.className='phase5BookHeroCopy';
    Array.from(wrap.children).forEach(n=>copy.appendChild(n));
    const image=document.createElement('div'); image.className='phase5BookHeroImage'; image.setAttribute('role','img'); image.setAttribute('aria-label','A peaceful scene reflecting Scripture, hope, and healing');
    wrap.append(copy,image);
  }

  function improveBookPage(){
    if(!isBook()) return;
    const grid=document.querySelector('.salesGrid');
    const updates=document.querySelector('.bookUpdates');
    if(grid && updates && updates.nextElementSibling!==grid) grid.parentElement.insertBefore(updates,grid);
    const cards=grid?[...grid.querySelectorAll('.salesCard')]:[];
    const copy=[
      ['The 24 questions','Questions people actually ask','Grief, suffering, unanswered prayer, relational hurt, doubt, and the moments when faith stops feeling theoretical.'],
      ['Biblical without clichés','Scripture handled carefully','Each chapter makes room for the real hurt before moving toward biblical truth, Christ, and hope.'],
      ['Pastoral and practical','A next step you can carry','Not just ideas to understand, but prayers, perspective, and faithful next steps for the days when you need help living the answer.']
    ];
    cards.forEach((card,i)=>{
      if(!copy[i] || card.dataset.phase5BookClean==='1') return;
      card.dataset.phase5BookClean='1';
      card.innerHTML=`<p class="eyebrow">${copy[i][0]}</p><h3>${copy[i][1]}</h3><p>${copy[i][2]}</p>`;
    });
  }

  function enhanceChurchHero(){
    if(!isChurch()) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase5Hero==='1') return;
    wrap.dataset.phase5Hero='1';
    const copy=document.createElement('div'); copy.className='phase5ChurchHeroCopy';
    Array.from(wrap.children).forEach(n=>copy.appendChild(n));
    const image=document.createElement('div'); image.className='phase5ChurchHeroImage'; image.setAttribute('role','img'); image.setAttribute('aria-label','A peaceful scene reflecting pastoral care and ministry');
    wrap.append(copy,image);
  }

  function apply(){ensureCss();setClasses();ensureThanksNoindex();cleanBookConfirmation();enhanceBookHero();improveBookPage();enhanceChurchHero();}
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply); else apply();
  setTimeout(apply,120);
  setTimeout(apply,500);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
