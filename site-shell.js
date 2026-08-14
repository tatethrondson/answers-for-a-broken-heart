(()=>{
  const ITEMS=[
    ['Start Here','/start-here'],
    ['24 Answers','/all-answers'],
    ['Free Resources','/free-guides'],
    ['The Book','/book'],
    ['About','/about']
  ];

  function normalizePath(p){
    if(!p||p==='/') return '/';
    return p.replace(/\.html$/,'').replace(/\/$/,'')||'/';
  }

  function isActive(href){
    const here=normalizePath(window.location.pathname);
    const target=normalizePath(href);
    if(target==='/start-here' && (here==='/begin-here'||here==='/what-hurts-today')) return true;
    return here===target;
  }

  function linkMarkup(mobile=false){
    return ITEMS.map(([label,href])=>`<a href="${href}"${isActive(href)?' aria-current="page"':''}>${label}</a>`).join('');
  }

  function canonicalHeader(){
    return `<div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation">${linkMarkup()}</nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation">${linkMarkup(true)}</nav></details></div>`;
  }

  function enforce(){
    const body=document.body;
    if(!body) return;

    // Remove any leftover top-level legacy header. The shared shell is the only
    // primary site navigation allowed at the top of a page.
    document.querySelectorAll('body > header:not(.siteShellHeader)').forEach(el=>el.remove());

    let header=document.querySelector('body > header.siteShellHeader');
    if(!header){
      header=document.createElement('header');
      header.className='siteShellHeader';
      body.insertBefore(header,body.firstChild);
    }
    header.innerHTML=canonicalHeader();

    let guard=document.getElementById('site-shell-runtime-guard');
    if(!guard){
      guard=document.createElement('style');
      guard.id='site-shell-runtime-guard';
      guard.textContent=`
        body>header:not(.siteShellHeader){display:none!important}
        .siteShellHeader .siteShellNav{display:flex!important;align-items:center!important;justify-content:space-between!important}
        .siteShellHeader .siteShellLinks{display:flex!important;align-items:center!important}
        .siteShellHeader .siteShellMobile{display:none!important}
        @media(max-width:760px){
          .siteShellHeader .siteShellLinks{display:none!important}
          .siteShellHeader .siteShellMobile{display:block!important}
        }
      `;
      document.head.appendChild(guard);
    }

    header.querySelectorAll('.siteShellMobileMenu a').forEach(a=>a.addEventListener('click',()=>{
      const d=header.querySelector('.siteShellMobile'); if(d) d.open=false;
    }));
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',enforce,{once:true});
  else enforce();
})();
