(()=>{
  const P='/tate-throndson-portrait-final.jpg?v=20260811-restore';
  const HOME_STYLE='/homepage-original.css?v=20260811-1';
  let originalHeaderHTML='';

  function isHomepage(){
    const params=new URLSearchParams(location.search);
    return location.pathname==='/' && !params.has('view') && !params.has('answer');
  }

  function captureHeader(){
    const header=document.querySelector('.siteShellHeader');
    if(header && !originalHeaderHTML) originalHeaderHTML=header.innerHTML;
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

  function homeHeader(){
    const header=document.querySelector('.siteShellHeader');
    if(!header) return;
    captureHeader();
    if(header.dataset.homeOriginal==='1') return;
    header.dataset.homeOriginal='1';
    header.innerHTML=`<div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/"><span class="siteShellBrandWords">answers<small>for a broken heart</small></span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/">Home</a><a href="/all-answers">Encouragement⌄</a><a href="/start-here">Pastoral Care⌄</a><a href="/free-guides">Resources⌄</a><a href="/about">About</a><a href="/contact">Contact</a><a class="homeFindHope" href="/what-hurts-today">Find Hope</a><a class="homeSearch" href="/all-answers" aria-label="Search">⌕</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/">Home</a><a href="/all-answers">Encouragement</a><a href="/start-here">Pastoral Care</a><a href="/free-guides">Resources</a><a href="/about">About</a><a href="/contact">Contact</a><a href="/what-hurts-today">Find Hope</a></nav></details></div>`;
  }

  function restoreHeader(){
    const header=document.querySelector('.siteShellHeader');
    if(header && header.dataset.homeOriginal==='1' && originalHeaderHTML){
      header.innerHTML=originalHeaderHTML;
      delete header.dataset.homeOriginal;
    }
  }

  function homepageMarkup(){
    return `<div class="homeOriginalRoot" data-home-original="1">
      <section class="homeHero"><div class="homeOriginalWrap homeHeroGrid">
        <div class="homeHeroCopy"><div class="homeEyebrow">You are not alone</div><h1>Hope and healing<br>for the brokenhearted.</h1><p class="homeHeroLead">Biblical encouragement and pastoral care for life’s deepest hurts.</p><div class="homeHeroRule"></div><p class="homeHeroVerse">“The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.”<small>— Psalm 34:18</small></p><div class="homeHeroActions"><a class="homeHeroBtn primary" href="/what-hurts-today">Find Encouragement</a><a class="homeHeroBtn secondary" href="/free-guides">Explore Resources</a></div></div>
        <div class="homeHeroImage" role="img" aria-label="An open Bible overlooking a peaceful mountain landscape"></div>
      </div></section>

      <section class="homeResources"><div class="homeOriginalWrap"><div class="homeSectionTop"><div><div class="homeEyebrow">Featured resources</div><h2>Resources for your journey</h2></div><a class="homeViewAll" href="/free-guides">View all resources →</a></div><div class="homeResourceGrid">
        <a class="homeResourceCard" href="/all-answers"><div class="homeResourcePhoto one"><div class="homeResourceIcon">▣</div></div><div class="homeResourceBody"><h3>Encouraging Articles</h3><p>Truth and hope for the hard places.</p></div></a>
        <a class="homeResourceCard" href="/2am-guide"><div class="homeResourcePhoto two"><div class="homeResourceIcon">♧</div></div><div class="homeResourceBody"><h3>Devotions</h3><p>Daily reflections to strengthen your heart.</p></div></a>
        <a class="homeResourceCard" href="/start-here"><div class="homeResourcePhoto three"><div class="homeResourceIcon">♡</div></div><div class="homeResourceBody"><h3>Pastoral Care</h3><p>Compassionate support when you need it most.</p></div></a>
        <a class="homeResourceCard" href="/help-someone"><div class="homeResourcePhoto four"><div class="homeResourceIcon">♧</div></div><div class="homeResourceBody"><h3>Community</h3><p>You were never meant to walk alone.</p></div></a>
        <a class="homeResourceCard" href="/free-guides"><div class="homeResourcePhoto five"><div class="homeResourceIcon">↓</div></div><div class="homeResourceBody"><h3>Free Resources</h3><p>Guides and tools to encourage your soul.</p></div></a>
      </div></div></section>

      <section class="homeHurtsWrap"><div class="homeOriginalWrap"><div class="homeHurts"><div><h2>What hurts today?</h2><p>Take a moment to reflect and let us help you find encouragement that meets you where you are.</p><a class="homeHurtsBtn" href="/what-hurts-today">Begin Guided Entry</a></div><div class="homeHurtsPills"><a class="homeHurtPill" href="/grief-and-loss"><span>♧</span> Grief &amp; Loss</a><a class="homeHurtPill" href="/what-hurts-today"><span>⌁</span> Anxiety &amp; Fear</a><a class="homeHurtPill" href="/god-feels-far-away"><span>♙</span> Loneliness</a><a class="homeHurtPill" href="/forgiveness-and-relational-hurt"><span>♡</span> Broken Relationships</a><div class="homeHurtsNote">You can always come as you are. There is hope for today.</div></div></div></div></section>

      <section class="homeTestimonial"><div class="homeOriginalWrap"><div class="homeTestimonialInner"><div class="homeTestimonialPhoto"></div><div class="homeQuote"><blockquote>Answers for a Broken Heart has been a lifeline in my hardest season. The truth, grace, and compassion here remind me that God sees me, He hears me, and He is with me.</blockquote><cite>— Jessica, Reader</cite></div></div></div></section>

      <footer class="homeFooter"><div class="homeOriginalWrap homeFooterMain"><div><div class="homeFooterBrand">answers<small>for a broken heart</small></div><div class="homeFooterTag">Biblical encouragement and pastoral care for life’s deepest hurts.</div></div><div class="homeFooterCol"><strong>Encouragement</strong><a href="/all-answers">Encouraging Articles</a><a href="/2am-guide">Devotions</a><a href="/all-answers">Bible Promises</a><a href="/all-answers">Stories of Hope</a></div><div class="homeFooterCol"><strong>Pastoral Care</strong><a href="/start-here">Pastoral Care</a><a href="/contact">Submit a Prayer Request</a><a href="/about">About Our Care</a><a href="/contact">FAQs</a></div><div class="homeFooterCol"><strong>Stay Encouraged</strong><p>Subscribe for weekly hope and encouragement.</p><form class="homeFooterForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Email address" required><input type="hidden" name="_subject" value="Answers for a Broken Heart encouragement signup"><input type="hidden" name="_captcha" value="false"><button type="submit">Subscribe</button></form></div></div><div class="homeFooterBottom"><div class="homeOriginalWrap"><span>© 2026 Answers for a Broken Heart</span><span><a href="/contact">Privacy Policy</a><a href="/contact">Terms of Use</a><a href="/contact">Contact</a></span></div></div></footer>
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
    restoreApprovedHomepage();
    applyPortrait();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',applyAll);
  else applyAll();
  new MutationObserver(applyAll).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',()=>setTimeout(applyAll,0));
})();
