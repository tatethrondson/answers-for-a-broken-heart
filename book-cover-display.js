(()=>{
  const cover='/answers-for-a-broken-heart-cover.svg?v=20261015-1';
  function styles(){
    if(document.getElementById('answers-book-cover-20261015')) return;
    const s=document.createElement('style');
    s.id='answers-book-cover-20261015';
    s.textContent=`
      .bookStage .updatedBookCover{display:block;width:min(100%,295px);height:auto;max-height:100%;object-fit:contain;filter:drop-shadow(12px 18px 13px rgba(16,21,17,.24));margin:auto;border-radius:3px}
      .bookBridgeCopy .bookMiniCover{float:left;display:block;width:104px;height:156px;object-fit:cover;margin:2px 23px 12px 0;box-shadow:6px 9px 15px rgba(16,21,17,.18);border-radius:2px}
      .bookBridgeCopy::after{content:"";display:block;clear:both}
      @media(max-width:650px){.bookBridgeCopy .bookMiniCover{width:78px;height:117px;margin-right:16px}.bookStage .updatedBookCover{width:min(100%,255px)}}
    `;
    document.head.appendChild(s);
  }
  function apply(){
    styles();
    document.querySelectorAll('.bookStage .bookCover, .bookStage .heroBook').forEach(el=>{
      if(el.dataset.coverReplaced) return;
      const img=document.createElement('img');
      img.className='updatedBookCover';
      img.src=cover;
      img.alt='Answers for a Broken Heart by Tate Throndson — black linen and gold book cover';
      img.width=720;
      img.height=1080;
      img.decoding='async';
      el.replaceWith(img);
    });
    document.querySelectorAll('.bookBridgeHome .bookBridgeCopy').forEach(el=>{
      if(el.querySelector('.bookMiniCover'))return;
      const a=document.createElement('a');
      a.href='/book';a.setAttribute('aria-label','View Answers for a Broken Heart book');
      a.innerHTML='<img class="bookMiniCover" src="'+cover+'" width="104" height="156" alt="Answers for a Broken Heart book cover">';
      el.insertBefore(a,el.firstChild);
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply); else apply();
  const observer=new MutationObserver(()=>apply());
  observer.observe(document.documentElement,{childList:true,subtree:true});
  window.addEventListener('pageshow',apply);
})();