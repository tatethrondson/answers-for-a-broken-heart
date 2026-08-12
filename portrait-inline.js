(()=>{
  const P='/tate-throndson-portrait-final.jpg?v=20260811-restore';
  const HOME_STYLE='/home-simple.css?v=20260811-1';

  function ensureHomeStyle(){
    if(!document.querySelector('link[data-ab-heart-home-simple]')){
      const link=document.createElement('link');
      link.rel='stylesheet';
      link.href=HOME_STYLE;
      link.setAttribute('data-ab-heart-home-simple','1');
      document.head.appendChild(link);
    }
  }

  function isHomepage(){
    const params=new URLSearchParams(location.search);
    return location.pathname==='/' && !params.has('view') && !params.has('answer');
  }

  function simplifyHomepage(){
    ensureHomeStyle();
    document.body.classList.toggle('homeSimple',isHomepage());
    if(!isHomepage()) return;

    const hero=document.querySelector('#app .hero');
    if(!hero || hero.dataset.simpleHome==='1') return;
    hero.dataset.simpleHome='1';

    const h1=hero.querySelector('h1');
    if(h1) h1.innerHTML='Hope and healing<br>for the brokenhearted.';

    const lead=hero.querySelector('.heroLead');
    if(lead) lead.textContent="Biblical encouragement and pastoral care for life’s deepest hurts.";

    const primary=hero.querySelector('.heroButtons .primary');
    if(primary){primary.textContent='Find Hope';primary.setAttribute('href','/start-here');}
    const secondary=hero.querySelector('.heroButtons .outline');
    if(secondary){secondary.textContent='Explore Resources';secondary.setAttribute('href','/free-guides');}

    const promise=hero.querySelector('.promise');
    if(promise) promise.innerHTML='<span>“The LORD is nigh unto them that are of a broken heart…” — Psalm 34:18</span>';

    const hurts=document.querySelector('#app .hurts');
    if(hurts){
      const intro=hurts.querySelector('.centerIntro');
      if(intro) intro.innerHTML='Start with what hurts most today. You do not need to have all the right words.';
      const items=hurts.querySelectorAll('.hurtItem');
      if(items.length>4) items[items.length-1].remove();
      const all=hurts.querySelector('.allTopics .btn');
      if(all){all.textContent='See All Topics';all.setAttribute('href','/what-hurts-today');}
    }

    const resources=document.querySelector('#app .freeGuidesHome');
    if(resources){
      const eyebrow=resources.querySelector('.freeGuidesHead .eyebrow');
      if(eyebrow) eyebrow.textContent='Featured Resources';
      const title=resources.querySelector('.freeGuidesHead h2');
      if(title) title.textContent='Resources for your journey';
      const intro=resources.querySelector('.guideIntro');
      if(intro) intro.textContent='Three simple ways to find biblical help without having to sort through everything at once.';
      const all=resources.querySelector('.freeGuidesAll');
      if(all){all.textContent='View all resources →';all.setAttribute('href','/free-guides');}
      const cards=resources.querySelector('.guideCards');
      if(cards && !cards.querySelector('[data-simple-resource="answers"]')){
        const card=document.createElement('a');
        card.className='guideCard';
        card.href='/all-answers';
        card.setAttribute('data-simple-resource','answers');
        card.innerHTML='<small>24 Biblical Answers</small><strong>Find the Question Beneath the Pain</strong><span>Browse the questions people ask in grief, suffering, doubt, betrayal, loneliness, and unanswered prayer.</span><b>Explore the answers →</b>';
        cards.appendChild(card);
      }
    }

    const author=document.querySelector('#app .authorSample .authorPane');
    if(author){
      const title=author.querySelector('.paneTitle');
      if(title) title.textContent='A word from Pastor Tate';
      const text=author.querySelector('.authorText');
      if(text) text.innerHTML='<p>If you came here because something hurts, you do not have to pretend you are doing better than you are. This site is here to help you bring the real questions into the light of Scripture and take the next faithful step.</p><p>Start wherever you are. There is hope, even here.</p><a class="textLink" href="/about">Meet Pastor Tate →</a>';
    }
  }

  function applyPortrait(){
    document.querySelectorAll('img').forEach(img=>{
      const alt=(img.alt||'').toLowerCase();
      const src=img.getAttribute('src')||'';
      const isTate=alt.includes('tate throndson') || src.includes('tate-throndson-portrait') || src.includes('author-tate') || src.includes('avatars.githubusercontent.com/u/314793130') || src.includes('/api/portrait-sharp');
      if(isTate && img.getAttribute('src')!==P){
        img.removeAttribute('srcset');
        img.removeAttribute('sizes');
        img.loading='eager';
        img.decoding='sync';
        img.src=P;
      }
    });
  }

  function applyAll(){
    simplifyHomepage();
    applyPortrait();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',applyAll);
  else applyAll();
  new MutationObserver(applyAll).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',applyAll);
})();
