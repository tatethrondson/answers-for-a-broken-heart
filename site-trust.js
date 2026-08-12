(()=>{
  const TOPIC_PATHS=new Set([
    '/god-feels-far-away','/why-god-allows-suffering','/grief-and-loss',
    '/anger-and-unanswered-prayer','/forgiveness-and-relational-hurt','/doubt-and-church-hurt'
  ]);

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

  function ensureFlowStyles(){
    if(document.getElementById('visitor-flow-styles')) return;
    const style=document.createElement('style');
    style.id='visitor-flow-styles';
    style.textContent=`
      .visitorSecondary{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0 0}
      .visitorSecondary .choice{background:#f7f3eb}
      .homeBookBandWrap{padding:0 0 38px;background:#fbfaf7}
      .homeBookBand{display:grid;grid-template-columns:1.25fr .75fr;gap:42px;align-items:center;background:#f3eee4;border:1px solid #ddd5c8;border-radius:18px;padding:34px 42px}
      .homeBookBand h2{font:400 2rem/1.08 Georgia,"Times New Roman",serif;margin:0 0 10px;color:#4b4e45}
      .homeBookBand p{font-size:.76rem;line-height:1.6;color:#686961;max-width:620px;margin:0 0 18px}
      .homeBookActions{display:flex;gap:10px;flex-wrap:wrap}
      .homeBookAction{display:inline-flex;padding:10px 14px;border-radius:9px;font-size:.69rem;font-weight:800;text-decoration:none}
      .homeBookAction.primary{background:#777d55;color:#fff}.homeBookAction.secondary{border:1px solid #c8c2b4;color:#62645a;background:#faf8f3}
      .homeMiniBook{justify-self:center;width:150px;min-height:205px;background:#fbf9f3;border:1px solid #d7d0c3;box-shadow:10px 14px 24px rgba(35,43,35,.15);padding:28px 18px;text-align:center;color:#58644a}
      .homeMiniBook strong{display:block;font:1.65rem/.92 Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.045em}.homeMiniBook span{display:block;margin:14px 0 10px;font:2.7rem/.9 Georgia,serif;color:#a87335}.homeMiniBook small{font:.58rem/1.35 Arial,sans-serif;text-transform:uppercase;letter-spacing:.08em}
      .homePromiseLabel{display:block;margin:0 0 9px;font-size:.58rem;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:#a27335}
      .topicBookBridge{margin:30px 0 8px;padding:27px 29px;background:#f6f1e8;border:1px solid #ded8cd;display:grid;grid-template-columns:1fr auto;gap:28px;align-items:center}
      .topicBookBridge small{display:block;text-transform:uppercase;letter-spacing:.14em;font-size:.62rem;font-weight:800;color:#8b6939;margin-bottom:6px}.topicBookBridge strong{display:block;font:1.55rem/1.14 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:6px}.topicBookBridge p{margin:0!important;font-size:.82rem!important;line-height:1.55;color:#626a64}.topicBookBridge a{display:inline-flex;text-decoration:none;background:#294533;color:#fff;padding:11px 15px;font-size:.69rem;font-weight:800;white-space:nowrap}
      @media(max-width:760px){.visitorSecondary,.homeBookBand,.topicBookBridge{grid-template-columns:1fr}.homeMiniBook{justify-self:start}.homeBookBand{padding:28px 24px}.topicBookBridge a{justify-self:start}}
    `;
    document.head.appendChild(style);
  }

  function normalizeLinks(){
    document.querySelectorAll('a[href]').forEach(a=>{
      const href=a.getAttribute('href')||'';
      if(href==='/?view=book' || href==='?view=book') a.setAttribute('href','/book');
      if(href==='/?view=about' || href==='?view=about') a.setAttribute('href','/about');
      if(href==='/?view=hurts' || href==='?view=hurts' || href==='/what-hurts-today') a.setAttribute('href','/start-here');
      const label=(a.textContent||'').trim().replace(/\s+/g,' ').toLowerCase();
      if(label.includes('browse all 24 answers') || label.includes('see all 24 questions')) a.setAttribute('href','/all-answers');
    });
  }

  function literalNavigation(){
    document.querySelectorAll('.siteShellHeader .siteShellLinks,.siteShellHeader .siteShellMobileMenu').forEach(nav=>{
      const anchors=[...nav.querySelectorAll('a[href]')];
      anchors.forEach(a=>{
        const href=a.getAttribute('href')||'';
        const label=(a.textContent||'').trim();
        if(href==='/all-answers' && !a.classList.contains('homeSearch') && !a.classList.contains('phase1Search')) a.textContent='24 Answers';
        if(href==='/start-here' && label!=='Find Hope' && !a.classList.contains('homeFindHope') && !a.classList.contains('phase1FindHope')) a.textContent='Start Here';
        if(href==='/free-guides') a.textContent='Free Guides';
        if(href==='/about') a.textContent='About';
        if(href==='/contact') a.textContent='Contact';
      });
      if(!nav.querySelector('a[href="/book"]')){
        const about=nav.querySelector('a[href="/about"]');
        const book=document.createElement('a');
        book.href='/book';book.textContent='The Book';
        if(about) nav.insertBefore(book,about); else nav.appendChild(book);
      }
    });
  }

  function simplifyStartHere(){
    if(!/^\/start-here(?:\.html)?$/.test(location.pathname) && location.pathname!=='/begin-here.html') return;
    const grid=document.querySelector('.choiceGrid');
    if(grid && !document.querySelector('.visitorSecondary')){
      const choices=[...grid.querySelectorAll(':scope > .choice')];
      if(choices.length>6){
        const secondary=document.createElement('div');
        secondary.className='visitorSecondary';
        choices.slice(6).forEach(choice=>secondary.appendChild(choice));
        grid.insertAdjacentElement('afterend',secondary);
      }
    }
    document.querySelectorAll('.bottom a').forEach(a=>{
      const text=(a.textContent||'').toLowerCase();
      if(text.includes('tell me where it hurts') || a.getAttribute('href')==='/what-hurts-today' || (a.getAttribute('href')==='/start-here' && text.includes('where it hurts'))) a.remove();
    });
  }

  function exactHomepageTopics(){
    if(!document.body.classList.contains('homeOriginal')) return;
    const pills=document.querySelector('.homeHurtsPills');
    if(!pills || pills.dataset.flowClean==='1') return;
    pills.dataset.flowClean='1';
    pills.innerHTML=`
      <a class="homeHurtPill" href="/grief-and-loss"><span>♧</span> Grief &amp; Loss</a>
      <a class="homeHurtPill" href="/why-god-allows-suffering"><span>?</span> Suffering &amp; Why</a>
      <a class="homeHurtPill" href="/god-feels-far-away"><span>♙</span> God Feels Far Away</a>
      <a class="homeHurtPill" href="/anger-and-unanswered-prayer"><span>◌</span> Unanswered Prayer</a>
      <a class="homeHurtPill" href="/forgiveness-and-relational-hurt"><span>♡</span> Relational Hurt</a>
      <a class="homeHurtPill" href="/doubt-and-church-hurt"><span>✦</span> Doubt &amp; Church Hurt</a>
      <div class="homeHurtsNote">Choose the closest one. You can always come back and choose another.</div>`;
  }

  function addHomepageBookBand(){
    if(!document.body.classList.contains('homeOriginal')) return;
    if(document.querySelector('.homeBookBandWrap')) return;
    const hurts=document.querySelector('.homeHurtsWrap');
    if(!hurts) return;
    const section=document.createElement('section');
    section.className='homeBookBandWrap';
    section.innerHTML=`<div class="homeOriginalWrap"><div class="homeBookBand"><div><div class="homeEyebrow">The deeper journey</div><h2>Twenty-four questions. One deeper journey.</h2><p><em>Answers for a Broken Heart</em> takes the questions on this site further with Scripture, pastoral stories, and a path toward hope that does not rush past the hurt.</p><div class="homeBookActions"><a class="homeBookAction primary" href="/book">Explore the Book</a><a class="homeBookAction secondary" href="/book#book-updates">Get Release Updates</a></div></div><div class="homeMiniBook" aria-label="Answers for a Broken Heart book"><strong>Answers<br>for a<br>Broken<br>Heart</strong><span>♡</span><small>24 Biblical Answers for Life’s Deepest Hurts</small></div></div></div>`;
    hurts.insertAdjacentElement('afterend',section);
  }

  function replaceUnverifiedTestimonial(){
    if(!document.body.classList.contains('homeOriginal')) return;
    const quote=document.querySelector('.homeQuote blockquote');
    const cite=document.querySelector('.homeQuote cite');
    if(!quote || !cite) return;
    quote.textContent='Come unto me, all ye that labour and are heavy laden, and I will give you rest.';
    cite.textContent='— Matthew 11:28';
    const box=document.querySelector('.homeQuote');
    if(box && !box.querySelector('.homePromiseLabel')){
      const label=document.createElement('span');label.className='homePromiseLabel';label.textContent='A promise for the weary';
      box.insertBefore(label,quote);
    }
  }

  function improveBookPage(){
    if(!/^\/book(?:\.html)?$/.test(location.pathname)) return;
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
      if(!copy[i] || card.dataset.flowClean==='1') return;
      card.dataset.flowClean='1';
      card.innerHTML=`<p class="eyebrow">${copy[i][0]}</p><h3>${copy[i][1]}</h3><p>${copy[i][2]}</p>`;
    });
  }

  function addTopicBookBridge(){
    if(!TOPIC_PATHS.has(location.pathname)) return;
    const grid=document.querySelector('.answerGrid');
    if(!grid || document.querySelector('.topicBookBridge')) return;
    const bridge=document.createElement('div');
    bridge.className='topicBookBridge';
    bridge.innerHTML='<div><small>The deeper journey</small><strong>These questions are part of a larger pastoral journey.</strong><p><em>Answers for a Broken Heart</em> goes deeper into the Scripture, stories, and hope behind the questions you are reading here.</p></div><a href="/book">Explore the Book →</a>';
    grid.insertAdjacentElement('afterend',bridge);
  }

  function simplifyAnswerJourney(){
    if(!/^\/answer-\d{2}(?:\.html)?$/.test(location.pathname)) return;
    const journey=document.querySelector('.answerJourney .journeyGrid');
    if(!journey) return;
    const cards=[...journey.querySelectorAll('.journeyCard')];
    if(cards.length<3) return;
    const related=document.querySelector('.relatedAnswers .relatedCard');
    if(related){
      const relatedTitle=related.querySelector('strong');
      cards[1].href=related.getAttribute('href')||'/all-answers';
      const small=cards[1].querySelector('small'),strong=cards[1].querySelector('strong'),span=cards[1].querySelector('span');
      if(small) small.textContent='Read another answer';
      if(strong && relatedTitle) strong.textContent=relatedTitle.textContent;
      if(span) span.textContent='Continue with this question →';
    }
    cards[2].href='/book';
    const small=cards[2].querySelector('small'),strong=cards[2].querySelector('strong'),span=cards[2].querySelector('span');
    if(small) small.textContent='Go deeper';
    if(strong) strong.textContent='Answers for a Broken Heart';
    if(span) span.textContent='Explore the book →';
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
    ensureFlowStyles();
    normalizeLinks();
    literalNavigation();
    simplifyStartHere();
    exactHomepageTopics();
    addHomepageBookBand();
    replaceUnverifiedTestimonial();
    improveBookPage();
    addTopicBookBridge();
    simplifyAnswerJourney();
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
