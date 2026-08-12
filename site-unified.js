(()=>{
  const CSS='/site-unified.css?v=20260811-1';
  const topicMap={
    '/grief-and-loss':'topicGrief',
    '/why-god-allows-suffering':'topicSuffering',
    '/god-feels-far-away':'topicFar',
    '/anger-and-unanswered-prayer':'topicAnger',
    '/forgiveness-and-relational-hurt':'topicForgiveness',
    '/doubt-and-church-hurt':'topicDoubt'
  };

  function normalizedPath(){return location.pathname.replace(/\.html$/,'').replace(/\/$/,'')||'/';}
  function topicClass(){return topicMap[normalizedPath()]||'';}

  function ensureCss(){
    let link=document.querySelector('link[data-ab-heart-unified]');
    if(!link){
      link=document.createElement('link');
      link.rel='stylesheet';
      link.href=CSS;
      link.setAttribute('data-ab-heart-unified','1');
      document.head.appendChild(link);
    }
    if(!document.getElementById('topic-book-bridge-style')){
      const style=document.createElement('style');
      style.id='topic-book-bridge-style';
      style.textContent=`.topicBookBridge{margin:30px 0 8px;padding:27px 29px;background:#f6f1e8;border:1px solid #ded8cd;display:grid;grid-template-columns:1fr auto;gap:28px;align-items:center}.topicBookBridge small{display:block;text-transform:uppercase;letter-spacing:.14em;font-size:.62rem;font-weight:800;color:#8b6939;margin-bottom:6px}.topicBookBridge strong{display:block;font:1.55rem/1.14 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:6px}.topicBookBridge p{margin:0!important;font-size:.82rem!important;line-height:1.55;color:#626a64}.topicBookBridge a{display:inline-flex;text-decoration:none;background:#294533;color:#fff;padding:11px 15px;font-size:.69rem;font-weight:800;white-space:nowrap}@media(max-width:760px){.topicBookBridge{grid-template-columns:1fr}.topicBookBridge a{justify-self:start}}`;
      document.head.appendChild(style);
    }
  }

  function setTopicClasses(){
    const cls=topicClass();
    document.body.classList.toggle('siteUnifiedTopic',!!cls);
    Object.values(topicMap).forEach(c=>document.body.classList.toggle(c,c===cls));
  }

  function enhanceTopicHero(){
    if(!topicClass()) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero&&hero.querySelector(':scope>.wrap');
    if(!wrap||wrap.dataset.siteUnifiedHero==='1') return;
    wrap.dataset.siteUnifiedHero='1';
    const copy=document.createElement('div');
    copy.className='siteUnifiedTopicHeroCopy';
    Array.from(wrap.children).forEach(node=>copy.appendChild(node));
    const image=document.createElement('div');
    image.className='siteUnifiedTopicHeroImage';
    image.setAttribute('role','img');
    image.setAttribute('aria-label','A peaceful scene reflecting hope and pastoral care');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function addTopicBookBridge(){
    if(!topicClass()) return;
    const grid=document.querySelector('.answerGrid');
    if(!grid || document.querySelector('.topicBookBridge')) return;
    const bridge=document.createElement('div');
    bridge.className='topicBookBridge';
    bridge.innerHTML='<div><small>The deeper journey</small><strong>These questions are part of a larger pastoral journey.</strong><p><em>Answers for a Broken Heart</em> goes deeper into the Scripture, stories, and hope behind the questions you are reading here.</p></div><a href="/book">Explore the Book →</a>';
    grid.insertAdjacentElement('afterend',bridge);
  }

  function setAnswerVariant(){
    document.body.classList.remove('answerVisual1','answerVisual2','answerVisual3','answerVisual4');
    const m=normalizedPath().match(/^\/answer-(\d{2})$/);
    if(!m) return;
    const n=parseInt(m[1],10);
    document.body.classList.add(`answerVisual${((n-1)%4)+1}`);
  }

  function moveCssLast(){
    const link=document.querySelector('link[data-ab-heart-unified]');
    if(!link) return;
    const later=Array.from(document.head.querySelectorAll('link[rel="stylesheet"]')).some(el=>{
      if(el===link) return false;
      const pos=link.compareDocumentPosition(el);
      return !!(pos & Node.DOCUMENT_POSITION_FOLLOWING) && (el.dataset.abHeartPhase1!==undefined || el.dataset.abHeartPhase2!==undefined || el.dataset.abHeartPhase3!==undefined || el.dataset.abHeartPhase4!==undefined || el.dataset.abHeartPhase5!==undefined || el.dataset.abHeartHomeHero!==undefined);
    });
    if(later) document.head.appendChild(link);
  }

  function apply(){
    ensureCss();
    setTopicClasses();
    setAnswerVariant();
    enhanceTopicHero();
    addTopicBookBridge();
    moveCssLast();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  setTimeout(apply,100);
  setTimeout(apply,400);
  setTimeout(apply,800);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
