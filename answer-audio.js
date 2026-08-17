(function(){
  function ready(fn){
    if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',fn,{once:true});
    else fn();
  }

  ready(function(){
    var body=document.body;
    if(!body) return;
    var match=(body.className||'').match(/page-answer-(\d{2})/);
    if(!match) return;

    var number=match[1];
    var canonical=document.querySelector('link[rel="canonical"]');
    var slug='';
    try{
      var canonicalUrl=canonical && canonical.href ? new URL(canonical.href,window.location.origin) : null;
      slug=canonicalUrl ? canonicalUrl.pathname.replace(/^\/+|\/+$/g,'') : '';
    }catch(e){}
    if(!slug) slug=(window.location.pathname||'').replace(/^\/+|\/+$/g,'');
    if(!slug || /^answer-\d{2}$/.test(slug)) return;

    var src='/audio/'+slug+'.mp3';

    fetch(src,{method:'HEAD',cache:'no-store'}).then(function(r){
      if(!r.ok) return;
      mount(src,number);
    }).catch(function(){});
  });

  function mount(src,number){
    if(document.querySelector('.answerAudio')) return;
    var anchor=document.querySelector('.minuteHelp') || document.querySelector('.short') || document.querySelector('.article');
    if(!anchor) return;

    if(!document.getElementById('answer-audio-styles')){
      var style=document.createElement('style');
      style.id='answer-audio-styles';
      style.textContent='\
.answerAudio{margin:0 0 38px;border:1px solid #ded8cd;background:#f5f0e7;padding:24px 26px;display:grid;grid-template-columns:minmax(0,1fr) minmax(260px,.8fr);gap:24px;align-items:center}\
.answerAudioEyebrow{margin:0 0 6px;text-transform:uppercase;letter-spacing:.13em;color:#88683b;font-size:.65rem;font-weight:800}\
.answerAudio h2{font:400 1.7rem/1.1 Georgia,"Times New Roman",serif;color:#183024;margin:0 0 7px}\
.answerAudio p{margin:0!important;color:#59635d;font-size:.84rem;line-height:1.55}\
.answerAudio audio{width:100%;display:block}\
@media(max-width:700px){.answerAudio{grid-template-columns:1fr;padding:22px}}';
      document.head.appendChild(style);
    }

    var box=document.createElement('section');
    box.className='answerAudio';
    box.setAttribute('aria-label','Audio version of this Answer');
    box.innerHTML='<div><p class="answerAudioEyebrow">Prefer to listen?</p><h2>Listen to Pastor Tate.</h2><p>A short pastoral audio version of this Answer.</p></div><audio controls preload="none" src="'+src+'">Your browser does not support the audio element.</audio>';

    if(anchor.classList && anchor.classList.contains('minuteHelp')) anchor.insertAdjacentElement('afterend',box);
    else if(anchor.classList && anchor.classList.contains('short')) anchor.insertAdjacentElement('afterend',box);
    else anchor.insertAdjacentElement('afterbegin',box);

    var audio=box.querySelector('audio');
    var tracked=false;
    if(audio){
      audio.addEventListener('play',function(){
        if(tracked) return;
        tracked=true;
        try{
          if(typeof window.va==='function') window.va('event',{name:'Answer Audio Play',data:{answer:number}});
        }catch(e){}
      });
    }
  }
})();
