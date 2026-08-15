(()=>{
  const ITEMS=[
    ['Start Here','/start-here'],
    ['24 Answers','/all-answers'],
    ['Free Resources','/free-guides'],
    ['The Book','/book'],
    ['About','/about']
  ];
  const SITE_HREFS=new Set(['/','/start-here','/begin-here','/what-hurts-today','/all-answers','/free-guides','/book','/about','/contact','/church-resources']);

  function normalizePath(p){
    if(!p||p==='/') return '/';
    return p.replace(/\.html$/,'').replace(/\/$/,'')||'/';
  }
  function isActive(href){
    const here=normalizePath(window.location.pathname);
    const target=normalizePath(href);
    if(target==='/start-here'&&(here==='/begin-here'||here==='/what-hurts-today')) return true;
    return here===target;
  }
  function links(){
    return ITEMS.map(([label,href])=>`<a href="${href}"${isActive(href)?' aria-current="page"':''}>${label}</a>`).join('');
  }
  function headerMarkup(){
    return `<div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation">${links()}</nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation">${links()}</nav></details></div>`;
  }
  function hasSiteLinks(el){
    return [...el.querySelectorAll('a[href]')].some(a=>SITE_HREFS.has(normalizePath(a.getAttribute('href'))));
  }
  function beforeMain(el,main){
    if(!main) return true;
    if(main.contains(el)) return false;
    return !!(el.compareDocumentPosition(main)&Node.DOCUMENT_POSITION_FOLLOWING);
  }
  function enforce(){
    const body=document.body;
    if(!body) return;
    const main=document.querySelector('main');

    let header=document.querySelector('header.siteShellHeader');
    if(!header){
      header=document.createElement('header');
      header.className='siteShellHeader';
    }

    document.querySelectorAll('header').forEach(h=>{
      if(h===header) return;
      if(beforeMain(h,main)&&hasSiteLinks(h)) h.remove();
    });
    document.querySelectorAll('nav').forEach(nav=>{
      if(header.contains(nav)) return;
      if(beforeMain(nav,main)&&hasSiteLinks(nav)) nav.remove();
    });

    if(body.firstElementChild!==header) body.insertBefore(header,body.firstChild);
    header.className='siteShellHeader';
    header.innerHTML=headerMarkup();

    header.querySelectorAll('.siteShellMobileMenu a').forEach(a=>a.addEventListener('click',()=>{
      const d=header.querySelector('.siteShellMobile');
      if(d) d.open=false;
    }));

    if(!document.getElementById('site-shell-runtime-guard')){
      const style=document.createElement('style');
      style.id='site-shell-runtime-guard';
      style.textContent=`
        body>header.siteShellHeader{display:block!important}
        .siteShellHeader .siteShellLinks{display:flex!important}
        .siteShellHeader .siteShellMobile{display:none!important}
        @media(max-width:760px){
          .siteShellHeader .siteShellLinks{display:none!important}
          .siteShellHeader .siteShellMobile{display:block!important}
        }
      `;
      document.head.appendChild(style);
    }
  }

  const run=()=>{try{enforce()}catch(e){console.error('site shell enforcement failed',e)}};
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',run,{once:true});
  else run();
  window.addEventListener('load',run,{once:true});
  setTimeout(run,50);
  setTimeout(run,350);
  setTimeout(run,1200);
})();
