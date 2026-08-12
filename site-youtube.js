(()=>{
  function youtubeId(href){
    try{
      const u=new URL(href,location.origin);
      if(u.hostname==='youtu.be' || u.hostname.endsWith('.youtu.be')) return u.pathname.split('/').filter(Boolean)[0]||'';
      if(u.hostname.includes('youtube.com')){
        if(u.pathname==='/watch') return u.searchParams.get('v')||'';
        const parts=u.pathname.split('/').filter(Boolean);
        const i=parts.findIndex(x=>x==='shorts'||x==='embed'||x==='live');
        if(i>=0 && parts[i+1]) return parts[i+1];
      }
    }catch(e){}
    return '';
  }

  function ensureStyles(){
    if(document.getElementById('youtube-card-match-styles')) return;
    const style=document.createElement('style');
    style.id='youtube-card-match-styles';
    style.textContent=`
      .youtubeMatchCard{display:grid!important;grid-template-columns:200px 1fr!important;gap:22px!important;align-items:center!important;background:#eef2ed!important;border:1px solid #d9e0d8!important;border-left:4px solid #789078!important;padding:22px 24px!important;border-radius:15px!important;overflow:hidden!important}
      .youtubeMatchThumb{display:block!important;width:100%!important;border-radius:10px!important;overflow:hidden!important;line-height:0!important;background:transparent!important;padding:0!important;text-decoration:none!important}
      .youtubeMatchThumb img{display:block!important;width:100%!important;aspect-ratio:16/9!important;object-fit:cover!important}
      .youtubeMatchCopy{min-width:0!important}.youtubeMatchCopy>a[href*="youtu"]{display:inline-flex!important;width:auto!important;background:#294533!important;color:#fff!important;text-decoration:none!important;padding:10px 14px!important;margin-top:12px!important;border-radius:0!important;font-size:.69rem!important;font-weight:800!important;line-height:1.2!important}
      .youtubeMatchCopy small{display:block!important;text-transform:uppercase!important;letter-spacing:.14em!important;font-size:.61rem!important;font-weight:800!important;color:#88683b!important;margin-bottom:5px!important}
      .youtubeMatchCopy strong,.youtubeMatchCopy h3{font-family:Georgia,"Times New Roman",serif!important;font-weight:400!important;color:#20372a!important}
      .youtubeJourneyCard{overflow:hidden!important;padding:0!important}.youtubeJourneyVisual{display:block!important;line-height:0!important;margin:0!important}.youtubeJourneyVisual img{display:block!important;width:100%!important;aspect-ratio:16/9!important;object-fit:cover!important}.youtubeJourneyBody{display:block!important;padding:20px 21px!important}
      @media(max-width:760px){.youtubeMatchCard{grid-template-columns:1fr!important}.youtubeMatchThumb{max-width:420px!important}}
    `;
    document.head.appendChild(style);
  }

  function enhancePodcastResource(card,link,id){
    if(card.dataset.youtubeMatch==='1' || card.querySelector('.podcastThumb,.youtubeMatchThumb')) return;
    card.dataset.youtubeMatch='1';
    card.classList.add('youtubeMatchCard');
    const href=link.href;
    const label=(link.textContent||'Watch on YouTube').trim();
    const thumb=document.createElement('a');
    thumb.className='youtubeMatchThumb';
    thumb.href=href;thumb.target='_blank';thumb.rel='noopener noreferrer';
    thumb.setAttribute('aria-label',label);
    thumb.innerHTML=`<img src="https://img.youtube.com/vi/${id}/hqdefault.jpg" alt="YouTube interview thumbnail" loading="lazy">`;
    const copy=document.createElement('div');
    copy.className='youtubeMatchCopy';
    Array.from(card.childNodes).forEach(node=>copy.appendChild(node));
    card.appendChild(thumb);
    card.appendChild(copy);
  }

  function enhanceJourneyLink(link,id){
    const card=link.closest('.journeyCard');
    if(!card || card.dataset.youtubeMatch==='1') return;
    card.dataset.youtubeMatch='1';
    if(link===card){
      card.classList.add('youtubeJourneyCard');
      const visual=document.createElement('span');
      visual.className='youtubeJourneyVisual';
      visual.innerHTML=`<img src="https://img.youtube.com/vi/${id}/hqdefault.jpg" alt="YouTube interview thumbnail" loading="lazy">`;
      const body=document.createElement('span');
      body.className='youtubeJourneyBody';
      while(card.firstChild) body.appendChild(card.firstChild);
      card.appendChild(visual);card.appendChild(body);
      return;
    }
    const thumb=document.createElement('a');
    thumb.className='youtubeMatchThumb';
    thumb.href=link.href;thumb.target='_blank';thumb.rel='noopener noreferrer';
    thumb.innerHTML=`<img src="https://img.youtube.com/vi/${id}/hqdefault.jpg" alt="YouTube interview thumbnail" loading="lazy">`;
    card.insertBefore(thumb,card.firstChild);
  }

  function apply(){
    ensureStyles();
    document.querySelectorAll('main a[href*="youtu.be"],main a[href*="youtube.com"]').forEach(link=>{
      if(link.classList.contains('podcastThumb') || link.classList.contains('youtubeMatchThumb') || link.closest('.homePodcastStrip,.startPodcast,.answerDepressionPodcast')) return;
      const id=youtubeId(link.href);
      if(!id) return;
      const podcast=link.closest('.podcastResource');
      if(podcast){enhancePodcastResource(podcast,link,id);return;}
      if(link.closest('.answerJourney')) enhanceJourneyLink(link,id);
    });
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply); else apply();
  setTimeout(apply,150);setTimeout(apply,600);setTimeout(apply,1200);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();