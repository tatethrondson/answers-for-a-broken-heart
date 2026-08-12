(()=>{
  const P='/tate-throndson-portrait-final.jpg?v=20260811-restore';
  const HOME_STYLE='/homepage-original.css?v=20260811-1';
  const PHASE1_STYLE='/site-phase1.css?v=20260811-1';
  const PODCAST_URL='https://youtu.be/cCnEWfS5M0o?si=oge2LySLWOMjpva8';
  const PODCAST_THUMB='https://img.youtube.com/vi/cCnEWfS5M0o/hqdefault.jpg';
  let originalHeaderHTML='';

  function isHomepage(){
    const params=new URLSearchParams(location.search);
    return location.pathname==='/' && !params.has('view') && !params.has('answer');
  }

  function isStartHere(){
    return location.pathname==='/start-here' || location.pathname==='/begin-here.html';
  }

  function isWhatHurts(){
    return location.pathname==='/what-hurts-today' || location.pathname==='/start-here.html';
  }

  function captureHeader(){
    const header=document.querySelector('.siteShellHeader');
    if(header && !originalHeaderHTML) originalHeaderHTML=header.innerHTML;
  }

  function ensureStyles(){
    if(!document.querySelector('link[data-ab-heart-phase1]')){
      const link=document.createElement('link');
      link.rel='stylesheet';
      link.href=PHASE1_STYLE;
      link.setAttribute('data-ab-heart-phase1','1');
      document.head.appendChild(link);
    }
    if(!document.getElementById('phase1-visitor-extras')){
      const style=document.createElement('style');
      style.id='phase1-visitor-extras';
      style.textContent=`
        .visitorSecondary{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0 0}.visitorSecondary .choice{background:#f7f3eb!important}
        .homePodcastStripWrap{padding:0 0 30px;background:#fbfaf7}.homePodcastStrip{display:grid;grid-template-columns:180px 1fr auto;gap:24px;align-items:center;border:1px solid #d9ddd8;background:#eef2ed;border-radius:14px;padding:20px 24px}.homePodcastStrip small,.startPodcast small{display:block;text-transform:uppercase;letter-spacing:.14em;font-size:.61rem;font-weight:800;color:#88683b;margin-bottom:5px}.homePodcastStrip strong,.startPodcast strong{display:block;font:400 1.35rem/1.17 Georgia,"Times New Roman",serif;color:#20372a}.homePodcastStrip p,.startPodcast p{margin:5px 0 0;font-size:.76rem;line-height:1.5;color:#626a64}
        .phase1PodcastThumb{display:block!important;background:transparent!important;padding:0!important;border-radius:10px!important;overflow:hidden!important;line-height:0!important;text-decoration:none!important}.phase1PodcastThumb img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}.phase1PodcastAction{display:inline-flex!important;text-decoration:none!important;background:#294533!important;color:#fff!important;padding:10px 14px!important;font-size:.69rem!important;font-weight:800!important;white-space:nowrap!important}
        .startPodcast{margin:20px 0 0;padding:20px 22px;background:#eef2ed;border:1px solid #d9e0d8;display:grid;grid-template-columns:180px 1fr auto;gap:22px;align-items:center}
        @media(max-width:760px){.visitorSecondary,.homePodcastStrip,.startPodcast{grid-template-columns:1fr}.phase1PodcastAction{justify-self:start}.phase1PodcastThumb{max-width:420px}}
      `;
      document.head.appendChild(style);
    }
  }

  function ensureHomeStyle(){
    if(!document.querySelector('link[data-ab-heart-home-original]')){
      const link=document.createElement('link');
      link.rel='stylesheet';
      link.href=HOME_STYLE;
      link.setAttribute('data-ab-heart-home-original','1');
      document.head.appendChild(link);
    }
    document.querySelectorAll('link[data-ab-heart-theme],link[data-ab-heart-home-simple]').forEach(x=>x.remove());
  }

  function navMarkup(findHopeClass,searchClass){
    return `<div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/"><span class="siteShellBrandWords">answers<small>for a broken heart</small></span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a><a class="${findHopeClass}" href="/start-here">Find Hope</a><a class="${searchClass}" href="/all-answers" aria-label="Search the 24 Answers">⌕</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a><a href="/start-here">Find Hope</a></nav></details></div>`;
  }

  function homeHeader(){
    const header=document.querySelector('.siteShellHeader');
    if(!header) return;
    captureHeader();
    header.classList.remove('phase1GlobalHeader');
    if(header.dataset.homeOriginal==='1') return;
    header.dataset.homeOriginal='1';
    header.innerHTML=navMarkup('homeFindHope','homeSearch');
  }

  function restoreHeader(){
    const header=document.querySelector('.siteShellHeader');
    if(header && header.dataset.homeOriginal==='1' && originalHeaderHTML){
      header.innerHTML=originalHeaderHTML;
      delete header.dataset.homeOriginal;
    }
  }

  function globalHeader(){
    if(isHomepage()) return;
    const header=document.querySelector('.siteShellHeader');
    if(!header) return;
    captureHeader();
    if(header.dataset.phase1Shell==='1') return;
    delete header.dataset.homeOriginal;
    header.dataset.phase1Shell='1';
    header.classList.add('phase1GlobalHeader');
    header.innerHTML=navMarkup('phase1FindHope','phase1Search');
  }

  function globalFooter(){
    if(isHomepage()) return;
    const footer=document.querySelector('.siteShellFooter');
    if(!footer || footer.dataset.phase1Shell==='1') return;
    footer.dataset.phase1Shell='1';
    footer.classList.add('phase1GlobalFooter');
    footer.innerHTML=`<div class="phase1FooterMain"><div><div class="phase1FooterBrand">answers<small>for a broken heart</small></div><div class="phase1FooterTag">Biblical encouragement and pastoral care for life’s deepest hurts.</div></div><div class="phase1FooterCol"><strong>Encouragement</strong><a href="/all-answers">24 Biblical Answers</a><a href="/2am-guide">2:00 A.M. Guide</a><a href="/can-christians-be-depressed">Depression &amp; Faith</a><a href="/free-guides">Free Guides</a></div><div class="phase1FooterCol"><strong>Pastoral Care</strong><a href="/start-here">Start Here</a><a href="/help-someone">Help Someone</a><a href="/unsafe">Immediate Safety Help</a><a href="/contact">Contact Pastor Tate</a></div><div class="phase1FooterCol"><strong>Resources</strong><a href="/book">The Book</a><a href="/church-resources">For Churches</a><a href="/about">About Tate</a><p style="margin-top:14px">Stay encouraged with occasional hope and pastoral care.</p><form class="phase1FooterForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Email address" aria-label="Email address" required><input type="hidden" name="_subject" value="Answers for a Broken Heart encouragement signup"><input type="hidden" name="_captcha" value="false"><button type="submit">Subscribe</button></form></div></div><div class="phase1FooterBottom"><div class="phase1FooterBottomInner"><span>© 2026 Answers for a Broken Heart</span><span><a href="/about">About</a><a href="/contact">Contact</a></span></div></div>`;
  }

  function homepageMarkup(){
    return `<div class="homeOriginalRoot" data-home-original="1">
      <section class="homeHero"><div class="homeOriginalWrap homeHeroGrid">
        <div class="homeHeroCopy"><div class="homeEyebrow">You are not alone</div><h1>Hope and healing<br>for the brokenhearted.</h1><p class="homeHeroLead">Biblical encouragement and pastoral care for life’s deepest hurts.</p><div class="homeHeroRule"></div><p class="homeHeroVerse">“The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.”<small>— Psalm 34:18</small></p><div class="homeHeroActions"><a class="homeHeroBtn primary" href="/start-here">Find Encouragement</a><a class="homeHeroBtn secondary" href="/free-guides">Explore Resources</a></div></div>
        <div class="homeHeroImage" role="img" aria-label="An open Bible overlooking a peaceful mountain landscape"></div>
      </div></section>

      <section class="homeResources"><div class="homeOriginalWrap"><div class="homeSectionTop"><div><div class="homeEyebrow">Featured resources</div><h2>Resources for your journey</h2></div><a class="homeViewAll" href="/free-guides">View all resources →</a></div><div class="homeResourceGrid">
        <a class="homeResourceCard" href="/all-answers"><div class="homeResourcePhoto one"><div class="homeResourceIcon">▣</div></div><div class="homeResourceBody"><h3>Encouraging Articles</h3><p>Truth and hope for the hard places.</p></div></a>
        <a class="homeResourceCard" href="/2am-guide"><div class="homeResourcePhoto two"><div class="homeResourceIcon">♧</div></div><div class="homeResourceBody"><h3>2:00 A.M. Guide</h3><p>Seven Scriptures for the hardest hour of the night.</p></div></a>
        <a class="homeResourceCard" href="/start-here"><div class="homeResourcePhoto three"><div class="homeResourceIcon">♡</div></div><div class="homeResourceBody"><h3>Pastoral Care</h3><p>Compassionate support when you need a place to begin.</p></div></a>
        <a class="homeResourceCard" href="/help-someone"><div class="homeResourcePhoto four"><div class="homeResourceIcon">♧</div></div><div class="homeResourceBody"><h3>Help Someone</h3><p>Practical guidance for walking with someone who is hurting.</p></div></a>
        <a class="homeResourceCard" href="/free-guides"><div class="homeResourcePhoto five"><div class="homeResourceIcon">↓</div></div><div class="homeResourceBody"><h3>Free Resources</h3><p>Guides and tools to encourage your soul.</p></div></a>
      </div></div></section>

      <section class="homePodcastStripWrap"><div class="homeOriginalWrap"><div class="homePodcastStrip"><a class="phase1PodcastThumb" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer" aria-label="Watch the depression and faith podcast episode on YouTube"><img src="${PODCAST_THUMB}" alt="Depression and faith podcast episode thumbnail" loading="lazy"></a><div><small>New podcast episode</small><strong>A pastoral conversation about depression and faith.</strong><p>For the Christian who feels low, exhausted, or guilty for struggling emotionally.</p></div><a class="phase1PodcastAction" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer">Listen on YouTube →</a></div></div></section>

      <section class="homeHurtsWrap"><div class="homeOriginalWrap"><div class="homeHurts"><div><h2>What hurts today?</h2><p>Take a moment to reflect and let us help you find encouragement that meets you where you are.</p><a class="homeHurtsBtn" href="/start-here">Begin Guided Entry</a></div><div class="homeHurtsPills">
        <a class="homeHurtPill" href="/grief-and-loss"><span>♧</span> Grief &amp; Loss</a>
        <a class="homeHurtPill" href="/why-god-allows-suffering"><span>?</span> Suffering &amp; Why</a>
        <a class="homeHurtPill" href="/god-feels-far-away"><span>♙</span> God Feels Far Away</a>
        <a class="homeHurtPill" href="/anger-and-unanswered-prayer"><span>◌</span> Unanswered Prayer</a>
        <a class="homeHurtPill" href="/forgiveness-and-relational-hurt"><span>♡</span> Relational Hurt</a>
        <a class="homeHurtPill" href="/doubt-and-church-hurt"><span>✦</span> Doubt &amp; Church Hurt</a>
        <div class="homeHurtsNote">Choose the closest one. You can always come back and choose another.</div>
      </div></div></div></section>

      <section class="homeBookBandWrap"><div class="homeOriginalWrap"><div class="homeBookBand"><div><div class="homeEyebrow">The deeper journey</div><h2>Twenty-four questions. One deeper journey.</h2><p><em>Answers for a Broken Heart</em> takes the questions on this site further with Scripture, pastoral stories, and a path toward hope that does not rush past the hurt.</p><div class="homeBookActions"><a class="homeBookAction primary" href="/book">Explore the Book</a><a class="homeBookAction secondary" href="/book#book-updates">Get Release Updates</a></div></div><div class="homeMiniBook" aria-label="Answers for a Broken Heart book"><strong>Answers<br>for a<br>Broken<br>Heart</strong><span>♡</span><small>24 Biblical Answers for Life’s Deepest Hurts</small></div></div></div></section>

      <section class="homeTestimonial"><div class="homeOriginalWrap"><div class="homeTestimonialInner"><div class="homeTestimonialPhoto"></div><div class="homeQuote"><span class="homePromiseLabel">A promise for the weary</span><blockquote>Come unto me, all ye that labour and are heavy laden, and I will give you rest.</blockquote><cite>— Matthew 11:28</cite></div></div></div></section>

      <footer class="homeFooter"><div class="homeOriginalWrap homeFooterMain"><div><div class="homeFooterBrand">answers<small>for a broken heart</small></div><div class="homeFooterTag">Biblical encouragement and pastoral care for life’s deepest hurts.</div></div><div class="homeFooterCol"><strong>Encouragement</strong><a href="/all-answers">24 Biblical Answers</a><a href="/2am-guide">2:00 A.M. Guide</a><a href="/can-christians-be-depressed">Depression &amp; Faith</a><a href="/free-guides">Free Guides</a></div><div class="homeFooterCol"><strong>Pastoral Care</strong><a href="/start-here">Start Here</a><a href="/help-someone">Help Someone</a><a href="/unsafe">Immediate Safety Help</a><a href="/contact">Contact Pastor Tate</a></div><div class="homeFooterCol"><strong>Resources</strong><a href="/book">The Book</a><a href="/church-resources">For Churches</a><a href="/about">About Tate</a><p style="margin-top:14px">Stay encouraged with occasional hope and pastoral care.</p><form class="homeFooterForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Email address" required><input type="hidden" name="_subject" value="Answers for a Broken Heart encouragement signup"><input type="hidden" name="_captcha" value="false"><button type="submit">Subscribe</button></form></div></div><div class="homeFooterBottom"><div class="homeOriginalWrap"><span>© 2026 Answers for a Broken Heart</span><span><a href="/about">About</a><a href="/contact">Contact</a></span></div></div></footer>
    </div>`;
  }

  function restoreApprovedHomepage(){
    captureHeader();
    const home=isHomepage();
    document.body.classList.toggle('homeOriginal',home);
    document.body.classList.remove('homeSimple');
    if(!home){restoreHeader();return;}
    ensureHomeStyle();
    homeHeader();
    const meta=document.querySelector('meta[name="theme-color"]');
    if(meta) meta.setAttribute('content','#f7f4ed');
    const app=document.getElementById('app');
    if(app && !app.querySelector('[data-home-original="1"]')) app.innerHTML=homepageMarkup();
  }

  function pageClasses(){
    const start=isStartHere();
    const hurts=isWhatHurts();
    document.body.classList.toggle('phase1Start',start);
    document.body.classList.toggle('phase1Hurts',hurts);
    if(!isHomepage()){
      const meta=document.querySelector('meta[name="theme-color"]');
      if(meta) meta.setAttribute('content','#f7f4ed');
    }
  }

  function enhanceEntryHero(){
    if(!(isStartHere() || isWhatHurts())) return;
    const hero=document.querySelector('main>.hero');
    const wrap=hero && hero.querySelector(':scope>.wrap');
    if(!wrap || wrap.dataset.phase1Hero==='1') return;
    wrap.dataset.phase1Hero='1';
    const copy=document.createElement('div');
    copy.className='phase1HeroCopy';
    Array.from(wrap.children).forEach(node=>copy.appendChild(node));
    const image=document.createElement('div');
    image.className='phase1HeroImage';
    image.setAttribute('role','img');
    image.setAttribute('aria-label','A peaceful landscape reflecting hope and pastoral care');
    wrap.appendChild(copy);
    wrap.appendChild(image);
  }

  function simplifyStartHere(){
    if(!isStartHere()) return;
    const grid=document.querySelector('.choiceGrid');
    let secondary=document.querySelector('.visitorSecondary');
    if(grid && !secondary){
      const choices=[...grid.querySelectorAll(':scope > .choice')];
      if(choices.length>6){
        secondary=document.createElement('div');
        secondary.className='visitorSecondary';
        choices.slice(6).forEach(choice=>secondary.appendChild(choice));
        grid.insertAdjacentElement('afterend',secondary);
      }
    }
    document.querySelectorAll('.bottom a').forEach(a=>{
      const text=(a.textContent||'').toLowerCase();
      if(text.includes('tell me where it hurts') || a.getAttribute('href')==='/what-hurts-today') a.remove();
    });
    if(!document.querySelector('.startPodcast')){
      const anchor=secondary||grid;
      if(anchor){
        const box=document.createElement('div');
        box.className='startPodcast';
        box.innerHTML=`<a class="phase1PodcastThumb" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer" aria-label="Watch the depression and faith podcast episode on YouTube"><img src="${PODCAST_THUMB}" alt="Depression and faith podcast episode thumbnail" loading="lazy"></a><div><small>Prefer to listen?</small><strong>Hear a pastoral conversation about depression and faith.</strong><p>If emotional heaviness is part of what brought you here, you can listen instead of reading right now.</p></div><a class="phase1PodcastAction" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer">Listen →</a>`;
        anchor.insertAdjacentElement('afterend',box);
      }
    }
  }

  function normalizeLinks(){
    document.querySelectorAll('a[href]').forEach(a=>{
      const href=a.getAttribute('href')||'';
      if(href==='/?view=book' || href==='?view=book') a.setAttribute('href','/book');
      if(href==='/?view=about' || href==='?view=about') a.setAttribute('href','/about');
      if(href==='/?view=hurts' || href==='?view=hurts' || href==='/what-hurts-today') a.setAttribute('href','/start-here');
    });
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
    ensureStyles();
    restoreApprovedHomepage();
    pageClasses();
    if(!isHomepage()){
      globalHeader();
      globalFooter();
      enhanceEntryHero();
      simplifyStartHere();
    }
    normalizeLinks();
    applyPortrait();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',applyAll);
  else applyAll();
  setTimeout(applyAll,120);
  setTimeout(applyAll,500);
  setTimeout(applyAll,1000);
  addEventListener('popstate',()=>setTimeout(applyAll,0));
})();
