(()=>{
  const CSS='/site-finish.css?v=20260811-1';

  function ensureCss(){
    let link=document.querySelector('link[data-ab-heart-finish]');
    if(!link){
      link=document.createElement('link');
      link.rel='stylesheet';
      link.href=CSS;
      link.setAttribute('data-ab-heart-finish','1');
      document.head.appendChild(link);
    }
  }

  function moveLast(){
    const link=document.querySelector('link[data-ab-heart-finish]');
    if(!link) return;
    const sheets=Array.from(document.head.querySelectorAll('link[rel="stylesheet"]'));
    if(sheets[sheets.length-1]!==link) document.head.appendChild(link);
  }

  function apply(){ensureCss();moveLast();}
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  setTimeout(apply,100);
  setTimeout(apply,450);
  setTimeout(apply,900);
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
