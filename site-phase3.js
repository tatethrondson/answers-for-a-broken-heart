(()=>{
  const CSS='/site-phase3.css?v=20260811-1';

  const path=()=>location.pathname.replace(/\.html$/,'');
  const isResources=()=>path()==='/free-guides';
  const isTwoAm=()=>path()==='/2am-guide';
  const isDepression=()=>path()==='/can-christians-be-depressed';
  const isHelp=()=>path()==='/help-someone';
  const isPhase3=()=>isResources()||isTwoAm()||isDepression()||isHelp();

  function ensureCss(){
    if(document.querySelector('link[data-ab-heart-phase3]')) return;
    const link=document.createElement('link');
    link.rel='stylesheet';
    link.href=CSS;
    link.setAttribute('data-ab-heart-phase3','1');
    document.head.appendChild(link);
  }

  function setClasses(){
    document.body.classList.toggle('phase3Resources',isResources());
    document.body.classList.toggle('phase3TwoAm',isTwoAm());
    document.body.classList.toggle('phase3Depression',isDepression());
    document.body.classList.toggle('phase3Help',isHelp());
    if(isPhase3()){
      const meta=document.querySelector('meta[name="theme-color"]');
      if(meta) meta.setAttribute('content','#f7f4ed');
    }
  }

  function enhanceScenicHero(){
    if(!(isResources()||isDepression()||isHelp())) return;
    const hero=document.querySelector('body>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase3Hero==='1') return;
    wrap.dataset.phase3Hero='1';
    const copy=document.createElement('div');
    copy.className='phase3HeroCopy';
    Array.from(wrap.children).forEach(node=>copy.appendChild(node));
    const image=document.createElement('div');
    image.className='phase3HeroImage';
    image.setAttribute('role','img');
    image.setAttribute('aria-label','A peaceful scene reflecting hope and care');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function fixHelpLibraryCta(){
    if(!isHelp()) return;
    document.querySelectorAll('.cta a').forEach(a=>{
      if((a.textContent||'').includes('Browse What Hurts Today')){
        a.setAttribute('href','/all-answers');
        a.textContent='Browse All 24 Answers';
      }
    });
  }

  function apply(){
    ensureCss();
    setClasses();
    enhanceScenicHero();
    fixHelpLibraryCta();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  new MutationObserver(apply).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
