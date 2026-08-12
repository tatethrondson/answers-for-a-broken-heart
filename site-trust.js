(()=>{
  const PODCAST_URL='https://youtu.be/cCnEWfS5M0o?si=oge2LySLWOMjpva8';
  const PODCAST_THUMB='https://img.youtube.com/vi/cCnEWfS5M0o/hqdefault.jpg';

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

  function ensureStyles(){
    if(document.getElementById('trust-minimal-styles')) return;
    const style=document.createElement('style');
    style.id='trust-minimal-styles';
    style.textContent=`
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
      .podcastResource.answerDepressionPodcast{margin:30px 0;padding:22px 24px;background:#eef2ed;border:1px solid #d9e0d8;border-left:4px solid #789078;display:grid;grid-template-columns:200px 1fr;gap:22px;align-items:center}
      .answerDepressionPodcast small{display:block;text-transform:uppercase;letter-spacing:.14em;font-size:.61rem;font-weight:800;color:#88683b;margin-bottom:5px}.answerDepressionPodcast strong{display:block;font:400 1.35rem/1.17 Georgia,"Times New Roman",serif;color:#20372a}.answerDepressionPodcast p{margin:5px 0 0;font-size:.76rem;line-height:1.5;color:#626a64}
      .answerDepressionPodcast .podcastThumb{display:block!important;background:transparent!important;padding:0!important;border-radius:10px!important;overflow:hidden!important;line-height:0!important;text-decoration:none!important}.answerDepressionPodcast .podcastThumb img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}.answerDepressionPodcast .podcastAction{display:inline-flex!important;text-decoration:none!important;background:#294533!important;color:#fff!important;padding:10px 14px!important;font-size:.69rem!important;font-weight:800!important;white-space:nowrap!important;margin-top:13px}
      @media(max-width:760px){.homeBookBand,.podcastResource.answerDepressionPodcast{grid-template-columns:1fr}.homeMiniBook{justify-self:start}.homeBookBand{padding:28px 24px}.answerDepressionPodcast .podcastAction{justify-self:start}.answerDepressionPodcast .podcastThumb{max-width:420px}}
    `;
    document.head.appendChild(style);
  }

  function addAnswer17Podcast(){
    if(!/^\/answer-17(?:\.html)?$/.test(location.pathname) || document.querySelector('.answerDepressionPodcast')) return;
    const minute=document.querySelector('.minuteHelp');
    if(!minute) return;
    const box=document.createElement('section');
    box.className='podcastResource answerDepressionPodcast';
    box.setAttribute('aria-label','Related podcast episode about depression');
    box.innerHTML=`<a class="podcastThumb" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer" aria-label="Watch the depression and faith podcast episode on YouTube"><img src="${PODCAST_THUMB}" alt="Depression and faith podcast episode thumbnail" loading="lazy"></a><div><small>Related listening · Depression & faith</small><strong>If the heaviness feels bigger than grief alone.</strong><p>Pastor Tate talks about depression, faith, emotional exhaustion, and the guilt Christians sometimes feel when they are not getting better.</p><a class="podcastAction" href="${PODCAST_URL}" target="_blank" rel="noopener noreferrer">Listen on YouTube →</a></div>`;
    minute.insertAdjacentElement('afterend',box);
  }

  function trackBookClicks(){
    if(document.documentElement.dataset.bookTracking==='1') return;
    document.documentElement.dataset.bookTracking='1';
    document.addEventListener('click',e=>{
      const a=e.target.closest('a[href]');
      if(!a || a.getAttribute('href')!=='/book') return;
      try{
        if(typeof window.va==='function') window.va('event',{name:'Book Interest Click',data:{page:location.pathname||'/',label:(a.textContent||'').trim().replace(/\s+/g,' ').slice(0,80)}});
      }catch(err){}
    });
  }

  function apply(){
    if(legacyRedirect()) return;
    ensureStyles();
    addAnswer17Podcast();
    trackBookClicks();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  setTimeout(apply,180);
  setTimeout(apply,600);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
