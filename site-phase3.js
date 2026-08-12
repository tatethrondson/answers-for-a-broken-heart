(()=>{
  const CSS='/site-phase3.css?v=20260811-1';
  const PODCAST_URL='https://youtu.be/cCnEWfS5M0o?si=oge2LySLWOMjpva8';
  const PODCAST_THUMB='https://img.youtube.com/vi/cCnEWfS5M0o/hqdefault.jpg';

  const path=()=>location.pathname.replace(/\.html$/,'');
  const isResources=()=>path()==='/free-guides';
  const isTwoAm=()=>path()==='/2am-guide';
  const isDepression=()=>path()==='/can-christians-be-depressed';
  const isHelp=()=>path()==='/help-someone';
  const isPhase3=()=>isResources()||isTwoAm()||isDepression()||isHelp();

  function ensureCss(){
    if(!document.querySelector('link[data-ab-heart-phase3]')){
      const link=document.createElement('link');
      link.rel='stylesheet';
      link.href=CSS;
      link.setAttribute('data-ab-heart-phase3','1');
      document.head.appendChild(link);
    }
    if(!document.getElementById('phase3-podcast-styles')){
      const style=document.createElement('style');
      style.id='phase3-podcast-styles';
      style.textContent=`
        .podcastResource{margin:30px 0;padding:25px 27px;background:#eef2ed;border:1px solid #d9e0d8;border-left:4px solid #789078;display:grid;grid-template-columns:220px 1fr;gap:24px;align-items:center}
        .podcastThumb{display:block!important;text-decoration:none!important;background:transparent!important;padding:0!important;border-radius:10px!important;overflow:hidden!important;line-height:0!important}
        .podcastThumb img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}
        .podcastResource small{display:block;text-transform:uppercase;letter-spacing:.14em;font-size:.64rem;font-weight:800;color:#88683b;margin-bottom:7px}
        .podcastResource strong{display:block;font:400 1.55rem/1.18 Georgia,"Times New Roman",serif;color:#20372a;margin-bottom:7px}
        .podcastResource p{margin:0 0 14px!important;color:#5e6861;font-size:.88rem;line-height:1.58}
        .podcastButton{display:inline-flex!important;align-items:center;justify-content:center;text-decoration:none!important;background:#294533!important;color:#fff!important;padding:11px 15px!important;font-size:.72rem!important;font-weight:800!important;letter-spacing:.03em}
        .phase3PodcastHub{margin:34px 0 0}
        @media(max-width:760px){.podcastResource{grid-template-columns:1fr;padding:22px 20px}.podcastResource strong{font-size:1.35rem}.podcastThumb{max-width:420px}}
      `;
      document.head.appendChild(style);
    }
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

  function podcastMarkup(extraClass=''){
    return `<section class="podcastResource ${extraClass}" aria-label="Podcast episode about depression"><a class="podcastThumb" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer" aria-label="Watch the depression and faith podcast episode on YouTube"><img src="${PODCAST_THUMB}" alt="Depression and faith podcast episode thumbnail" loading="lazy"></a><div><small>New podcast · Prefer to listen?</small><strong>A pastoral conversation about depression and faith.</strong><p>Pastor Tate talks through depression, spiritual guilt, emotional exhaustion, and why struggling emotionally does not automatically mean your faith has failed.</p><a class="podcastButton" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer">Listen on YouTube →</a></div></section>`;
  }

  function addDepressionPodcast(){
    if(!isDepression() || document.querySelector('[data-depression-podcast]')) return;
    const keyline=document.querySelector('.article .keyline');
    if(!keyline) return;
    const holder=document.createElement('div');
    holder.setAttribute('data-depression-podcast','1');
    holder.innerHTML=podcastMarkup();
    keyline.insertAdjacentElement('afterend',holder);
  }

  function addResourcesPodcast(){
    if(!isResources() || document.querySelector('[data-resources-podcast]')) return;
    const grid=document.querySelector('.resources .grid');
    if(!grid) return;
    const holder=document.createElement('div');
    holder.setAttribute('data-resources-podcast','1');
    holder.className='phase3PodcastHub';
    holder.innerHTML=podcastMarkup();
    grid.insertAdjacentElement('afterend',holder);
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
    addDepressionPodcast();
    addResourcesPodcast();
    fixHelpLibraryCta();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  setTimeout(apply,120);
  setTimeout(apply,500);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();